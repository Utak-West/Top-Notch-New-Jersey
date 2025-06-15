# Custom Post Types Setup - Top Notch New Jersey

## Custom Post Type UI Plugin Configuration

### Plugin Installation
**Plugin Name:** Custom Post Type UI
**Version:** 1.13+ recommended
**Purpose:** Create custom post types for Projects, Testimonials, and Service Areas

### Installation Steps
```bash
# WordPress Admin Dashboard
1. Navigate to Plugins > Add New
2. Search for "Custom Post Type UI"
3. Install and activate the plugin
4. Navigate to CPT UI > Add/Edit Post Types
```

## Custom Post Types Configuration

### 1. Projects Post Type (`projects`)
**Purpose:** Kitchen and bathroom project portfolio showcase
**Slug:** `projects`
**Menu Position:** 5 (below Posts)

**Basic Settings:**
```
Post Type Slug: projects
Plural Label: Projects
Singular Label: Project
Description: Kitchen and bathroom renovation project portfolio
```

**Advanced Settings:**
```
Public: True
Publicly Queryable: True
Show UI: True
Show in Menu: True
Menu Position: 5
Menu Icon: dashicons-hammer
Show in Admin Bar: True
Show in Nav Menus: True
Can Export: True
Delete with User: False
Show in REST: True
REST Base: projects
REST Controller Class: WP_REST_Posts_Controller
Has Archive: True
Archive Slug: portfolio
Exclude from Search: False
Capability Type: post
Hierarchical: False
Rewrite: True
Rewrite Slug: portfolio
Rewrite with Front: True
Query Var: True
Query Var Slug: projects
```

**Supports:**
- Title
- Editor
- Thumbnail
- Excerpt
- Custom Fields
- Revisions
- Author
- Page Attributes

**Labels Configuration:**
```
Menu Name: Projects
All Items: All Projects
Add New: Add New Project
Add New Item: Add New Project
Edit Item: Edit Project
New Item: New Project
View Item: View Project
View Items: View Projects
Search Items: Search Projects
Not Found: No projects found
Not Found in Trash: No projects found in trash
Parent Item Colon: Parent Project:
Featured Image: Project Featured Image
Set Featured Image: Set project featured image
Remove Featured Image: Remove project featured image
Use as Featured Image: Use as project featured image
Archives: Project Archives
Insert into Item: Insert into project
Uploaded to this Item: Uploaded to this project
Filter Items List: Filter projects list
Items List Navigation: Projects list navigation
Items List: Projects list
Attributes: Project Attributes
Name Admin Bar: Project
Item Published: Project published
Item Published Privately: Project published privately
Item Reverted to Draft: Project reverted to draft
Item Scheduled: Project scheduled
Item Updated: Project updated
Item Link: Project Link
Item Link Description: A link to a project
```

**Taxonomies:**
- Project Type (Kitchen, Bathroom, Complete Home)
- Project Style (Modern, Traditional, Farmhouse, Luxury)
- Investment Level (Basic, Mid-Range, Luxury)
- Location (Union County, Essex County, etc.)

### 2. Testimonials Post Type (`testimonials`)
**Purpose:** Customer reviews and testimonials management
**Slug:** `testimonials`
**Menu Position:** 6

**Basic Settings:**
```
Post Type Slug: testimonials
Plural Label: Testimonials
Singular Label: Testimonial
Description: Customer reviews and testimonials
```

**Advanced Settings:**
```
Public: True
Publicly Queryable: True
Show UI: True
Show in Menu: True
Menu Position: 6
Menu Icon: dashicons-star-filled
Show in Admin Bar: True
Show in Nav Menus: False
Can Export: True
Delete with User: False
Show in REST: True
REST Base: testimonials
Has Archive: True
Archive Slug: testimonials
Exclude from Search: False
Capability Type: post
Hierarchical: False
Rewrite: True
Rewrite Slug: testimonials
Rewrite with Front: True
Query Var: True
Query Var Slug: testimonials
```

**Supports:**
- Title
- Editor
- Thumbnail
- Custom Fields
- Revisions

**Labels Configuration:**
```
Menu Name: Testimonials
All Items: All Testimonials
Add New: Add New Testimonial
Add New Item: Add New Testimonial
Edit Item: Edit Testimonial
New Item: New Testimonial
View Item: View Testimonial
View Items: View Testimonials
Search Items: Search Testimonials
Not Found: No testimonials found
Not Found in Trash: No testimonials found in trash
Featured Image: Customer Photo
Set Featured Image: Set customer photo
Remove Featured Image: Remove customer photo
Use as Featured Image: Use as customer photo
```

**Taxonomies:**
- Service Type (Kitchen, Bathroom, Complete Home)
- Rating (5 Stars, 4 Stars, etc.)
- Location (by county)

### 3. Service Areas Post Type (`service_areas`)
**Purpose:** Local SEO pages for service areas
**Slug:** `service_areas`
**Menu Position:** 7

**Basic Settings:**
```
Post Type Slug: service_areas
Plural Label: Service Areas
Singular Label: Service Area
Description: Local SEO pages for service coverage areas
```

**Advanced Settings:**
```
Public: True
Publicly Queryable: True
Show UI: True
Show in Menu: True
Menu Position: 7
Menu Icon: dashicons-location-alt
Show in Admin Bar: True
Show in Nav Menus: True
Can Export: True
Delete with User: False
Show in REST: True
REST Base: service-areas
Has Archive: True
Archive Slug: service-areas
Exclude from Search: False
Capability Type: post
Hierarchical: True
Rewrite: True
Rewrite Slug: service-areas
Rewrite with Front: True
Query Var: True
Query Var Slug: service_areas
```

**Supports:**
- Title
- Editor
- Thumbnail
- Excerpt
- Custom Fields
- Revisions
- Page Attributes
- Hierarchical (for county > city structure)

**Labels Configuration:**
```
Menu Name: Service Areas
All Items: All Service Areas
Add New: Add New Service Area
Add New Item: Add New Service Area
Edit Item: Edit Service Area
New Item: New Service Area
View Item: View Service Area
View Items: View Service Areas
Search Items: Search Service Areas
Not Found: No service areas found
Not Found in Trash: No service areas found in trash
Parent Item Colon: Parent Service Area:
```

**Taxonomies:**
- County (Union, Essex, Middlesex, Bergen)
- Service Type (Primary, Extended)
- Population Size (Small Town, City, Large City)

## Custom Taxonomies Configuration

### 1. Project Type Taxonomy
**Taxonomy Slug:** `project_type`
**Object Types:** Projects
**Hierarchical:** True

**Terms:**
- Kitchen Remodeling
  - Basic Kitchen Refresh
  - Mid-Range Kitchen Renovation
  - Luxury Kitchen Transformation
- Bathroom Renovation
  - Essential Bathroom Update
  - Complete Bathroom Renovation
  - Luxury Spa Bathroom
- Complete Home Remodel
  - Multi-Room Projects
  - Whole House Renovations

### 2. Project Style Taxonomy
**Taxonomy Slug:** `project_style`
**Object Types:** Projects
**Hierarchical:** False

**Terms:**
- Modern
- Traditional
- Farmhouse
- Contemporary
- Transitional
- Luxury
- Minimalist
- Industrial

### 3. Investment Level Taxonomy
**Taxonomy Slug:** `investment_level`
**Object Types:** Projects, Testimonials
**Hierarchical:** True

**Terms:**
- Basic ($8,000 - $25,000)
- Mid-Range ($25,000 - $55,000)
- Luxury ($55,000+)

### 4. Location Taxonomy
**Taxonomy Slug:** `location`
**Object Types:** Projects, Testimonials, Service Areas
**Hierarchical:** True

**Terms:**
- Union County
  - Linden
  - Elizabeth
  - Westfield
  - Summit
  - Cranford
  - Plainfield
  - Rahway
- Essex County
  - Newark
  - Montclair
  - Bloomfield
  - East Orange
  - Nutley
  - Belleville
- Middlesex County
  - Edison
  - Woodbridge
  - New Brunswick
  - Perth Amboy
  - Carteret
- Bergen County
  - Hackensack
  - Paramus
  - Fort Lee
  - Englewood
  - Teaneck

### 5. Service Type Taxonomy
**Taxonomy Slug:** `service_type`
**Object Types:** Testimonials, Service Areas
**Hierarchical:** False

**Terms:**
- Kitchen Remodeling
- Bathroom Renovation
- Complete Home Remodel
- Accessibility Modifications

## Implementation Checklist

### Phase 1: Plugin Installation
- [ ] Install Custom Post Type UI plugin
- [ ] Activate plugin and verify functionality
- [ ] Configure plugin settings and permissions

### Phase 2: Post Types Creation
- [ ] Create Projects post type with all settings
- [ ] Create Testimonials post type with all settings
- [ ] Create Service Areas post type with all settings
- [ ] Test post type creation and editing

### Phase 3: Taxonomies Setup
- [ ] Create Project Type taxonomy with hierarchical terms
- [ ] Create Project Style taxonomy with style terms
- [ ] Create Investment Level taxonomy with pricing tiers
- [ ] Create Location taxonomy with county/city structure
- [ ] Create Service Type taxonomy with service categories

### Phase 4: Content Migration
- [ ] Import existing project data from content files
- [ ] Add sample testimonials for testing
- [ ] Create service area pages for primary counties
- [ ] Configure taxonomy assignments

### Phase 5: Template Integration
- [ ] Update Elementor templates to use custom post types
- [ ] Configure archive pages for each post type
- [ ] Set up single post templates
- [ ] Test frontend display and functionality

### Phase 6: SEO Configuration
- [ ] Configure URL structures for SEO
- [ ] Set up meta tags and descriptions
- [ ] Configure schema markup for each post type
- [ ] Test search engine indexing

## URL Structure Configuration

### Projects URLs
```
Single Project: /portfolio/project-name/
Project Archive: /portfolio/
Project by Type: /portfolio/kitchen-remodeling/
Project by Style: /portfolio/modern/
Project by Location: /portfolio/union-county/
```

### Testimonials URLs
```
Single Testimonial: /testimonials/customer-name/
Testimonials Archive: /testimonials/
Testimonials by Service: /testimonials/kitchen-remodeling/
Testimonials by Location: /testimonials/linden-nj/
```

### Service Areas URLs
```
Single Service Area: /service-areas/linden-nj/
Service Areas Archive: /service-areas/
Service Areas by County: /service-areas/union-county/
```

## Database Considerations

### Performance Optimization
- Index custom fields for faster queries
- Optimize taxonomy queries for large datasets
- Configure caching for custom post type archives
- Set up database maintenance schedules

### Backup Strategy
- Include custom post types in regular backups
- Export custom field configurations
- Document taxonomy structures
- Maintain content migration scripts

---

**Custom Post Types Setup Version:** 1.0  
**Last Updated:** June 2024  
**Plugin Dependency:** Custom Post Type UI 1.13+  
**WordPress Version:** 6.5+ required
