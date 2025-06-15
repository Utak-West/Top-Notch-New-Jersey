# Phase 1 Plugin Setup Guide - Top Notch New Jersey

## 🔌 Essential Plugin Installation for SeedProd Landing Page

### Plugin Installation Priority Order

#### 1. SeedProd Pro v6.15+ (FIRST PRIORITY)
**Purpose:** Landing page creation and maintenance mode
**License:** Pro subscription required
**Installation:**
1. Download from SeedProd account dashboard
2. Upload via WordPress admin (Plugins > Add New > Upload)
3. Activate and enter license key
4. Verify license activation

**Initial Configuration:**
- Enable "Coming Soon Mode" during development
- Configure email settings for form notifications
- Set up brand colors and typography
- Import landing page template

#### 2. Yoast SEO v22.0+ (CRITICAL FOR SEO)
**Purpose:** SEO optimization and local business schema
**License:** Free (Premium optional for advanced features)
**Installation:**
1. Install from WordPress plugin directory
2. Activate plugin
3. Run Yoast SEO configuration wizard

**Configuration Steps:**
```
Site Type: Business
Organization Name: Top Notch New Jersey
Logo: Upload company logo
Social Profiles:
- Facebook: [To be provided]
- Instagram: [To be provided]
- LinkedIn: [To be provided]

Local Business Settings:
Business Type: Home Improvement Contractor
Business Name: Top Notch New Jersey
Address: Linden, NJ (full address to be provided)
Phone: [Business phone number]
Email: pedro@topnotchnewjersey.com
Opening Hours: Monday-Friday 8AM-6PM, Saturday 9AM-4PM
```

**Local SEO Schema Configuration:**
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
  "paymentAccepted": "Cash, Check, Credit Card, Financing",
  "areaServed": ["Union County", "Essex County", "Middlesex County", "Bergen County"]
}
```

#### 3. WP Rocket v3.15+ (PERFORMANCE OPTIMIZATION)
**Purpose:** Caching and performance optimization
**License:** Premium required ($59/year)
**Installation:**
1. Download from WP Rocket account
2. Upload and activate plugin
3. Enter license key

**Contractor-Optimized Settings:**
```
Cache Settings:
✓ Enable Caching for Mobile Devices
✓ Enable Caching for Logged-in Users
✓ Cache Lifespan: 10 hours

File Optimization:
✓ Minify CSS files
✓ Combine CSS files
✓ Optimize CSS delivery
✓ Minify JavaScript files
✓ Combine JavaScript files
✓ Load JavaScript deferred

Media:
✓ Enable LazyLoad for images
✓ Enable LazyLoad for iframes and videos
✓ Replace YouTube iframe with preview image

Advanced Rules:
Never cache URLs: /estimate/, /contact/
Always purge URLs: /services/, /about/
```

#### 4. Wordfence Security v7.11+ (SECURITY PROTECTION)
**Purpose:** Security protection and firewall
**License:** Free (Premium recommended for business sites)
**Installation:**
1. Install from WordPress plugin directory
2. Activate plugin
3. Run initial security scan

**High-Security Configuration:**
```
Firewall Settings:
✓ Enable Wordfence Firewall
✓ Optimize the Wordfence Firewall
Protection Level: High Sensitivity

Login Security:
✓ Enable brute force protection
✓ Lock out after 5 failed logins
✓ Lock out duration: 4 hours
✓ Enable two-factor authentication

Scan Settings:
✓ Scan frequency: Daily
✓ Scan core files
✓ Scan themes and plugins
✓ Scan for malware signatures
✓ Check file permissions

Email Alerts:
Send alerts to: pedro@topnotchnewjersey.com
Alert on: Security issues, blocked attacks, scan results
```

#### 5. UpdraftPlus v1.23+ (BACKUP MANAGEMENT)
**Purpose:** Backup management and restoration
**License:** Free (Premium for cloud storage and advanced features)
**Installation:**
1. Install from WordPress plugin directory
2. Activate plugin
3. Configure backup schedule

**Backup Configuration:**
```
Backup Schedule:
Files: Daily at 2:00 AM
Database: Daily at 2:30 AM

Backup Retention:
Keep 7 daily backups
Keep 4 weekly backups
Keep 3 monthly backups

Remote Storage:
Primary: Google Drive (Premium feature)
Secondary: Dropbox (Premium feature)
Fallback: Local server storage

Email Reports:
Send to: pedro@topnotchnewjersey.com
Report frequency: Weekly summary
Include: Backup status, file sizes, any errors
```

## 🎨 Theme Installation and Configuration

### Recommended Theme: Astra Pro
**Why Astra Pro:**
- Lightweight and fast-loading
- Excellent SeedProd compatibility
- Built-in schema markup support
- Mobile-first responsive design
- Extensive customization options

**Installation Steps:**
1. Purchase Astra Pro license
2. Download theme from Astra account
3. Upload and activate via WordPress admin
4. Install Astra Pro addon plugin
5. Create child theme for customizations

**Basic Astra Configuration:**
```
Layout Settings:
Container Width: 1200px
Content Width: 1200px
Header Layout: Header Builder
Footer Layout: Footer Builder

Typography:
Primary Font: Inter (Google Fonts)
Headings Font: Inter
Body Font Size: 16px
Heading Font Sizes: H1(48px), H2(36px), H3(24px)

Colors:
Primary Color: #1E3A8A (Brand Blue)
Accent Color: #F59E0B (Accent Gold)
Text Color: #1F2937
Link Color: #1E3A8A
```

### Child Theme Creation
**Create child theme for customizations:**
1. Create new folder: `/wp-content/themes/astra-child/`
2. Create `style.css` with proper header
3. Create `functions.php` for customizations
4. Activate child theme

## 📊 Analytics and Tracking Setup

### Google Analytics 4 Configuration
**Plugin Recommendation:** MonsterInsights (Free version for Phase 1)
**Installation:**
1. Install MonsterInsights from plugin directory
2. Connect to Google Analytics account
3. Configure tracking settings

**GA4 Setup:**
```
Property Settings:
Property Name: Top Notch New Jersey
Industry Category: Home Improvement
Business Size: Small Business
Data Sharing: Enhanced measurement enabled

Enhanced Ecommerce:
✓ Track form submissions as conversions
✓ Track phone clicks as events
✓ Track CTA button clicks
✓ Track scroll depth

Custom Events:
- estimate_form_submission
- phone_number_click
- service_cta_click
- contact_form_view
```

### Google Search Console Setup
1. Verify website ownership via HTML tag method
2. Submit XML sitemap (generated by Yoast SEO)
3. Set up mobile usability monitoring
4. Configure performance monitoring

## 🔒 Security Hardening Checklist

### WordPress Core Security
- [ ] Change default admin username
- [ ] Use strong passwords (minimum 12 characters)
- [ ] Enable two-factor authentication
- [ ] Hide WordPress version information
- [ ] Disable file editing in admin panel
- [ ] Limit login attempts
- [ ] Regular security updates

### File Permissions
```
Directories: 755
Files: 644
wp-config.php: 600
.htaccess: 644
```

### Additional Security Measures
- [ ] Install SSL certificate
- [ ] Configure security headers
- [ ] Set up regular malware scanning
- [ ] Enable automatic WordPress updates
- [ ] Configure database backup encryption

## 📱 Mobile Optimization Setup

### Responsive Design Testing
**Test on devices:**
- iPhone 12/13 (375px width)
- Samsung Galaxy S21 (360px width)
- iPad (768px width)
- Desktop (1200px+ width)

**Mobile Performance Targets:**
- Page load speed: <3 seconds on 3G
- First Contentful Paint: <2 seconds
- Largest Contentful Paint: <2.5 seconds
- Cumulative Layout Shift: <0.1

### Touch-Friendly Design
- Button minimum size: 44px x 44px
- Form fields: Easy to tap and type
- Phone numbers: Click-to-call enabled
- Navigation: Touch-friendly menu

## 🚀 Phase 1 Launch Preparation

### Pre-Launch Testing Checklist
- [ ] All plugins installed and configured
- [ ] Theme installed and customized
- [ ] SeedProd landing page created
- [ ] Contact forms tested and working
- [ ] Email notifications functioning
- [ ] Analytics tracking verified
- [ ] Mobile responsiveness confirmed
- [ ] Page speed optimized
- [ ] Security measures active
- [ ] Backup system operational
- [ ] SSL certificate installed
- [ ] SEO settings configured

### Performance Optimization
**Target Metrics:**
- Google PageSpeed Score: 90+ (mobile and desktop)
- GTmetrix Grade: A
- Pingdom Load Time: <3 seconds
- Core Web Vitals: All green

**Optimization Steps:**
1. Optimize images (WebP format, compression)
2. Enable caching (WP Rocket)
3. Minify CSS and JavaScript
4. Enable GZIP compression
5. Optimize database
6. Use CDN if available

### SEO Foundation
**On-Page SEO:**
- Title tags optimized for target keywords
- Meta descriptions compelling and keyword-rich
- Header tags (H1, H2, H3) properly structured
- Image alt tags descriptive and keyword-optimized
- Internal linking structure planned

**Local SEO:**
- Google My Business profile optimized
- Local business schema markup implemented
- NAP (Name, Address, Phone) consistency
- Local keyword targeting
- Service area pages planned

## 📞 Support and Maintenance

### Plugin Update Schedule
- **Security plugins:** Update immediately
- **Core plugins:** Update weekly
- **Theme updates:** Test on staging first
- **WordPress core:** Update within 48 hours

### Monitoring Schedule
- **Daily:** Security alerts, backup status
- **Weekly:** Performance metrics, analytics review
- **Monthly:** Full security scan, plugin audit

### Emergency Procedures
**Website Down:**
1. Check hosting provider status
2. Review recent changes
3. Restore from backup if necessary
4. Contact hosting support

**Security Breach:**
1. Change all passwords immediately
2. Run full malware scan
3. Review security logs
4. Update all plugins and themes
5. Consider professional security audit

---

**Phase 1 Plugin Setup Version:** 1.0  
**Last Updated:** June 2024  
**WordPress Version:** 6.5+  
**Next Review:** August 2024
