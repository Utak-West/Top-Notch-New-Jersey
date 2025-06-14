"""
Unit Tests for Webhook Integration System
========================================

Comprehensive test suite for webhook integration and lead processing,
specifically testing home improvement lead generation functionality.

Test Coverage:
- Contact form processing
- Lead scoring algorithms
- Data enrichment
- CRM integration
- Follow-up automation
- Business logic validation

Author: Top Notch New Jersey Development Team
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import json
from datetime import datetime

# Import the modules to test
from webhooks.contact_form_handler import ContactFormHandler
from config.settings import Config

class TestContactFormHandler(unittest.TestCase):
    """Test cases for ContactFormHandler class"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Mock configuration
        self.mock_config = Mock(spec=Config)
        self.mock_config.get.side_effect = self._mock_config_get
        
        # Initialize handler with mock config
        self.handler = ContactFormHandler(self.mock_config)
        
        # Sample form data for testing
        self.sample_form_data = {
            'name': 'John Smith',
            'email': 'john.smith@email.com',
            'phone': '(908) 555-1234',
            'address': '123 Main St, Linden, NJ 07036',
            'message': 'I need a kitchen renovation estimate. Looking for a complete remodel with new cabinets and countertops. Budget around $30k. Timeline is flexible.',
            'subject': 'Kitchen Renovation Quote',
            'user_agent': 'Mozilla/5.0...',
            'page_url': 'https://topnotchnj.com/contact',
            'referrer': 'https://google.com'
        }
    
    def _mock_config_get(self, key, default=None):
        """Mock configuration getter"""
        config_values = {
            'webhooks.contact_forms.enrichment_api_key': 'test_api_key',
            'webhooks.contact_forms.crm_webhook_url': 'https://test-crm.com/webhook',
            'webhooks.contact_forms.email_service_key': 'test_email_key',
            'business.lead_scoring_keywords': {
                'kitchen': 10, 'bathroom': 10, 'renovation': 8, 'quote': 15,
                'estimate': 15, 'budget': 12, 'urgent': 20
            },
            'business.contact_info.email': 'info@topnotchnewjersey.com'
        }
        return config_values.get(key, default)
    
    def test_initialization(self):
        """Test handler initialization"""
        self.assertIsNotNone(self.handler)
        self.assertIsInstance(self.handler.lead_scoring_keywords, dict)
        self.assertIn('kitchen', self.handler.lead_scoring_keywords)
        self.assertIn('bathroom', self.handler.lead_scoring_keywords)
    
    def test_form_data_sanitization(self):
        """Test form data cleaning and validation"""
        # Test with messy input data
        messy_data = {
            'name': '  John <script>alert("test")</script> Smith  ',
            'email': 'JOHN.SMITH@EMAIL.COM',
            'phone': '908-555-1234',
            'message': 'Need   kitchen   renovation\n\nASAP!'
        }
        
        cleaned = self.handler._sanitize_form_data(messy_data)
        
        # Verify cleaning
        self.assertEqual(cleaned['name'], 'John alert("test") Smith')  # Script tags removed
        self.assertEqual(cleaned['email'], 'JOHN.SMITH@EMAIL.COM')
        self.assertEqual(cleaned['phone'], '(908) 555-1234')  # Formatted
        self.assertIn('Need kitchen renovation', cleaned['message'])  # Whitespace normalized
        
        # Verify metadata addition
        self.assertIn('source', cleaned)
        self.assertIn('submission_time', cleaned)
        self.assertEqual(cleaned['source'], 'website_form')
    
    def test_email_validation(self):
        """Test email format validation"""
        # Valid emails
        valid_emails = [
            'test@example.com',
            'user.name@domain.co.uk',
            'user+tag@example.org'
        ]
        
        for email in valid_emails:
            self.assertTrue(self.handler._is_valid_email(email))
        
        # Invalid emails
        invalid_emails = [
            'invalid-email',
            '@domain.com',
            'user@',
            'user space@domain.com'
        ]
        
        for email in invalid_emails:
            self.assertFalse(self.handler._is_valid_email(email))
    
    def test_phone_number_cleaning(self):
        """Test phone number formatting"""
        test_cases = [
            ('9085551234', '(908) 555-1234'),
            ('(908) 555-1234', '(908) 555-1234'),
            ('908-555-1234', '(908) 555-1234'),
            ('1-908-555-1234', '(908) 555-1234'),
            ('908.555.1234', '(908) 555-1234'),
            ('invalid', ''),  # Invalid phone
            ('123', '')  # Too short
        ]
        
        for input_phone, expected in test_cases:
            result = self.handler._clean_phone_number(input_phone)
            self.assertEqual(result, expected)
    
    def test_lead_id_generation(self):
        """Test unique lead ID generation"""
        lead_id1 = self.handler._generate_lead_id(self.sample_form_data)
        lead_id2 = self.handler._generate_lead_id(self.sample_form_data)
        
        # IDs should be unique (different timestamps)
        self.assertNotEqual(lead_id1, lead_id2)
        self.assertTrue(lead_id1.startswith('TNJ_'))
        self.assertTrue(lead_id2.startswith('TNJ_'))
    
    def test_lead_scoring_kitchen_renovation(self):
        """Test lead scoring for kitchen renovation inquiry"""
        # Kitchen renovation with high-value keywords
        kitchen_data = {
            'message': 'I need a complete kitchen renovation with new cabinets, countertops, and electrical work. Looking for a quote ASAP.',
            'email_valid': True,
            'phone_valid': True,
            'address': '123 Main St, Linden, NJ',
            'property_info': {'confirmed_nj': True, 'property_type': 'house'},
            'submission_time': datetime.now().replace(hour=10).isoformat()  # Business hours
        }
        
        score = self.handler._calculate_lead_score(kitchen_data)
        
        # Should be high score due to:
        # - Kitchen (10) + renovation (8) + quote (15) + urgent keywords
        # - Complete contact info (25)
        # - NJ location (15)
        # - House property type (5)
        # - Business hours (5)
        self.assertGreater(score, 60)
    
    def test_lead_scoring_low_priority(self):
        """Test lead scoring for low priority inquiry"""
        low_priority_data = {
            'message': 'Just looking for some general information about your services.',
            'email_valid': False,
            'phone_valid': False,
            'submission_time': datetime.now().replace(hour=2).isoformat()  # Off hours
        }
        
        score = self.handler._calculate_lead_score(low_priority_data)
        
        # Should be low score due to:
        # - No specific keywords
        # - Incomplete contact info
        # - Off-hours submission
        self.assertLess(score, 30)
    
    def test_renovation_type_categorization(self):
        """Test renovation type analysis"""
        test_cases = [
            ('I need a kitchen remodel with new cabinets', 'kitchen_renovation'),
            ('Bathroom renovation needed - shower and vanity', 'bathroom_renovation'),
            ('Complete home renovation project', 'full_home_renovation'),
            ('Need electrical work - new outlets and wiring', 'electrical_work'),
            ('General inquiry about your services', 'general_inquiry')
        ]
        
        for message, expected_type in test_cases:
            data = {'message': message, 'subject': ''}
            result = self.handler._analyze_renovation_request(data)
            self.assertEqual(result['renovation_type'], expected_type)
    
    def test_urgency_level_detection(self):
        """Test urgency level classification"""
        test_cases = [
            ('Need this done ASAP - emergency situation', 'urgent'),
            ('Looking for urgent renovation help', 'high'),
            ('Would like to start this project soon', 'normal'),
            ('Just exploring options for future project', 'normal')
        ]
        
        for message, expected_urgency in test_cases:
            data = {'message': message, 'subject': ''}
            result = self.handler._analyze_renovation_request(data)
            self.assertEqual(result['urgency_level'], expected_urgency)
    
    def test_project_value_estimation(self):
        """Test project value estimation"""
        # Kitchen renovation - large scope
        kitchen_data = {
            'renovation_type': 'kitchen_renovation',
            'project_scope': 'large',
            'urgency_level': 'high',
            'property_info': {'property_type': 'house'}
        }
        
        estimate = self.handler._estimate_project_value(kitchen_data)
        
        self.assertIn('estimated_min', estimate)
        self.assertIn('estimated_max', estimate)
        self.assertIn('estimated_average', estimate)
        
        # Large kitchen should be high value
        self.assertGreater(estimate['estimated_average'], 50000)
        
        # Bathroom renovation - small scope
        bathroom_data = {
            'renovation_type': 'bathroom_renovation',
            'project_scope': 'small',
            'urgency_level': 'normal',
            'property_info': {'property_type': 'apartment'}
        }
        
        estimate = self.handler._estimate_project_value(bathroom_data)
        self.assertLess(estimate['estimated_average'], 15000)
    
    def test_lead_priority_determination(self):
        """Test lead priority classification"""
        # Urgent priority
        urgent_data = {
            'lead_score': 85,
            'urgency_level': 'urgent',
            'estimated_project_value': {'estimated_average': 50000}
        }
        priority = self.handler._determine_lead_priority(urgent_data)
        self.assertEqual(priority, 'urgent')
        
        # High priority
        high_data = {
            'lead_score': 65,
            'urgency_level': 'normal',
            'estimated_project_value': {'estimated_average': 35000}
        }
        priority = self.handler._determine_lead_priority(high_data)
        self.assertEqual(priority, 'high')
        
        # Low priority
        low_data = {
            'lead_score': 25,
            'urgency_level': 'normal',
            'estimated_project_value': {'estimated_average': 5000}
        }
        priority = self.handler._determine_lead_priority(low_data)
        self.assertEqual(priority, 'low')
    
    def test_nj_area_code_detection(self):
        """Test New Jersey area code recognition"""
        nj_phones = [
            '(908) 555-1234',  # Union County
            '(201) 555-1234',  # Bergen County
            '(732) 555-1234',  # Middlesex County
            '(973) 555-1234'   # Essex County
        ]
        
        for phone in nj_phones:
            enrichment = self.handler._enrich_by_phone(phone)
            self.assertTrue(enrichment.get('in_service_area', False))
            self.assertIn('inferred_location', enrichment)
    
    def test_property_information_extraction(self):
        """Test property information parsing"""
        # New Jersey address
        nj_address = "123 Main Street, Linden, NJ 07036"
        property_info = self.handler._get_property_information(nj_address)
        
        self.assertTrue(property_info['in_new_jersey'])
        self.assertEqual(property_info['zip_code'], '07036')
        self.assertTrue(property_info['confirmed_nj'])
        
        # Out of state address
        oos_address = "456 Oak Ave, New York, NY 10001"
        property_info = self.handler._get_property_information(oos_address)
        
        self.assertFalse(property_info.get('in_new_jersey', False))
    
    @patch('requests.post')
    def test_crm_integration_success(self, mock_post):
        """Test successful CRM integration"""
        # Mock successful CRM response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'status': 'success', 'id': 'crm_123'}
        mock_post.return_value = mock_response
        
        lead_data = {
            'lead_id': 'TNJ_123',
            'name': 'John Smith',
            'email': 'john@email.com',
            'lead_score': 75,
            'priority': 'high'
        }
        
        result = self.handler._send_to_crm(lead_data)
        
        self.assertEqual(result['status'], 'success')
        mock_post.assert_called_once()
        
        # Verify payload structure
        call_args = mock_post.call_args
        payload = call_args[1]['json']
        self.assertIn('lead_id', payload)
        self.assertIn('contact_info', payload)
        self.assertIn('lead_details', payload)
    
    @patch('requests.post')
    def test_crm_integration_failure(self, mock_post):
        """Test CRM integration failure handling"""
        # Mock failed CRM response
        mock_response = Mock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response
        
        lead_data = {'lead_id': 'TNJ_123'}
        result = self.handler._send_to_crm(lead_data)
        
        self.assertEqual(result['status'], 'failed')
        self.assertIn('error', result)
    
    def test_followup_automation_setup(self):
        """Test follow-up automation configuration"""
        # Urgent priority lead
        urgent_data = {'priority': 'urgent', 'renovation_type': 'kitchen_renovation'}
        result = self.handler._setup_followup_automation(urgent_data)
        
        self.assertTrue(result['success'])
        self.assertEqual(result['sequence_type'], 'urgent')
        self.assertTrue(result['immediate_action'])
        self.assertEqual(result['phone_call_scheduled'], 0)  # Immediate call
        
        # Low priority lead
        low_data = {'priority': 'low', 'renovation_type': 'general_inquiry'}
        result = self.handler._setup_followup_automation(low_data)
        
        self.assertTrue(result['success'])
        self.assertEqual(result['sequence_type'], 'low')
        self.assertFalse(result['immediate_action'])
        self.assertGreater(result['phone_call_scheduled'], 0)  # Delayed call
    
    @patch('webhooks.contact_form_handler.log_business_event')
    def test_complete_form_processing(self, mock_log_event):
        """Test complete form processing workflow"""
        # Mock external dependencies
        with patch.object(self.handler, '_send_to_crm') as mock_crm, \
             patch.object(self.handler, '_setup_followup_automation') as mock_followup:
            
            mock_crm.return_value = {'status': 'success'}
            mock_followup.return_value = {'success': True}
            
            result = self.handler.process_form_submission(self.sample_form_data)
            
            # Verify successful processing
            self.assertTrue(result['success'])
            self.assertIn('lead_id', result)
            self.assertIn('lead_score', result)
            self.assertIn('renovation_type', result)
            self.assertIn('priority', result)
            
            # Verify business event was logged
            mock_log_event.assert_called_once()
            
            # Verify CRM and follow-up were called
            mock_crm.assert_called_once()
            mock_followup.assert_called_once()

class TestLeadScoringAlgorithms(unittest.TestCase):
    """Test cases for lead scoring algorithms"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.mock_config = Mock(spec=Config)
        self.mock_config.get.side_effect = lambda key, default=None: {
            'business.lead_scoring_keywords': {
                'kitchen': 10, 'bathroom': 10, 'renovation': 8, 'quote': 15
            }
        }.get(key, default)
        
        self.handler = ContactFormHandler(self.mock_config)
    
    def test_keyword_scoring_accuracy(self):
        """Test accuracy of keyword-based scoring"""
        # High-value message
        high_value_data = {
            'message': 'kitchen renovation quote estimate budget',
            'email_valid': True,
            'phone_valid': True
        }
        
        score = self.handler._calculate_lead_score(high_value_data)
        
        # Should include: kitchen(10) + renovation(8) + quote(15) + estimate(15) + budget(12) + contact info(20)
        expected_min = 10 + 8 + 15 + 15 + 12 + 20
        self.assertGreaterEqual(score, expected_min)
    
    def test_service_area_bonus(self):
        """Test service area scoring bonus"""
        # Message mentioning service area
        area_data = {
            'message': 'Looking for contractor in Union County',
            'address': 'Linden, NJ'
        }
        
        score_with_area = self.handler._calculate_lead_score(area_data)
        
        # Same message without area mention
        no_area_data = {
            'message': 'Looking for contractor',
            'address': ''
        }
        
        score_without_area = self.handler._calculate_lead_score(no_area_data)
        
        self.assertGreater(score_with_area, score_without_area)

        self.assertGreater(score_with_area, score_without_area)

if __name__ == '__main__':
    unittest.main()
