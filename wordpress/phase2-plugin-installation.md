# Phase 2 Plugin Installation - Top Notch New Jersey

## 🔌 Lead Generation Plugin Setup

### Purpose
Install and configure Phase 2 plugins focused on lead generation, analytics, and mobile functionality for Top Notch New Jersey's WordPress site.

---

## 📋 Phase 2 Plugin List

### Required Plugins (From plugins-list.md lines 338-342)
1. **Gravity Forms** - Advanced form creation
2. **MonsterInsights** - Analytics setup  
3. **WP Call Button** - Mobile functionality
4. **WP Mail SMTP** - Email reliability

---

## 🚀 Installation Instructions

### 1. Gravity Forms (Premium - $59-259/year)
**Purpose:** Advanced form creation and lead management

**Installation Steps:**
1. Purchase Gravity Forms license from gravityforms.com
2. Download plugin zip file from account dashboard
3. WordPress Admin → Plugins → Add New → Upload Plugin
4. Upload gravity-forms.zip and activate
5. Enter license key in Forms → Settings → License

**Initial Configuration:**
```php
// Gravity Forms basic settings
add_filter('gform_enable_logging', '__return_true');
add_filter('gform_logging_enabled', '__return_true');

// Custom form styling
add_filter('gform_field_css_class', 'topnotch_custom_form_classes', 10, 3);
function topnotch_custom_form_classes($classes, $field, $form) {
    $classes .= ' topnotch-field';
    return $classes;
}
```

**Forms to Create:**
- Free estimate request form (primary lead capture)
- Service-specific consultation forms
- Contact forms for each service page
- Newsletter signup forms

### 2. MonsterInsights (Free/Premium - $99-399/year)
**Purpose:** Google Analytics integration and reporting

**Installation Steps:**
1. Install from WordPress Plugin Directory (free version)
2. Or purchase premium from monsterinsights.com
3. WordPress Admin → Plugins → Add New → Search "MonsterInsights"
4. Install and activate
5. Run setup wizard to connect Google Analytics

**Configuration:**
```php
// MonsterInsights custom tracking
add_action('wp_head', 'topnotch_custom_analytics_events');
function topnotch_custom_analytics_events() {
    if (function_exists('MonsterInsights')) {
        ?>
        <script>
        // Track form submissions
        document.addEventListener('gform_confirmation_loaded', function(event) {
            gtag('event', 'form_submit', {
                'event_category': 'lead_generation',
                'event_label': 'estimate_request'
            });
        });
        </script>
        <?php
    }
}
```

**Analytics Goals:**
- Form submissions tracking
- Phone call conversions
- Service page engagement
- Mobile vs desktop performance

### 3. WP Call Button (Free)
**Purpose:** Click-to-call functionality for mobile users

**Installation Steps:**
1. WordPress Admin → Plugins → Add New → Search "WP Call Button"
2. Install and activate
3. Configure in Settings → WP Call Button

**Configuration Settings:**
```json
{
  "phone_number": "(908) 555-0123",
  "button_text": "Call Now",
  "button_position": "bottom_right",
  "mobile_only": true,
  "button_color": "#10B981",
  "text_color": "#FFFFFF",
  "show_on_pages": ["all"],
  "analytics_tracking": true
}
```

**Custom Styling:**
```css
/* WP Call Button customization */
.wp-call-button {
    background-color: #10B981 !important;
    border-radius: 50px !important;
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3) !important;
    font-weight: 600 !important;
    min-height: 56px !important;
    min-width: 56px !important;
}

.wp-call-button:hover {
    background-color: #0D9668 !important;
    transform: scale(1.05) !important;
}

@media (max-width: 768px) {
    .wp-call-button {
        bottom: 20px !important;
        right: 20px !important;
        z-index: 9999 !important;
    }
}
```

### 4. WP Mail SMTP (Free/Premium)
**Purpose:** Reliable email delivery

**Installation Steps:**
1. WordPress Admin → Plugins → Add New → Search "WP Mail SMTP"
2. Install and activate
3. Configure SMTP settings in Settings → WP Mail SMTP

**SMTP Configuration:**
```php
// WP Mail SMTP configuration
define('WPMS_ON', true);
define('WPMS_SMTP_HOST', 'smtp.gmail.com');
define('WPMS_SMTP_PORT', 587);
define('WPMS_SSL', 'tls');
define('WPMS_SMTP_AUTH', true);
define('WPMS_SMTP_USER', 'pedro@topnotchnewjersey.com');
define('WPMS_SMTP_PASS', 'app_password_here');
```

**Email Templates:**
- Lead notification emails
- Auto-responder confirmations
- Consultation booking confirmations
- Follow-up email sequences

---

## 🔧 Plugin Integration Setup

### Gravity Forms Integration

#### Lead Capture Form Configuration
```php
// Custom Gravity Forms hooks
add_action('gform_after_submission_1', 'topnotch_process_lead_submission', 10, 2);
function topnotch_process_lead_submission($entry, $form) {
    // Extract form data
    $name = rgar($entry, '1');
    $phone = rgar($entry, '2');
    $email = rgar($entry, '3');
    $service = rgar($entry, '4');
    
    // Send notification to Pedro
    wp_mail(
        'pedro@topnotchnewjersey.com',
        'New Lead: ' . $service . ' - ' . $name,
        "New lead submission:\n\nName: $name\nPhone: $phone\nEmail: $email\nService: $service"
    );
    
    // Track conversion
    if (function_exists('MonsterInsights')) {
        // Analytics tracking handled by MonsterInsights
    }
}
```

#### Form Field Configuration
```json
{
  "form_fields": [
    {
      "type": "text",
      "label": "Full Name",
      "required": true,
      "css_class": "topnotch-name-field"
    },
    {
      "type": "phone",
      "label": "Phone Number", 
      "required": true,
      "format": "(999) 999-9999"
    },
    {
      "type": "email",
      "label": "Email Address",
      "required": true
    },
    {
      "type": "select",
      "label": "Service Needed",
      "options": [
        "Kitchen Remodeling",
        "Bathroom Renovation",
        "Home Renovation",
        "Multiple Services"
      ],
      "required": true
    },
    {
      "type": "textarea",
      "label": "Project Description",
      "required": false,
      "rows": 4
    }
  ]
}
```

### MonsterInsights Analytics Setup

#### Custom Event Tracking
```javascript
// Enhanced analytics tracking
document.addEventListener('DOMContentLoaded', function() {
    // Track service page views
    if (document.body.classList.contains('page-kitchen-remodeling')) {
        gtag('event', 'service_page_view', {
            'event_category': 'engagement',
            'event_label': 'kitchen_remodeling'
        });
    }
    
    // Track phone button clicks
    document.querySelectorAll('.wp-call-button').forEach(function(button) {
        button.addEventListener('click', function() {
            gtag('event', 'phone_click', {
                'event_category': 'contact',
                'event_label': 'mobile_call_button'
            });
        });
    });
    
    // Track estimate form views
    const estimateForm = document.querySelector('#gform_1');
    if (estimateForm) {
        gtag('event', 'form_view', {
            'event_category': 'lead_generation',
            'event_label': 'estimate_form'
        });
    }
});
```

---

## 📱 Mobile Optimization

### WP Call Button Mobile Settings
```css
/* Mobile-first call button optimization */
@media (max-width: 768px) {
    .wp-call-button {
        position: fixed !important;
        bottom: 20px !important;
        right: 20px !important;
        width: 60px !important;
        height: 60px !important;
        border-radius: 50% !important;
        font-size: 18px !important;
        z-index: 9999 !important;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.4) !important;
    }
    
    .wp-call-button::before {
        content: "📞";
        font-size: 24px;
    }
}

/* Hide on desktop if mobile-only enabled */
@media (min-width: 769px) {
    .wp-call-button.mobile-only {
        display: none !important;
    }
}
```

### Gravity Forms Mobile Optimization
```css
/* Mobile form styling */
@media (max-width: 768px) {
    .gform_wrapper .gfield {
        margin-bottom: 20px !important;
    }
    
    .gform_wrapper input[type="text"],
    .gform_wrapper input[type="email"],
    .gform_wrapper input[type="tel"],
    .gform_wrapper select,
    .gform_wrapper textarea {
        font-size: 16px !important; /* Prevent zoom on iOS */
        min-height: 44px !important; /* Touch target size */
        padding: 12px 16px !important;
        border-radius: 8px !important;
    }
    
    .gform_wrapper .gform_button {
        width: 100% !important;
        min-height: 48px !important;
        font-size: 18px !important;
        font-weight: 600 !important;
    }
}
```

---

## 🔍 Testing & Validation

### Plugin Functionality Tests
1. **Gravity Forms Testing:**
   - Test form submission process
   - Verify email notifications
   - Check analytics tracking
   - Test mobile responsiveness

2. **MonsterInsights Testing:**
   - Verify Google Analytics connection
   - Test custom event tracking
   - Check real-time data
   - Validate conversion tracking

3. **WP Call Button Testing:**
   - Test click-to-call functionality
   - Verify mobile-only display
   - Check analytics tracking
   - Test button positioning

4. **WP Mail SMTP Testing:**
   - Send test emails
   - Verify delivery rates
   - Check spam folder placement
   - Test email formatting

### Performance Impact Assessment
```php
// Monitor plugin performance impact
add_action('wp_footer', 'topnotch_performance_monitoring');
function topnotch_performance_monitoring() {
    if (current_user_can('administrator')) {
        $queries = get_num_queries();
        $memory = memory_get_peak_usage(true) / 1024 / 1024;
        echo "<!-- Queries: $queries | Memory: " . round($memory, 2) . "MB -->";
    }
}
```

---

## 🚀 Post-Installation Checklist

### Immediate Setup Tasks
- [ ] Install all four Phase 2 plugins
- [ ] Configure Gravity Forms with license key
- [ ] Set up MonsterInsights Google Analytics connection
- [ ] Configure WP Call Button for mobile users
- [ ] Set up WP Mail SMTP with proper credentials

### Form Creation Tasks
- [ ] Create primary estimate request form
- [ ] Set up kitchen remodeling consultation form
- [ ] Create bathroom renovation inquiry form
- [ ] Configure contact forms for service pages
- [ ] Test all form submissions and notifications

### Analytics Configuration
- [ ] Set up conversion goals in Google Analytics
- [ ] Configure custom event tracking
- [ ] Test phone call tracking
- [ ] Verify form submission analytics
- [ ] Set up automated reporting

### Mobile Optimization
- [ ] Test call button on mobile devices
- [ ] Verify form responsiveness
- [ ] Check touch target sizes
- [ ] Test analytics on mobile
- [ ] Validate email delivery on mobile

---

## 📊 Success Metrics

### Lead Generation KPIs
- Form submission rate: Target 3-5% of visitors
- Phone call conversions: Target 1-2% of mobile visitors
- Email delivery rate: Target 95%+ delivery
- Mobile conversion rate: Target 2-4% of mobile traffic

### Technical Performance
- Page load impact: <500ms additional load time
- Mobile usability: 100% mobile-friendly score
- Email deliverability: <5% bounce rate
- Analytics accuracy: 100% event tracking

---

**Phase 2 Plugin Installation Version:** 1.0  
**Last Updated:** June 2024  
**Dependencies:** WordPress 6.0+, SSL certificate, SMTP credentials  
**Estimated Setup Time:** 3-4 hours
