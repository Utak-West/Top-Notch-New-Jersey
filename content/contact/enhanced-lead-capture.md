# Enhanced Lead Capture System - Top Notch New Jersey

---
**Document Type:** Advanced Lead Generation & Conversion Optimization System
**Project:** Top Notch New Jersey Website
**Owner:** Pedro Ribeiro, Licensed Master Electrician
**License:** NJ Home Improvement Contractor #13VH13
**Last Updated:** June 2024
**Version:** 2.0 - Kitchen & Bathroom Focus
**Dependencies:** kitchen-remodeling.md, bathroom-remodeling.md, pricing-strategy.md
---

## CONVERSION ARCHITECTURE OVERVIEW

### Primary Business Focus
- **Kitchen Remodeling** (Primary specialty)
- **Bathroom Renovations** (Primary specialty)
- **Whole Home Renovations** (Complete transformations)
- **Electrical Services** (Supporting service with Master Electrician advantage)

### Key Differentiator
**Master Electrician Advantage:** Pedro's electrical expertise eliminates subcontractor markups during renovations, saving customers thousands while ensuring seamless project coordination.

## HERO SECTION CONVERSION PANEL

### Main Conversion Component

```html
<div class="hero-conversion-panel">
  <div class="credential-badge">
    <span class="license-number">Master Electrician #13VH13</span>
    <span class="location">Serving Union, Essex, Middlesex & Bergen Counties</span>
  </div>
  
  <h1>New Jersey's Kitchen & Bathroom Remodeling Experts</h1>
  <h2>Master Electrician Advantage - No Electrical Subcontractor Markups</h2>
  <p>Pedro Ribeiro personally oversees every renovation project from start to finish</p>
  
  <div class="cta-button-group">
    <button class="primary-cta">Get Free Kitchen Estimate</button>
    <button class="secondary-cta">Get Free Bathroom Estimate</button>
    <button class="tertiary-cta">Call (XXX) XXX-XXXX</button>
  </div>
  
  <div class="trust-indicators">
    <span>→ Kitchen & Bathroom Specialists</span>
    <span>→ Master Electrician Licensed</span>
    <span>→ No Electrical Subcontractor Markups</span>
    <span>→ 15+ Years Experience</span>
  </div>
</div>
```

## SERVICE-SPECIFIC LEAD CAPTURE FORMS

### Kitchen Remodeling Lead System

#### Kitchen Transformation Calculator

```html
<div class="kitchen-estimator-widget">
  <h3>Get Your Kitchen Remodeling Estimate</h3>
  <p><strong>Master Electrician Advantage:</strong> No electrical subcontractor fees - Pedro handles it all!</p>
  
  <form class="kitchen-capture-form">
    <div class="form-section">
      <label>Kitchen Size:</label>
      <select name="kitchen_size" required>
        <option value="">Select kitchen size...</option>
        <option value="small">Small (Under 100 sq ft)</option>
        <option value="medium">Medium (100-200 sq ft)</option>
        <option value="large">Large (200+ sq ft)</option>
        <option value="galley">Galley Kitchen</option>
        <option value="open_concept">Open Concept</option>
      </select>
    </div>
    
    <div class="form-section">
      <label>Renovation Level:</label>
      <select name="renovation_level" required>
        <option value="">Select renovation level...</option>
        <option value="refresh">Kitchen Refresh ($10K-25K)</option>
        <option value="standard">Standard Remodel ($30K-55K)</option>
        <option value="luxury">Luxury Transformation ($60K+)</option>
        <option value="not_sure">Not sure yet</option>
      </select>
    </div>
    
    <div class="form-section">
      <label>Electrical Work Needed (Check all that apply):</label>
      <div class="checkbox-group">
        <input type="checkbox" id="outlets" name="electrical[]" value="outlets">
        <label for="outlets">Additional Outlets & USB Charging</label>
        
        <input type="checkbox" id="lighting" name="electrical[]" value="lighting">
        <label for="lighting">Under-Cabinet & Accent Lighting</label>
        
        <input type="checkbox" id="appliances" name="electrical[]" value="appliances">
        <label for="appliances">Appliance Circuits & Connections</label>
        
        <input type="checkbox" id="island" name="electrical[]" value="island">
        <label for="island">Kitchen Island Electrical</label>
        
        <input type="checkbox" id="panel" name="electrical[]" value="panel">
        <label for="panel">Electrical Panel Upgrade</label>
        
        <input type="checkbox" id="none" name="electrical[]" value="none">
        <label for="none">No electrical work needed</label>
      </div>
    </div>
    
    <div class="form-section">
      <label>Project Timeline:</label>
      <select name="timeline" required>
        <option value="">When do you want to start?</option>
        <option value="asap">ASAP - Ready to start</option>
        <option value="month">Within 1 month</option>
        <option value="quarter">Within 3 months</option>
        <option value="planning">Still planning (6+ months)</option>
      </select>
    </div>
    
    <div class="contact-info">
      <input type="text" name="name" placeholder="Your Name" required>
      <input type="email" name="email" placeholder="Email Address" required>
      <input type="tel" name="phone" placeholder="Phone Number" required>
      <input type="text" name="address" placeholder="Project Address (City, NJ)">
    </div>
    
    <textarea name="project_details" placeholder="Tell us about your dream kitchen..."></textarea>
    
    <button type="submit" class="estimate-cta">
      Get My No-Markup Kitchen Estimate
    </button>
    
    <p class="form-footer">
      <span>→ Master Electrician Pedro will personally review your project</span><br>
      <span>→ We respond within 2 hours during business hours</span><br>
      <span>→ Free in-home consultation included</span>
    </p>
  </form>
</div>
```

### Bathroom Renovation Lead System

#### Bathroom Transformation Form

```html
<div class="bathroom-estimator-widget">
  <h3>Get Your Bathroom Renovation Estimate</h3>
  <p><strong>Complete Renovation Expertise:</strong> From design to electrical - all handled by Pedro's team</p>
  
  <form class="bathroom-capture-form">
    <div class="form-section">
      <label>Bathroom Type:</label>
      <select name="bathroom_type" required>
        <option value="">Select bathroom type...</option>
        <option value="master">Master Bathroom</option>
        <option value="guest">Guest/Hall Bathroom</option>
        <option value="powder">Powder Room</option>
        <option value="ensuite">En-Suite Bathroom</option>
        <option value="basement">Basement Bathroom</option>
      </select>
    </div>
    
    <div class="form-section">
      <label>Renovation Level:</label>
      <select name="renovation_level" required>
        <option value="">Select renovation level...</option>
        <option value="essential">Essential Updates ($8K-20K)</option>
        <option value="full">Full Renovation ($25K-45K)</option>
        <option value="luxury">Luxury Spa Bathroom ($50K+)</option>
        <option value="not_sure">Not sure yet</option>
      </select>
    </div>
    
    <div class="form-section">
      <label>Special Features Desired:</label>
      <div class="checkbox-group">
        <input type="checkbox" id="heated_floors" name="features[]" value="heated_floors">
        <label for="heated_floors">Heated Floors</label>
        
        <input type="checkbox" id="smart_lighting" name="features[]" value="smart_lighting">
        <label for="smart_lighting">Smart Lighting & Controls</label>
        
        <input type="checkbox" id="accessibility" name="features[]" value="accessibility">
        <label for="accessibility">Accessibility Features</label>
        
        <input type="checkbox" id="steam_shower" name="features[]" value="steam_shower">
        <label for="steam_shower">Steam Shower</label>
        
        <input type="checkbox" id="double_vanity" name="features[]" value="double_vanity">
        <label for="double_vanity">Double Vanity</label>
      </div>
    </div>
    
    <div class="contact-info">
      <input type="text" name="name" placeholder="Your Name" required>
      <input type="email" name="email" placeholder="Email Address" required>
      <input type="tel" name="phone" placeholder="Phone Number" required>
      <input type="text" name="address" placeholder="Project Address (City, NJ)">
    </div>
    
    <div class="form-section">
      <label>Project Timeline:</label>
      <select name="timeline" required>
        <option value="">When do you want to start?</option>
        <option value="asap">ASAP - Ready to start</option>
        <option value="month">Within 1 month</option>
        <option value="quarter">Within 3 months</option>
        <option value="planning">Still planning</option>
      </select>
    </div>
    
    <textarea name="project_details" placeholder="Describe your ideal bathroom renovation..."></textarea>
    
    <button type="submit" class="estimate-cta">
      Get My Expert Bathroom Estimate
    </button>
    
    <p class="form-footer">
      <span>→ Complete renovation expertise from design to finish</span><br>
      <span>→ Master Electrician handles all electrical work</span><br>
      <span>→ Free consultation and detailed estimate</span>
    </p>
  </form>
</div>
```

## WHOLE HOME RENOVATION LEAD CAPTURE

### Comprehensive Home Transformation Form

```html
<div class="whole-home-estimator-widget">
  <h3>Whole Home Renovation Consultation</h3>
  <p><strong>Complete Home Transformation:</strong> Kitchen, bathrooms, electrical, and more - all coordinated by Pedro</p>
  
  <form class="whole-home-capture-form">
    <div class="form-section">
      <label>Home Type:</label>
      <select name="home_type" required>
        <option value="">Select home type...</option>
        <option value="single_family">Single Family Home</option>
        <option value="townhouse">Townhouse</option>
        <option value="condo">Condo/Apartment</option>
        <option value="multi_family">Multi-Family Property</option>
      </select>
    </div>
    
    <div class="form-section">
      <label>Areas to Renovate (Check all that apply):</label>
      <div class="checkbox-group">
        <input type="checkbox" id="kitchen_reno" name="areas[]" value="kitchen">
        <label for="kitchen_reno">Kitchen</label>
        
        <input type="checkbox" id="bathrooms_reno" name="areas[]" value="bathrooms">
        <label for="bathrooms_reno">Bathrooms</label>
        
        <input type="checkbox" id="electrical_upgrade" name="areas[]" value="electrical">
        <label for="electrical_upgrade">Electrical System Upgrade</label>
        
        <input type="checkbox" id="flooring" name="areas[]" value="flooring">
        <label for="flooring">Flooring</label>
        
        <input type="checkbox" id="basement" name="areas[]" value="basement">
        <label for="basement">Basement Finishing</label>
        
        <input type="checkbox" id="additions" name="areas[]" value="additions">
        <label for="additions">Room Additions</label>
      </div>
    </div>
    
    <div class="contact-info">
      <input type="text" name="name" placeholder="Your Name" required>
      <input type="email" name="email" placeholder="Email Address" required>
      <input type="tel" name="phone" placeholder="Phone Number" required>
      <input type="text" name="address" placeholder="Property Address (City, NJ)" required>
    </div>
    
    <div class="form-section">
      <label>Project Budget Range:</label>
      <select name="budget" required>
        <option value="">Select budget range...</option>
        <option value="50k_100k">$50K - $100K</option>
        <option value="100k_200k">$100K - $200K</option>
        <option value="200k_plus">$200K+</option>
        <option value="discuss">Prefer to discuss</option>
      </select>
    </div>
    
    <textarea name="project_vision" placeholder="Tell us about your home renovation vision..." required></textarea>
    
    <button type="submit" class="estimate-cta">
      Schedule My Whole Home Consultation
    </button>
    
    <p class="form-footer">
      <span>→ Comprehensive project planning and coordination</span><br>
      <span>→ Master Electrician expertise throughout</span><br>
      <span>→ Single point of contact for entire project</span>
    </p>
  </form>
</div>
```

## ELECTRICAL SERVICES LEAD CAPTURE

### Emergency vs. Planned Electrical Services

```html
<div class="electrical-capture-system">
  <div class="service-type-tabs">
    <button class="tab-btn active" data-tab="emergency">Emergency Service</button>
    <button class="tab-btn" data-tab="planned">Planned Project</button>
    <button class="tab-btn" data-tab="renovation">Renovation Electrical</button>
  </div>

  <!-- Emergency Tab -->
  <div id="emergency" class="tab-content active">
    <h3>Electrical Emergency - Master Electrician Response</h3>
    <div class="emergency-contact">
      <a href="tel:XXXXXXXXXX" class="emergency-call-btn">
        Call Pedro Now: (XXX) XXX-XXXX
      </a>
      <p>Master Electrician #13VH13 - 24/7 Emergency Response</p>
    </div>

    <form class="emergency-form">
      <div class="emergency-type">
        <label>What's the electrical emergency?</label>
        <select name="emergency_type" required>
          <option value="">Select emergency type...</option>
          <option value="no_power">Complete power outage</option>
          <option value="partial_power">Partial power loss</option>
          <option value="sparking">Sparking/burning smell</option>
          <option value="tripping">Circuit breaker keeps tripping</option>
          <option value="flickering">Lights flickering</option>
          <option value="shock">Electrical shock hazard</option>
          <option value="other">Other electrical emergency</option>
        </select>
      </div>

      <textarea name="description" placeholder="Describe the emergency situation..." required></textarea>

      <div class="contact-urgent">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="tel" name="phone" placeholder="Phone Number" required>
        <input type="text" name="address" placeholder="Emergency Address in NJ" required>
      </div>

      <button type="submit" class="emergency-submit">Send Emergency Request</button>

      <p class="emergency-note">
        For immediate emergencies, call directly: (XXX) XXX-XXXX
      </p>
    </form>
  </div>

  <!-- Planned Project Tab -->
  <div id="planned" class="tab-content">
    <h3>Electrical Project Planning</h3>
    <p>Master Electrician Pedro will design the perfect electrical solution</p>

    <form class="planned-electrical-form">
      <div class="project-type">
        <label>Electrical Project Type:</label>
        <div class="checkbox-group">
          <input type="checkbox" id="panel_upgrade" name="services[]" value="panel_upgrade">
          <label for="panel_upgrade">Panel Upgrade/Replacement</label>

          <input type="checkbox" id="whole_home_rewire" name="services[]" value="whole_home_rewire">
          <label for="whole_home_rewire">Whole Home Rewiring</label>

          <input type="checkbox" id="outlets_switches" name="services[]" value="outlets_switches">
          <label for="outlets_switches">Outlets & Switches</label>

          <input type="checkbox" id="lighting_design" name="services[]" value="lighting_design">
          <label for="lighting_design">Lighting Design & Installation</label>

          <input type="checkbox" id="ev_charger" name="services[]" value="ev_charger">
          <label for="ev_charger">EV Charger Installation</label>

          <input type="checkbox" id="generator" name="services[]" value="generator">
          <label for="generator">Generator Installation</label>

          <input type="checkbox" id="smart_home" name="services[]" value="smart_home">
          <label for="smart_home">Smart Home Wiring</label>
        </div>
      </div>

      <div class="property-info">
        <label>Property Type:</label>
        <select name="property_type" required>
          <option value="">Select property type...</option>
          <option value="single_family">Single Family Home</option>
          <option value="townhouse">Townhouse</option>
          <option value="condo">Condo/Apartment</option>
          <option value="commercial">Commercial Property</option>
        </select>
      </div>

      <div class="contact-planned">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Email Address" required>
        <input type="tel" name="phone" placeholder="Phone Number" required>
        <input type="text" name="address" placeholder="Project Address (City, NJ)">
      </div>

      <textarea name="project_details" placeholder="Tell us about your electrical project..."></textarea>

      <button type="submit" class="planned-submit">Get Expert Electrical Consultation</button>
    </form>
  </div>

  <!-- Renovation Electrical Tab -->
  <div id="renovation" class="tab-content">
    <h3>Electrical Work for Your Renovation</h3>
    <p>Seamless electrical integration with your kitchen or bathroom project</p>

    <form class="renovation-electrical-form">
      <div class="renovation-type">
        <label>What are you renovating?</label>
        <select name="renovation_type" required>
          <option value="">Select renovation type...</option>
          <option value="kitchen">Kitchen Remodeling</option>
          <option value="bathroom">Bathroom Renovation</option>
          <option value="whole_home">Whole Home Renovation</option>
          <option value="addition">Room Addition</option>
          <option value="basement">Basement Finishing</option>
        </select>
      </div>

      <div class="electrical-needs">
        <label>Electrical work needed:</label>
        <div class="checkbox-group">
          <input type="checkbox" id="new_circuits" name="electrical_work[]" value="new_circuits">
          <label for="new_circuits">New Electrical Circuits</label>

          <input type="checkbox" id="lighting_reno" name="electrical_work[]" value="lighting_reno">
          <label for="lighting_reno">Lighting Design & Installation</label>

          <input type="checkbox" id="outlets_reno" name="electrical_work[]" value="outlets_reno">
          <label for="outlets_reno">Additional Outlets & USB</label>

          <input type="checkbox" id="appliance_circuits" name="electrical_work[]" value="appliance_circuits">
          <label for="appliance_circuits">Appliance Electrical Connections</label>
        </div>
      </div>

      <div class="contact-renovation">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Email Address" required>
        <input type="tel" name="phone" placeholder="Phone Number" required>
        <input type="text" name="address" placeholder="Project Address (City, NJ)">
      </div>

      <textarea name="project_details" placeholder="Tell us about your renovation and electrical needs..."></textarea>

      <button type="submit" class="renovation-submit">Get Integrated Renovation Estimate</button>

      <p class="renovation-advantage">
        <strong>Advantage:</strong> No electrical subcontractor markups when you choose Top Notch for your complete renovation!
      </p>
    </form>
  </div>
</div>
```
