# Top Notch New Jersey - WordPress Automation Scripts

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![WordPress](https://img.shields.io/badge/WordPress-5.0+-blue.svg)](https://wordpress.org/)
[![Elementor Pro](https://img.shields.io/badge/Elementor-Pro-orange.svg)](https://elementor.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Comprehensive WordPress/Elementor automation suite for Top Notch New Jersey's home improvement business, specializing in kitchen and bathroom renovation lead generation and site optimization.**

## 🏠 About Top Notch New Jersey

Top Notch New Jersey is Pedro Ribeiro's premier home improvement company, specializing in kitchen and bathroom remodeling throughout New Jersey. As a Licensed Home Improvement Contractor, Pedro offers expert project coordination with high-quality renovations.

## 🚀 Features

### 🔧 Elementor Troubleshooting & Optimization
- **Performance Monitoring**: Automated detection of slow-loading galleries and sliders
- **Issue Resolution**: Auto-fix common Elementor problems affecting lead generation
- **Mobile Optimization**: Ensure responsive design for 60%+ mobile traffic
- **Before/After Sliders**: Specialized optimization for renovation showcases
- **Contact Form Validation**: Critical lead capture form troubleshooting

### 🔗 Advanced Webhook Integration
- **Multi-Form Support**: Elementor, Contact Form 7, Gravity Forms integration
- **Lead Scoring**: AI-powered scoring based on renovation keywords and urgency
- **Data Enrichment**: Contact information enhancement and property analysis
- **CRM Integration**: Automated lead routing to HubSpot, Salesforce, etc.
- **Follow-up Automation**: Priority-based automated sequences

### 🛡️ WordPress Security & Maintenance
- **Security Hardening**: Automated vulnerability scanning and fixes
- **Performance Optimization**: Database cleanup, image optimization, caching
- **Backup Management**: Automated site and database backups
- **Update Management**: Safe plugin and theme updates
- **SEO Monitoring**: Local SEO optimization for New Jersey market

### 📊 Business Intelligence
- **Lead Analytics**: Track conversion rates and lead quality
- **Performance Metrics**: Monitor site speed and user engagement
- **ROI Tracking**: Measure automation impact on business growth
- **Reporting**: Automated email reports for business insights

## 📁 Directory Structure

```
scripts/
├── 📂 config/                    # Configuration management
│   ├── __init__.py              # Configuration module
│   ├── settings.py              # Settings and environment handling
│   └── production.json          # Production configuration template
├── 📂 elementor/                # Elementor troubleshooting
│   ├── __init__.py              # Elementor module
│   └── troubleshooter.py        # Main troubleshooting engine
├── 📂 webhooks/                 # Webhook integration system
│   ├── __init__.py              # Webhooks module
│   ├── contact_form_handler.py  # Lead processing and scoring
│   └── integration_manager.py   # Multi-form integration management
├── 📂 wordpress/                # WordPress maintenance
│   ├── __init__.py              # WordPress module
│   └── maintenance.py           # Maintenance and optimization
├── 📂 utils/                    # Utility functions
│   ├── __init__.py              # Utils module
│   ├── logger.py                # Business-context logging
│   └── email_notifier.py        # Email notification system
├── 📂 tests/                    # Comprehensive test suite
│   ├── __init__.py              # Test module
│   ├── test_elementor.py        # Elementor tests
│   └── test_webhooks.py         # Webhook tests
├── 📂 demos/                    # Interactive demonstrations
│   └── demo_runner.py           # Demo script runner
├── 📂 logs/                     # Log files (auto-created)
├── 📂 reports/                  # Generated reports (auto-created)
├── main.py                      # Main entry point
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🛠 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- WordPress 5.0+ with Elementor Pro
- MySQL/MariaDB database access
- SMTP server for email notifications

### 1. Environment Setup

```bash
# Clone or download the scripts
cd /path/to/Top-Notch-New-Jersey/scripts

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Create a `.env` file in the scripts directory:

```bash
# WordPress Configuration
WP_ADMIN_USER=your_admin_username
WP_ADMIN_PASSWORD=your_admin_password

# Database Configuration
DB_HOST=localhost
DB_NAME=your_wordpress_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password

# Email Configuration
SMTP_HOST=smtp.gmail.com
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password

# API Keys (Optional)
ENRICHMENT_API_KEY=your_enrichment_api_key
CRM_WEBHOOK_URL=https://your-crm.com/webhook
EMAIL_SERVICE_KEY=your_email_service_key

# Business Information
BUSINESS_PHONE=(908) 555-1234
```

### 3. WordPress Integration

Add the webhook endpoint to your WordPress site by adding this to your theme's `functions.php`:

```php
// Add this code to your theme's functions.php file
add_action('rest_api_init', function () {
    register_rest_route('topnotch/v1', '/contact-form', array(
        'methods' => 'POST',
        'callback' => 'tnj_handle_contact_form',
        'permission_callback' => '__return_true'
    ));
});

function tnj_handle_contact_form($request) {
    $data = $request->get_json_params();
    
    // Forward to Python webhook handler
    $webhook_url = 'http://your-server.com:8000/webhook/contact-form';
    
    $response = wp_remote_post($webhook_url, array(
        'headers' => array('Content-Type' => 'application/json'),
        'body' => json_encode($data),
        'timeout' => 30
    ));
    
    return rest_ensure_response(array('success' => true));
}
```

## 🎯 Usage Examples

### Basic Usage

```bash
# Run all maintenance tasks
python main.py --task all

# Run specific tasks
python main.py --task elementor
python main.py --task webhooks
python main.py --task maintenance

# Dry run (preview changes without executing)
python main.py --dry-run

# Verbose logging
python main.py --verbose

# Send email report after completion
python main.py --email-report
```

### Advanced Usage

```bash
# Use custom configuration
python main.py --config config/staging.json

# Run specific Elementor optimizations
python -c "
from elementor.troubleshooter import ElementorTroubleshooter
from config.settings import load_config

config = load_config()
troubleshooter = ElementorTroubleshooter(config)
troubleshooter.optimize_for_home_renovation()
"

# Test webhook integration
python -c "
from webhooks.contact_form_handler import ContactFormHandler
from config.settings import load_config

config = load_config()
handler = ContactFormHandler(config)

# Process sample lead
sample_lead = {
    'name': 'John Smith',
    'email': 'john@email.com',
    'phone': '(908) 555-1234',
    'message': 'Need kitchen renovation quote ASAP'
}

result = handler.process_form_submission(sample_lead)
print(f'Lead Score: {result[\"lead_score\"]}/100')
"
```

### Demo Mode

```bash
# Run interactive demo
python demos/demo_runner.py

# Run specific demo
python demos/demo_runner.py --demo elementor
python demos/demo_runner.py --demo webhooks
python demos/demo_runner.py --demo maintenance

# Interactive mode
python demos/demo_runner.py --interactive
```

## 🧪 Testing

### Run Test Suite

```bash
# Run all tests
pytest tests/

# Run specific test modules
pytest tests/test_elementor.py
pytest tests/test_webhooks.py

# Run with coverage
pytest tests/ --cov=. --cov-report=html

# Run performance tests
pytest tests/ -m performance
```

### Test Categories

- **Unit Tests**: Individual component testing
- **Integration Tests**: System interaction testing
- **Performance Tests**: Speed and efficiency validation
- **Security Tests**: Vulnerability assessment
- **Business Logic Tests**: Home improvement specific validation

## 📊 Monitoring & Analytics

### Log Files

Logs are automatically created in the `logs/` directory:

- `topnotch_automation_YYYYMMDD.log` - General automation logs
- `topnotch_errors_YYYYMMDD.log` - Error-specific logs
- Business events are logged with special formatting for analytics

### Reports

Diagnostic reports are saved in the `reports/` directory:

- `elementor_diagnostics_YYYYMMDD_HHMMSS.json` - Elementor analysis
- `webhook_performance_YYYYMMDD.json` - Webhook metrics
- `maintenance_summary_YYYYMMDD.json` - Maintenance results

### Email Notifications

Automated email reports include:

- **Daily**: Critical issues and security alerts
- **Weekly**: Performance summaries and recommendations
- **Monthly**: Business intelligence and ROI analysis

## 🔧 Customization

### Lead Scoring Configuration

Modify lead scoring keywords in `config/production.json`:

```json
{
  "business": {
    "lead_scoring_keywords": {
      "kitchen": 10,
      "bathroom": 10,
      "renovation": 8,
      "quote": 15,
      "estimate": 15,
      "urgent": 20,
      "electrical": 7,
      "pedro": 5
    }
  }
}
```

### Service Area Configuration

Update service areas for location-based scoring:

```json
{
  "business": {
    "service_areas": [
      "Union County",
      "Essex County", 
      "Middlesex County",
      "Bergen County"
    ]
  }
}
```

## 🚨 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'config'`
**Solution**: Ensure you're running from the scripts directory and have activated the virtual environment.

**Issue**: Database connection errors
**Solution**: Verify database credentials in `.env` file and ensure MySQL/MariaDB is running.

**Issue**: Webhook integration not working
**Solution**: Check WordPress REST API is enabled and the endpoint is properly registered.

**Issue**: Email notifications not sending
**Solution**: Verify SMTP configuration and app passwords for Gmail.

### Debug Mode

Enable debug logging:

```bash
python main.py --verbose --task all
```

Check log files in `logs/` directory for detailed error information.

## 📞 Support

For technical support or business inquiries:

- **Email**: info@topnotchnewjersey.com
- **Phone**: [Business Phone Number]
- **License**: NJ Home Improvement Contractor #13VH13

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

---

**Ready to transform your home improvement business with automation? Contact Top Notch New Jersey today!**
