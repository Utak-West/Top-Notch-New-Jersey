# WordPress Installation Guide - Top Notch New Jersey

## 🚀 WordPress 6.5+ Installation Requirements

### System Requirements
**Minimum Server Specifications:**
- **WordPress Version:** 6.5+ (Latest stable)
- **PHP Version:** 8.1+ (Recommended: 8.2)
- **MySQL Version:** 8.0+ or MariaDB 10.6+
- **Memory Limit:** 512MB minimum (1GB recommended)
- **Max Execution Time:** 300 seconds
- **File Upload Limit:** 64MB minimum

### Pre-Installation Checklist
- [ ] Domain name configured and DNS propagated
- [ ] SSL certificate installed and verified
- [ ] Hosting environment meets minimum requirements
- [ ] Database created with appropriate user permissions
- [ ] FTP/SFTP access credentials available

## 📋 Step-by-Step Installation Process

### Step 1: Download and Upload WordPress
1. Download latest WordPress from wordpress.org
2. Extract files to local computer
3. Upload all files to web server root directory
4. Set appropriate file permissions (755 for directories, 644 for files)

### Step 2: Database Configuration
1. Create MySQL database for WordPress
2. Create database user with full privileges
3. Note database name, username, and password for configuration

### Step 3: WordPress Configuration
1. Navigate to your domain in web browser
2. Select language (English - United States)
3. Enter database connection details:
   - Database Name: [your_database_name]
   - Username: [your_database_user]
   - Password: [your_database_password]
   - Database Host: localhost (or provided host)
   - Table Prefix: wp_ (or custom prefix for security)

### Step 4: Site Information Setup
1. **Site Title:** "Top Notch New Jersey - Kitchen & Bathroom Remodeling"
2. **Username:** Create secure admin username (not "admin")
3. **Password:** Generate strong password
4. **Email:** pedro@topnotchnewjersey.com
5. **Search Engine Visibility:** Unchecked (allow indexing)

## 🔧 Essential WordPress Configuration

### Basic Settings Configuration
**General Settings (Settings > General):**
- Site Title: "Top Notch New Jersey"
- Tagline: "Licensed Kitchen & Bathroom Remodeling Contractor"
- WordPress Address: https://topnotchnewjersey.com
- Site Address: https://topnotchnewjersey.com
- Email Address: pedro@topnotchnewjersey.com
- Timezone: America/New_York
- Date Format: F j, Y
- Time Format: g:i a

**Permalink Settings (Settings > Permalinks):**
- Select "Post name" structure for SEO-friendly URLs
- Custom Structure: /%postname%/

### Security Hardening
**Immediate Security Steps:**
1. Change default "admin" username
2. Use strong passwords (minimum 12 characters)
3. Limit login attempts
4. Hide WordPress version information
5. Disable file editing in admin panel
6. Regular security updates

## 🔌 Phase 1 Plugin Installation Priority

### Tier 1 - Critical Plugins (Install First)
1. **SeedProd Pro** v6.15+
   - Purpose: Landing page creation and maintenance mode
   - License: Pro subscription required
   - Configuration: Coming soon/maintenance mode setup

2. **Yoast SEO** v22.0+
   - Purpose: SEO optimization and local business schema
   - License: Free (Premium optional)
   - Configuration: Local business setup for New Jersey

3. **WP Rocket** v3.15+
   - Purpose: Caching and performance optimization
   - License: Premium required
   - Configuration: Contractor-optimized caching settings

4. **Wordfence Security** v7.11+
   - Purpose: Security protection and firewall
   - License: Free (Premium recommended)
   - Configuration: High-security mode for business site

5. **UpdraftPlus** v1.23+
   - Purpose: Backup management and restoration
   - License: Free (Premium for advanced features)
   - Configuration: Daily automated backups to cloud storage

### Plugin Installation Process
1. Navigate to Plugins > Add New
2. Search for plugin name
3. Install and activate
4. Configure according to specifications below

## 🎨 Theme Installation

### Recommended Theme Options
**Primary Choice:** Astra Pro
- Lightweight and fast-loading
- Excellent Elementor Pro compatibility
- Built-in schema markup support
- Mobile-first responsive design

**Alternative:** GeneratePress Pro
- Performance-optimized
- Extensive customization options
- SEO-friendly structure

**Fallback:** Hello Elementor
- Official Elementor theme
- Minimal and lightweight
- Perfect for Elementor-based designs

### Theme Installation Steps
1. Go to Appearance > Themes
2. Click "Add New"
3. Upload theme ZIP file or search theme directory
4. Install and activate chosen theme
5. Create child theme for customizations

## 🔧 Initial WordPress Optimization

### Performance Optimization
**WP Rocket Configuration:**
- Enable page caching
- Enable GZIP compression
- Optimize CSS and JavaScript delivery
- Enable lazy loading for images
- Configure CDN if available

**Image Optimization:**
- Install image optimization plugin
- Configure WebP format support
- Set up responsive image sizes
- Optimize existing media library

### SEO Foundation Setup
**Yoast SEO Configuration:**
- Set up local business information
- Configure social media profiles
- Enable XML sitemaps
- Set up breadcrumb navigation
- Configure schema markup for contractor business

### Security Configuration
**Wordfence Setup:**
- Enable firewall protection
- Configure login security
- Set up malware scanning schedule
- Enable two-factor authentication
- Configure email notifications

## 📊 Analytics and Tracking Setup

### Google Analytics 4 Setup
1. Create Google Analytics account
2. Set up GA4 property for website
3. Install Google Analytics plugin or add tracking code
4. Configure enhanced ecommerce tracking
5. Set up conversion goals for estimate requests

### Google Search Console
1. Verify website ownership
2. Submit XML sitemap
3. Monitor search performance
4. Set up mobile usability monitoring

## 🚀 Phase 1 Launch Preparation

### Pre-Launch Checklist
- [ ] WordPress core installation completed
- [ ] All Tier 1 plugins installed and configured
- [ ] Theme installed and basic customization complete
- [ ] SSL certificate verified and working
- [ ] Basic SEO settings configured
- [ ] Security measures implemented
- [ ] Backup system operational
- [ ] Analytics tracking installed
- [ ] Contact forms tested and working

### Post-Installation Next Steps
1. Proceed to SeedProd Pro landing page setup
2. Configure brand colors and typography
3. Import landing page template
4. Set up conversion forms and lead capture
5. Test all functionality before going live

## 📞 Support and Troubleshooting

### Common Installation Issues
**Database Connection Error:**
- Verify database credentials
- Check database server status
- Confirm user permissions

**File Permission Issues:**
- Set directories to 755
- Set files to 644
- Ensure web server can write to wp-content

**Memory Limit Errors:**
- Increase PHP memory limit to 512MB or higher
- Contact hosting provider if needed

### Getting Help
- WordPress.org support forums
- Hosting provider technical support
- Plugin-specific documentation
- Professional WordPress developer consultation

---

**Installation Guide Version:** 1.0  
**Last Updated:** June 2024  
**WordPress Version Tested:** 6.5.3  
**Next Review:** September 2024
