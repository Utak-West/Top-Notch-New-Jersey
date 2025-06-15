# WPForms Pro Configuration - Top Notch New Jersey

## 📝 Advanced Lead Capture Form Setup

### Purpose
Configure WPForms Pro to create a comprehensive, multi-step lead capture form that maximizes conversion from inquiry to signed contract for kitchen and bathroom renovation projects.

---

## 🎯 Form Objectives

### Primary Goals
- Capture qualified leads for kitchen remodeling and bathroom renovation services
- Gather sufficient project details to provide accurate estimates
- Segment leads by service type, budget, and timeline for personalized follow-up
- Maintain high completion rates through intuitive UX design

### Target Metrics
- Form completion rate: 15-25%
- Lead qualification rate: 60%+ qualified leads
- Response time: <2 hours during business hours
- Conversion to consultation: 40%+ of form submissions

---

## 🏗️ Multi-Step Form Structure

### Step 1: Service Selection
**Layout:** Radio buttons with visual icons

```json
{
  "step_1": {
    "title": "What service do you need?",
    "subtitle": "Select the primary service for your project",
    "fields": [
      {
        "type": "radio",
        "name": "service_type",
        "label": "Service Type",
        "required": true,
        "options": [
          {
            "value": "kitchen_remodeling",
            "label": "Kitchen Remodeling",
            "description": "Complete kitchen transformations and updates",
            "icon": "kitchen-icon.svg"
          },
          {
            "value": "bathroom_renovation",
            "label": "Bathroom Renovation", 
            "description": "Luxury spa bathrooms and accessibility upgrades",
            "icon": "bathroom-icon.svg"
          },
          {
            "value": "complete_home_remodel",
            "label": "Complete Home Remodel",
            "description": "Multi-room renovation projects",
            "icon": "home-icon.svg"
          },
          {
            "value": "multiple_rooms",
            "label": "Multiple Rooms/Services",
            "description": "Kitchen, bathroom, and other areas",
            "icon": "multiple-icon.svg"
          }
        ]
      }
    ]
  }
}
```

### Step 2: Project Details (Conditional Logic)
**Layout:** Dynamic fields based on service selection

```json
{
  "step_2": {
    "title": "Tell us about your project",
    "subtitle": "Help us understand your vision and requirements",
    "conditional_fields": {
      "kitchen_remodeling": [
        {
          "type": "radio",
          "name": "kitchen_scope",
          "label": "Project Scope",
          "required": true,
          "options": [
            {"value": "full_remodel", "label": "Full Kitchen Remodel"},
            {"value": "kitchen_refresh", "label": "Kitchen Refresh/Update"},
            {"value": "cabinet_only", "label": "Cabinets Only"},
            {"value": "countertops_only", "label": "Countertops Only"}
          ]
        },
        {
          "type": "checkbox",
          "name": "kitchen_features",
          "label": "Desired Features",
          "options": [
            {"value": "island", "label": "Kitchen Island"},
            {"value": "pantry", "label": "Walk-in Pantry"},
            {"value": "breakfast_nook", "label": "Breakfast Nook"},
            {"value": "open_concept", "label": "Open Concept Layout"},
            {"value": "smart_appliances", "label": "Smart Appliances"},
            {"value": "wine_storage", "label": "Wine Storage"}
          ]
        },
        {
          "type": "select",
          "name": "kitchen_condition",
          "label": "Current Kitchen Condition",
          "required": true,
          "options": [
            {"value": "excellent", "label": "Excellent - Minor updates needed"},
            {"value": "good", "label": "Good - Some updates needed"},
            {"value": "fair", "label": "Fair - Significant updates needed"},
            {"value": "poor", "label": "Poor - Complete renovation needed"}
          ]
        }
      ],
      "bathroom_renovation": [
        {
          "type": "radio",
          "name": "bathroom_scope",
          "label": "Renovation Type",
          "required": true,
          "options": [
            {"value": "full_renovation", "label": "Full Bathroom Renovation"},
            {"value": "luxury_spa", "label": "Luxury Spa Bathroom"},
            {"value": "accessibility", "label": "Accessibility Modifications"},
            {"value": "powder_room", "label": "Powder Room Update"}
          ]
        },
        {
          "type": "checkbox",
          "name": "bathroom_features",
          "label": "Desired Features",
          "options": [
            {"value": "walk_in_shower", "label": "Walk-in Shower"},
            {"value": "soaking_tub", "label": "Soaking Tub"},
            {"value": "double_vanity", "label": "Double Vanity"},
            {"value": "heated_floors", "label": "Heated Floors"},
            {"value": "smart_mirror", "label": "Smart Mirror"},
            {"value": "steam_shower", "label": "Steam Shower"}
          ]
        },
        {
          "type": "radio",
          "name": "accessibility_needs",
          "label": "Accessibility Requirements",
          "options": [
            {"value": "none", "label": "No special requirements"},
            {"value": "grab_bars", "label": "Grab bars and safety features"},
            {"value": "walk_in_shower", "label": "Walk-in shower access"},
            {"value": "full_ada", "label": "Full ADA compliance needed"}
          ]
        }
      ]
    }
  }
}
```

### Step 3: Investment & Timeline
**Layout:** Budget and timeline selection

```json
{
  "step_3": {
    "title": "Investment and Timeline",
    "subtitle": "Help us provide the most accurate estimate",
    "fields": [
      {
        "type": "select",
        "name": "budget_range",
        "label": "Investment Range",
        "required": true,
        "options": [
          {"value": "under_15k", "label": "Under $15,000"},
          {"value": "15k_30k", "label": "$15,000 - $30,000"},
          {"value": "30k_60k", "label": "$30,000 - $60,000"},
          {"value": "60k_100k", "label": "$60,000 - $100,000"},
          {"value": "100k_plus", "label": "$100,000+"},
          {"value": "not_sure", "label": "Not sure yet"}
        ]
      },
      {
        "type": "select",
        "name": "timeline",
        "label": "Desired Timeline",
        "required": true,
        "options": [
          {"value": "asap", "label": "ASAP (Within 1 month)"},
          {"value": "1_3_months", "label": "1-3 months"},
          {"value": "3_6_months", "label": "3-6 months"},
          {"value": "6_plus_months", "label": "6+ months"},
          {"value": "planning_phase", "label": "Planning phase"}
        ]
      },
      {
        "type": "radio",
        "name": "financing_interest",
        "label": "Financing Interest",
        "options": [
          {"value": "yes", "label": "Yes, I'm interested in financing options"},
          {"value": "no", "label": "No, I plan to pay in full"},
          {"value": "maybe", "label": "Maybe, I'd like to learn more"}
        ]
      }
    ]
  }
}
```

### Step 4: Contact Information
**Layout:** Contact details and preferences

```json
{
  "step_4": {
    "title": "Contact Information",
    "subtitle": "How can Pedro reach you with your estimate?",
    "fields": [
      {
        "type": "text",
        "name": "first_name",
        "label": "First Name",
        "required": true,
        "width": "50%"
      },
      {
        "type": "text",
        "name": "last_name",
        "label": "Last Name",
        "required": true,
        "width": "50%"
      },
      {
        "type": "phone",
        "name": "phone",
        "label": "Phone Number",
        "required": true,
        "format": "(999) 999-9999",
        "width": "50%"
      },
      {
        "type": "email",
        "name": "email",
        "label": "Email Address",
        "required": true,
        "width": "50%"
      },
      {
        "type": "address",
        "name": "property_address",
        "label": "Property Address",
        "required": false,
        "fields": {
          "address_line_1": true,
          "city": true,
          "state": true,
          "zip": true,
          "country": false
        },
        "description": "Helps us verify service area coverage"
      },
      {
        "type": "radio",
        "name": "preferred_contact",
        "label": "Preferred Contact Method",
        "required": true,
        "options": [
          {"value": "phone", "label": "Phone call"},
          {"value": "text", "label": "Text message"},
          {"value": "email", "label": "Email"},
          {"value": "any", "label": "Any method is fine"}
        ]
      },
      {
        "type": "select",
        "name": "best_time",
        "label": "Best Time to Contact",
        "options": [
          {"value": "morning", "label": "Morning (7 AM - 12 PM)"},
          {"value": "afternoon", "label": "Afternoon (12 PM - 5 PM)"},
          {"value": "evening", "label": "Evening (5 PM - 7 PM)"},
          {"value": "weekend", "label": "Weekend"},
          {"value": "anytime", "label": "Anytime"}
        ]
      },
      {
        "type": "select",
        "name": "how_found_us",
        "label": "How did you find us?",
        "options": [
          {"value": "google_search", "label": "Google search"},
          {"value": "referral", "label": "Referral from friend/family"},
          {"value": "social_media", "label": "Social media"},
          {"value": "local_directory", "label": "Local directory"},
          {"value": "previous_customer", "label": "Previous customer"},
          {"value": "other", "label": "Other"}
        ]
      }
    ]
  }
}
```

---

## 🎨 Form Design & UX

### Mobile-Responsive Design
```css
/* WPForms mobile optimization */
.wpforms-container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
}

.wpforms-field {
    margin-bottom: 24px;
}

.wpforms-field input,
.wpforms-field select,
.wpforms-field textarea {
    font-size: 16px !important; /* Prevent iOS zoom */
    min-height: 44px;
    padding: 12px 16px;
    border: 2px solid #E5E7EB;
    border-radius: 8px;
    transition: border-color 0.3s ease;
}

.wpforms-field input:focus,
.wpforms-field select:focus,
.wpforms-field textarea:focus {
    border-color: #1B365D;
    box-shadow: 0 0 0 3px rgba(27, 54, 93, 0.1);
    outline: none;
}

/* Multi-step progress indicator */
.wpforms-progress-bar {
    background-color: #F3F4F6;
    height: 8px;
    border-radius: 4px;
    margin-bottom: 32px;
    overflow: hidden;
}

.wpforms-progress-bar-fill {
    background: linear-gradient(90deg, #1B365D 0%, #10B981 100%);
    height: 100%;
    transition: width 0.3s ease;
}

/* Service selection with icons */
.wpforms-field-radio .wpforms-field-choice {
    display: flex;
    align-items: center;
    padding: 16px;
    border: 2px solid #E5E7EB;
    border-radius: 12px;
    margin-bottom: 12px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.wpforms-field-radio .wpforms-field-choice:hover {
    border-color: #1B365D;
    background-color: #F8FAFC;
}

.wpforms-field-radio .wpforms-field-choice.selected {
    border-color: #10B981;
    background-color: #ECFDF5;
}

/* Touch-friendly buttons */
.wpforms-submit {
    background-color: #10B981 !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 16px 32px !important;
    font-size: 18px !important;
    font-weight: 600 !important;
    min-height: 48px !important;
    width: 100% !important;
    cursor: pointer !important;
    transition: background-color 0.3s ease !important;
}

.wpforms-submit:hover {
    background-color: #0D9668 !important;
}

@media (max-width: 768px) {
    .wpforms-container {
        padding: 16px;
    }
    
    .wpforms-field-row {
        flex-direction: column;
    }
    
    .wpforms-field-row .wpforms-field {
        width: 100% !important;
        margin-right: 0 !important;
    }
}
```

### Progress Indicator
```html
<!-- Multi-step progress indicator -->
<div class="wpforms-progress-container">
    <div class="wpforms-progress-bar">
        <div class="wpforms-progress-bar-fill" style="width: 25%;"></div>
    </div>
    <div class="wpforms-progress-text">
        Step 1 of 4: Service Selection
    </div>
</div>
```

---

## 🔧 Lead Scoring Algorithm

### Automatic Lead Scoring
```php
// WPForms lead scoring hook
add_action('wpforms_process_complete', 'topnotch_lead_scoring', 10, 4);
function topnotch_lead_scoring($fields, $entry, $form_data, $entry_id) {
    $score = 0;
    
    // Budget scoring
    $budget = $fields[5]['value'] ?? '';
    switch($budget) {
        case '100k_plus': $score += 50; break;
        case '60k_100k': $score += 40; break;
        case '30k_60k': $score += 30; break;
        case '15k_30k': $score += 20; break;
        case 'under_15k': $score += 10; break;
        case 'not_sure': $score += 15; break;
    }
    
    // Timeline scoring
    $timeline = $fields[6]['value'] ?? '';
    switch($timeline) {
        case 'asap': $score += 30; break;
        case '1_3_months': $score += 25; break;
        case '3_6_months': $score += 20; break;
        case '6_plus_months': $score += 10; break;
        case 'planning_phase': $score += 5; break;
    }
    
    // Service type scoring
    $service = $fields[1]['value'] ?? '';
    switch($service) {
        case 'complete_home_remodel': $score += 25; break;
        case 'multiple_rooms': $score += 20; break;
        case 'kitchen_remodeling': $score += 15; break;
        case 'bathroom_renovation': $score += 15; break;
    }
    
    // Location scoring (service area)
    $address = $fields[9]['value'] ?? '';
    if (stripos($address, 'Union') !== false || 
        stripos($address, 'Linden') !== false) {
        $score += 15;
    } elseif (stripos($address, 'Essex') !== false || 
              stripos($address, 'Middlesex') !== false || 
              stripos($address, 'Bergen') !== false) {
        $score += 10;
    }
    
    // Determine lead quality
    if ($score >= 70) {
        $lead_quality = 'hot';
        $priority = 'high';
    } elseif ($score >= 50) {
        $lead_quality = 'warm';
        $priority = 'medium';
    } else {
        $lead_quality = 'cold';
        $priority = 'low';
    }
    
    // Store lead score
    update_post_meta($entry_id, 'lead_score', $score);
    update_post_meta($entry_id, 'lead_quality', $lead_quality);
    update_post_meta($entry_id, 'priority', $priority);
    
    // Send priority notification for hot leads
    if ($lead_quality === 'hot') {
        topnotch_send_priority_notification($fields, $score);
    }
}
```

---

## 📧 Email Integration & Automation

### Immediate Notifications
```php
// Instant notification to Pedro
add_action('wpforms_process_complete', 'topnotch_instant_notification', 10, 4);
function topnotch_instant_notification($fields, $entry, $form_data, $entry_id) {
    $name = $fields[7]['value'] . ' ' . $fields[8]['value'];
    $phone = $fields[9]['value'];
    $email = $fields[10]['value'];
    $service = $fields[1]['value'];
    $budget = $fields[5]['value'];
    $timeline = $fields[6]['value'];
    
    $subject = "🔥 New Lead: $service - $name";
    
    $message = "
    New estimate request received!
    
    CONTACT INFO:
    Name: $name
    Phone: $phone
    Email: $email
    
    PROJECT DETAILS:
    Service: $service
    Budget: $budget
    Timeline: $timeline
    
    Lead Score: " . get_post_meta($entry_id, 'lead_score', true) . "
    Priority: " . get_post_meta($entry_id, 'priority', true) . "
    
    View full details in WordPress admin.
    ";
    
    wp_mail('pedro@topnotchnewjersey.com', $subject, $message);
    
    // Send SMS for hot leads (if SMS service configured)
    $lead_quality = get_post_meta($entry_id, 'lead_quality', true);
    if ($lead_quality === 'hot') {
        // SMS notification code here
    }
}
```

### Auto-Responder Email
```php
// Customer auto-responder
add_action('wpforms_process_complete', 'topnotch_customer_autoresponder', 10, 4);
function topnotch_customer_autoresponder($fields, $entry, $form_data, $entry_id) {
    $name = $fields[7]['value'];
    $email = $fields[10]['value'];
    $service = $fields[1]['value'];
    
    $subject = "Your Free Estimate Request - Top Notch New Jersey";
    
    $message = "
    Hi $name,
    
    Thank you for requesting a free estimate for your $service project!
    
    I've received your information and will personally review your project details. You can expect to hear from me within 2 hours during business hours (Monday-Friday 7 AM - 7 PM, Saturday 8 AM - 5 PM).
    
    What happens next:
    1. I'll review your project details and requirements
    2. I'll call or email you (based on your preference) to discuss your vision
    3. We'll schedule a free in-home consultation at your convenience
    4. I'll provide a detailed, written estimate within 24 hours of our meeting
    
    As a Licensed Home Improvement Contractor with 15+ years of experience, I'm committed to providing you with:
    ✓ Professional, quality craftsmanship
    ✓ Transparent pricing with no hidden costs
    ✓ Licensed, bonded & insured service
    ✓ 2-year warranty on all workmanship
    
    If you have any immediate questions, feel free to call me directly at (908) 555-0123.
    
    Best regards,
    Pedro Ribeiro
    Licensed Home Improvement Contractor
    Top Notch New Jersey
    
    P.S. Check out our recent project gallery at topnotchnewjersey.com/portfolio
    ";
    
    wp_mail($email, $subject, $message);
}
```

---

## 📊 Form Analytics & Tracking

### Conversion Tracking
```javascript
// WPForms analytics integration
document.addEventListener('wpformsFormSubmitSuccess', function(event) {
    const formId = event.detail.formId;
    const formData = event.detail.fields;
    
    // Google Analytics 4 tracking
    gtag('event', 'form_submit', {
        'event_category': 'lead_generation',
        'event_label': 'estimate_request',
        'form_id': formId,
        'service_type': formData.service_type || 'unknown',
        'budget_range': formData.budget_range || 'unknown',
        'timeline': formData.timeline || 'unknown'
    });
    
    // Track as conversion
    gtag('event', 'conversion', {
        'send_to': 'GA_MEASUREMENT_ID/CONVERSION_ID',
        'value': 100,
        'currency': 'USD'
    });
    
    // Facebook Pixel tracking (if configured)
    if (typeof fbq !== 'undefined') {
        fbq('track', 'Lead', {
            content_name: formData.service_type,
            value: 100,
            currency: 'USD'
        });
    }
});

// Form abandonment tracking
let formStarted = false;
document.addEventListener('wpformsFormInit', function(event) {
    formStarted = true;
    
    // Track form start
    gtag('event', 'form_start', {
        'event_category': 'lead_generation',
        'event_label': 'estimate_form'
    });
});

// Track form step completion
document.addEventListener('wpformsStepNext', function(event) {
    const currentStep = event.detail.currentStep;
    
    gtag('event', 'form_step_complete', {
        'event_category': 'lead_generation',
        'event_label': 'step_' + currentStep,
        'value': currentStep
    });
});
```

---

## 🚀 Implementation Checklist

### Form Setup
- [ ] Install WPForms Pro plugin
- [ ] Create multi-step estimate request form
- [ ] Configure conditional logic for service types
- [ ] Set up form styling and mobile optimization
- [ ] Test form functionality across devices

### Lead Scoring
- [ ] Implement lead scoring algorithm
- [ ] Configure automatic lead quality assignment
- [ ] Set up priority notifications for hot leads
- [ ] Test scoring accuracy with sample data

### Email Integration
- [ ] Configure instant notifications to Pedro
- [ ] Set up customer auto-responder emails
- [ ] Test email delivery and formatting
- [ ] Configure SMTP settings for reliability

### Analytics & Tracking
- [ ] Set up form conversion tracking
- [ ] Configure Google Analytics goals
- [ ] Implement form abandonment tracking
- [ ] Test all tracking events

### Testing & Optimization
- [ ] Test form on mobile devices
- [ ] Verify touch target sizes (44px minimum)
- [ ] Test form completion flow
- [ ] Optimize for conversion rate

---

**WPForms Pro Configuration Version:** 1.0  
**Last Updated:** June 2024  
**Dependencies:** WPForms Pro license, SMTP configuration  
**Estimated Setup Time:** 4-6 hours
