# Advanced Custom Fields Configuration - Top Notch New Jersey

## 🔧 ACF Pro Setup for Content Management

### Purpose
Configure Advanced Custom Fields Pro to create custom field groups for Projects, Testimonials, and Service Areas post types, enabling rich content management for Top Notch New Jersey's portfolio and customer reviews.

---

## 📋 Plugin Installation & Setup

### ACF Pro Installation
**Plugin:** Advanced Custom Fields Pro (Premium)
**Version:** 6.0+ recommended
**License:** Required for Pro features

**Installation Steps:**
1. Purchase ACF Pro license from advancedcustomfields.com
2. Download plugin zip from account dashboard
3. WordPress Admin → Plugins → Add New → Upload Plugin
4. Upload advanced-custom-fields-pro.zip and activate
5. Enter license key in Custom Fields → Updates

**Initial Configuration:**
```php
// ACF Pro configuration
add_action('acf/init', 'topnotch_acf_init');
function topnotch_acf_init() {
    // Configure ACF settings
    acf_update_setting('google_api_key', 'YOUR_GOOGLE_MAPS_API_KEY');
    acf_update_setting('show_admin', true);
    acf_update_setting('capability', 'manage_options');
}
```

---

## 🏗️ Projects Post Type Field Groups

### Field Group: Project Details
**Location:** Projects post type
**Group Key:** `group_project_details`

```json
{
  "field_group": {
    "key": "group_project_details",
    "title": "Project Details",
    "fields": [
      {
        "key": "field_project_type",
        "label": "Project Type",
        "name": "project_type",
        "type": "select",
        "required": 1,
        "choices": {
          "kitchen_remodeling": "Kitchen Remodeling",
          "bathroom_renovation": "Bathroom Renovation",
          "complete_home_remodel": "Complete Home Remodel",
          "multiple_rooms": "Multiple Rooms"
        },
        "default_value": "kitchen_remodeling"
      },
      {
        "key": "field_project_scope",
        "label": "Project Scope",
        "name": "project_scope",
        "type": "select",
        "required": 1,
        "choices": {
          "basic_refresh": "Basic Refresh",
          "mid_range_renovation": "Mid-Range Renovation",
          "luxury_transformation": "Luxury Transformation",
          "complete_overhaul": "Complete Overhaul"
        }
      },
      {
        "key": "field_investment_range",
        "label": "Investment Range",
        "name": "investment_range",
        "type": "select",
        "required": 1,
        "choices": {
          "8k_25k": "$8,000 - $25,000",
          "25k_55k": "$25,000 - $55,000",
          "55k_100k": "$55,000 - $100,000",
          "100k_plus": "$100,000+"
        }
      },
      {
        "key": "field_project_timeline",
        "label": "Project Timeline",
        "name": "project_timeline",
        "type": "text",
        "required": 1,
        "placeholder": "e.g., 3-4 weeks"
      },
      {
        "key": "field_square_footage",
        "label": "Square Footage",
        "name": "square_footage",
        "type": "number",
        "required": 0,
        "placeholder": "e.g., 120"
      },
      {
        "key": "field_completion_date",
        "label": "Completion Date",
        "name": "completion_date",
        "type": "date_picker",
        "required": 1,
        "display_format": "F j, Y",
        "return_format": "Y-m-d"
      }
    ],
    "location": [
      [
        {
          "param": "post_type",
          "operator": "==",
          "value": "projects"
        }
      ]
    ]
  }
}
```

### Field Group: Project Images
**Location:** Projects post type
**Group Key:** `group_project_images`

```json
{
  "field_group": {
    "key": "group_project_images",
    "title": "Project Images",
    "fields": [
      {
        "key": "field_before_images",
        "label": "Before Images",
        "name": "before_images",
        "type": "gallery",
        "required": 1,
        "min": 1,
        "max": 10,
        "insert": "append",
        "library": "all",
        "mime_types": "jpg,jpeg,png,webp"
      },
      {
        "key": "field_after_images",
        "label": "After Images",
        "name": "after_images",
        "type": "gallery",
        "required": 1,
        "min": 1,
        "max": 10,
        "insert": "append",
        "library": "all",
        "mime_types": "jpg,jpeg,png,webp"
      },
      {
        "key": "field_process_images",
        "label": "Process Images",
        "name": "process_images",
        "type": "gallery",
        "required": 0,
        "max": 15,
        "insert": "append",
        "library": "all",
        "mime_types": "jpg,jpeg,png,webp"
      },
      {
        "key": "field_featured_before_after",
        "label": "Featured Before/After Comparison",
        "name": "featured_before_after",
        "type": "group",
        "required": 1,
        "sub_fields": [
          {
            "key": "field_featured_before",
            "label": "Before Image",
            "name": "before_image",
            "type": "image",
            "required": 1,
            "return_format": "array",
            "preview_size": "medium"
          },
          {
            "key": "field_featured_after",
            "label": "After Image",
            "name": "after_image",
            "type": "image",
            "required": 1,
            "return_format": "array",
            "preview_size": "medium"
          }
        ]
      }
    ],
    "location": [
      [
        {
          "param": "post_type",
          "operator": "==",
          "value": "projects"
        }
      ]
    ]
  }
}
```

### Field Group: Project Specifications
**Location:** Projects post type
**Group Key:** `group_project_specs`

```json
{
  "field_group": {
    "key": "group_project_specs",
    "title": "Project Specifications",
    "fields": [
      {
        "key": "field_materials_used",
        "label": "Materials Used",
        "name": "materials_used",
        "type": "repeater",
        "required": 0,
        "min": 0,
        "max": 20,
        "layout": "table",
        "button_label": "Add Material",
        "sub_fields": [
          {
            "key": "field_material_category",
            "label": "Category",
            "name": "category",
            "type": "select",
            "choices": {
              "cabinets": "Cabinets",
              "countertops": "Countertops",
              "flooring": "Flooring",
              "fixtures": "Fixtures",
              "appliances": "Appliances",
              "tile": "Tile",
              "paint": "Paint",
              "hardware": "Hardware"
            }
          },
          {
            "key": "field_material_brand",
            "label": "Brand/Manufacturer",
            "name": "brand",
            "type": "text"
          },
          {
            "key": "field_material_model",
            "label": "Model/Style",
            "name": "model",
            "type": "text"
          },
          {
            "key": "field_material_color",
            "label": "Color/Finish",
            "name": "color",
            "type": "text"
          }
        ]
      },
      {
        "key": "field_special_features",
        "label": "Special Features",
        "name": "special_features",
        "type": "checkbox",
        "choices": {
          "kitchen_island": "Kitchen Island",
          "walk_in_shower": "Walk-in Shower",
          "double_vanity": "Double Vanity",
          "pantry": "Walk-in Pantry",
          "heated_floors": "Heated Floors",
          "smart_lighting": "Smart Lighting",
          "accessibility_features": "Accessibility Features",
          "custom_storage": "Custom Storage Solutions"
        }
      },
      {
        "key": "field_challenges_overcome",
        "label": "Challenges Overcome",
        "name": "challenges_overcome",
        "type": "textarea",
        "required": 0,
        "rows": 4,
        "placeholder": "Describe any unique challenges and how they were solved"
      }
    ],
    "location": [
      [
        {
          "param": "post_type",
          "operator": "==",
          "value": "projects"
        }
      ]
    ]
  }
}
```

### Field Group: Client Information
**Location:** Projects post type
**Group Key:** `group_client_info`

```json
{
  "field_group": {
    "key": "group_client_info",
    "title": "Client Information",
    "fields": [
      {
        "key": "field_client_name",
        "label": "Client Name",
        "name": "client_name",
        "type": "text",
        "required": 1,
        "placeholder": "First Name L. (for privacy)"
      },
      {
        "key": "field_project_location",
        "label": "Project Location",
        "name": "project_location",
        "type": "select",
        "required": 1,
        "choices": {
          "union_county": "Union County",
          "essex_county": "Essex County",
          "middlesex_county": "Middlesex County",
          "bergen_county": "Bergen County"
        }
      },
      {
        "key": "field_city",
        "label": "City",
        "name": "city",
        "type": "text",
        "required": 1,
        "placeholder": "e.g., Linden, Elizabeth, Newark"
      },
      {
        "key": "field_client_testimonial",
        "label": "Client Testimonial",
        "name": "client_testimonial",
        "type": "textarea",
        "required": 0,
        "rows": 4,
        "placeholder": "Optional testimonial from the client"
      },
      {
        "key": "field_permission_to_showcase",
        "label": "Permission to Showcase",
        "name": "permission_to_showcase",
        "type": "true_false",
        "required": 1,
        "default_value": 1,
        "message": "Client has given permission to showcase this project"
      }
    ],
    "location": [
      [
        {
          "param": "post_type",
          "operator": "==",
          "value": "projects"
        }
      ]
    ]
  }
}
```

---

## 💬 Testimonials Post Type Field Groups

### Field Group: Customer Information
**Location:** Testimonials post type
**Group Key:** `group_customer_info`

```json
{
  "field_group": {
    "key": "group_customer_info",
    "title": "Customer Information",
    "fields": [
      {
        "key": "field_customer_name",
        "label": "Customer Name",
        "name": "customer_name",
        "type": "text",
        "required": 1,
        "placeholder": "First Name L. (for privacy)"
      },
      {
        "key": "field_customer_photo",
        "label": "Customer Photo",
        "name": "customer_photo",
        "type": "image",
        "required": 0,
        "return_format": "array",
        "preview_size": "thumbnail"
      },
      {
        "key": "field_customer_location",
        "label": "Customer Location",
        "name": "customer_location",
        "type": "select",
        "required": 1,
        "choices": {
          "linden_nj": "Linden, NJ",
          "elizabeth_nj": "Elizabeth, NJ",
          "westfield_nj": "Westfield, NJ",
          "summit_nj": "Summit, NJ",
          "cranford_nj": "Cranford, NJ",
          "newark_nj": "Newark, NJ",
          "montclair_nj": "Montclair, NJ",
          "bloomfield_nj": "Bloomfield, NJ",
          "edison_nj": "Edison, NJ",
          "woodbridge_nj": "Woodbridge, NJ",
          "hackensack_nj": "Hackensack, NJ",
          "paramus_nj": "Paramus, NJ"
        }
      },
      {
        "key": "field_project_completed",
        "label": "Project Completed",
        "name": "project_completed",
        "type": "date_picker",
        "required": 1,
        "display_format": "F Y",
        "return_format": "Y-m-d"
      }
    ],
    "location": [
      [
        {
          "param": "post_type",
          "operator": "==",
          "value": "testimonials"
        }
      ]
    ]
  }
}
```

### Field Group: Review Details
**Location:** Testimonials post type
**Group Key:** `group_review_details`

```json
{
  "field_group": {
    "key": "group_review_details",
    "title": "Review Details",
    "fields": [
      {
        "key": "field_star_rating",
        "label": "Star Rating",
        "name": "star_rating",
        "type": "select",
        "required": 1,
        "choices": {
          "5": "5 Stars - Excellent",
          "4": "4 Stars - Very Good",
          "3": "3 Stars - Good",
          "2": "2 Stars - Fair",
          "1": "1 Star - Poor"
        },
        "default_value": "5"
      },
      {
        "key": "field_review_text",
        "label": "Review Text",
        "name": "review_text",
        "type": "textarea",
        "required": 1,
        "rows": 6,
        "placeholder": "Customer's review of the work performed"
      },
      {
        "key": "field_service_provided",
        "label": "Service Provided",
        "name": "service_provided",
        "type": "select",
        "required": 1,
        "choices": {
          "kitchen_remodeling": "Kitchen Remodeling",
          "bathroom_renovation": "Bathroom Renovation",
          "complete_home_remodel": "Complete Home Remodel",
          "multiple_services": "Multiple Services"
        }
      },
      {
        "key": "field_project_value",
        "label": "Project Investment Range",
        "name": "project_value",
        "type": "select",
        "required": 0,
        "choices": {
          "under_15k": "Under $15,000",
          "15k_30k": "$15,000 - $30,000",
          "30k_60k": "$30,000 - $60,000",
          "60k_100k": "$60,000 - $100,000",
          "100k_plus": "$100,000+"
        }
      },
      {
        "key": "field_review_source",
        "label": "Review Source",
        "name": "review_source",
        "type": "select",
        "required": 1,
        "choices": {
          "google": "Google Reviews",
          "facebook": "Facebook",
          "direct": "Direct Feedback",
          "email": "Email Follow-up",
          "phone": "Phone Interview"
        }
      },
      {
        "key": "field_featured_review",
        "label": "Featured Review",
        "name": "featured_review",
        "type": "true_false",
        "required": 0,
        "default_value": 0,
        "message": "Display this review prominently on homepage"
      }
    ],
    "location": [
      [
        {
          "param": "post_type",
          "operator": "==",
          "value": "testimonials"
        }
      ]
    ]
  }
}
```

---

## 📍 Service Areas Post Type Field Groups

### Field Group: Area Information
**Location:** Service Areas post type
**Group Key:** `group_area_info`

```json
{
  "field_group": {
    "key": "group_area_info",
    "title": "Service Area Information",
    "fields": [
      {
        "key": "field_area_type",
        "label": "Area Type",
        "name": "area_type",
        "type": "select",
        "required": 1,
        "choices": {
          "county": "County",
          "city": "City",
          "neighborhood": "Neighborhood"
        }
      },
      {
        "key": "field_county",
        "label": "County",
        "name": "county",
        "type": "select",
        "required": 1,
        "choices": {
          "union": "Union County",
          "essex": "Essex County",
          "middlesex": "Middlesex County",
          "bergen": "Bergen County"
        }
      },
      {
        "key": "field_population",
        "label": "Population",
        "name": "population",
        "type": "number",
        "required": 0,
        "placeholder": "e.g., 42000"
      },
      {
        "key": "field_median_home_value",
        "label": "Median Home Value",
        "name": "median_home_value",
        "type": "number",
        "required": 0,
        "placeholder": "e.g., 350000"
      },
      {
        "key": "field_service_priority",
        "label": "Service Priority",
        "name": "service_priority",
        "type": "select",
        "required": 1,
        "choices": {
          "primary": "Primary Service Area",
          "secondary": "Secondary Service Area",
          "extended": "Extended Service Area"
        },
        "default_value": "primary"
      }
    ],
    "location": [
      [
        {
          "param": "post_type",
          "operator": "==",
          "value": "service_areas"
        }
      ]
    ]
  }
}
```

### Field Group: Local SEO Data
**Location:** Service Areas post type
**Group Key:** `group_local_seo`

```json
{
  "field_group": {
    "key": "group_local_seo",
    "title": "Local SEO Data",
    "fields": [
      {
        "key": "field_primary_keywords",
        "label": "Primary Keywords",
        "name": "primary_keywords",
        "type": "repeater",
        "required": 1,
        "min": 1,
        "max": 10,
        "layout": "table",
        "button_label": "Add Keyword",
        "sub_fields": [
          {
            "key": "field_keyword",
            "label": "Keyword",
            "name": "keyword",
            "type": "text",
            "required": 1,
            "placeholder": "e.g., kitchen remodeling linden nj"
          },
          {
            "key": "field_search_volume",
            "label": "Monthly Search Volume",
            "name": "search_volume",
            "type": "number",
            "required": 0,
            "placeholder": "e.g., 90"
          },
          {
            "key": "field_difficulty",
            "label": "Keyword Difficulty",
            "name": "difficulty",
            "type": "select",
            "choices": {
              "low": "Low",
              "medium": "Medium",
              "high": "High"
            }
          }
        ]
      },
      {
        "key": "field_local_landmarks",
        "label": "Local Landmarks",
        "name": "local_landmarks",
        "type": "textarea",
        "required": 0,
        "rows": 3,
        "placeholder": "Notable landmarks, schools, shopping centers"
      },
      {
        "key": "field_nearby_cities",
        "label": "Nearby Cities",
        "name": "nearby_cities",
        "type": "text",
        "required": 0,
        "placeholder": "Comma-separated list of nearby cities"
      },
      {
        "key": "field_zip_codes",
        "label": "Zip Codes Served",
        "name": "zip_codes",
        "type": "text",
        "required": 0,
        "placeholder": "Comma-separated list of zip codes"
      }
    ],
    "location": [
      [
        {
          "param": "post_type",
          "operator": "==",
          "value": "service_areas"
        }
      ]
    ]
  }
}
```

---

## 🔧 Custom Functions & Integration

### ACF Template Functions
```php
// Custom functions for displaying ACF fields
function topnotch_get_project_details($post_id = null) {
    if (!$post_id) $post_id = get_the_ID();
    
    return [
        'type' => get_field('project_type', $post_id),
        'scope' => get_field('project_scope', $post_id),
        'investment' => get_field('investment_range', $post_id),
        'timeline' => get_field('project_timeline', $post_id),
        'completion' => get_field('completion_date', $post_id),
        'location' => get_field('project_location', $post_id),
        'city' => get_field('city', $post_id)
    ];
}

function topnotch_get_project_images($post_id = null) {
    if (!$post_id) $post_id = get_the_ID();
    
    return [
        'before' => get_field('before_images', $post_id),
        'after' => get_field('after_images', $post_id),
        'process' => get_field('process_images', $post_id),
        'featured_comparison' => get_field('featured_before_after', $post_id)
    ];
}

function topnotch_get_testimonial_data($post_id = null) {
    if (!$post_id) $post_id = get_the_ID();
    
    return [
        'customer_name' => get_field('customer_name', $post_id),
        'rating' => get_field('star_rating', $post_id),
        'review' => get_field('review_text', $post_id),
        'service' => get_field('service_provided', $post_id),
        'location' => get_field('customer_location', $post_id),
        'date' => get_field('project_completed', $post_id),
        'featured' => get_field('featured_review', $post_id)
    ];
}

function topnotch_display_star_rating($rating) {
    $stars = '';
    for ($i = 1; $i <= 5; $i++) {
        if ($i <= $rating) {
            $stars .= '<span class="star filled">★</span>';
        } else {
            $stars .= '<span class="star empty">☆</span>';
        }
    }
    return $stars;
}
```

### Elementor Integration
```php
// Register ACF fields for Elementor dynamic content
add_action('elementor/init', 'topnotch_register_acf_elementor');
function topnotch_register_acf_elementor() {
    // Register custom dynamic tags for ACF fields
    \Elementor\Plugin::$instance->dynamic_tags->register_group('topnotch-acf', [
        'title' => 'Top Notch ACF Fields'
    ]);
}

// Custom Elementor widget for project showcase
class TopNotch_Project_Widget extends \Elementor\Widget_Base {
    public function get_name() {
        return 'topnotch-project';
    }
    
    public function get_title() {
        return 'Top Notch Project Showcase';
    }
    
    public function get_icon() {
        return 'eicon-gallery-grid';
    }
    
    protected function render() {
        $projects = get_posts([
            'post_type' => 'projects',
            'posts_per_page' => 6,
            'meta_key' => 'featured_project',
            'meta_value' => '1'
        ]);
        
        foreach ($projects as $project) {
            $details = topnotch_get_project_details($project->ID);
            $images = topnotch_get_project_images($project->ID);
            
            // Render project card
            echo '<div class="project-card">';
            echo '<h3>' . get_the_title($project->ID) . '</h3>';
            echo '<p>Type: ' . $details['type'] . '</p>';
            echo '<p>Investment: ' . $details['investment'] . '</p>';
            echo '</div>';
        }
    }
}
```

---

## 🚀 Implementation Checklist

### Phase 1: Plugin Setup
- [ ] Install ACF Pro plugin
- [ ] Activate plugin and enter license key
- [ ] Configure basic ACF settings
- [ ] Test field group creation

### Phase 2: Projects Field Groups
- [ ] Create Project Details field group
- [ ] Create Project Images field group
- [ ] Create Project Specifications field group
- [ ] Create Client Information field group
- [ ] Test all project fields

### Phase 3: Testimonials Field Groups
- [ ] Create Customer Information field group
- [ ] Create Review Details field group
- [ ] Test testimonial field functionality

### Phase 4: Service Areas Field Groups
- [ ] Create Area Information field group
- [ ] Create Local SEO Data field group
- [ ] Test service area field functionality

### Phase 5: Template Integration
- [ ] Create custom template functions
- [ ] Integrate ACF fields with Elementor
- [ ] Test frontend display of custom fields
- [ ] Optimize for mobile responsiveness

### Phase 6: Content Migration
- [ ] Import existing project data
- [ ] Add sample testimonials
- [ ] Create service area pages
- [ ] Test all custom field displays

---

## 📊 Field Validation & Security

### Data Validation
```php
// Custom validation for ACF fields
add_filter('acf/validate_value/name=star_rating', 'topnotch_validate_rating', 10, 4);
function topnotch_validate_rating($valid, $value, $field, $input) {
    if (!$valid) return $valid;
    
    if ($value < 1 || $value > 5) {
        $valid = 'Rating must be between 1 and 5 stars';
    }
    
    return $valid;
}

// Sanitize customer information
add_filter('acf/update_value/name=customer_name', 'topnotch_sanitize_customer_name', 10, 3);
function topnotch_sanitize_customer_name($value, $post_id, $field) {
    // Ensure privacy by limiting to first name and last initial
    $parts = explode(' ', trim($value));
    if (count($parts) > 1) {
        $first_name = $parts[0];
        $last_initial = substr($parts[count($parts) - 1], 0, 1);
        return $first_name . ' ' . $last_initial . '.';
    }
    return $value;
}
```

### Security Measures
```php
// Restrict ACF field access
add_filter('acf/settings/capability', 'topnotch_acf_capability');
function topnotch_acf_capability($capability) {
    return 'manage_options';
}

// Hide sensitive fields from non-admin users
add_filter('acf/prepare_field/name=client_testimonial', 'topnotch_hide_sensitive_fields');
function topnotch_hide_sensitive_fields($field) {
    if (!current_user_can('administrator')) {
        return false;
    }
    return $field;
}
```

---

**ACF Configuration Version:** 1.0  
**Last Updated:** June 2024  
**Dependencies:** ACF Pro 6.0+, Custom Post Types  
**Estimated Setup Time:** 3-4 hours
