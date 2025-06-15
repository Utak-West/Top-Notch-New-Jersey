# Contact Page Template - Top Notch New Jersey

## Contact Page Elementor Pro Implementation

### Template Overview
**Template Name:** `contact-page-template`
**Template Type:** Contact Page Template
**URL Structure:** `/contact/`
**Focus:** Lead generation and contact information

## Section-by-Section Implementation

### Section 1: Contact Hero (`contact-header`)
**Elementor Widget:** Hero Section
**Background:** Subtle pattern or solid brand color

**Hero Content Structure:**
```html
<div class="contact-hero-section">
  <div class="hero-content">
    <h1>Get Your Free Estimate Today</h1>
    <h2>Licensed, Bonded & Insured</h2>
    <p class="hero-subtitle">Ready to transform your kitchen or bathroom? Contact Pedro Ribeiro for a professional consultation and detailed estimate.</p>
    
    <div class="contact-credentials">
      <div class="credential-item">
        <span class="credential-text">Licensed, Bonded & Insured Contractor</span>
      </div>
      <div class="credential-item">
        <span class="credential-text">Serving Union, Essex, Middlesex & Bergen Counties</span>
      </div>
      <div class="credential-item">
        <span class="credential-text">Response within 2 hours during business hours</span>
      </div>
    </div>
  </div>
</div>
```

### Section 2: Contact Methods (`contact-options`)
**Elementor Widget:** Icon Box Grid
**Layout:** 3-column grid

**Contact Methods Implementation:**
```html
<div class="contact-methods-section">
  <div class="section-header">
    <h2>How to Reach Us</h2>
    <p>Choose the contact method that works best for you</p>
  </div>
  
  <div class="contact-methods-grid">
    <!-- Phone Contact -->
    <div class="contact-method phone-contact">
      <div class="method-icon">
        <img src="/wp-content/uploads/phone-icon.svg" alt="Phone">
      </div>
      <h3>Call or Text</h3>
      <div class="contact-details">
        <a href="tel:+1XXXXXXXXXX" class="phone-number">(XXX) XXX-XXXX</a>
        <p>Fastest response - call or text anytime</p>
        <div class="hours">
          <strong>Business Hours:</strong><br>
          Monday-Friday: 8AM-6PM<br>
          Saturday: 9AM-4PM<br>
          Sunday: Emergency only
        </div>
      </div>
      <a href="tel:+1XXXXXXXXXX" class="method-cta">Call Now</a>
    </div>
    
    <!-- Email Contact -->
    <div class="contact-method email-contact">
      <div class="method-icon">
        <img src="/wp-content/uploads/email-icon.svg" alt="Email">
      </div>
      <h3>Email Us</h3>
      <div class="contact-details">
        <a href="mailto:info@topnotchnewjersey.com" class="email-address">info@topnotchnewjersey.com</a>
        <p>Detailed project inquiries and questions</p>
        <div class="response-time">
          <strong>Response Time:</strong><br>
          Within 4 hours during business hours<br>
          Next business day for weekend emails
        </div>
      </div>
      <a href="mailto:info@topnotchnewjersey.com" class="method-cta">Send Email</a>
    </div>
    
    <!-- In-Person Consultation -->
    <div class="contact-method consultation-contact">
      <div class="method-icon">
        <img src="/wp-content/uploads/consultation-icon.svg" alt="Consultation">
      </div>
      <h3>Free Consultation</h3>
      <div class="contact-details">
        <p class="consultation-text">In-home assessment and estimate</p>
        <p>Pedro personally visits your home to assess your project and provide detailed recommendations</p>
        <div class="consultation-includes">
          <strong>Includes:</strong><br>
          Space assessment<br>
          Design recommendations<br>
          Written estimate<br>
          Timeline discussion
        </div>
      </div>
      <a href="#main-contact-form" class="method-cta">Schedule Consultation</a>
    </div>
  </div>
</div>
```

### Section 3: Main Contact Form (`main-contact-form`)
**Elementor Widget:** WPForms Pro Integration
**Layout:** Comprehensive contact form

**Form Implementation:**
```html
<div class="main-contact-form-section" id="main-contact-form">
  <div class="section-header">
    <h2>Request Your Free Estimate</h2>
    <p>Tell us about your project and we'll provide a detailed estimate</p>
  </div>
  
  <div class="form-content">
    <div class="form-container">
      <!-- WPForms Pro Main Contact Form -->
      [wpforms id="1001" title="false" description="false"]
    </div>
    
    <div class="form-sidebar">
      <div class="form-benefits">
        <h3>What You Get:</h3>
        <ul class="benefits-list">
          <li>
            <span class="benefit-icon">✓</span>
            <span>Free in-home consultation</span>
          </li>
          <li>
            <span class="benefit-icon">✓</span>
            <span>Detailed written estimate</span>
          </li>
          <li>
            <span class="benefit-icon">✓</span>
            <span>Design recommendations</span>
          </li>
          <li>
            <span class="benefit-icon">✓</span>
            <span>Timeline and process explanation</span>
          </li>
          <li>
            <span class="benefit-icon">✓</span>
            <span>No obligation or pressure</span>
          </li>
        </ul>
      </div>
      
      <div class="trust-indicators">
        <h3>Why Choose Top Notch:</h3>
        <div class="trust-item">
          <span class="trust-icon">✓</span>
          <span>Licensed Home Improvement Contractor</span>
        </div>
        <div class="trust-item">
          <span class="trust-icon">✓</span>
          <span>Bonded & Insured</span>
        </div>
        <div class="trust-item">
          <span class="trust-icon">✓</span>
          <span>15+ Years Experience</span>
        </div>
        <div class="trust-item">
          <span class="trust-icon">✓</span>
          <span>Local Linden Business</span>
        </div>
        <div class="trust-item">
          <span class="trust-icon">✓</span>
          <span>Transparent Pricing</span>
        </div>
      </div>
    </div>
  </div>
</div>
```

### Section 4: Service Areas (`coverage-areas`)
**Elementor Widget:** Map + Text
**Layout:** Service area coverage details

**Service Areas Implementation:**
```html
<div class="service-areas-section">
  <div class="section-header">
    <h2>Our Service Areas</h2>
    <p>Professional kitchen and bathroom remodeling across New Jersey</p>
  </div>
  
  <div class="service-areas-content">
    <div class="areas-map">
      <img src="/wp-content/uploads/nj-service-areas.png" alt="Top Notch New Jersey Service Areas">
    </div>
    
    <div class="areas-details">
      <div class="primary-areas">
        <h3>Primary Service Areas</h3>
        <div class="areas-grid">
          <div class="area-column">
            <h4>Union County</h4>
            <ul>
              <li>Linden (Headquarters)</li>
              <li>Elizabeth</li>
              <li>Westfield</li>
              <li>Summit</li>
              <li>Cranford</li>
              <li>Plainfield</li>
              <li>Rahway</li>
              <li>Roselle</li>
            </ul>
          </div>
          
          <div class="area-column">
            <h4>Essex County</h4>
            <ul>
              <li>Newark</li>
              <li>Montclair</li>
              <li>Bloomfield</li>
              <li>East Orange</li>
              <li>Nutley</li>
              <li>Belleville</li>
              <li>Irvington</li>
              <li>Maplewood</li>
            </ul>
          </div>
          
          <div class="area-column">
            <h4>Middlesex County</h4>
            <ul>
              <li>Edison</li>
              <li>Woodbridge</li>
              <li>New Brunswick</li>
              <li>Perth Amboy</li>
              <li>Carteret</li>
              <li>Metuchen</li>
              <li>Piscataway</li>
              <li>Sayreville</li>
            </ul>
          </div>
          
          <div class="area-column">
            <h4>Bergen County</h4>
            <ul>
              <li>Hackensack</li>
              <li>Paramus</li>
              <li>Fort Lee</li>
              <li>Englewood</li>
              <li>Teaneck</li>
              <li>Bergenfield</li>
              <li>Fair Lawn</li>
              <li>Garfield</li>
            </ul>
          </div>
        </div>
      </div>
      
      <div class="extended-coverage">
        <h3>Extended Coverage</h3>
        <p>We also serve surrounding New Jersey communities. If you don't see your town listed, please contact us to confirm service availability in your area.</p>
        
        <div class="coverage-note">
          <p><strong>Travel Policy:</strong> No additional travel charges within our primary service areas. Minimal travel fees may apply for extended coverage areas.</p>
        </div>
      </div>
    </div>
  </div>
</div>
```

### Section 5: Business Information (`business-info`)
**Elementor Widget:** Text + Image
**Layout:** Business details and credentials

**Business Information Implementation:**
```html
<div class="business-info-section">
  <div class="section-header">
    <h2>About Top Notch New Jersey</h2>
    <p>Licensed, experienced, and trusted in the community</p>
  </div>
  
  <div class="business-content">
    <div class="business-details">
      <div class="business-item">
        <h3>Business Information</h3>
        <div class="info-grid">
          <div class="info-item">
            <strong>Business Name:</strong>
            <span>Top Notch New Jersey</span>
          </div>
          <div class="info-item">
            <strong>Owner:</strong>
            <span>Pedro Ribeiro</span>
          </div>
          <div class="info-item">
            <strong>License:</strong>
            <span>Licensed, Bonded & Insured</span>
          </div>
          <div class="info-item">
            <strong>Established:</strong>
            <span>2018</span>
          </div>
          <div class="info-item">
            <strong>Headquarters:</strong>
            <span>Linden, New Jersey</span>
          </div>
          <div class="info-item">
            <strong>Insurance:</strong>
            <span>Bonded & Insured</span>
          </div>
        </div>
      </div>
      
      <div class="business-item">
        <h3>Services Offered</h3>
        <ul class="services-list">
          <li>Kitchen Remodeling</li>
          <li>Bathroom Renovation</li>
          <li>Complete Home Remodels</li>
          <li>Electrical Work & Upgrades</li>
          <li>Accessibility Modifications</li>
          <li>Custom Cabinetry Installation</li>
          <li>Tile & Flooring Installation</li>
          <li>Plumbing Fixture Installation</li>
        </ul>
      </div>
      
      <div class="business-item">
        <h3>Payment Options</h3>
        <div class="payment-options">
          <div class="payment-item">
            <span class="payment-icon">✓</span>
            <span>Cash</span>
          </div>
          <div class="payment-item">
            <span class="payment-icon">✓</span>
            <span>Check</span>
          </div>
          <div class="payment-item">
            <span class="payment-icon">✓</span>
            <span>Credit Cards</span>
          </div>
          <div class="payment-item">
            <span class="payment-icon">✓</span>
            <span>Financing Available</span>
          </div>
        </div>
      </div>
    </div>
    
    <div class="business-image">
      <img src="/wp-content/uploads/pedro-business-photo.jpg" alt="Pedro Ribeiro - Top Notch New Jersey">
      <div class="image-caption">
        <p>Pedro Ribeiro, Licensed Home Improvement Contractor and Owner of Top Notch New Jersey</p>
      </div>
    </div>
  </div>
</div>
```

### Section 6: FAQ Section (`contact-faq`)
**Elementor Widget:** Accordion/Toggle
**Layout:** Common contact and process questions

**FAQ Implementation:**
```html
<div class="contact-faq-section">
  <div class="section-header">
    <h2>Frequently Asked Questions</h2>
    <p>Common questions about our process and services</p>
  </div>
  
  <div class="faq-grid">
    <div class="faq-column">
      <!-- FAQ Item 1 -->
      <div class="faq-item">
        <div class="faq-question">
          <h3>How quickly can you provide an estimate?</h3>
          <span class="faq-toggle">+</span>
        </div>
        <div class="faq-answer">
          <p>We respond to all inquiries within 2 hours during business hours. For most projects, we can schedule an in-home consultation within 24-48 hours and provide a detailed written estimate the same day as the consultation.</p>
        </div>
      </div>
      
      <!-- FAQ Item 2 -->
      <div class="faq-item">
        <div class="faq-question">
          <h3>Is the consultation really free?</h3>
          <span class="faq-toggle">+</span>
        </div>
        <div class="faq-answer">
          <p>Yes, absolutely! Our in-home consultation is completely free with no obligation. Pedro will assess your space, discuss your vision, and provide a detailed written estimate at no cost to you.</p>
        </div>
      </div>
      
      <!-- FAQ Item 3 -->
      <div class="faq-item">
        <div class="faq-question">
          <h3>Do you provide financing options?</h3>
          <span class="faq-toggle">+</span>
        </div>
        <div class="faq-answer">
          <p>Yes, we offer financing options for qualified customers. We can discuss financing during your consultation and help you find a payment plan that works for your budget.</p>
        </div>
      </div>
    </div>
    
    <div class="faq-column">
      <!-- FAQ Item 4 -->
      <div class="faq-item">
        <div class="faq-question">
          <h3>What areas do you serve?</h3>
          <span class="faq-toggle">+</span>
        </div>
        <div class="faq-answer">
          <p>We primarily serve Union, Essex, Middlesex, and Bergen Counties in New Jersey. Our headquarters is in Linden, NJ. We also serve surrounding communities - contact us to confirm service availability in your area.</p>
        </div>
      </div>
      
      <!-- FAQ Item 5 -->
      <div class="faq-item">
        <div class="faq-question">
          <h3>Are you licensed and insured?</h3>
          <span class="faq-toggle">+</span>
        </div>
        <div class="faq-answer">
          <p>Yes, Pedro is a Licensed Home Improvement Contractor and Top Notch New Jersey is fully bonded and insured. All work is performed to code and backed by comprehensive insurance coverage.</p>
        </div>
      </div>
      
      <!-- FAQ Item 6 -->
      <div class="faq-item">
        <div class="faq-question">
          <h3>What makes you different from other contractors?</h3>
          <span class="faq-toggle">+</span>
        </div>
        <div class="faq-answer">
          <p>Pedro's Licensed Contractor credentials allow us to handle electrical work coordination in-house, eliminating subcontractor markups. You get one point of contact, coordinated project management, and the expertise of a licensed professional overseeing every aspect of your project.</p>
        </div>
      </div>
    </div>
  </div>
</div>
```

## Mobile Optimization

### Contact Page Mobile Settings
```css
@media (max-width: 768px) {
  /* Contact Methods Grid */
  .contact-methods-grid {
    grid-template-columns: 1fr;
    gap: 30px;
  }
  
  /* Form Content */
  .form-content {
    flex-direction: column;
  }
  
  .form-sidebar {
    margin-top: 30px;
  }
  
  /* Service Areas Grid */
  .areas-grid {
    grid-template-columns: 1fr;
  }
  
  /* Business Content */
  .business-content {
    flex-direction: column;
  }
  
  .business-image {
    margin-top: 30px;
  }
  
  /* FAQ Grid */
  .faq-grid {
    grid-template-columns: 1fr;
  }
}
```

## SEO Configuration

### Contact Page SEO Elements
```html
<!-- Page Title -->
<title>Contact Top Notch New Jersey | Free Estimates | Licensed Contractor</title>

<!-- Meta Description -->
<meta name="description" content="Contact Top Notch New Jersey for free kitchen and bathroom remodeling estimates. Licensed Home Improvement Contractor Pedro Ribeiro. Serving Union, Essex, Middlesex & Bergen Counties.">

<!-- Local Keywords -->
<meta name="keywords" content="contact contractor NJ, free estimate kitchen bathroom, licensed electrician Linden, home improvement consultation Union County">

<!-- Schema Markup -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "name": "Contact Top Notch New Jersey",
  "description": "Contact information for Top Notch New Jersey home improvement services",
  "url": "https://topnotchnewjersey.com/contact/",
  "mainEntity": {
    "@type": "LocalBusiness",
    "name": "Top Notch New Jersey",
    "telephone": "+1XXXXXXXXXX",
    "email": "info@topnotchnewjersey.com"
  }
}
</script>
```

---

**Contact Page Template Version:** 1.0  
**Last Updated:** June 2024  
**Elementor Pro Version:** 3.21+  
**Mobile Optimization:** Complete  
**SEO Optimization:** Contact + Local Business
