# Advanced Custom Fields Setup - Top Notch New Jersey

## ACF Pro Plugin Configuration

### Plugin Installation
**Plugin Name:** Advanced Custom Fields Pro
**Version:** 6.2+ recommended
**Purpose:** Create custom fields for Projects, Testimonials, and Service Areas

### Installation Steps
```bash
# WordPress Admin Dashboard
1. Navigate to Plugins > Add New
2. Upload ACF Pro plugin file (requires license)
3. Install and activate the plugin
4. Enter license key in ACF > Updates
5. Navigate to Custom Fields > Field Groups
```

## Field Groups Configuration

### 1. Project Details Field Group
**Field Group Name:** Project Details
**Location Rules:** Post Type is equal to Projects

#### Fields Configuration:

##### Project Information Section
```
Field Label: Project Type
Field Name: project_type
Field Type: Select
Choices:
- kitchen : Kitchen Remodeling
- bathroom : Bathroom Renovation
- complete_home : Complete Home Remodel
Default Value: kitchen
Required: Yes
```

```
Field Label: Investment Level
Field Name: investment_level
Field Type: Select
Choices:
- basic : Basic ($8,000 - $25,000)
- midrange : Mid-Range ($25,000 - $55,000)
- luxury : Luxury ($55,000+)
Default Value: midrange
Required: Yes
```

```
Field Label: Project Timeline
Field Name: project_timeline
Field Type: Text
Instructions: How long did this project take? (e.g., "3 weeks", "6 weeks")
Required: Yes
```

```
Field Label: Project Location
Field Name: project_location
Field Type: Text
Instructions: City and county (e.g., "Linden, Union County")
Required: Yes
```

##### Before/After Images Section
```
Field Label: Before Images
Field Name: before_images
Field Type: Gallery
Instructions: Upload before renovation images
Return Format: Array
Preview Size: Medium
Library: All
Required: Yes
```

```
Field Label: After Images
Field Name: after_images
Field Type: Gallery
Instructions: Upload after renovation images
Return Format: Array
Preview Size: Medium
Library: All
Required: Yes
```

```
Field Label: Featured Before Image
Field Name: featured_before_image
Field Type: Image
Instructions: Primary before image for comparisons
Return Format: Array
Preview Size: Medium
Library: All
Required: Yes
```

```
Field Label: Featured After Image
Field Name: featured_after_image
Field Type: Image
Instructions: Primary after image for comparisons
Return Format: Array
Preview Size: Medium
Library: All
Required: Yes
```

##### Project Details Section
```
Field Label: Project Scope
Field Name: project_scope
Field Type: Textarea
Instructions: Detailed description of work performed
Rows: 4
Required: Yes
```

```
Field Label: Key Features
Field Name: key_features
Field Type: Repeater
Sub Fields:
  - Feature Name (Text)
  - Feature Description (Textarea, 2 rows)
Min: 1
Max: 10
Layout: Table
Button Label: Add Feature
Required: Yes
```

```
Field Label: Materials Used
Field Name: materials_used
Field Type: Repeater
Sub Fields:
  - Material Type (Text)
  - Brand/Supplier (Text)
  - Notes (Text)
Min: 1
Max: 15
Layout: Table
Button Label: Add Material
Required: No
```

##### Customer Information Section
```
Field Label: Customer Name
Field Name: customer_name
Field Type: Text
Instructions: First name only or initials for privacy
Required: Yes
```

```
Field Label: Customer Location
Field Name: customer_location
Field Type: Text
Instructions: City only (e.g., "Linden")
Required: Yes
```

```
Field Label: Customer Quote
Field Name: customer_quote
Field Type: Textarea
Instructions: Brief testimonial or quote about the project
Rows: 3
Required: No
```

##### SEO and Marketing Section
```
Field Label: Project Highlights
Field Name: project_highlights
Field Type: Checkbox
Choices:
- electrical_work : Professional Electrical Work
- custom_cabinetry : Custom Cabinetry
- luxury_finishes : Luxury Finishes
- accessibility : Accessibility Features
- smart_home : Smart Home Integration
- energy_efficient : Energy Efficient Upgrades
Instructions: Select applicable highlights for marketing
Required: No
```

```
Field Label: SEO Keywords
Field Name: seo_keywords
Field Type: Text
Instructions: Comma-separated keywords for this project
Required: No
```

### 2. Testimonial Details Field Group
**Field Group Name:** Testimonial Details
**Location Rules:** Post Type is equal to Testimonials

#### Fields Configuration:

##### Customer Information Section
```
Field Label: Customer Name
Field Name: customer_name
Field Type: Text
Instructions: Full name or first name + last initial
Required: Yes
```

```
Field Label: Customer Location
Field Name: customer_location
Field Type: Text
Instructions: City and county (e.g., "Linden, Union County")
Required: Yes
```

```
Field Label: Customer Photo
Field Name: customer_photo
Field Type: Image
Instructions: Optional customer photo (with permission)
Return Format: Array
Preview Size: Thumbnail
Library: All
Required: No
```

##### Service Information Section
```
Field Label: Service Type
Field Name: service_type
Field Type: Select
Choices:
- kitchen : Kitchen Remodeling
- bathroom : Bathroom Renovation
- complete_home : Complete Home Remodel
- electrical : Electrical Work
- accessibility : Accessibility Modifications
Required: Yes
```

```
Field Label: Project Investment
Field Name: project_investment
Field Type: Select
Choices:
- under_15k : Under $15,000
- 15k_30k : $15,000 - $30,000
- 30k_60k : $30,000 - $60,000
- 60k_100k : $60,000 - $100,000
- over_100k : Over $100,000
Required: No
```

```
Field Label: Project Date
Field Name: project_date
Field Type: Date Picker
Instructions: When was the project completed?
Display Format: F Y (e.g., "June 2024")
Return Format: Y-m-d
Required: Yes
```

##### Review Details Section
```
Field Label: Star Rating
Field Name: star_rating
Field Type: Select
Choices:
- 5 : 5 Stars
- 4 : 4 Stars
- 3 : 3 Stars
- 2 : 2 Stars
- 1 : 1 Star
Default Value: 5
Required: Yes
```

```
Field Label: Review Title
Field Name: review_title
Field Type: Text
Instructions: Short headline for the review
Required: Yes
```

```
Field Label: Review Text
Field Name: review_text
Field Type: Textarea
Instructions: Full customer review/testimonial
Rows: 6
Required: Yes
```

```
Field Label: Favorite Aspect
Field Name: favorite_aspect
Field Type: Text
Instructions: What the customer liked most about the project
Required: No
```

##### Verification Section
```
Field Label: Verified Review
Field Name: verified_review
Field Type: True/False
Instructions: Has this review been verified?
Default Value: 0
Required: Yes
```

```
Field Label: Review Source
Field Name: review_source
Field Type: Select
Choices:
- direct : Direct Customer Feedback
- google : Google Reviews
- facebook : Facebook Reviews
- referral : Referral Feedback
- email : Email Follow-up
Default Value: direct
Required: Yes
```

```
Field Label: Permission to Use
Field Name: permission_to_use
Field Type: True/False
Instructions: Customer gave permission to use review publicly
Default Value: 0
Required: Yes
```

### 3. Service Area Details Field Group
**Field Group Name:** Service Area Details
**Location Rules:** Post Type is equal to Service Areas

#### Fields Configuration:

##### Location Information Section
```
Field Label: County
Field Name: county
Field Type: Select
Choices:
- union : Union County
- essex : Essex County
- middlesex : Middlesex County
- bergen : Bergen County
Default Value: union
Required: Yes
```

```
Field Label: City/Town
Field Name: city_town
Field Type: Text
Instructions: Primary city or town name
Required: Yes
```

```
Field Label: ZIP Codes Served
Field Name: zip_codes_served
Field Type: Text
Instructions: Comma-separated ZIP codes (e.g., "07036, 07040")
Required: Yes
```

```
Field Label: Service Area Type
Field Name: service_area_type
Field Type: Select
Choices:
- primary : Primary Service Area
- extended : Extended Service Area
Default Value: primary
Required: Yes
```

##### Local SEO Section
```
Field Label: Local Keywords
Field Name: local_keywords
Field Type: Textarea
Instructions: Local SEO keywords for this area (one per line)
Rows: 5
Required: Yes
```

```
Field Label: Local Landmarks
Field Name: local_landmarks
Field Type: Repeater
Sub Fields:
  - Landmark Name (Text)
  - Landmark Type (Select: School, Hospital, Shopping Center, Park, Government)
Min: 0
Max: 10
Layout: Table
Button Label: Add Landmark
Required: No
```

```
Field Label: Population Data
Field Name: population_data
Field Type: Text
Instructions: Approximate population (for local SEO context)
Required: No
```

##### Service Information Section
```
Field Label: Primary Services
Field Name: primary_services
Field Type: Checkbox
Choices:
- kitchen : Kitchen Remodeling
- bathroom : Bathroom Renovation
- complete_home : Complete Home Remodel
- electrical : Electrical Work
- accessibility : Accessibility Modifications
Instructions: Services actively promoted in this area
Required: Yes
```

```
Field Label: Travel Time
Field Name: travel_time
Field Type: Text
Instructions: Travel time from Linden headquarters (e.g., "15 minutes")
Required: Yes
```

```
Field Label: Service Notes
Field Name: service_notes
Field Type: Textarea
Instructions: Special considerations for this service area
Rows: 3
Required: No
```

##### Local Business Information Section
```
Field Label: Local Competitors
Field Name: local_competitors
Field Type: Repeater
Sub Fields:
  - Competitor Name (Text)
  - Competitor Type (Select: General Contractor, Kitchen Specialist, Bathroom Specialist, Electrician)
  - Notes (Textarea, 2 rows)
Min: 0
Max: 5
Layout: Table
Button Label: Add Competitor
Required: No
```

```
Field Label: Local Partnerships
Field Name: local_partnerships
Field Type: Repeater
Sub Fields:
  - Partner Name (Text)
  - Partner Type (Select: Supplier, Subcontractor, Referral Source, Business Network)
  - Contact Info (Text)
Min: 0
Max: 10
Layout: Table
Button Label: Add Partner
Required: No
```

## Field Group Display Settings

### Projects Field Group Settings
```
Position: Normal (after content)
Style: Default
Label Placement: Top
Instruction Placement: Label
Hide on Screen: 
  - Permalink
  - The Content Editor (if using custom layout)
  - Discussion
  - Comments
  - Slug
  - Author
```

### Testimonials Field Group Settings
```
Position: Normal (after content)
Style: Default
Label Placement: Top
Instruction Placement: Label
Hide on Screen:
  - Permalink
  - The Content Editor (if using custom layout)
  - Discussion
  - Comments
  - Slug
  - Author
  - Featured Image (using custom customer photo field)
```

### Service Areas Field Group Settings
```
Position: Normal (after content)
Style: Default
Label Placement: Top
Instruction Placement: Label
Hide on Screen:
  - Discussion
  - Comments
  - Slug
  - Author
```

## Template Integration Code

### Display Project Details in Templates
```php
<?php
// Get project custom fields
$project_type = get_field('project_type');
$investment_level = get_field('investment_level');
$project_timeline = get_field('project_timeline');
$project_location = get_field('project_location');
$before_images = get_field('before_images');
$after_images = get_field('after_images');
$project_scope = get_field('project_scope');
$key_features = get_field('key_features');
$customer_name = get_field('customer_name');
$customer_quote = get_field('customer_quote');

// Display project information
if ($project_type) {
    echo '<div class="project-type">' . esc_html($project_type) . '</div>';
}

if ($investment_level) {
    echo '<div class="investment-level">' . esc_html($investment_level) . '</div>';
}

// Display before/after images
if ($before_images && $after_images) {
    echo '<div class="before-after-gallery">';
    // Before/After slider implementation
    echo '</div>';
}

// Display key features
if ($key_features) {
    echo '<div class="key-features">';
    echo '<h3>Key Features</h3>';
    echo '<ul>';
    foreach ($key_features as $feature) {
        echo '<li><strong>' . esc_html($feature['feature_name']) . '</strong>: ' . esc_html($feature['feature_description']) . '</li>';
    }
    echo '</ul>';
    echo '</div>';
}
?>
```

### Display Testimonial Details in Templates
```php
<?php
// Get testimonial custom fields
$customer_name = get_field('customer_name');
$customer_location = get_field('customer_location');
$service_type = get_field('service_type');
$star_rating = get_field('star_rating');
$review_title = get_field('review_title');
$review_text = get_field('review_text');
$project_date = get_field('project_date');
$verified_review = get_field('verified_review');

// Display testimonial
echo '<div class="testimonial-card">';
echo '<div class="testimonial-header">';
echo '<h3>' . esc_html($review_title) . '</h3>';
echo '<div class="star-rating">';
for ($i = 1; $i <= 5; $i++) {
    if ($i <= $star_rating) {
        echo '<span class="star filled">★</span>';
    } else {
        echo '<span class="star">☆</span>';
    }
}
echo '</div>';
echo '</div>';

echo '<div class="testimonial-content">';
echo '<p>"' . esc_html($review_text) . '"</p>';
echo '</div>';

echo '<div class="testimonial-footer">';
echo '<div class="customer-info">';
echo '<strong>' . esc_html($customer_name) . '</strong>';
echo '<span class="location">' . esc_html($customer_location) . '</span>';
echo '<span class="service">' . esc_html($service_type) . '</span>';
if ($verified_review) {
    echo '<span class="verified">✓ Verified</span>';
}
echo '</div>';
echo '</div>';
echo '</div>';
?>
```

### Display Service Area Details in Templates
```php
<?php
// Get service area custom fields
$county = get_field('county');
$city_town = get_field('city_town');
$zip_codes = get_field('zip_codes_served');
$service_area_type = get_field('service_area_type');
$primary_services = get_field('primary_services');
$travel_time = get_field('travel_time');
$local_landmarks = get_field('local_landmarks');

// Display service area information
echo '<div class="service-area-details">';
echo '<h2>Kitchen & Bathroom Remodeling in ' . esc_html($city_town) . ', ' . esc_html($county) . '</h2>';

if ($primary_services) {
    echo '<div class="services-offered">';
    echo '<h3>Services Available in ' . esc_html($city_town) . '</h3>';
    echo '<ul>';
    foreach ($primary_services as $service) {
        echo '<li>' . esc_html($service) . '</li>';
    }
    echo '</ul>';
    echo '</div>';
}

if ($travel_time) {
    echo '<div class="service-info">';
    echo '<p><strong>Service Response Time:</strong> ' . esc_html($travel_time) . ' from our Linden headquarters</p>';
    echo '</div>';
}

if ($local_landmarks) {
    echo '<div class="local-landmarks">';
    echo '<h3>Serving Areas Near:</h3>';
    echo '<ul>';
    foreach ($local_landmarks as $landmark) {
        echo '<li>' . esc_html($landmark['landmark_name']) . ' (' . esc_html($landmark['landmark_type']) . ')</li>';
    }
    echo '</ul>';
    echo '</div>';
}
echo '</div>';
?>
```

## Implementation Checklist

### Phase 1: Plugin Setup
- [ ] Install ACF Pro plugin
- [ ] Activate plugin and enter license key
- [ ] Configure plugin settings

### Phase 2: Field Groups Creation
- [ ] Create Project Details field group with all fields
- [ ] Create Testimonial Details field group with all fields
- [ ] Create Service Area Details field group with all fields
- [ ] Test field group functionality

### Phase 3: Template Integration
- [ ] Update single-projects.php template
- [ ] Update single-testimonials.php template
- [ ] Update single-service_areas.php template
- [ ] Update archive templates

### Phase 4: Content Entry
- [ ] Add sample project with all custom fields
- [ ] Add sample testimonials with all custom fields
- [ ] Add service area pages with all custom fields
- [ ] Test frontend display

### Phase 5: Optimization
- [ ] Configure field caching for performance
- [ ] Set up field validation rules
- [ ] Test mobile responsiveness
- [ ] Optimize database queries

---

**Advanced Custom Fields Setup Version:** 1.0  
**Last Updated:** June 2024  
**Plugin Dependency:** ACF Pro 6.2+  
**WordPress Version:** 6.5+ required
