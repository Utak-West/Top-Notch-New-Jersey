# Automation Integration Setup - Top Notch New Jersey

## Python Scripts Integration with WordPress

### Overview
Integration of Python automation scripts from `/scripts/main.py` with WordPress for lead processing, CRM integration, and automated maintenance tasks.

### Prerequisites
```bash
# Server Requirements
- Python 3.8+
- WordPress 6.5+
- WPForms Pro plugin
- Webhook support
- SSL certificate for secure data transmission
```

## Webhook Integration Setup

### WPForms Pro Webhook Configuration
**Purpose:** Send form submissions to Python automation scripts for processing

#### Webhook Settings in WPForms
```
Webhook URL: https://topnotchnewjersey.com/api/webhooks/form-submission
Method: POST
Content Type: application/json
Authentication: Bearer Token (generated)
```

#### Form Submission Webhook Payload
```json
{
  "form_id": "1001",
  "entry_id": "12345",
  "timestamp": "2024-06-15T12:00:00Z",
  "form_data": {
    "service_selection": "kitchen_remodeling",
    "project_scope": "complete_renovation",
    "budget_range": "30k_60k",
    "timeline": "3_months",
    "contact_info": {
      "first_name": "John",
      "last_name": "Smith",
      "email": "john.smith@email.com",
      "phone": "(555) 123-4567",
      "address": "123 Main St, Linden, NJ 07036"
    },
    "project_details": {
      "kitchen_size": "medium",
      "renovation_level": "mid_range",
      "electrical_work": ["outlets", "lighting", "appliances"],
      "special_requirements": "accessibility modifications"
    }
  },
  "lead_source": "website_form",
  "user_agent": "Mozilla/5.0...",
  "ip_address": "192.168.1.100",
  "referrer": "https://google.com/search?q=kitchen+remodeling+nj"
}
```

### WordPress Webhook Handler
```php
<?php
// wp-content/themes/topnotch/functions.php

// Register webhook endpoint
add_action('rest_api_init', function () {
    register_rest_route('topnotch/v1', '/webhook/form-submission', array(
        'methods' => 'POST',
        'callback' => 'handle_form_submission_webhook',
        'permission_callback' => 'verify_webhook_token'
    ));
});

// Verify webhook authentication
function verify_webhook_token($request) {
    $token = $request->get_header('Authorization');
    $expected_token = 'Bearer ' . get_option('topnotch_webhook_token');
    return $token === $expected_token;
}

// Handle form submission webhook
function handle_form_submission_webhook($request) {
    $data = $request->get_json_params();
    
    // Validate required fields
    if (!isset($data['form_id']) || !isset($data['form_data'])) {
        return new WP_Error('invalid_data', 'Missing required fields', array('status' => 400));
    }
    
    // Send to Python automation script
    $response = wp_remote_post('http://localhost:8000/process-lead', array(
        'headers' => array(
            'Content-Type' => 'application/json',
            'Authorization' => 'Bearer ' . get_option('python_api_token')
        ),
        'body' => json_encode($data),
        'timeout' => 30
    ));
    
    if (is_wp_error($response)) {
        error_log('Failed to send data to Python script: ' . $response->get_error_message());
        return new WP_Error('processing_failed', 'Lead processing failed', array('status' => 500));
    }
    
    return array('status' => 'success', 'message' => 'Lead processed successfully');
}

// WPForms integration hook
add_action('wpforms_process_complete', 'send_to_automation_script', 10, 4);

function send_to_automation_script($fields, $entry, $form_data, $entry_id) {
    // Prepare data for webhook
    $webhook_data = array(
        'form_id' => $form_data['id'],
        'entry_id' => $entry_id,
        'timestamp' => current_time('c'),
        'form_data' => format_form_data($fields),
        'lead_source' => 'website_form',
        'user_agent' => $_SERVER['HTTP_USER_AGENT'] ?? '',
        'ip_address' => $_SERVER['REMOTE_ADDR'] ?? '',
        'referrer' => $_SERVER['HTTP_REFERER'] ?? ''
    );
    
    // Trigger webhook
    do_action('topnotch_form_submission', $webhook_data);
}

function format_form_data($fields) {
    $formatted = array();
    
    foreach ($fields as $field) {
        switch ($field['type']) {
            case 'name':
                $formatted['contact_info']['first_name'] = $field['first'] ?? '';
                $formatted['contact_info']['last_name'] = $field['last'] ?? '';
                break;
            case 'email':
                $formatted['contact_info']['email'] = $field['value'] ?? '';
                break;
            case 'phone':
                $formatted['contact_info']['phone'] = $field['value'] ?? '';
                break;
            case 'address':
                $formatted['contact_info']['address'] = $field['address1'] ?? '';
                break;
            case 'select':
                if ($field['name'] === 'service_selection') {
                    $formatted['service_selection'] = $field['value'];
                } elseif ($field['name'] === 'budget_range') {
                    $formatted['budget_range'] = $field['value'];
                }
                break;
            case 'checkbox':
                if ($field['name'] === 'electrical_work') {
                    $formatted['project_details']['electrical_work'] = $field['value'];
                }
                break;
        }
    }
    
    return $formatted;
}
?>
```

## Python Automation Script Integration

### Enhanced main.py Configuration
```python
# /scripts/main.py enhancements for WordPress integration

import asyncio
import aiohttp
import json
import logging
from datetime import datetime
from typing import Dict, Any
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class WordPressIntegration:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.wp_api_url = config.get('wordpress_api_url', 'https://topnotchnewjersey.com/wp-json/wp/v2/')
        self.wp_auth_token = config.get('wordpress_auth_token')
        self.logger = logging.getLogger(__name__)
    
    async def process_form_submission(self, webhook_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process incoming form submission from WordPress webhook"""
        try:
            # Calculate lead score
            lead_score = self.calculate_lead_score(webhook_data['form_data'])
            
            # Classify lead priority
            lead_priority = self.classify_lead_priority(lead_score)
            
            # Send notifications
            await self.send_notifications(webhook_data, lead_score, lead_priority)
            
            # Store in CRM
            crm_result = await self.store_in_crm(webhook_data, lead_score)
            
            # Update WordPress with lead score
            await self.update_wordpress_lead_data(webhook_data['entry_id'], {
                'lead_score': lead_score,
                'lead_priority': lead_priority,
                'processing_timestamp': datetime.now().isoformat()
            })
            
            return {
                'status': 'success',
                'lead_score': lead_score,
                'lead_priority': lead_priority,
                'crm_id': crm_result.get('id')
            }
            
        except Exception as e:
            self.logger.error(f"Error processing form submission: {str(e)}")
            return {'status': 'error', 'message': str(e)}
    
    def calculate_lead_score(self, form_data: Dict[str, Any]) -> int:
        """Calculate lead score based on form responses"""
        score = 0
        
        # Service Type Scoring (0-30 points)
        service_scores = {
            'complete_home': 30,
            'kitchen_remodeling': 20,
            'bathroom_renovation': 15
        }
        score += service_scores.get(form_data.get('service_selection'), 0)
        
        # Budget Range Scoring (0-25 points)
        budget_scores = {
            'over_100k': 25,
            '60k_100k': 20,
            '30k_60k': 15,
            '15k_30k': 10,
            'under_15k': 5
        }
        score += budget_scores.get(form_data.get('budget_range'), 0)
        
        # Timeline Urgency Scoring (0-20 points)
        timeline_scores = {
            'asap': 20,
            '1_month': 15,
            '3_months': 10,
            '6_months': 5,
            'planning': 2
        }
        score += timeline_scores.get(form_data.get('timeline'), 0)
        
        # Project Scope Scoring (0-15 points)
        scope_scores = {
            'complete_renovation': 15,
            'major_updates': 10,
            'refresh': 5
        }
        score += scope_scores.get(form_data.get('project_scope'), 0)
        
        # Location Scoring (0-10 points)
        if 'contact_info' in form_data and 'address' in form_data['contact_info']:
            address = form_data['contact_info']['address'].lower()
            if any(city in address for city in ['linden', 'elizabeth', 'westfield']):
                score += 10  # Primary service area
            elif any(county in address for county in ['union', 'essex', 'middlesex', 'bergen']):
                score += 7   # Secondary service area
            else:
                score += 3   # Extended service area
        
        return min(score, 100)  # Cap at 100 points
    
    def classify_lead_priority(self, lead_score: int) -> str:
        """Classify lead priority based on score"""
        if lead_score >= 80:
            return 'HOT'
        elif lead_score >= 60:
            return 'WARM'
        elif lead_score >= 40:
            return 'QUALIFIED'
        else:
            return 'COLD'
    
    async def send_notifications(self, webhook_data: Dict[str, Any], lead_score: int, priority: str):
        """Send email notifications to Pedro and customer"""
        
        # Admin notification to Pedro
        admin_subject = f"[{priority} LEAD - Score: {lead_score}] New {webhook_data['form_data'].get('service_selection', 'Unknown')} Inquiry"
        admin_body = self.format_admin_notification(webhook_data, lead_score, priority)
        
        await self.send_email(
            to_email=self.config['admin_email'],
            subject=admin_subject,
            body=admin_body,
            is_html=True
        )
        
        # Customer auto-responder
        customer_email = webhook_data['form_data'].get('contact_info', {}).get('email')
        if customer_email:
            customer_subject = "Your Free Estimate Request - Top Notch New Jersey"
            customer_body = self.format_customer_autoresponder(webhook_data)
            
            await self.send_email(
                to_email=customer_email,
                subject=customer_subject,
                body=customer_body,
                is_html=True
            )
    
    def format_admin_notification(self, webhook_data: Dict[str, Any], lead_score: int, priority: str) -> str:
        """Format admin notification email"""
        form_data = webhook_data['form_data']
        contact_info = form_data.get('contact_info', {})
        
        return f"""
        <html>
        <body>
            <h2>New Lead Alert - {priority} Priority</h2>
            <p><strong>Lead Score:</strong> {lead_score}/100</p>
            
            <h3>Contact Information</h3>
            <ul>
                <li><strong>Name:</strong> {contact_info.get('first_name', '')} {contact_info.get('last_name', '')}</li>
                <li><strong>Email:</strong> {contact_info.get('email', '')}</li>
                <li><strong>Phone:</strong> {contact_info.get('phone', '')}</li>
                <li><strong>Address:</strong> {contact_info.get('address', '')}</li>
            </ul>
            
            <h3>Project Details</h3>
            <ul>
                <li><strong>Service:</strong> {form_data.get('service_selection', '')}</li>
                <li><strong>Budget Range:</strong> {form_data.get('budget_range', '')}</li>
                <li><strong>Timeline:</strong> {form_data.get('timeline', '')}</li>
                <li><strong>Project Scope:</strong> {form_data.get('project_scope', '')}</li>
            </ul>
            
            <h3>Lead Source Information</h3>
            <ul>
                <li><strong>Source:</strong> {webhook_data.get('lead_source', '')}</li>
                <li><strong>Referrer:</strong> {webhook_data.get('referrer', '')}</li>
                <li><strong>Timestamp:</strong> {webhook_data.get('timestamp', '')}</li>
            </ul>
            
            <p><strong>Recommended Action:</strong> 
            {'Contact within 1 hour' if priority == 'HOT' else 
             'Contact within 4 hours' if priority == 'WARM' else 
             'Contact within 24 hours' if priority == 'QUALIFIED' else 
             'Contact within 48 hours'}</p>
        </body>
        </html>
        """
    
    def format_customer_autoresponder(self, webhook_data: Dict[str, Any]) -> str:
        """Format customer auto-responder email"""
        form_data = webhook_data['form_data']
        contact_info = form_data.get('contact_info', {})
        first_name = contact_info.get('first_name', 'there')
        
        return f"""
        <html>
        <body>
            <h2>Thank you for your interest, {first_name}!</h2>
            
            <p>We received your request for a free estimate for your {form_data.get('service_selection', 'home improvement')} project.</p>
            
            <h3>What happens next:</h3>
            <ol>
                <li><strong>Quick Response:</strong> Pedro will personally contact you within 2 hours during business hours</li>
                <li><strong>Free Consultation:</strong> We'll schedule a convenient time for an in-home assessment</li>
                <li><strong>Detailed Estimate:</strong> You'll receive a comprehensive written estimate with no obligation</li>
            </ol>
            
            <h3>Your Project Details:</h3>
            <ul>
                <li><strong>Service:</strong> {form_data.get('service_selection', '')}</li>
                <li><strong>Timeline:</strong> {form_data.get('timeline', '')}</li>
            </ul>
            
            <h3>Contact Information:</h3>
            <p><strong>Phone:</strong> (XXX) XXX-XXXX<br>
            <strong>Email:</strong> info@topnotchnewjersey.com</p>
            
            <p><strong>Business Hours:</strong><br>
            Monday-Friday: 8AM-6PM<br>
            Saturday: 9AM-4PM</p>
            
            <p>Thank you for considering Top Notch New Jersey for your home improvement project!</p>
            
            <p>Best regards,<br>
            Pedro Ribeiro<br>
            Licensed Home Improvement Contractor<br>
            Top Notch New Jersey</p>
        </body>
        </html>
        """
    
    async def send_email(self, to_email: str, subject: str, body: str, is_html: bool = False):
        """Send email using SMTP"""
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.config['smtp_from_email']
            msg['To'] = to_email
            
            if is_html:
                msg.attach(MIMEText(body, 'html'))
            else:
                msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.config['smtp_server'], self.config['smtp_port']) as server:
                server.starttls()
                server.login(self.config['smtp_username'], self.config['smtp_password'])
                server.send_message(msg)
                
            self.logger.info(f"Email sent successfully to {to_email}")
            
        except Exception as e:
            self.logger.error(f"Failed to send email to {to_email}: {str(e)}")
    
    async def store_in_crm(self, webhook_data: Dict[str, Any], lead_score: int) -> Dict[str, Any]:
        """Store lead data in CRM system"""
        crm_data = {
            'id': f"lead_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            'timestamp': webhook_data.get('timestamp'),
            'contact_info': webhook_data['form_data'].get('contact_info', {}),
            'project_details': webhook_data['form_data'],
            'lead_score': lead_score,
            'lead_source': webhook_data.get('lead_source'),
            'status': 'new'
        }
        
        self.logger.info(f"Stored lead in CRM: {crm_data['id']}")
        return crm_data
    
    async def update_wordpress_lead_data(self, entry_id: str, data: Dict[str, Any]):
        """Update WordPress entry with processed lead data"""
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.wp_api_url}wpforms-entries/{entry_id}"
                headers = {
                    'Authorization': f'Bearer {self.wp_auth_token}',
                    'Content-Type': 'application/json'
                }
                
                async with session.patch(url, json=data, headers=headers) as response:
                    if response.status == 200:
                        self.logger.info(f"Updated WordPress entry {entry_id} with lead data")
                    else:
                        self.logger.error(f"Failed to update WordPress entry: {response.status}")
                        
        except Exception as e:
            self.logger.error(f"Error updating WordPress entry: {str(e)}")

# FastAPI server for webhook handling
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
wp_integration = WordPressIntegration(config={
    'admin_email': 'pedro@topnotchnewjersey.com',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'smtp_username': 'notifications@topnotchnewjersey.com',
    'smtp_password': 'app_password',
    'smtp_from_email': 'notifications@topnotchnewjersey.com',
    'wordpress_api_url': 'https://topnotchnewjersey.com/wp-json/wp/v2/',
    'wordpress_auth_token': 'wp_auth_token'
})

class WebhookData(BaseModel):
    form_id: str
    entry_id: str
    timestamp: str
    form_data: dict
    lead_source: str
    user_agent: str = ""
    ip_address: str = ""
    referrer: str = ""

@app.post("/process-lead")
async def process_lead(data: WebhookData):
    """Process lead from WordPress webhook"""
    try:
        result = await wp_integration.process_form_submission(data.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## Implementation Checklist

### Phase 1: Basic Integration Setup
- [ ] Install FastAPI and dependencies
- [ ] Create webhook endpoint for form submissions
- [ ] Implement lead scoring algorithm
- [ ] Set up email notification system
- [ ] Test basic webhook functionality

### Phase 2: WordPress Integration
- [ ] Configure WPForms Pro webhooks
- [ ] Set up WordPress API authentication
- [ ] Implement form data processing
- [ ] Test end-to-end form submission flow
- [ ] Configure error handling and logging

### Phase 3: CRM Integration
- [ ] Choose and configure CRM system
- [ ] Implement CRM API integration
- [ ] Set up lead data synchronization
- [ ] Test CRM lead creation
- [ ] Configure lead status updates

### Phase 4: Security and Monitoring
- [ ] Implement API authentication
- [ ] Set up rate limiting
- [ ] Configure SSL certificates
- [ ] Implement health check endpoints
- [ ] Set up monitoring and alerting

### Phase 5: Testing and Deployment
- [ ] Write unit tests for all components
- [ ] Create integration tests
- [ ] Set up staging environment
- [ ] Deploy to production server
- [ ] Configure monitoring and logging

---

**Automation Integration Setup Version:** 1.0  
**Last Updated:** June 2024  
**Dependencies:** FastAPI, WordPress 6.5+, WPForms Pro  
**Security:** JWT authentication, rate limiting, SSL required
