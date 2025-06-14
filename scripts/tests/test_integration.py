"""
Integration Tests for Top Notch New Jersey Automation Suite
==========================================================

End-to-end integration tests that validate the complete automation
workflow from form submission to CRM integration and follow-up.

Test Scenarios:
- Complete lead processing workflow
- Multi-system integration (WordPress, CRM, Email)
- Error handling and recovery
- Performance under load
- Business logic validation

Author: Top Notch New Jersey Development Team
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import json
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Import modules to test
from main import main
from config.settings import load_config
from elementor.troubleshooter import ElementorTroubleshooter
from webhooks.contact_form_handler import ContactFormHandler
from webhooks.integration_manager import WebhookIntegrationManager
from wordpress.maintenance import WordPressMaintenance

class TestCompleteWorkflow(unittest.TestCase):
    """Test complete automation workflow integration"""
    
    def setUp(self):
        """Set up integration test environment"""
        # Create mock configuration
        self.mock_config = Mock()
        self.mock_config.get.side_effect = self._mock_config_get
        
        # Initialize all components
        self.elementor = ElementorTroubleshooter(self.mock_config)
        self.contact_handler = ContactFormHandler(self.mock_config)
        self.webhook_manager = WebhookIntegrationManager(self.mock_config)
        self.maintenance = WordPressMaintenance(self.mock_config)
        
        # Sample business data
        self.sample_leads = [
            {
                'name': 'Maria Garcia',
                'email': 'maria.garcia@email.com',
                'phone': '(908) 555-2468',
                'address': '789 Pine Street, Linden, NJ 07036',
                'message': 'Emergency kitchen renovation needed - water damage from pipe burst. Need licensed contractor ASAP!',
                'subject': 'Emergency Kitchen Renovation',
                'expected_score': 90,
                'expected_priority': 'urgent'
            },
            {
                'name': 'David Kim',
                'email': 'david.kim@email.com', 
                'phone': '(732) 555-3579',
                'address': '321 Maple Ave, Edison, NJ 08817',
                'message': 'Looking to remodel master bathroom. Interested in walk-in shower and new vanity. Budget around $25k.',
                'subject': 'Bathroom Remodel Inquiry',
                'expected_score': 65,
                'expected_priority': 'high'
            },
            {
                'name': 'Jennifer Wilson',
                'email': 'jen.wilson@email.com',
                'phone': '(201) 555-4680',
                'address': '654 Oak Drive, Hackensack, NJ 07601',
                'message': 'Just exploring options for future kitchen update. No rush.',
                'subject': 'Kitchen Ideas',
                'expected_score': 25,
                'expected_priority': 'low'
            }
        ]
    
    def _mock_config_get(self, key, default=None):
        """Mock configuration getter for integration tests"""
        config_values = {
            'wordpress.url': 'https://test-topnotchnj.com',
            'wordpress.admin_user': 'test_admin',
            'wordpress.admin_password': 'test_password',
            'wordpress.database.host': 'localhost',
            'wordpress.database.name': 'test_wp',
            'wordpress.database.user': 'test_user',
            'wordpress.database.password': 'test_pass',
            'webhooks.contact_forms.crm_webhook_url': 'https://test-crm.com/webhook',
            'webhooks.contact_forms.lead_scoring': True,
            'business.lead_scoring_keywords': {
                'kitchen': 10, 'bathroom': 10, 'renovation': 8, 'emergency': 25,
                'urgent': 20, 'asap': 20, 'budget': 12, 'licensed': 5
            },
            'business.contact_info.email': 'test@topnotchnj.com'
        }
        return config_values.get(key, default)
    
    def test_end_to_end_lead_processing(self):
        """Test complete lead processing from form to CRM"""
        
        for lead_data in self.sample_leads:
            with self.subTest(lead=lead_data['name']):
                
                # Mock external dependencies
                with patch('requests.post') as mock_post:
                    mock_post.return_value.status_code = 200
                    mock_post.return_value.json.return_value = {'status': 'success'}
                    
                    # Process lead through complete workflow
                    result = self.contact_handler.process_form_submission(lead_data)
                    
                    # Verify processing success
                    self.assertTrue(result['success'])
                    self.assertIn('lead_id', result)
                    self.assertIn('lead_score', result)
                    
                    # Verify lead scoring accuracy
                    score_diff = abs(result['lead_score'] - lead_data['expected_score'])
                    self.assertLess(score_diff, 15, f"Lead score deviation too high for {lead_data['name']}")
                    
                    # Verify priority assignment
                    self.assertEqual(result['priority'], lead_data['expected_priority'])
                    
                    # Verify CRM integration was called
                    if mock_post.called:
                        call_args = mock_post.call_args
                        payload = call_args[1]['json']
                        self.assertIn('lead_id', payload)
                        self.assertIn('contact_info', payload)
    
    def test_webhook_integration_setup(self):
        """Test webhook integration setup process"""
        
        # Mock WordPress accessibility
        with patch.object(self.webhook_manager, '_check_wordpress_accessibility', return_value=True):
            
            # Setup integrations
            result = self.webhook_manager.setup_integrations(dry_run=True)
            
            # Verify setup success
            self.assertIn('integrations_setup', result)
            self.assertIn('javascript_code', result)
            
            # Verify form types are covered
            expected_forms = ['.elementor-form', '.contact-form-7', '.gravity-form']
            setup_forms = [i['form_selector'] for i in result['integrations_setup']]
            
            for form_type in expected_forms:
                self.assertIn(form_type, setup_forms)
    
    def test_elementor_troubleshooting_workflow(self):
        """Test Elementor troubleshooting and optimization workflow"""
        
        # Mock website accessibility
        with patch.object(self.elementor, '_check_website_accessibility', return_value=True):
            
            # Mock issue detection
            with patch.object(self.elementor, '_check_issue') as mock_check:
                mock_check.side_effect = lambda issue: issue in [
                    'slow_loading_galleries', 'contact_form_not_submitting'
                ]
                
                # Mock fix application
                with patch.object(self.elementor, '_fix_issue') as mock_fix:
                    mock_fix.return_value = {'success': True, 'actions': ['test_fix']}
                    
                    # Run diagnostics
                    result = self.elementor.run_diagnostics(dry_run=False)
                    
                    # Verify diagnostics completed
                    self.assertIn('issues_found', result)
                    self.assertIn('fixes_applied', result)
                    
                    # Verify critical issues are prioritized
                    critical_issues = [
                        issue for issue in result['issues_found'] 
                        if issue.get('severity') == 'critical'
                    ]
                    
                    if critical_issues:
                        # Critical issues should be in fixes_applied
                        self.assertGreater(len(result['fixes_applied']), 0)
    
    def test_wordpress_maintenance_workflow(self):
        """Test WordPress maintenance and optimization workflow"""
        
        # Mock WordPress accessibility
        with patch.object(self.maintenance, '_check_wordpress_accessibility', return_value=True):
            
            # Mock database connection
            with patch('mysql.connector.connect') as mock_connect:
                mock_conn = Mock()
                mock_cursor = Mock()
                mock_connect.return_value = mock_conn
                mock_conn.cursor.return_value = mock_cursor
                mock_cursor.fetchone.return_value = (100,)  # Mock query result
                
                # Run maintenance
                result = self.maintenance.run_maintenance(dry_run=True)
                
                # Verify maintenance completed
                self.assertIn('tasks_completed', result)
                self.assertIn('maintenance_summary', result)
                
                # Verify business optimizations were included
                self.assertIn('business_optimizations', result)
    
    def test_error_handling_and_recovery(self):
        """Test error handling and recovery mechanisms"""
        
        # Test with invalid lead data
        invalid_lead = {
            'name': '',  # Empty name
            'email': 'invalid-email',  # Invalid email
            'phone': '123',  # Invalid phone
            'message': ''  # Empty message
        }
        
        # Should handle gracefully without crashing
        result = self.contact_handler.process_form_submission(invalid_lead)
        
        # Should still return a result (even if unsuccessful)
        self.assertIsInstance(result, dict)
        self.assertIn('success', result)
        
        # Test CRM integration failure
        with patch('requests.post') as mock_post:
            mock_post.side_effect = Exception("CRM connection failed")
            
            valid_lead = self.sample_leads[0]
            result = self.contact_handler.process_form_submission(valid_lead)
            
            # Should handle CRM failure gracefully
            self.assertIsInstance(result, dict)
    
    def test_performance_under_load(self):
        """Test system performance under concurrent load"""
        
        def process_lead(lead_data):
            """Process a single lead"""
            with patch('requests.post') as mock_post:
                mock_post.return_value.status_code = 200
                mock_post.return_value.json.return_value = {'status': 'success'}
                
                return self.contact_handler.process_form_submission(lead_data)
        
        # Test concurrent processing
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            # Submit multiple leads concurrently
            futures = []
            for _ in range(10):
                for lead in self.sample_leads:
                    future = executor.submit(process_lead, lead)
                    futures.append(future)
            
            # Wait for all to complete
            results = [future.result() for future in futures]
        
        end_time = time.time()
        processing_time = end_time - start_time
        
        # Verify all processed successfully
        successful_results = [r for r in results if r.get('success')]
        self.assertEqual(len(successful_results), len(results))
        
        # Verify reasonable performance (should process 30 leads in under 10 seconds)
        self.assertLess(processing_time, 10.0)
        
        # Verify average processing time per lead
        avg_time_per_lead = processing_time / len(results)
        self.assertLess(avg_time_per_lead, 1.0)  # Less than 1 second per lead
    
    def test_business_logic_validation(self):
        """Test business-specific logic and rules"""
        
        # Test New Jersey service area prioritization
        nj_lead = {
            'name': 'Local Customer',
            'email': 'local@email.com',
            'phone': '(908) 555-1234',  # Union County area code
            'address': 'Linden, NJ 07036',
            'message': 'Kitchen renovation in Linden'
        }
        
        out_of_area_lead = {
            'name': 'Out of Area Customer',
            'email': 'outofarea@email.com', 
            'phone': '(212) 555-1234',  # NYC area code
            'address': 'New York, NY 10001',
            'message': 'Kitchen renovation in Manhattan'
        }
        
        # Process both leads
        nj_result = self.contact_handler.process_form_submission(nj_lead)
        oos_result = self.contact_handler.process_form_submission(out_of_area_lead)
        
        # NJ lead should score higher due to service area
        self.assertGreater(nj_result['lead_score'], oos_result['lead_score'])
        
        # Test renovation type categorization
        kitchen_lead = {'message': 'Need kitchen cabinets and countertops', 'subject': ''}
        bathroom_lead = {'message': 'Bathroom shower renovation needed', 'subject': ''}
        electrical_lead = {'message': 'Need electrical work - new outlets', 'subject': ''}
        
        kitchen_analysis = self.contact_handler._analyze_renovation_request(kitchen_lead)
        bathroom_analysis = self.contact_handler._analyze_renovation_request(bathroom_lead)
        electrical_analysis = self.contact_handler._analyze_renovation_request(electrical_lead)
        
        self.assertEqual(kitchen_analysis['renovation_type'], 'kitchen_renovation')
        self.assertEqual(bathroom_analysis['renovation_type'], 'bathroom_renovation')
        self.assertEqual(electrical_analysis['renovation_type'], 'electrical_work')
    
    def test_data_consistency_across_systems(self):
        """Test data consistency across all integrated systems"""
        
        lead_data = self.sample_leads[0]  # High-priority lead
        
        # Mock all external integrations
        with patch('requests.post') as mock_crm, \
             patch.object(self.webhook_manager, '_setup_followup_automation') as mock_followup:
            
            mock_crm.return_value.status_code = 200
            mock_crm.return_value.json.return_value = {'status': 'success', 'id': 'crm_123'}
            mock_followup.return_value = {'success': True}
            
            # Process lead
            result = self.contact_handler.process_form_submission(lead_data)
            
            # Verify data consistency
            self.assertEqual(result['success'], True)
            
            # Check that lead ID is consistent format
            self.assertTrue(result['lead_id'].startswith('TNJ_'))
            
            # Verify timestamp format
            timestamp = result['timestamp']
            # Should be valid ISO format
            datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            
            # Verify CRM payload consistency
            if mock_crm.called:
                crm_payload = mock_crm.call_args[1]['json']
                self.assertEqual(crm_payload['lead_id'], result['lead_id'])
                self.assertEqual(crm_payload['contact_info']['name'], lead_data['name'])

class TestSystemIntegration(unittest.TestCase):
    """Test integration between different system components"""
    
    def test_configuration_consistency(self):
        """Test configuration consistency across all modules"""
        
        # Test that all modules can load the same configuration
        mock_config = Mock()
        mock_config.get.return_value = 'test_value'
        
        # All modules should accept the same config object
        elementor = ElementorTroubleshooter(mock_config)
        contact_handler = ContactFormHandler(mock_config)
        webhook_manager = WebhookIntegrationManager(mock_config)
        maintenance = WordPressMaintenance(mock_config)
        
        # Verify all initialized successfully
        self.assertIsNotNone(elementor)
        self.assertIsNotNone(contact_handler)
        self.assertIsNotNone(webhook_manager)
        self.assertIsNotNone(maintenance)
    
    def test_logging_integration(self):
        """Test logging integration across all modules"""
        
        from utils.logger import setup_logging, get_logger
        
        # Setup logging
        setup_logging(level='DEBUG')
        
        # Get loggers for different modules
        elementor_logger = get_logger('elementor.troubleshooter')
        webhook_logger = get_logger('webhooks.contact_form_handler')
        maintenance_logger = get_logger('wordpress.maintenance')
        
        # All loggers should be configured
        self.assertIsNotNone(elementor_logger)
        self.assertIsNotNone(webhook_logger)
        self.assertIsNotNone(maintenance_logger)
        
        # Test logging functionality
        elementor_logger.info("Test elementor log")
        webhook_logger.info("Test webhook log")
        maintenance_logger.info("Test maintenance log")

if __name__ == '__main__':
    # Run integration tests
    unittest.main(verbosity=2)
