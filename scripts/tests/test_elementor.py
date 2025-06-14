"""
Unit Tests for Elementor Troubleshooter
======================================

Comprehensive test suite for Elementor troubleshooting functionality,
specifically testing home improvement website optimization features.

Test Coverage:
- Issue detection algorithms
- Performance optimization
- Gallery and slider functionality
- Contact form validation
- Mobile responsiveness checks
- Cache management
- Business-specific optimizations

Author: Top Notch New Jersey Development Team
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import json
import time
from datetime import datetime

# Import the modules to test
from elementor.troubleshooter import ElementorTroubleshooter
from config.settings import Config

class TestElementorTroubleshooter(unittest.TestCase):
    """Test cases for ElementorTroubleshooter class"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Mock configuration
        self.mock_config = Mock(spec=Config)
        self.mock_config.get.side_effect = self._mock_config_get
        
        # Initialize troubleshooter with mock config
        self.troubleshooter = ElementorTroubleshooter(self.mock_config)
        
        # Mock the session to avoid actual HTTP requests
        self.troubleshooter.session = Mock()
        
    def _mock_config_get(self, key, default=None):
        """Mock configuration getter"""
        config_values = {
            'wordpress.url': 'https://test-topnotchnj.com',
            'wordpress.database.host': 'localhost',
            'wordpress.database.name': 'test_wp',
            'wordpress.database.user': 'test_user',
            'wordpress.database.password': 'test_pass',
            'wordpress.database.port': 3306,
            'elementor.troubleshooting.notification_email': 'test@topnotchnj.com'
        }
        return config_values.get(key, default)
    
    def test_initialization(self):
        """Test troubleshooter initialization"""
        self.assertIsNotNone(self.troubleshooter)
        self.assertEqual(self.troubleshooter.wp_url, 'https://test-topnotchnj.com')
        self.assertIsInstance(self.troubleshooter.common_issues, list)
        self.assertIn('slow_loading_galleries', self.troubleshooter.common_issues)
        self.assertIn('contact_form_not_submitting', self.troubleshooter.common_issues)
    
    @patch('elementor.troubleshooter.requests.Session')
    def test_website_accessibility_check_success(self, mock_session):
        """Test successful website accessibility check"""
        # Mock successful response
        mock_response = Mock()
        mock_response.status_code = 200
        self.troubleshooter.session.get.return_value = mock_response
        
        result = self.troubleshooter._check_website_accessibility()
        self.assertTrue(result)
        self.troubleshooter.session.get.assert_called_once()
    
    @patch('elementor.troubleshooter.requests.Session')
    def test_website_accessibility_check_failure(self, mock_session):
        """Test failed website accessibility check"""
        # Mock failed response
        mock_response = Mock()
        mock_response.status_code = 500
        self.troubleshooter.session.get.return_value = mock_response
        
        result = self.troubleshooter._check_website_accessibility()
        self.assertFalse(result)
    
    def test_gallery_performance_check_slow_loading(self):
        """Test gallery performance check detecting slow loading"""
        # Mock slow response
        mock_response = Mock()
        mock_response.text = '<img src="gallery1.jpg" /><img src="gallery2.jpg" />'
        
        # Mock time.time to simulate slow loading
        with patch('time.time') as mock_time:
            mock_time.side_effect = [0, 6.0]  # 6 second load time
            self.troubleshooter.session.get.return_value = mock_response
            
            result = self.troubleshooter._check_gallery_performance()
            self.assertTrue(result)  # Should detect slow loading
    
    def test_gallery_performance_check_fast_loading(self):
        """Test gallery performance check with fast loading"""
        # Mock fast response
        mock_response = Mock()
        mock_response.text = '<img src="gallery1.jpg" loading="lazy" />'
        
        # Mock time.time to simulate fast loading
        with patch('time.time') as mock_time:
            mock_time.side_effect = [0, 2.0]  # 2 second load time
            self.troubleshooter.session.get.return_value = mock_response
            
            result = self.troubleshooter._check_gallery_performance()
            self.assertFalse(result)  # Should not detect issues
    
    def test_contact_form_check_missing_forms(self):
        """Test contact form check when no forms are present"""
        # Mock response without forms
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = '<div>No forms here</div>'
        self.troubleshooter.session.get.return_value = mock_response
        
        result = self.troubleshooter._check_contact_forms()
        self.assertTrue(result)  # Should detect missing forms as an issue
    
    def test_contact_form_check_forms_present(self):
        """Test contact form check when forms are present with security"""
        # Mock response with forms and security
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = '<form class="elementor-form"><input name="wp_nonce" /></form>'
        self.troubleshooter.session.get.return_value = mock_response
        
        result = self.troubleshooter._check_contact_forms()
        self.assertFalse(result)  # Should not detect issues
    
    def test_mobile_responsiveness_check_missing_viewport(self):
        """Test mobile responsiveness check with missing viewport"""
        # Mock response without viewport
        mock_response = Mock()
        mock_response.text = '<html><head></head><body></body></html>'
        self.troubleshooter.session.get.return_value = mock_response
        
        result = self.troubleshooter._check_mobile_responsiveness()
        self.assertTrue(result)  # Should detect missing viewport as issue
    
    def test_mobile_responsiveness_check_responsive_design(self):
        """Test mobile responsiveness check with responsive design"""
        # Mock response with responsive elements
        mock_response = Mock()
        mock_response.text = '''
        <html>
        <head><meta name="viewport" content="width=device-width"></head>
        <body>
        <style>@media (max-width: 768px) { .responsive { display: block; } }</style>
        </body>
        </html>
        '''
        self.troubleshooter.session.get.return_value = mock_response
        
        result = self.troubleshooter._check_mobile_responsiveness()
        self.assertFalse(result)  # Should not detect issues
    
    def test_lead_scoring_keywords_detection(self):
        """Test that business-specific keywords are properly configured"""
        expected_keywords = ['kitchen', 'bathroom', 'renovation', 'quote', 'estimate']
        
        for keyword in expected_keywords:
            self.assertIn(keyword, self.troubleshooter.lead_scoring_keywords)
    
    def test_issue_severity_classification(self):
        """Test issue severity classification"""
        # Test critical issue
        severity = self.troubleshooter._get_issue_severity('contact_form_not_submitting')
        self.assertEqual(severity, 'critical')
        
        # Test high priority issue
        severity = self.troubleshooter._get_issue_severity('mobile_responsive_issues')
        self.assertEqual(severity, 'high')
        
        # Test medium priority issue
        severity = self.troubleshooter._get_issue_severity('slow_loading_galleries')
        self.assertEqual(severity, 'medium')
    
    def test_business_impact_assessment(self):
        """Test business impact assessment for home improvement context"""
        impact = self.troubleshooter._get_business_impact('contact_form_not_submitting')
        self.assertIn('lead', impact.lower())
        self.assertIn('critical', impact.lower())
        
        impact = self.troubleshooter._get_business_impact('slow_loading_galleries')
        self.assertIn('customer', impact.lower())
    
    @patch('elementor.troubleshooter.mysql.connector.connect')
    def test_database_bloat_check(self, mock_connect):
        """Test database bloat detection"""
        # Mock database connection and cursor
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        
        # Mock query result indicating large Elementor data
        mock_cursor.fetchone.return_value = (1000, 60 * 1024 * 1024)  # 60MB
        
        result = self.troubleshooter._check_database_bloat()
        self.assertTrue(result)  # Should detect bloat
        
        # Verify database queries were made
        mock_cursor.execute.assert_called()
        mock_cursor.close.assert_called()
        mock_conn.close.assert_called()
    
    def test_performance_thresholds(self):
        """Test performance threshold configuration"""
        thresholds = self.troubleshooter.performance_thresholds
        
        self.assertIn('page_load_time', thresholds)
        self.assertIn('gallery_load_time', thresholds)
        self.assertIn('mobile_score', thresholds)
        
        # Verify reasonable threshold values
        self.assertGreater(thresholds['page_load_time'], 0)
        self.assertLess(thresholds['page_load_time'], 10)
    
    def test_fix_gallery_performance(self):
        """Test gallery performance fix implementation"""
        result = self.troubleshooter._fix_gallery_performance()
        
        self.assertTrue(result['success'])
        self.assertIn('actions', result)
        self.assertIn('lazy_loading_enabled', result['actions'])
        self.assertEqual(result['issue_type'], 'slow_loading_galleries')
    
    def test_fix_contact_forms(self):
        """Test contact form fix implementation"""
        result = self.troubleshooter._fix_contact_forms()
        
        self.assertTrue(result['success'])
        self.assertIn('actions', result)
        self.assertEqual(result['issue_type'], 'contact_form_not_submitting')
    
    @patch('elementor.troubleshooter.datetime')
    def test_diagnostic_report_generation(self, mock_datetime):
        """Test diagnostic report generation"""
        # Mock datetime for consistent testing
        mock_datetime.now.return_value.isoformat.return_value = '2024-06-14T10:00:00'
        
        # Mock website accessibility check
        self.troubleshooter._check_website_accessibility = Mock(return_value=True)
        
        # Mock issue checks to return no issues
        for issue in self.troubleshooter.common_issues:
            setattr(self.troubleshooter, f'_check_{issue}', Mock(return_value=False))
        
        # Mock performance analysis
        self.troubleshooter._analyze_performance = Mock(return_value={
            'page_load_times': {'homepage': {'load_time': 2.5}},
            'recommendations': []
        })
        
        # Run diagnostics
        result = self.troubleshooter.run_diagnostics(dry_run=True)
        
        # Verify result structure
        self.assertIn('timestamp', result)
        self.assertIn('issues_found', result)
        self.assertIn('performance_metrics', result)
        self.assertIn('recommendations', result)
        self.assertTrue(result['dry_run'])
    
    def test_home_renovation_optimizations(self):
        """Test home renovation specific optimizations"""
        # Mock optimization methods
        self.troubleshooter._optimize_before_after_widgets = Mock()
        self.troubleshooter._optimize_contact_forms = Mock()
        self.troubleshooter._optimize_project_galleries = Mock()
        self.troubleshooter._setup_conversion_tracking = Mock()
        
        # Run optimizations
        self.troubleshooter.optimize_for_home_renovation()
        
        # Verify all optimization methods were called
        self.troubleshooter._optimize_before_after_widgets.assert_called_once()
        self.troubleshooter._optimize_contact_forms.assert_called_once()
        self.troubleshooter._optimize_project_galleries.assert_called_once()
        self.troubleshooter._setup_conversion_tracking.assert_called_once()

class TestElementorPerformanceAnalysis(unittest.TestCase):
    """Test cases for Elementor performance analysis"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.mock_config = Mock(spec=Config)
        self.mock_config.get.side_effect = lambda key, default=None: {
            'wordpress.url': 'https://test-topnotchnj.com'
        }.get(key, default)
        
        self.troubleshooter = ElementorTroubleshooter(self.mock_config)
        self.troubleshooter.session = Mock()
    
    def test_image_analysis(self):
        """Test image optimization analysis"""
        # Mock response with images
        mock_response = Mock()
        mock_response.text = '''
        <img src="large-image.jpg" />
        <img src="optimized.webp" />
        <img src="unoptimized.png" alt="Kitchen renovation" />
        '''
        self.troubleshooter.session.get.return_value = mock_response
        
        # Mock image size checks
        mock_head_response = Mock()
        mock_head_response.headers = {'content-length': '600000'}  # 600KB
        self.troubleshooter.session.head.return_value = mock_head_response
        
        result = self.troubleshooter._analyze_images()
        
        self.assertIn('total_images', result)
        self.assertIn('large_images', result)
        self.assertIn('unoptimized_formats', result)
    
    def test_mobile_performance_check(self):
        """Test mobile-specific performance analysis"""
        # Mock mobile response
        mock_response = Mock()
        mock_response.content = b'Mobile optimized content'
        
        with patch('time.time') as mock_time:
            mock_time.side_effect = [0, 2.5]  # 2.5 second load time
            self.troubleshooter.session.get.return_value = mock_response
            
            result = self.troubleshooter._check_mobile_performance()
            
            self.assertIn('mobile_load_time', result)
            self.assertIn('mobile_size_kb', result)
            self.assertIn('performance_score', result)

if __name__ == '__main__':
    unittest.main()
