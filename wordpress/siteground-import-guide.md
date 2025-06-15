# SiteGround WordPress Import Guide - Top Notch New Jersey

## Step 3: Template Import & Configuration for SiteGround Hosting

**Environment:** SiteGround Cloud Hosting  
**SEO Plugin:** All-in-One SEO (instead of Yoast SEO)  
**Security:** Wordfence (already installed)  
**Target:** Import all templates and configurations for Pedro Ribeiro's business

---

## 🚀 Import Order & Process

### 1. Homepage Template Import
**File:** `/wordpress/homepage-template.md`

**SiteGround-Specific Steps:**
1. Access WordPress admin via SiteGround Site Tools
2. Navigate to Elementor > Templates > Import Template
3. Create new page: "Homepage" 
4. Apply homepage template structure
5. Configure SiteGround caching after import

**Content to Import:**
- Hero section with Pedro's Master Electrician credentials (#13VH13054200)
- Service overview (Kitchen, Bathroom, Electrical)
- Trust indicators and testimonials
- Service area coverage (Union, Essex, Middlesex, Bergen Counties)
- Multiple conversion CTAs

### 2. Kitchen Service Page Import
**File:** `/wordpress/kitchen-page-template.md`

**Implementation Steps:**
1. Create new page: "Kitchen Remodeling"
2. Import Elementor template structure
3. Add content from `/content/services/kitchen-remodeling.md`
4. Configure service-specific contact forms
5. Optimize for SiteGround Speed Optimizer

**Key Elements:**
- Kitchen renovation process steps
- Before/after project galleries
- Pricing tiers and investment levels
- Master Electrician electrical work emphasis
- Local New Jersey project examples

### 3. Bathroom Service Page Import
**File:** `/wordpress/bathroom-page-template.md`

**Implementation Steps:**
1. Create new page: "Bathroom Renovation"
2. Import template with accessibility features
3. Add luxury and standard renovation options
4. Configure bathroom-specific estimate forms
5. Test mobile responsiveness on SiteGround

### 4. Contact Page Template Import
**File:** `/wordpress/contact-page-template.md`

**SiteGround Integration:**
1. Import contact page template
2. Configure Google Maps integration
3. Set up multiple contact methods
4. Add business hours and service areas
5. Test form submissions with SiteGround email

---

## 🔧 All-in-One SEO Configuration (Adapted from Yoast)

### Local Business Schema Setup
**Replace Yoast configurations with All-in-One SEO:**

```json
{
  "@type": "LocalBusiness",
  "name": "Top Notch New Jersey",
  "description": "Licensed Master Electrician Pedro Ribeiro providing kitchen remodeling, bathroom renovation, and electrical services",
  "url": "https://topnotchnewjersey.com",
  "telephone": "+1-XXX-XXX-XXXX",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "New Jersey",
    "addressRegion": "NJ",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "40.7128",
    "longitude": "-74.0060"
  },
  "areaServed": [
    "Union County, NJ",
    "Essex County, NJ", 
    "Middlesex County, NJ",
    "Bergen County, NJ"
  ],
  "hasCredential": {
    "@type": "EducationalOccupationalCredential",
    "credentialCategory": "Professional License",
    "recognizedBy": "State of New Jersey",
    "name": "Master Electrician License #13VH13054200"
  }
}
```

### All-in-One SEO Settings
**Navigate to: All in One SEO > Local SEO**

1. **Business Info:**
   - Business Name: Top Notch New Jersey
   - Business Type: Electrician/Home Improvement
   - Phone: [Your business phone]
   - Address: [Your business address]

2. **Service Areas:**
   - Union County, New Jersey
   - Essex County, New Jersey
   - Middlesex County, New Jersey
   - Bergen County, New Jersey

3. **Business Hours:**
   - Monday-Friday: 7:00 AM - 6:00 PM
   - Saturday: 8:00 AM - 4:00 PM
   - Sunday: Emergency calls only

4. **Credentials:**
   - Add custom field: "Licensed Master Electrician #13VH13054200"
   - Include in business description

### Page-Specific SEO Configuration

**Homepage:**
- Title: "Top Notch Kitchen & Bathroom Remodeling | Licensed Master Electrician NJ"
- Meta Description: "Pedro Ribeiro, Licensed Master Electrician #13VH13054200, provides expert kitchen remodeling and bathroom renovation in Union, Essex, Middlesex & Bergen Counties."
- Focus Keyword: "kitchen remodeling New Jersey"

**Kitchen Page:**
- Title: "Kitchen Remodeling New Jersey | Licensed Master Electrician | Top Notch"
- Meta Description: "Professional kitchen remodeling by Licensed Master Electrician Pedro Ribeiro. Serving Union, Essex, Middlesex & Bergen Counties. Free estimates."
- Focus Keyword: "kitchen remodeling New Jersey"

**Bathroom Page:**
- Title: "Bathroom Renovation NJ | Licensed Master Electrician | Top Notch"
- Meta Description: "Expert bathroom renovation services by Licensed Master Electrician Pedro Ribeiro. Accessibility & luxury options. Serving all of New Jersey."
- Focus Keyword: "bathroom renovation New Jersey"

---

## 📋 WPForms Pro Lead Capture Import

### Multi-Step Form Configuration
**File:** `/wordpress/wpforms-pro-lead-capture.md`

**SiteGround-Optimized Setup:**
1. Install WPForms Pro via SiteGround WordPress Toolkit
2. Import form configuration from implementation file
3. Configure conditional logic for service types
4. Set up lead scoring integration
5. Test form submissions with SiteGround email delivery

### Form Structure (4 Steps):
1. **Service Selection** - Kitchen, Bathroom, Complete Home, Multiple Rooms
2. **Project Details** - Scope, timeline, special features
3. **Investment & Timeline** - Budget ranges, urgency assessment
4. **Contact Information** - Name, phone, email, service area validation

### Lead Scoring Integration:
- **Service Type (0-30 points):** Complete Home (30), Kitchen (20), Bathroom (15)
- **Budget Range (0-25 points):** $100K+ (25), $60K-$100K (20), etc.
- **Timeline (0-20 points):** ASAP (20), 1 month (15), 3 months (10), etc.
- **Location (0-10 points):** Primary counties (10), Secondary (7), Extended (3)

### Email Notifications:
- **Admin Email:** Immediate notification with lead score and priority
- **Customer Auto-Response:** Personalized based on service selection
- **Follow-up Sequence:** Automated based on lead priority classification

---

## 🔒 SiteGround Security Integration

### Wordfence Configuration (Already Installed)
**Optimize for SiteGround environment:**

1. **Firewall Settings:**
   - Enable SiteGround-compatible firewall rules
   - Configure rate limiting for form submissions
   - Set up country blocking if needed

2. **Scan Settings:**
   - Schedule daily scans during low-traffic hours
   - Configure SiteGround backup integration
   - Set up email alerts for security issues

3. **Login Security:**
   - Enable two-factor authentication
   - Configure login attempt limits
   - Set up CAPTCHA for forms

### SiteGround Security Features:
- **SSL Certificate:** Ensure Let's Encrypt is active
- **Security Headers:** Configure via SiteGround Security plugin
- **Backup Integration:** Connect with SiteGround backup system

---

## ⚡ SiteGround Performance Optimization

### Speed Optimizer Configuration
**Optimize imported templates:**

1. **Caching Settings:**
   - Enable SiteGround SuperCacher
   - Configure dynamic caching for forms
   - Set up Memcached if available

2. **Image Optimization:**
   - Enable WebP conversion
   - Configure lazy loading for galleries
   - Optimize project photos for fast loading

3. **CSS/JS Optimization:**
   - Minify CSS and JavaScript
   - Combine files where possible
   - Defer non-critical resources

### Core Web Vitals Targets:
- **LCP (Largest Contentful Paint):** <2.5 seconds
- **FID (First Input Delay):** <100ms
- **CLS (Cumulative Layout Shift):** <0.1
- **Overall Page Load:** <3 seconds

---

## 📱 Mobile Optimization for SiteGround

### Responsive Design Testing:
1. Test all imported templates on mobile devices
2. Verify touch-friendly button sizes (44px minimum)
3. Optimize form navigation for mobile
4. Ensure click-to-call functionality works
5. Test SiteGround mobile caching

### Mobile Performance:
- **3G Load Time:** <3 seconds target
- **Mobile PageSpeed Score:** >90 target
- **Touch Target Size:** Minimum 44px
- **Viewport Configuration:** Properly set for all pages

---

## 🧪 Testing Checklist for SiteGround

### Functionality Testing:
- [ ] All forms submit correctly via SiteGround email
- [ ] Contact information displays properly
- [ ] Phone click-to-call works on mobile
- [ ] Email links function correctly
- [ ] Service area validation works
- [ ] Lead scoring calculates properly

### Performance Testing:
- [ ] Page load speeds meet targets
- [ ] SiteGround caching works properly
- [ ] Images load with lazy loading
- [ ] Mobile performance optimized
- [ ] Core Web Vitals pass

### Security Testing:
- [ ] SSL certificate active and working
- [ ] Wordfence firewall configured
- [ ] Form submissions secure
- [ ] Login security enabled
- [ ] Backup system operational

### SEO Testing:
- [ ] All-in-One SEO schema markup active
- [ ] Meta tags properly configured
- [ ] Local business information correct
- [ ] Service area targeting working
- [ ] Pedro's credentials prominently displayed

---

## 📞 Next Steps After Import

### Immediate Actions:
1. **Test All Forms:** Submit test leads through each form
2. **Verify Email Delivery:** Ensure notifications reach Pedro
3. **Check Mobile Display:** Test on actual mobile devices
4. **Validate SEO:** Use Google Rich Results Test
5. **Performance Check:** Run PageSpeed Insights

### Configuration Verification:
1. **Business Information:** Verify all contact details are correct
2. **Service Areas:** Confirm coverage areas are accurate
3. **Pricing Information:** Ensure all pricing is current
4. **Credentials Display:** Pedro's license prominently shown
5. **Trust Elements:** All certifications and badges visible

### Launch Preparation:
1. **Final Content Review:** Check all text for accuracy
2. **Legal Pages:** Ensure privacy policy and terms are updated
3. **Analytics Setup:** Configure Google Analytics 4
4. **Backup Verification:** Confirm SiteGround backups working
5. **Go-Live Checklist:** Complete final pre-launch verification

---

**SiteGround Import Guide Version:** 1.0  
**Compatible with:** SiteGround Cloud Hosting, All-in-One SEO, Wordfence  
**Created:** June 15, 2024  
**For:** Pedro Ribeiro - Top Notch New Jersey
