"""
Test Suite for Top Notch New Jersey WordPress Automation Scripts
===============================================================

Comprehensive test suite covering all automation functionality including:
- Unit tests for individual components
- Integration tests for system interactions
- End-to-end tests for complete workflows
- Performance tests for optimization validation
- Security tests for vulnerability assessment

Test Categories:
- Elementor troubleshooting and optimization
- Webhook integration and lead processing
- WordPress maintenance and security
- Configuration management
- Email notifications
- Business logic validation

Author: Top Notch New Jersey Development Team
"""

import sys
import os
from pathlib import Path

# Add the scripts directory to Python path for imports
scripts_dir = Path(__file__).parent.parent
sys.path.insert(0, str(scripts_dir))

__version__ = "1.0.0"
__test_categories__ = [
    "unit_tests",
    "integration_tests", 
    "performance_tests",
    "security_tests",
    "business_logic_tests"
]
