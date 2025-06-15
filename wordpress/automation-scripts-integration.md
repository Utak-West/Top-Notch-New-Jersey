# Automation Scripts Integration - Top Notch New Jersey

## 🤖 Python Automation Suite Integration

### Purpose
Integrate Python automation scripts with WordPress to handle lead processing, CRM integration, email automation, and site maintenance for Top Notch New Jersey's kitchen and bathroom remodeling business.

---

## 📋 Script Architecture Overview

### Main Components
1. **Lead Processing Automation** - Process form submissions and score leads
2. **CRM Integration** - Sync leads with customer relationship management
3. **Email Marketing Automation** - Trigger personalized email sequences
4. **Site Maintenance** - Automated WordPress and Elementor maintenance
5. **Performance Monitoring** - Track site performance and uptime

### Dependencies
```python
# Required Python packages
requirements = [
    'requests>=2.28.0',
    'python-wordpress-xmlrpc>=2.3',
    'smtplib',
    'json',
    'datetime',
    'logging',
    'mysql-connector-python>=8.0.0',
    'schedule>=1.2.0',
    'python-dotenv>=0.19.0'
]
```

---

## 🔗 WordPress Integration Setup

### Webhook Endpoints Configuration
```php
// WordPress webhook endpoints for automation scripts
add_action('rest_api_init', 'topnotch_register_automation_endpoints');
function topnotch_register_automation_endpoints() {
    // Lead processing endpoint
    register_rest_route('topnotch/v1', '/process-lead', [
        'methods' => 'POST',
        'callback' => 'topnotch_process_lead_webhook',
        'permission_callback' => 'topnotch_verify_webhook_auth'
    ]);
    
    // CRM sync endpoint
    register_rest_route('topnotch/v1', '/sync-crm', [
        'methods' => 'POST',
        'callback' => 'topnotch_sync_crm_webhook',
        'permission_callback' => 'topnotch_verify_webhook_auth'
    ]);
    
    // Maintenance status endpoint
    register_rest_route('topnotch/v1', '/maintenance-status', [
        'methods' => 'GET',
        'callback' => 'topnotch_maintenance_status_webhook',
        'permission_callback' => 'topnotch_verify_webhook_auth'
    ]);
}

// Webhook authentication
function topnotch_verify_webhook_auth($request) {
    $auth_header = $request->get_header('Authorization');
    $expected_token = get_option('topnotch_webhook_token');
    
    if ($auth_header !== "Bearer {$expected_token}") {
        return new WP_Error('unauthorized', 'Invalid webhook token', ['status' => 401]);
    }
    
    return true;
}

// Lead processing webhook handler
function topnotch_process_lead_webhook($request) {
    $lead_data = $request->get_json_params();
    
    // Validate required fields
    $required_fields = ['name', 'email', 'phone', 'service_type'];
    foreach ($required_fields as $field) {
        if (empty($lead_data[$field])) {
            return new WP_Error('missing_field', "Missing required field: {$field}", ['status' => 400]);
        }
    }
    
    // Process lead through automation script
    $automation_response = wp_remote_post('http://localhost:8000/process-lead', [
        'body' => json_encode($lead_data),
        'headers' => [
            'Content-Type' => 'application/json',
            'Authorization' => 'Bearer ' . get_option('topnotch_automation_token')
        ]
    ]);
    
    if (is_wp_error($automation_response)) {
        return new WP_Error('automation_failed', 'Lead processing failed', ['status' => 500]);
    }
    
    return rest_ensure_response([
        'success' => true,
        'message' => 'Lead processed successfully',
        'lead_id' => $lead_data['lead_id'] ?? null
    ]);
}
```

### Form Integration Hooks
```php
// WPForms integration with automation scripts
add_action('wpforms_process_complete', 'topnotch_trigger_lead_automation', 10, 4);
function topnotch_trigger_lead_automation($fields, $entry, $form_data, $entry_id) {
    // Extract form data
    $lead_data = [
        'lead_id' => $entry_id,
        'form_id' => $form_data['id'],
        'name' => $fields[1]['value'] . ' ' . $fields[2]['value'], // First + Last name
        'email' => $fields[3]['value'],
        'phone' => $fields[4]['value'],
        'service_type' => $fields[5]['value'],
        'budget_range' => $fields[6]['value'],
        'timeline' => $fields[7]['value'],
        'location' => $fields[8]['value'],
        'source' => 'wpforms',
        'timestamp' => current_time('mysql'),
        'ip_address' => $_SERVER['REMOTE_ADDR'],
        'user_agent' => $_SERVER['HTTP_USER_AGENT']
    ];
    
    // Trigger automation script via webhook
    wp_remote_post(get_option('topnotch_automation_webhook_url'), [
        'body' => json_encode($lead_data),
        'headers' => [
            'Content-Type' => 'application/json',
            'Authorization' => 'Bearer ' . get_option('topnotch_webhook_token')
        ],
        'timeout' => 30
    ]);
    
    // Log for debugging
    error_log('Lead automation triggered for entry ID: ' . $entry_id);
}

// Gravity Forms integration (alternative)
add_action('gform_after_submission', 'topnotch_gravity_forms_automation', 10, 2);
function topnotch_gravity_forms_automation($entry, $form) {
    // Similar implementation for Gravity Forms
    $lead_data = [
        'lead_id' => $entry['id'],
        'form_id' => $form['id'],
        'name' => rgar($entry, '1'),
        'email' => rgar($entry, '2'),
        'phone' => rgar($entry, '3'),
        'service_type' => rgar($entry, '4'),
        'source' => 'gravity_forms',
        'timestamp' => current_time('mysql')
    ];
    
    // Trigger automation
    topnotch_trigger_automation_webhook($lead_data);
}
```

---

## 🐍 Python Automation Scripts

### Lead Processing Script
```python
#!/usr/bin/env python3
"""
Lead Processing Automation
Handles incoming leads from WordPress forms and processes them through
the lead scoring algorithm and CRM integration.
"""

import json
import requests
import logging
from datetime import datetime
from typing import Dict, Any
import mysql.connector
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

class LeadProcessor:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger(__name__)
        
    def process_lead(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process incoming lead through scoring and CRM integration"""
        try:
            # Score the lead
            lead_score = self.calculate_lead_score(lead_data)
            lead_data['score'] = lead_score
            lead_data['quality'] = self.determine_lead_quality(lead_score)
            
            # Store in database
            lead_id = self.store_lead(lead_data)
            lead_data['lead_id'] = lead_id
            
            # Sync with CRM
            crm_result = self.sync_with_crm(lead_data)
            
            # Trigger email automation
            email_result = self.trigger_email_sequence(lead_data)
            
            # Send notifications
            if lead_data['quality'] == 'hot':
                self.send_priority_notification(lead_data)
            
            return {
                'success': True,
                'lead_id': lead_id,
                'score': lead_score,
                'quality': lead_data['quality'],
                'crm_synced': crm_result,
                'email_triggered': email_result
            }
            
        except Exception as e:
            self.logger.error(f"Lead processing failed: {e}")
            return {'success': False, 'error': str(e)}
    
    def calculate_lead_score(self, lead_data: Dict[str, Any]) -> int:
        """Calculate lead score based on multiple factors"""
        score = 0
        
        # Budget scoring
        budget_scores = {
            '100k_plus': 50,
            '60k_100k': 40,
            '30k_60k': 30,
            '15k_30k': 20,
            'under_15k': 10,
            'not_sure': 15
        }
        score += budget_scores.get(lead_data.get('budget_range', ''), 0)
        
        # Timeline scoring
        timeline_scores = {
            'asap': 30,
            '1_3_months': 25,
            '3_6_months': 20,
            '6_plus_months': 10,
            'planning_phase': 5
        }
        score += timeline_scores.get(lead_data.get('timeline', ''), 0)
        
        # Service type scoring
        service_scores = {
            'complete_home_remodel': 25,
            'multiple_rooms': 20,
            'kitchen_remodeling': 15,
            'bathroom_renovation': 15
        }
        score += service_scores.get(lead_data.get('service_type', ''), 0)
        
        # Location scoring (primary service areas get higher scores)
        location = lead_data.get('location', '').lower()
        if any(area in location for area in ['union', 'linden', 'elizabeth']):
            score += 15
        elif any(area in location for area in ['essex', 'middlesex', 'bergen']):
            score += 10
        
        return score
    
    def determine_lead_quality(self, score: int) -> str:
        """Determine lead quality based on score"""
        if score >= 70:
            return 'hot'
        elif score >= 50:
            return 'warm'
        else:
            return 'cold'
    
    def store_lead(self, lead_data: Dict[str, Any]) -> int:
        """Store lead in database"""
        try:
            connection = mysql.connector.connect(**self.config['database'])
            cursor = connection.cursor()
            
            query = """
            INSERT INTO leads (name, email, phone, service_type, budget_range, 
                             timeline, location, score, quality, source, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            values = (
                lead_data['name'],
                lead_data['email'],
                lead_data['phone'],
                lead_data['service_type'],
                lead_data.get('budget_range'),
                lead_data.get('timeline'),
                lead_data.get('location'),
                lead_data['score'],
                lead_data['quality'],
                lead_data.get('source', 'website'),
                datetime.now()
            )
            
            cursor.execute(query, values)
            connection.commit()
            
            lead_id = cursor.lastrowid
            cursor.close()
            connection.close()
            
            return lead_id
            
        except Exception as e:
            self.logger.error(f"Database storage failed: {e}")
            raise
    
    def sync_with_crm(self, lead_data: Dict[str, Any]) -> bool:
        """Sync lead with CRM system"""
        try:
            crm_payload = {
                'contact': {
                    'name': lead_data['name'],
                    'email': lead_data['email'],
                    'phone': lead_data['phone'],
                    'tags': [lead_data['service_type'], lead_data['quality']],
                    'custom_fields': {
                        'budget_range': lead_data.get('budget_range'),
                        'timeline': lead_data.get('timeline'),
                        'lead_score': lead_data['score'],
                        'source': lead_data.get('source')
                    }
                }
            }
            
            response = requests.post(
                self.config['crm']['api_url'],
                json=crm_payload,
                headers={
                    'Authorization': f"Bearer {self.config['crm']['api_key']}",
                    'Content-Type': 'application/json'
                },
                timeout=30
            )
            
            return response.status_code == 200
            
        except Exception as e:
            self.logger.error(f"CRM sync failed: {e}")
            return False
    
    def trigger_email_sequence(self, lead_data: Dict[str, Any]) -> bool:
        """Trigger appropriate email sequence based on lead data"""
        try:
            # Determine email sequence based on service type and quality
            sequence_map = {
                'kitchen_remodeling': {
                    'hot': 'kitchen_hot_lead_sequence',
                    'warm': 'kitchen_warm_lead_sequence',
                    'cold': 'kitchen_nurture_sequence'
                },
                'bathroom_renovation': {
                    'hot': 'bathroom_hot_lead_sequence',
                    'warm': 'bathroom_warm_lead_sequence',
                    'cold': 'bathroom_nurture_sequence'
                },
                'complete_home_remodel': {
                    'hot': 'complete_remodel_hot_sequence',
                    'warm': 'complete_remodel_warm_sequence',
                    'cold': 'complete_remodel_nurture_sequence'
                }
            }
            
            service_type = lead_data.get('service_type', 'kitchen_remodeling')
            quality = lead_data.get('quality', 'warm')
            
            sequence_id = sequence_map.get(service_type, {}).get(quality, 'default_sequence')
            
            # Trigger email sequence via email marketing platform API
            email_payload = {
                'contact_email': lead_data['email'],
                'sequence_id': sequence_id,
                'contact_data': {
                    'name': lead_data['name'],
                    'service_type': service_type,
                    'budget_range': lead_data.get('budget_range'),
                    'timeline': lead_data.get('timeline')
                }
            }
            
            response = requests.post(
                self.config['email_marketing']['api_url'],
                json=email_payload,
                headers={
                    'Authorization': f"Bearer {self.config['email_marketing']['api_key']}",
                    'Content-Type': 'application/json'
                },
                timeout=30
            )
            
            return response.status_code == 200
            
        except Exception as e:
            self.logger.error(f"Email sequence trigger failed: {e}")
            return False
    
    def send_priority_notification(self, lead_data: Dict[str, Any]) -> bool:
        """Send priority notification for hot leads"""
        try:
            # Email notification to Pedro
            msg = MIMEMultipart()
            msg['From'] = self.config['smtp']['from_email']
            msg['To'] = self.config['notifications']['pedro_email']
            msg['Subject'] = f"🔥 HOT LEAD: {lead_data['service_type']} - {lead_data['name']}"
            
            body = f"""
            HIGH PRIORITY LEAD ALERT
            
            Lead Details:
            Name: {lead_data['name']}
            Phone: {lead_data['phone']}
            Email: {lead_data['email']}
            Service: {lead_data['service_type']}
            Budget: {lead_data.get('budget_range', 'Not specified')}
            Timeline: {lead_data.get('timeline', 'Not specified')}
            Location: {lead_data.get('location', 'Not specified')}
            
            Lead Score: {lead_data['score']}/100
            Quality: {lead_data['quality'].upper()}
            
            RECOMMENDED ACTION: Contact within 1 hour for best conversion rate.
            
            View full lead details in CRM dashboard.
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email
            server = smtplib.SMTP(self.config['smtp']['host'], self.config['smtp']['port'])
            server.starttls()
            server.login(self.config['smtp']['username'], self.config['smtp']['password'])
            server.send_message(msg)
            server.quit()
            
            # Optional: Send SMS notification for hot leads
            if self.config.get('sms_enabled'):
                self.send_sms_notification(lead_data)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Priority notification failed: {e}")
            return False
    
    def send_sms_notification(self, lead_data: Dict[str, Any]) -> bool:
        """Send SMS notification for hot leads"""
        try:
            sms_message = f"🔥 HOT LEAD: {lead_data['name']} - {lead_data['service_type']} - {lead_data['phone']} - Score: {lead_data['score']}"
            
            # SMS API integration (example with Twilio)
            response = requests.post(
                f"https://api.twilio.com/2010-04-01/Accounts/{self.config['sms']['account_sid']}/Messages.json",
                auth=(self.config['sms']['account_sid'], self.config['sms']['auth_token']),
                data={
                    'From': self.config['sms']['from_number'],
                    'To': self.config['sms']['pedro_number'],
                    'Body': sms_message
                }
            )
            
            return response.status_code == 201
            
        except Exception as e:
            self.logger.error(f"SMS notification failed: {e}")
            return False

# Flask web server for webhook handling
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuration
config = {
    'database': {
        'host': os.getenv('DB_HOST', 'localhost'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME')
    },
    'crm': {
        'api_url': os.getenv('CRM_API_URL'),
        'api_key': os.getenv('CRM_API_KEY')
    },
    'email_marketing': {
        'api_url': os.getenv('EMAIL_API_URL'),
        'api_key': os.getenv('EMAIL_API_KEY')
    },
    'smtp': {
        'host': os.getenv('SMTP_HOST'),
        'port': int(os.getenv('SMTP_PORT', 587)),
        'username': os.getenv('SMTP_USERNAME'),
        'password': os.getenv('SMTP_PASSWORD'),
        'from_email': os.getenv('FROM_EMAIL')
    },
    'notifications': {
        'pedro_email': os.getenv('PEDRO_EMAIL', 'pedro@topnotchnewjersey.com')
    },
    'sms': {
        'account_sid': os.getenv('TWILIO_ACCOUNT_SID'),
        'auth_token': os.getenv('TWILIO_AUTH_TOKEN'),
        'from_number': os.getenv('TWILIO_FROM_NUMBER'),
        'pedro_number': os.getenv('PEDRO_PHONE_NUMBER')
    },
    'sms_enabled': os.getenv('SMS_NOTIFICATIONS_ENABLED', 'false').lower() == 'true'
}

lead_processor = LeadProcessor(config)

@app.route('/process-lead', methods=['POST'])
def process_lead_webhook():
    """Webhook endpoint for processing leads"""
    try:
        # Verify authentication
        auth_header = request.headers.get('Authorization')
        expected_token = os.getenv('WEBHOOK_TOKEN')
        
        if not auth_header or auth_header != f"Bearer {expected_token}":
            return jsonify({'error': 'Unauthorized'}), 401
        
        # Process lead
        lead_data = request.get_json()
        result = lead_processor.process_lead(lead_data)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
```

---

## 🔧 Configuration Files

### Environment Configuration
```bash
# .env file for automation scripts
# Database Configuration
DB_HOST=localhost
DB_USER=topnotch_user
DB_PASSWORD=secure_password
DB_NAME=topnotch_leads

# CRM Integration
CRM_API_URL=https://api.crm-system.com/v1/contacts
CRM_API_KEY=your_crm_api_key

# Email Marketing
EMAIL_API_URL=https://api.mailchimp.com/3.0
EMAIL_API_KEY=your_mailchimp_api_key

# SMTP Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=pedro@topnotchnewjersey.com
SMTP_PASSWORD=app_specific_password
FROM_EMAIL=pedro@topnotchnewjersey.com

# Notifications
PEDRO_EMAIL=pedro@topnotchnewjersey.com
PEDRO_PHONE_NUMBER=+19085550123

# SMS Configuration (Optional)
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_FROM_NUMBER=+15551234567
SMS_NOTIFICATIONS_ENABLED=true

# Webhook Security
WEBHOOK_TOKEN=secure_random_token_here

# WordPress Integration
WP_API_URL=https://topnotchnewjersey.com/wp-json
WP_API_USER=automation_user
WP_API_PASSWORD=application_password
```

### Database Schema
```sql
-- Lead tracking database schema
CREATE TABLE leads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    service_type VARCHAR(100) NOT NULL,
    budget_range VARCHAR(50),
    timeline VARCHAR(50),
    location VARCHAR(255),
    score INT DEFAULT 0,
    quality ENUM('hot', 'warm', 'cold') DEFAULT 'warm',
    source VARCHAR(50) DEFAULT 'website',
    status ENUM('new', 'contacted', 'qualified', 'converted', 'lost') DEFAULT 'new',
    assigned_to VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_quality (quality),
    INDEX idx_status (status),
    INDEX idx_created_at (created_at)
);

-- Lead activities tracking
CREATE TABLE lead_activities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lead_id INT NOT NULL,
    activity_type VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lead_id) REFERENCES leads(id) ON DELETE CASCADE,
    INDEX idx_lead_id (lead_id),
    INDEX idx_activity_type (activity_type)
);

-- Email sequences tracking
CREATE TABLE email_sequences (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lead_id INT NOT NULL,
    sequence_name VARCHAR(100) NOT NULL,
    email_step INT DEFAULT 1,
    status ENUM('active', 'paused', 'completed') DEFAULT 'active',
    next_send_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lead_id) REFERENCES leads(id) ON DELETE CASCADE,
    INDEX idx_lead_id (lead_id),
    INDEX idx_next_send_date (next_send_date)
);
```

---

## 🚀 Deployment & Monitoring

### Systemd Service Configuration
```ini
# /etc/systemd/system/topnotch-automation.service
[Unit]
Description=Top Notch New Jersey Automation Service
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/var/www/topnotch-automation
Environment=PATH=/var/www/topnotch-automation/venv/bin
ExecStart=/var/www/topnotch-automation/venv/bin/python app.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### Monitoring & Logging
```python
# Enhanced logging configuration
import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging():
    """Configure logging for automation scripts"""
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    log_file = os.getenv('LOG_FILE', '/var/log/topnotch-automation.log')
    
    # Create logger
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, log_level))
    
    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_file, 
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(getattr(logging, log_level))
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Performance monitoring
class PerformanceMonitor:
    def __init__(self):
        self.metrics = {}
    
    def track_lead_processing_time(self, processing_time: float):
        """Track lead processing performance"""
        if 'lead_processing_times' not in self.metrics:
            self.metrics['lead_processing_times'] = []
        
        self.metrics['lead_processing_times'].append(processing_time)
        
        # Keep only last 100 measurements
        if len(self.metrics['lead_processing_times']) > 100:
            self.metrics['lead_processing_times'] = self.metrics['lead_processing_times'][-100:]
    
    def get_average_processing_time(self) -> float:
        """Get average lead processing time"""
        times = self.metrics.get('lead_processing_times', [])
        return sum(times) / len(times) if times else 0.0
    
    def track_api_response_time(self, api_name: str, response_time: float):
        """Track API response times"""
        key = f'{api_name}_response_times'
        if key not in self.metrics:
            self.metrics[key] = []
        
        self.metrics[key].append(response_time)
        
        # Keep only last 50 measurements per API
        if len(self.metrics[key]) > 50:
            self.metrics[key] = self.metrics[key][-50:]
```

---

## 🚀 Implementation Checklist

### Phase 1: Basic Integration
- [ ] Set up Python virtual environment
- [ ] Install required packages
- [ ] Configure environment variables
- [ ] Set up database schema
- [ ] Test basic webhook functionality

### Phase 2: WordPress Integration
- [ ] Install webhook endpoints in WordPress
- [ ] Configure form integration hooks
- [ ] Test lead data flow from forms to scripts
- [ ] Set up authentication and security

### Phase 3: CRM & Email Integration
- [ ] Configure CRM API integration
- [ ] Set up email marketing platform connection
- [ ] Test lead scoring algorithm
- [ ] Configure email sequences

### Phase 4: Notifications & Monitoring
- [ ] Set up email notifications
- [ ] Configure SMS notifications (optional)
- [ ] Implement logging and monitoring
- [ ] Set up performance tracking

### Phase 5: Deployment & Testing
- [ ] Deploy automation service to server
- [ ] Configure systemd service
- [ ] Test end-to-end lead processing
- [ ] Monitor performance and error rates

---

**Automation Scripts Integration Version:** 1.0  
**Last Updated:** June 2024  
**Dependencies:** Python 3.8+, MySQL 8.0+, WordPress 6.0+  
**Estimated Setup Time:** 6-8 hours
