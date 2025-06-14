"""
Contact Form Webhook Handler with Lead Enrichment
================================================

Advanced contact form processing system designed specifically for 
kitchen and bathroom renovation lead capture and qualification.

Features:
- Form submission processing and validation
- Lead scoring based on renovation keywords
- Contact information enrichment
- Property value estimation
- Automated lead routing
- CRM integration
- Follow-up automation

Author: Top Notch New Jersey Development Team
"""

import requests
import json
import hashlib
import hmac
import re
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
import logging
from urllib.parse import urlparse

from ..utils.logger import get_logger, log_business_event
from ..utils.email_notifier import EmailNotifier

class ContactFormHandler:
    """Handle contact form submissions with advanced lead processing"""
    
    def __init__(self, config):
        """
        Initialize contact form handler
        
        Args:
            config: Configuration object with webhook and CRM settings
        """
        self.config = config
        self.logger = get_logger(self.__class__.__name__)
        self.notifier = EmailNotifier(config)
        
        # API configurations
        self.enrichment_api = config.get('webhooks.contact_forms.enrichment_api_key')
        self.crm_webhook = config.get('webhooks.contact_forms.crm_webhook_url')
        self.email_service_key = config.get('webhooks.contact_forms.email_service_key')
        
        # Business-specific lead scoring for home improvement
        self.lead_scoring_keywords = config.get('business.lead_scoring_keywords', {
            'kitchen': 10,
            'bathroom': 10,
            'renovation': 8,
            'remodel': 8,
            'quote': 15,
            'estimate': 15,
            'budget': 12,
            'urgent': 20,
            'timeline': 5,
            'electrical': 7,
            'licensed': 3,
            'bonded': 3,
            'insured': 3,
            'pedro': 5,  # Brand recognition
            'top notch': 5
        })
        
        # Service area scoring
        self.service_areas = {
            'linden': 10,
            'union county': 8,
            'essex county': 8,
            'middlesex county': 8,
            'bergen county': 8,
            'new jersey': 5,
            'nj': 5
        }
        
        # Urgency indicators
        self.urgency_keywords = [
            'urgent', 'asap', 'immediately', 'emergency', 'quickly',
            'soon', 'this week', 'this month', 'deadline'
        ]
    
    def process_form_submission(self, form_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process contact form submission with comprehensive lead analysis
        
        Args:
            form_data: Raw form submission data
            
        Returns:
            Dictionary containing processing results and lead information
        """
        self.logger.info("📝 Processing contact form submission...")
        
        try:
            # Validate and sanitize input
            cleaned_data = self._sanitize_form_data(form_data)
            
            # Generate unique lead ID
            lead_id = self._generate_lead_id(cleaned_data)
            cleaned_data['lead_id'] = lead_id
            
            # Enrich contact information
            enriched_data = self._enrich_contact_data(cleaned_data)
            
            # Calculate comprehensive lead score
            lead_score = self._calculate_lead_score(enriched_data)
            enriched_data['lead_score'] = lead_score
            
            # Categorize renovation type and urgency
            renovation_analysis = self._analyze_renovation_request(enriched_data)
            enriched_data.update(renovation_analysis)
            
            # Estimate project value
            project_estimate = self._estimate_project_value(enriched_data)
            enriched_data['estimated_project_value'] = project_estimate
            
            # Determine lead priority and routing
            lead_priority = self._determine_lead_priority(enriched_data)
            enriched_data['priority'] = lead_priority
            
            # Send to CRM
            crm_result = self._send_to_crm(enriched_data)
            
            # Setup automated follow-up
            followup_result = self._setup_followup_automation(enriched_data)
            
            # Log business event
            log_business_event('lead_captured', {
                'lead_id': lead_id,
                'lead_score': lead_score,
                'renovation_type': renovation_analysis.get('renovation_type'),
                'priority': lead_priority,
                'estimated_value': project_estimate
            })
            
            # Send immediate notifications for high-priority leads
            if lead_priority in ['high', 'urgent']:
                self.notifier.send_lead_notification(enriched_data)
            
            result = {
                'success': True,
                'lead_id': lead_id,
                'lead_score': lead_score,
                'renovation_type': renovation_analysis.get('renovation_type'),
                'priority': lead_priority,
                'estimated_project_value': project_estimate,
                'crm_status': crm_result.get('status', 'unknown'),
                'followup_scheduled': followup_result.get('success', False),
                'timestamp': datetime.now().isoformat(),
                'processing_time': self._get_processing_time()
            }
            
            self.logger.info(f"✅ Form processed successfully: {lead_id} (Score: {lead_score})")
            return result
            
        except Exception as e:
            self.logger.error(f"❌ Form processing failed: {e}")
            return {
                'success': False,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def _sanitize_form_data(self, form_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Sanitize and validate form input data
        
        Args:
            form_data: Raw form data
            
        Returns:
            Cleaned and validated form data
        """
        cleaned_data = {}
        
        # Standard form fields with validation
        field_mappings = {
            'name': ['name', 'full_name', 'customer_name', 'your_name'],
            'email': ['email', 'email_address', 'your_email'],
            'phone': ['phone', 'phone_number', 'telephone', 'your_phone'],
            'address': ['address', 'property_address', 'location'],
            'message': ['message', 'description', 'details', 'comments'],
            'subject': ['subject', 'service_type', 'project_type']
        }
        
        # Extract and clean fields
        for standard_field, possible_names in field_mappings.items():
            for field_name in possible_names:
                if field_name in form_data and form_data[field_name]:
                    value = str(form_data[field_name]).strip()
                    if value:
                        cleaned_data[standard_field] = self._clean_text(value)
                        break
        
        # Validate email format
        if 'email' in cleaned_data:
            if not self._is_valid_email(cleaned_data['email']):
                self.logger.warning(f"Invalid email format: {cleaned_data['email']}")
                cleaned_data['email_valid'] = False
            else:
                cleaned_data['email_valid'] = True
        
        # Validate phone format
        if 'phone' in cleaned_data:
            cleaned_phone = self._clean_phone_number(cleaned_data['phone'])
            cleaned_data['phone'] = cleaned_phone
            cleaned_data['phone_valid'] = bool(cleaned_phone)
        
        # Add metadata
        cleaned_data.update({
            'source': 'website_form',
            'submission_time': datetime.now().isoformat(),
            'user_agent': form_data.get('user_agent', ''),
            'page_url': form_data.get('page_url', ''),
            'referrer': form_data.get('referrer', ''),
            'ip_address': form_data.get('ip_address', '')
        })
        
        return cleaned_data
    
    def _clean_text(self, text: str) -> str:
        """Clean and normalize text input"""
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text.strip())
        
        # Remove potentially harmful characters
        text = re.sub(r'[<>"\']', '', text)
        
        return text
    
    def _is_valid_email(self, email: str) -> bool:
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def _clean_phone_number(self, phone: str) -> str:
        """Clean and format phone number"""
        # Remove all non-digit characters
        digits = re.sub(r'\D', '', phone)
        
        # Handle US phone numbers
        if len(digits) == 10:
            return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        elif len(digits) == 11 and digits[0] == '1':
            return f"({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
        
        return digits if len(digits) >= 10 else ''
    
    def _generate_lead_id(self, form_data: Dict[str, Any]) -> str:
        """Generate unique lead identifier"""
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        email = form_data.get('email', 'unknown')
        hash_input = f"{timestamp}_{email}_{form_data.get('phone', '')}"
        hash_suffix = hashlib.md5(hash_input.encode()).hexdigest()[:8]
        return f"TNJ_{timestamp}_{hash_suffix}"

    def _enrich_contact_data(self, form_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Enrich contact data using external APIs and business intelligence

        Args:
            form_data: Cleaned form data

        Returns:
            Enriched contact data with additional information
        """
        enriched_data = form_data.copy()

        try:
            email = form_data.get('email')
            phone = form_data.get('phone')
            address = form_data.get('address')

            # Email-based enrichment
            if email and self.enrichment_api:
                email_enrichment = self._enrich_by_email(email)
                enriched_data.update(email_enrichment)

            # Phone-based enrichment
            if phone:
                phone_enrichment = self._enrich_by_phone(phone)
                enriched_data.update(phone_enrichment)

            # Address-based enrichment
            if address:
                property_info = self._get_property_information(address)
                enriched_data['property_info'] = property_info

            # Social media presence check
            if email:
                social_presence = self._check_social_presence(email)
                enriched_data['social_presence'] = social_presence

        except Exception as e:
            self.logger.warning(f"Enrichment failed: {e}")
            enriched_data['enrichment_error'] = str(e)

        return enriched_data

    def _enrich_by_email(self, email: str) -> Dict[str, Any]:
        """Enrich contact information using email address"""
        enrichment_data = {}

        try:
            # Extract domain information
            domain = email.split('@')[1].lower()
            enrichment_data['email_domain'] = domain

            # Check if it's a business email
            business_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
            enrichment_data['is_business_email'] = domain not in business_domains

            # If we have an enrichment API, use it
            if self.enrichment_api:
                # Placeholder for actual API integration
                # In production, this would call services like Clearbit, FullContact, etc.
                self.logger.debug(f"Would enrich email: {email}")

        except Exception as e:
            self.logger.error(f"Email enrichment failed: {e}")

        return enrichment_data

    def _enrich_by_phone(self, phone: str) -> Dict[str, Any]:
        """Enrich contact information using phone number"""
        enrichment_data = {}

        try:
            # Extract area code for location inference
            digits = re.sub(r'\D', '', phone)
            if len(digits) >= 10:
                area_code = digits[-10:-7]  # Get area code
                enrichment_data['area_code'] = area_code

                # New Jersey area codes
                nj_area_codes = {
                    '201': 'Bergen County',
                    '551': 'Bergen County',
                    '732': 'Middlesex County',
                    '848': 'Middlesex County',
                    '908': 'Union County',
                    '973': 'Essex County',
                    '862': 'Essex County'
                }

                if area_code in nj_area_codes:
                    enrichment_data['inferred_location'] = nj_area_codes[area_code]
                    enrichment_data['in_service_area'] = True
                else:
                    enrichment_data['in_service_area'] = False

        except Exception as e:
            self.logger.error(f"Phone enrichment failed: {e}")

        return enrichment_data

    def _get_property_information(self, address: str) -> Dict[str, Any]:
        """Get property information from address"""
        property_info = {}

        try:
            # Basic address parsing
            address_lower = address.lower()

            # Check if address is in New Jersey
            nj_indicators = ['nj', 'new jersey', 'n.j.']
            property_info['in_new_jersey'] = any(indicator in address_lower for indicator in nj_indicators)

            # Extract ZIP code
            zip_match = re.search(r'\b\d{5}(-\d{4})?\b', address)
            if zip_match:
                zip_code = zip_match.group()
                property_info['zip_code'] = zip_code

                # New Jersey ZIP code ranges (simplified)
                nj_zip_ranges = [
                    (7000, 8999),  # New Jersey ZIP codes
                ]

                zip_num = int(zip_code[:5])
                property_info['confirmed_nj'] = any(start <= zip_num <= end for start, end in nj_zip_ranges)

            # Estimate property type based on address format
            if any(word in address_lower for word in ['apt', 'unit', '#']):
                property_info['property_type'] = 'apartment'
            elif any(word in address_lower for word in ['st', 'ave', 'rd', 'dr', 'ln']):
                property_info['property_type'] = 'house'
            else:
                property_info['property_type'] = 'unknown'

            # In production, this would integrate with property databases
            # like Zillow API, county records, etc.

        except Exception as e:
            self.logger.error(f"Property information lookup failed: {e}")

        return property_info

    def _check_social_presence(self, email: str) -> Dict[str, Any]:
        """Check social media presence (simplified implementation)"""
        social_data = {
            'has_social_presence': False,
            'platforms': []
        }

        try:
            # In production, this would check various social platforms
            # For now, just check if email domain suggests social presence
            domain = email.split('@')[1].lower()

            if domain not in ['gmail.com', 'yahoo.com', 'hotmail.com']:
                social_data['has_social_presence'] = True
                social_data['platforms'].append('business_website')

        except Exception as e:
            self.logger.error(f"Social presence check failed: {e}")

        return social_data

    def _calculate_lead_score(self, data: Dict[str, Any]) -> int:
        """
        Calculate comprehensive lead score for home improvement business

        Args:
            data: Enriched contact data

        Returns:
            Lead score (0-100)
        """
        score = 0

        # Base score for complete contact information
        if data.get('email_valid'):
            score += 10
        if data.get('phone_valid'):
            score += 10
        if data.get('address'):
            score += 5

        # Score based on message content
        message = data.get('message', '').lower()
        subject = data.get('subject', '').lower()
        combined_text = f"{message} {subject}"

        # Keyword scoring
        for keyword, points in self.lead_scoring_keywords.items():
            if keyword in combined_text:
                score += points
                self.logger.debug(f"Keyword '{keyword}' found, adding {points} points")

        # Service area scoring
        for area, points in self.service_areas.items():
            if area in combined_text or area in data.get('address', '').lower():
                score += points
                self.logger.debug(f"Service area '{area}' detected, adding {points} points")

        # Urgency scoring
        urgency_score = sum(5 for keyword in self.urgency_keywords if keyword in combined_text)
        score += min(urgency_score, 20)  # Cap urgency bonus at 20 points

        # Property information bonus
        property_info = data.get('property_info', {})
        if property_info.get('confirmed_nj'):
            score += 15
        elif property_info.get('in_new_jersey'):
            score += 10

        if property_info.get('property_type') == 'house':
            score += 5  # Houses typically have larger renovation projects

        # Business email bonus
        if data.get('is_business_email'):
            score += 5

        # Social presence bonus
        if data.get('social_presence', {}).get('has_social_presence'):
            score += 3

        # Time-based scoring (business hours submission gets bonus)
        submission_time = datetime.fromisoformat(data.get('submission_time', datetime.now().isoformat()))
        if 8 <= submission_time.hour <= 17:  # Business hours
            score += 5

        # Cap score at 100
        final_score = min(score, 100)

        self.logger.info(f"📊 Lead score calculated: {final_score}/100")
        return final_score

    def _analyze_renovation_request(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze renovation request to categorize type and urgency

        Args:
            data: Contact data with message content

        Returns:
            Dictionary with renovation analysis results
        """
        message = data.get('message', '').lower()
        subject = data.get('subject', '').lower()
        combined_text = f"{message} {subject}"

        analysis = {
            'renovation_type': 'general_inquiry',
            'urgency_level': 'normal',
            'project_scope': 'unknown',
            'timeline_mentioned': False,
            'budget_mentioned': False
        }

        # Categorize renovation type
        if any(word in combined_text for word in ['kitchen', 'cook', 'cabinet', 'countertop']):
            analysis['renovation_type'] = 'kitchen_renovation'
        elif any(word in combined_text for word in ['bathroom', 'bath', 'shower', 'toilet', 'vanity']):
            analysis['renovation_type'] = 'bathroom_renovation'
        elif any(word in combined_text for word in ['whole house', 'entire home', 'full renovation']):
            analysis['renovation_type'] = 'full_home_renovation'
        elif any(word in combined_text for word in ['electrical', 'wiring', 'outlet', 'circuit']):
            analysis['renovation_type'] = 'electrical_work'

        # Determine urgency level
        if any(word in combined_text for word in self.urgency_keywords):
            analysis['urgency_level'] = 'high'
            if any(word in combined_text for word in ['emergency', 'urgent', 'asap']):
                analysis['urgency_level'] = 'urgent'

        # Detect project scope indicators
        scope_indicators = {
            'small': ['small', 'minor', 'simple', 'basic', 'quick'],
            'medium': ['medium', 'moderate', 'standard', 'typical'],
            'large': ['large', 'major', 'complete', 'full', 'extensive', 'luxury']
        }

        for scope, keywords in scope_indicators.items():
            if any(keyword in combined_text for keyword in keywords):
                analysis['project_scope'] = scope
                break

        # Check for timeline mentions
        timeline_patterns = [
            r'\b\d+\s*(week|month|day)s?\b',
            r'\bby\s+\w+\b',
            r'\bwithin\s+\d+\b'
        ]

        for pattern in timeline_patterns:
            if re.search(pattern, combined_text):
                analysis['timeline_mentioned'] = True
                break

        # Check for budget mentions
        budget_patterns = [
            r'\$[\d,]+',
            r'\b\d+k\b',
            r'\bbudget\b',
            r'\bcost\b',
            r'\bprice\b'
        ]

        for pattern in budget_patterns:
            if re.search(pattern, combined_text):
                analysis['budget_mentioned'] = True
                break

        return analysis

    def _estimate_project_value(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Estimate potential project value based on renovation type and details

        Args:
            data: Enriched contact data

        Returns:
            Dictionary with project value estimation
        """
        renovation_type = data.get('renovation_type', 'general_inquiry')
        project_scope = data.get('project_scope', 'unknown')

        # Base estimates for Top Notch New Jersey services
        base_estimates = {
            'kitchen_renovation': {'small': 15000, 'medium': 35000, 'large': 75000},
            'bathroom_renovation': {'small': 8000, 'medium': 20000, 'large': 45000},
            'full_home_renovation': {'small': 50000, 'medium': 100000, 'large': 200000},
            'electrical_work': {'small': 2000, 'medium': 5000, 'large': 15000},
            'general_inquiry': {'small': 5000, 'medium': 15000, 'large': 50000}
        }

        # Get base estimate
        if renovation_type in base_estimates and project_scope in base_estimates[renovation_type]:
            base_value = base_estimates[renovation_type][project_scope]
        else:
            base_value = base_estimates['general_inquiry']['medium']

        # Adjust based on property information
        property_info = data.get('property_info', {})
        if property_info.get('property_type') == 'house':
            base_value *= 1.2  # Houses typically have larger projects

        # Adjust based on urgency (urgent projects often have higher budgets)
        urgency_level = data.get('urgency_level', 'normal')
        if urgency_level == 'urgent':
            base_value *= 1.3
        elif urgency_level == 'high':
            base_value *= 1.1

        return {
            'estimated_min': int(base_value * 0.7),
            'estimated_max': int(base_value * 1.5),
            'estimated_average': int(base_value),
            'confidence_level': 'medium' if project_scope != 'unknown' else 'low'
        }

    def _determine_lead_priority(self, data: Dict[str, Any]) -> str:
        """
        Determine lead priority based on score and business factors

        Args:
            data: Enriched contact data with scores

        Returns:
            Priority level string
        """
        lead_score = data.get('lead_score', 0)
        urgency_level = data.get('urgency_level', 'normal')
        estimated_value = data.get('estimated_project_value', {}).get('estimated_average', 0)

        # Priority determination logic
        if urgency_level == 'urgent' or lead_score >= 80:
            return 'urgent'
        elif urgency_level == 'high' or lead_score >= 60 or estimated_value >= 30000:
            return 'high'
        elif lead_score >= 40 or estimated_value >= 15000:
            return 'medium'
        else:
            return 'low'

    def _send_to_crm(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send lead data to CRM system

        Args:
            lead_data: Complete lead information

        Returns:
            CRM integration result
        """
        if not self.crm_webhook:
            self.logger.warning("No CRM webhook configured")
            return {'status': 'no_crm_configured'}

        try:
            # Prepare CRM payload
            crm_payload = {
                'lead_id': lead_data.get('lead_id'),
                'contact_info': {
                    'name': lead_data.get('name'),
                    'email': lead_data.get('email'),
                    'phone': lead_data.get('phone'),
                    'address': lead_data.get('address')
                },
                'lead_details': {
                    'score': lead_data.get('lead_score'),
                    'priority': lead_data.get('priority'),
                    'renovation_type': lead_data.get('renovation_type'),
                    'estimated_value': lead_data.get('estimated_project_value'),
                    'urgency': lead_data.get('urgency_level')
                },
                'source': 'website_form',
                'timestamp': lead_data.get('submission_time'),
                'company': 'Top Notch New Jersey'
            }

            # Send to CRM
            response = requests.post(
                self.crm_webhook,
                json=crm_payload,
                timeout=30,
                headers={'Content-Type': 'application/json'}
            )

            if response.status_code == 200:
                self.logger.info(f"✅ Lead sent to CRM: {lead_data.get('lead_id')}")
                return {'status': 'success', 'crm_response': response.json()}
            else:
                self.logger.error(f"CRM integration failed: {response.status_code}")
                return {'status': 'failed', 'error': f"HTTP {response.status_code}"}

        except Exception as e:
            self.logger.error(f"CRM integration error: {e}")
            return {'status': 'error', 'error': str(e)}

    def _setup_followup_automation(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Setup automated follow-up sequence based on lead priority

        Args:
            lead_data: Complete lead information

        Returns:
            Follow-up setup result
        """
        try:
            priority = lead_data.get('priority', 'low')
            renovation_type = lead_data.get('renovation_type', 'general_inquiry')

            # Define follow-up sequences based on priority
            followup_sequences = {
                'urgent': {
                    'immediate': True,
                    'phone_call_delay': 0,  # Call immediately
                    'email_sequence': ['immediate_response', 'follow_up_1h', 'follow_up_24h']
                },
                'high': {
                    'immediate': True,
                    'phone_call_delay': 30,  # Call within 30 minutes
                    'email_sequence': ['immediate_response', 'follow_up_2h', 'follow_up_48h']
                },
                'medium': {
                    'immediate': False,
                    'phone_call_delay': 120,  # Call within 2 hours
                    'email_sequence': ['immediate_response', 'follow_up_24h', 'follow_up_week']
                },
                'low': {
                    'immediate': False,
                    'phone_call_delay': 480,  # Call within 8 hours
                    'email_sequence': ['immediate_response', 'follow_up_48h', 'follow_up_week']
                }
            }

            sequence = followup_sequences.get(priority, followup_sequences['medium'])

            # Schedule follow-up actions (in production, this would integrate with scheduling system)
            self.logger.info(f"📅 Scheduling follow-up for {priority} priority lead")

            return {
                'success': True,
                'sequence_type': priority,
                'immediate_action': sequence['immediate'],
                'phone_call_scheduled': sequence['phone_call_delay'],
                'email_sequence': sequence['email_sequence']
            }

        except Exception as e:
            self.logger.error(f"Follow-up automation setup failed: {e}")
            return {'success': False, 'error': str(e)}

    def _get_processing_time(self) -> float:
        """Get processing time (placeholder for actual timing)"""
        return 0.5  # Placeholder processing time
