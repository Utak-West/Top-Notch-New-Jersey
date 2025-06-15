# File Relationship Map - Top Notch New Jersey

## 🔗 Dependency Matrix

### Core Documentation Dependencies

#### `docs/brand-guidelines.md` (Master Reference)
**Referenced By:**
- `content/homepage/hero-section.md` - Brand voice and messaging
- `content/about/pedro-story.md` - Professional tone standards
- `seedprod/landing-page-structure.md` - Visual identity elements
- `wordpress/elementor-templates.md` - Color schemes and typography
- `assets/brand-assets/` - Logo usage and brand colors

**Contains:**
- Brand colors (hex codes)
- Typography specifications
- Logo usage guidelines
- Voice and tone standards
- Visual identity rules

#### `seo/keyword-research.md` (SEO Master)
**Referenced By:**
- `content/homepage/hero-section.md` - Primary keyword integration
- `content/services/kitchen-remodeling.md` - Service-specific keywords
- `content/services/bathroom-renovation.md` - Service-specific keywords
- `content/about/pedro-story.md` - Local SEO keywords
- `seedprod/landing-page-structure.md` - Meta descriptions and titles

**Contains:**
- Primary keywords list
- Local SEO terms
- Competitor keyword analysis
- Search volume data
- Keyword difficulty scores

### Implementation Dependencies

#### `wordpress/plugins-list.md` (Technical Foundation)
**Required For:**
- `wordpress/elementor-templates.md` - Plugin functionality dependencies
- `seedprod/landing-page-structure.md` - SeedProd Pro features
- `DEPLOYMENT-GUIDE.md` - Installation sequence
- `docs/site-architecture.md` - Technical requirements

**Depends On:**
- WordPress version compatibility
- Hosting environment specifications
- License requirements

#### `seedprod/landing-page-structure.md` (Phase 1 Implementation)
**Uses Content From:**
- `content/homepage/hero-section.md` - Hero content and CTAs
- `content/services/service-overview.md` - Service descriptions
- `content/contact/contact-info.md` - Contact details and forms
- `assets/images/` - Hero images and service photos

**References:**
- `docs/brand-guidelines.md` - Visual styling
- `seo/keyword-research.md` - SEO optimization
- `wordpress/plugins-list.md` - SeedProd Pro configuration

### Content Block Relationships

#### Homepage Content Chain
```
content/homepage/hero-section.md
├── Uses: docs/brand-guidelines.md (messaging)
├── Uses: seo/keyword-research.md (primary keywords)
├── Uses: content/contact/contact-info.md (CTA details)
└── Feeds Into: seedprod/landing-page-structure.md
```

#### Service Content Chain
```
content/services/
├── kitchen-remodeling.md
│   ├── Uses: seo/keyword-research.md (kitchen keywords)
│   ├── Uses: docs/brand-guidelines.md (service descriptions)
│   └── Feeds Into: wordpress/elementor-templates.md
└── bathroom-renovation.md
    ├── Uses: seo/keyword-research.md (bathroom keywords)
    ├── Uses: docs/brand-guidelines.md (service descriptions)
    └── Feeds Into: wordpress/elementor-templates.md
```

## 📊 Cross-Reference Index

### Business Information Consistency
**Pedro's Credentials (Must Match Across All Files):**
- License Number: `NJ Home Improvement Contractor #13VH13054200`
- Title: `Licensed General Contractor`
- Company: `Top Notch New Jersey`
- Location: `Linden, NJ`
- Established: `2018`

**Files Containing Business Info:**
- `README.md` - Overview and credentials
- `content/about/pedro-story.md` - Detailed background
- `content/contact/contact-info.md` - Contact details
- `seedprod/landing-page-structure.md` - Landing page content
- `docs/brand-guidelines.md` - Brand messaging

### Service Areas Consistency
**Coverage Areas (Must Match):**
- Primary: `Linden, NJ`
- Counties: `Union, Essex, Middlesex, Bergen`

**Files Containing Service Areas:**
- `README.md`
- `content/contact/contact-info.md`
- `seo/keyword-research.md` (local keywords)
- `seedprod/landing-page-structure.md`

### Contact Information Sync Points
**Master Contact Info Location:** `content/contact/contact-info.md`

**Synchronized Across:**
- `README.md` - Basic contact
- `seedprod/landing-page-structure.md` - Landing page forms
- `wordpress/elementor-templates.md` - Template contact sections
- `content/homepage/hero-section.md` - CTA buttons

## 🔄 Update Propagation Rules

### When Updating Brand Guidelines
**Cascade Updates To:**
1. All content files in `content/` directory
2. `seedprod/landing-page-structure.md`
3. `wordpress/elementor-templates.md`
4. Asset files in `assets/brand-assets/`

### When Updating SEO Keywords
**Cascade Updates To:**
1. All content files (natural integration)
2. Meta descriptions in implementation files
3. Alt text specifications in image guidelines

### When Updating Contact Information
**Cascade Updates To:**
1. `README.md` contact section
2. All files in `content/contact/`
3. CTA sections in all content files
4. Form configurations in implementation files

## 🎯 AI Editing Guidelines

### Before Modifying Any File
1. **Check this relationship map** for dependencies
2. **Identify cascade updates** needed
3. **Verify consistency requirements** (business info, contact details)
4. **Plan update sequence** to maintain coherence

### After Modifying Any File
1. **Update version numbers** and timestamps
2. **Check dependent files** for consistency
3. **Verify cross-references** still work
4. **Update this relationship map** if structure changes

### Critical Consistency Points
- **Never change** license numbers or credentials without verification
- **Always maintain** service area accuracy
- **Keep consistent** brand voice across all content
- **Synchronize** contact information changes immediately

## 📅 Relationship Audit Schedule

### Weekly Checks
- Contact information consistency
- Business credential accuracy
- Cross-reference link validation

### Monthly Reviews
- Content dependency updates
- SEO keyword integration consistency
- Brand guideline adherence

### Quarterly Audits
- Complete relationship map review
- File structure optimization
- Dependency simplification opportunities

**Last Updated:** June 2024  
**Next Audit:** September 2024
