# Technical Specifications - Top Notch New Jersey

## 🛠 WordPress Implementation Requirements

### Core Platform Specifications
**WordPress Version:** 6.5+ (Latest stable)  
**PHP Version:** 8.1+ (Recommended: 8.2)  
**MySQL Version:** 8.0+ or MariaDB 10.6+  
**Memory Limit:** 512MB minimum (1GB recommended)  
**Max Execution Time:** 300 seconds  
**File Upload Limit:** 64MB minimum  

### Essential Plugin Stack
**Reference:** `wordpress/plugins-list.md` for complete details

#### Tier 1 - Critical (Must Install First)
1. **Elementor Pro** v3.21+
   - License: Pro subscription required
   - Purpose: Primary page builder
   - Dependencies: None
   - Configuration: Custom templates, global colors, typography

2. **SeedProd Pro** v6.15+
   - License: Pro subscription required
   - Purpose: Phase 1 landing page
   - Dependencies: None
   - Configuration: Coming soon/maintenance mode

3. **Yoast SEO** v22.0+
   - License: Free (Premium optional)
   - Purpose: SEO optimization
   - Dependencies: None
   - Configuration: Local business schema

#### Tier 2 - Performance & Security
4. **WP Rocket** v3.15+
   - License: Premium required
   - Purpose: Caching and performance
   - Dependencies: None
   - Configuration: Contractor-optimized settings

5. **Wordfence Security** v7.11+
   - License: Free (Premium recommended)
   - Purpose: Security protection
   - Dependencies: None
   - Configuration: High-security mode

6. **UpdraftPlus** v1.23+
   - License: Free (Premium for advanced features)
   - Purpose: Backup management
   - Dependencies: Cloud storage (Google Drive/Dropbox)
   - Configuration: Daily automated backups

### Theme Requirements
**Primary Theme:** Astra Pro or GeneratePress Pro  
**Fallback:** Hello Elementor (Elementor's native theme)  
**Custom Child Theme:** Required for customizations  

**Theme Features Required:**
- Elementor Pro compatibility
- WooCommerce ready (future e-commerce)
- Schema markup support
- Mobile-first responsive design
- Fast loading (<2 seconds)

## 🎨 Design System Specifications

### Brand Color Palette
**Reference:** `docs/brand-guidelines.md` for complete specifications

**Top Notch Brand Colors:**
- Top Notch Blue: `#021e3a` (Primary brand color)
- Jersey Blue: `#27397d` (Secondary blue variant)
- Pedro's Orange: `#ff8b1e` (Primary accent/CTA color)
- Obrigada Orange: `#ffb570` (Secondary accent/highlight)
- Professional White: `#fef9f1` (Background/clean areas)
- Rio Green: `#41924a` (Success states)
- Neutral Gray: `#6B7280` (Supporting text)

### Typography System
**Primary Font:** Inter (Google Fonts)  
**Secondary Font:** Roboto Slab (Headings)  
**Fallback:** System fonts (Arial, Helvetica, sans-serif)  

**Font Sizes:**
- H1: 48px (mobile: 32px)
- H2: 36px (mobile: 28px)
- H3: 24px (mobile: 20px)
- Body: 16px (mobile: 14px)
- Small: 14px (mobile: 12px)

### Responsive Breakpoints
- **Mobile:** 320px - 767px
- **Tablet:** 768px - 1023px
- **Desktop:** 1024px - 1439px
- **Large Desktop:** 1440px+

## 📱 Mobile-First Requirements

### Performance Targets
- **Page Load Speed:** <3 seconds on 3G
- **Core Web Vitals:**
  - LCP (Largest Contentful Paint): <2.5s
  - FID (First Input Delay): <100ms
  - CLS (Cumulative Layout Shift): <0.1

### Mobile UX Requirements
- Touch-friendly buttons (44px minimum)
- Readable text without zooming
- Easy-to-use contact forms
- Click-to-call phone numbers
- Optimized images (WebP format)
- Minimal scrolling for key information

## 🔍 SEO Technical Requirements

### Schema Markup (Required)
**Reference:** `seo/keyword-research.md` for keyword specifications

**Local Business Schema:**
```json
{
  "@type": "LocalBusiness",
  "name": "Top Notch New Jersey",
  "description": "Licensed home improvement contractor specializing in kitchen and bathroom remodeling",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Linden",
    "addressRegion": "NJ",
    "addressCountry": "US"
  },
  "telephone": "[Phone Number]",
  "url": "https://topnotchnewjersey.com",
  "priceRange": "$$-$$$",
  "paymentAccepted": "Cash, Check, Credit Card, Financing"
}
```

**Service Schema:**
- Kitchen Remodeling Service
- Bathroom Renovation Service
- Home Improvement Service

### Meta Tag Requirements
**Homepage:**
- Title: "Kitchen & Bathroom Remodeling NJ | Licensed Contractor | Top Notch New Jersey"
- Description: "Expert kitchen & bathroom remodeling in NJ. Licensed Home Improvement Contractor Pedro Ribeiro. Bonded & insured. Serving Union, Essex, Middlesex Counties. Free estimates."

**Service Pages:**
- Kitchen: "Kitchen Remodeling NJ | Custom Designs | Licensed Contractor"
- Bathroom: "Bathroom Renovation NJ | Luxury Upgrades | Licensed Contractor"

## 🚀 Performance Optimization

### Image Optimization
**Formats:** WebP primary, JPEG fallback  
**Sizes:** Multiple responsive sizes  
**Compression:** 80% quality for photos, lossless for logos  
**Alt Text:** SEO-optimized descriptions  

### Caching Strategy
**Page Caching:** WP Rocket full-page caching  
**Object Caching:** Redis or Memcached (if available)  
**CDN:** Cloudflare or similar  
**Database Optimization:** Regular cleanup and optimization  

### Code Optimization
**CSS:** Minified and combined  
**JavaScript:** Minified, deferred loading  
**HTML:** Clean, semantic markup  
**Database:** Optimized queries, minimal plugins  

## 🔒 Security Configuration

### Security Headers
- Content Security Policy (CSP)
- X-Frame-Options: DENY
- X-Content-Type-Options: nosniff
- Referrer-Policy: strict-origin-when-cross-origin

### Access Control
- Strong admin passwords
- Two-factor authentication
- Limited login attempts
- Regular security scans

### Backup Strategy
**Frequency:** Daily automated backups  
**Retention:** 30 days local, 90 days cloud  
**Storage:** Multiple locations (local + cloud)  
**Testing:** Monthly restore tests  

## 📊 Analytics & Tracking

### Required Tracking
**Google Analytics 4:** Enhanced e-commerce tracking  
**Google Search Console:** SEO performance monitoring  
**Facebook Pixel:** Social media advertising (future)  
**Call Tracking:** Phone number analytics  

### Conversion Tracking
**Primary Goals:**
- Estimate form submissions
- Phone call clicks
- Contact page visits
- Service page engagement

**Secondary Goals:**
- Time on site
- Page views per session
- Bounce rate improvement
- Local search visibility

## 🔧 Development Environment

### Local Development
**Recommended:** Local by Flywheel or XAMPP  
**Version Control:** Git with GitHub  
**Code Editor:** VS Code with WordPress extensions  
**Testing:** Browser stack testing  

### Staging Environment
**Purpose:** Pre-production testing  
**URL:** staging.topnotchnewjersey.com  
**Access:** Password protected  
**Sync:** Weekly production sync  

### Production Environment
**Hosting:** WordPress-optimized hosting  
**SSL:** Let's Encrypt or premium certificate  
**Monitoring:** Uptime monitoring service  
**Support:** 24/7 technical support  

**Last Updated:** June 2024  
**WordPress Version Tested:** 6.5.3  
**Next Review:** September 2024
