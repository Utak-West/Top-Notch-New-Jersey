# Conversion Tracking & Analytics System - Top Notch New Jersey

---
**Document Type:** Conversion Tracking & Performance Analytics
**Project:** Top Notch New Jersey Website
**Owner:** Pedro Ribeiro, Licensed Master Electrician
**License:** NJ Home Improvement Contractor #13VH13
**Last Updated:** June 2024
**Version:** 2.0 - Enhanced Lead Capture Analytics
**Dependencies:** enhanced-lead-capture.md, mobile-conversion-system.md
---

## CONVERSION TRACKING ARCHITECTURE

### Primary Conversion Goals

**Lead Generation Metrics:**
- Form submissions by service type
- Phone call conversions
- Email lead magnet downloads
- Emergency service requests
- County-specific conversion rates

**Quality Metrics:**
- Lead scoring distribution
- Estimate-to-contract conversion
- Pedro's personal close rate
- Customer lifetime value by source

## GOOGLE ANALYTICS 4 SETUP

### Enhanced Event Tracking

```javascript
// Primary CTA Tracking
function trackPrimaryCTA(serviceType, location) {
  gtag('event', 'generate_lead', {
    'event_category': 'Lead Generation',
    'event_label': serviceType,
    'custom_parameters': {
      'service_type': serviceType,
      'form_location': location,
      'lead_source': 'website_cta'
    }
  });
}

// Service-Specific Form Tracking
function trackServiceForm(formType, step) {
  gtag('event', 'form_start', {
    'event_category': 'Form Interaction',
    'event_label': formType,
    'custom_parameters': {
      'form_type': formType,
      'form_step': step,
      'device_type': /Mobile|Android|iPhone|iPad/.test(navigator.userAgent) ? 'mobile' : 'desktop'
    }
  });
}

// Kitchen Remodeling Specific
function trackKitchenEstimate(formData) {
  gtag('event', 'kitchen_estimate_request', {
    'event_category': 'Kitchen Leads',
    'event_label': 'Estimate Request',
    'value': 1,
    'custom_parameters': {
      'kitchen_size': formData.kitchen_size,
      'budget_range': formData.renovation_level,
      'electrical_needed': formData.electrical.join(','),
      'timeline': formData.timeline
    }
  });
}

// Bathroom Renovation Specific
function trackBathroomEstimate(formData) {
  gtag('event', 'bathroom_estimate_request', {
    'event_category': 'Bathroom Leads',
    'event_label': 'Estimate Request',
    'value': 1,
    'custom_parameters': {
      'bathroom_type': formData.bathroom_type,
      'budget_range': formData.renovation_level,
      'special_features': formData.features.join(','),
      'timeline': formData.timeline
    }
  });
}

// Electrical Services Tracking
function trackElectricalService(serviceType, urgency) {
  gtag('event', 'electrical_service_request', {
    'event_category': 'Electrical Leads',
    'event_label': serviceType,
    'custom_parameters': {
      'service_type': serviceType,
      'urgency_level': urgency,
      'master_electrician_advantage': true
    }
  });
}

// County-Specific Tracking
function trackCountyLead(county, serviceType) {
  gtag('event', 'county_specific_lead', {
    'event_category': 'Geographic Targeting',
    'event_label': county,
    'custom_parameters': {
      'county': county,
      'service_requested': serviceType,
      'local_advantage': true
    }
  });
}

// Phone Call Tracking
function trackPhoneCall(callType) {
  gtag('event', 'phone_call', {
    'event_category': 'Contact Method',
    'event_label': callType,
    'custom_parameters': {
      'call_type': callType,
      'contact_preference': 'phone'
    }
  });
}

// Lead Magnet Downloads
function trackLeadMagnet(magnetType, userInfo) {
  gtag('event', 'lead_magnet_download', {
    'event_category': 'Lead Magnets',
    'event_label': magnetType,
    'custom_parameters': {
      'magnet_type': magnetType,
      'project_interest': userInfo.project_interest,
      'lead_quality': 'nurture'
    }
  });
}
```

### Custom Dimensions Setup

```javascript
// Set up custom dimensions for enhanced tracking
const customDimensions = {
  'service_type': 'custom_dimension_1',
  'lead_source': 'custom_dimension_2',
  'county': 'custom_dimension_3',
  'device_type': 'custom_dimension_4',
  'budget_range': 'custom_dimension_5',
  'timeline': 'custom_dimension_6',
  'electrical_needed': 'custom_dimension_7',
  'master_electrician_advantage': 'custom_dimension_8'
};

// Function to set custom dimensions
function setCustomDimensions(data) {
  Object.keys(data).forEach(key => {
    if (customDimensions[key]) {
      gtag('config', 'GA_MEASUREMENT_ID', {
        [customDimensions[key]]: data[key]
      });
    }
  });
}
```

## FACEBOOK PIXEL TRACKING

### Enhanced Conversion Events

```javascript
// Lead Generation Events
function trackFacebookLead(serviceType, value) {
  fbq('track', 'Lead', {
    content_name: `${serviceType} Estimate Request`,
    content_category: 'Home Improvement',
    value: value,
    currency: 'USD',
    custom_data: {
      service_type: serviceType,
      master_electrician: true,
      no_markup_advantage: true
    }
  });
}

// Service-Specific Facebook Events
function trackKitchenFacebookLead(formData) {
  fbq('track', 'CompleteRegistration', {
    content_name: 'Kitchen Remodeling Estimate',
    content_category: 'Kitchen Renovation',
    value: 50, // Estimated lead value
    currency: 'USD'
  });
}

function trackBathroomFacebookLead(formData) {
  fbq('track', 'CompleteRegistration', {
    content_name: 'Bathroom Renovation Estimate',
    content_category: 'Bathroom Renovation',
    value: 40, // Estimated lead value
    currency: 'USD'
  });
}

// Emergency Service Tracking
function trackEmergencyFacebookLead() {
  fbq('track', 'Contact', {
    content_name: 'Emergency Electrical Service',
    content_category: 'Electrical Emergency',
    value: 30,
    currency: 'USD'
  });
}
```

## CONVERSION FUNNEL ANALYSIS

### Key Performance Indicators (KPIs)

**Lead Quality Metrics:**
```
Lead Scoring Distribution:
├── Hot Leads (8+ points): Target 20%
├── Warm Leads (4-7 points): Target 50%
├── Cold Leads (0-3 points): Target 25%
└── Unqualified (<0 points): Target <5%

Service-Specific Conversion Rates:
├── Kitchen Remodeling: Target 15-20%
├── Bathroom Renovation: Target 18-25%
├── Whole Home Renovation: Target 10-15%
└── Electrical Services: Target 25-30%

Geographic Performance:
├── Union County: Baseline performance
├── Essex County: Target +10% vs Union
├── Middlesex County: Target +5% vs Union
└── Bergen County: Target +15% vs Union
```

**Conversion Funnel Metrics:**
```
Website Visitor → Lead Conversion:
├── Overall Target: 3-5%
├── Kitchen Pages: Target 4-6%
├── Bathroom Pages: Target 4-6%
├── Emergency Pages: Target 8-12%
└── County Pages: Target 5-7%

Lead → Estimate Conversion:
├── Overall Target: 80-90%
├── Hot Leads: Target 95%+
├── Warm Leads: Target 85-90%
└── Cold Leads: Target 70-80%

Estimate → Contract Conversion:
├── Pedro's Personal Close Rate: Target 60-70%
├── Kitchen Projects: Target 65-75%
├── Bathroom Projects: Target 70-80%
└── Electrical Projects: Target 55-65%
```

## ADVANCED TRACKING IMPLEMENTATION

### Heat Mapping and User Behavior

```javascript
// Hotjar or similar heat mapping setup
function initializeHeatMapping() {
  // Track form interactions
  hj('event', 'form_interaction');
  
  // Track CTA button clicks
  hj('event', 'cta_click');
  
  // Track mobile vs desktop behavior
  hj('event', 'device_type_behavior');
}

// Scroll depth tracking
function trackScrollDepth() {
  let maxScroll = 0;
  
  window.addEventListener('scroll', function() {
    const scrollPercent = Math.round((window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100);
    
    if (scrollPercent > maxScroll) {
      maxScroll = scrollPercent;
      
      // Track milestone scroll depths
      if ([25, 50, 75, 90].includes(scrollPercent)) {
        gtag('event', 'scroll_depth', {
          'event_category': 'User Engagement',
          'event_label': `${scrollPercent}%`,
          'value': scrollPercent
        });
      }
    }
  });
}
```

### A/B Testing Framework

```javascript
// A/B Testing for Headlines and CTAs
const abTestVariants = {
  hero_headline: {
    'variant_a': 'New Jersey\'s Kitchen & Bathroom Remodeling Experts',
    'variant_b': 'Master Electrician + Kitchen & Bathroom Specialist',
    'variant_c': 'Save Thousands on Your NJ Kitchen & Bathroom Renovation'
  },
  
  primary_cta: {
    'variant_a': 'Get Free Estimate',
    'variant_b': 'Get No-Markup Estimate',
    'variant_c': 'Start My Project'
  },
  
  trust_message: {
    'variant_a': 'Master Electrician #13VH13',
    'variant_b': 'No Electrical Subcontractor Markups',
    'variant_c': '15+ Years NJ Experience'
  }
};

// Function to assign and track A/B test variants
function assignABTestVariant(testName) {
  const variants = Object.keys(abTestVariants[testName]);
  const variant = variants[Math.floor(Math.random() * variants.length)];
  
  // Store variant in session
  sessionStorage.setItem(`ab_test_${testName}`, variant);
  
  // Track variant assignment
  gtag('event', 'ab_test_assignment', {
    'event_category': 'A/B Testing',
    'event_label': `${testName}_${variant}`,
    'custom_parameters': {
      'test_name': testName,
      'variant': variant
    }
  });
  
  return variant;
}
```

## REPORTING DASHBOARD SETUP

### Key Metrics Dashboard

**Daily Metrics:**
- Total leads generated
- Leads by service type
- Conversion rate by traffic source
- Pedro's call completion rate
- Emergency service requests

**Weekly Metrics:**
- Lead quality score distribution
- Estimate delivery rate
- Follow-up sequence performance
- County-specific performance
- Mobile vs desktop conversion rates

**Monthly Metrics:**
- Lead to contract conversion rate
- Customer acquisition cost by channel
- Lifetime value by lead source
- Referral generation rate
- Seasonal trend analysis

### Automated Reporting

```javascript
// Daily lead summary email
function generateDailyLeadReport() {
  const reportData = {
    total_leads: getTotalLeads('today'),
    kitchen_leads: getServiceLeads('kitchen', 'today'),
    bathroom_leads: getServiceLeads('bathroom', 'today'),
    electrical_leads: getServiceLeads('electrical', 'today'),
    emergency_calls: getEmergencyCalls('today'),
    conversion_rate: getConversionRate('today')
  };
  
  // Send to Pedro's email
  sendLeadReport(reportData, 'pedro@topnotchnewjersey.com');
}

// Weekly performance summary
function generateWeeklyPerformanceReport() {
  const reportData = {
    lead_quality_distribution: getLeadQualityDistribution('week'),
    county_performance: getCountyPerformance('week'),
    follow_up_effectiveness: getFollowUpMetrics('week'),
    ab_test_results: getABTestResults('week')
  };
  
  // Generate comprehensive report
  generatePerformanceReport(reportData);
}
```
