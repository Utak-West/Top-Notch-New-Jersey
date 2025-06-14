"""
Configuration management for Top-Notch New Jersey scripts
========================================================

Handles configuration loading, environment variable integration,
and business-specific settings for kitchen and bathroom renovation operations.

Features:
- JSON configuration file support
- Environment variable substitution
- Multi-environment support (dev, staging, production)
- Home improvement business-specific defaults
- Secure credential management

Author: Top Notch New Jersey Development Team
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

class Config:
    """Configuration management class for Top Notch New Jersey automation"""
    
    def __init__(self, config_path: str):
        """
        Initialize configuration from file path
        
        Args:
            config_path: Path to JSON configuration file
        """
        self.config_path = Path(config_path)
        self.data = self._load_config()
        self._validate_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from JSON file with environment variable substitution"""
        if not self.config_path.exists():
            logger.warning(f"Config file not found: {self.config_path}")
            logger.info("Using default configuration")
            return DEFAULT_CONFIG.copy()
        
        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
            
            # Recursively substitute environment variables
            config = self._substitute_env_vars(config)
            
            logger.info(f"Configuration loaded from: {self.config_path}")
            return config
            
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in config file: {e}")
            raise
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            raise
    
    def _substitute_env_vars(self, obj: Any) -> Any:
        """Recursively substitute environment variables in configuration"""
        if isinstance(obj, dict):
            return {key: self._substitute_env_vars(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [self._substitute_env_vars(item) for item in obj]
        elif isinstance(obj, str) and obj.startswith('ENV:'):
            env_key = obj[4:]  # Remove 'ENV:' prefix
            env_value = os.getenv(env_key, '')
            if not env_value:
                logger.warning(f"Environment variable not set: {env_key}")
            return env_value
        else:
            return obj
    
    def _validate_config(self):
        """Validate critical configuration parameters"""
        required_sections = ['wordpress', 'elementor', 'webhooks']
        
        for section in required_sections:
            if section not in self.data:
                logger.warning(f"Missing configuration section: {section}")
        
        # Validate WordPress URL
        wp_url = self.get('wordpress.url')
        if not wp_url or not wp_url.startswith(('http://', 'https://')):
            logger.warning("Invalid or missing WordPress URL")
        
        # Validate critical credentials
        critical_vars = [
            'wordpress.admin_user',
            'wordpress.admin_password',
            'wordpress.database.host'
        ]
        
        for var in critical_vars:
            if not self.get(var):
                logger.warning(f"Missing critical configuration: {var}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value using dot notation
        
        Args:
            key: Configuration key in dot notation (e.g., 'wordpress.url')
            default: Default value if key not found
            
        Returns:
            Configuration value or default
        """
        keys = key.split('.')
        value = self.data
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any):
        """
        Set configuration value using dot notation
        
        Args:
            key: Configuration key in dot notation
            value: Value to set
        """
        keys = key.split('.')
        current = self.data
        
        # Navigate to parent of target key
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        # Set the final value
        current[keys[-1]] = value
    
    def get_business_config(self) -> Dict[str, Any]:
        """Get business-specific configuration for Top Notch New Jersey"""
        return {
            'company_name': 'Top Notch New Jersey',
            'specializations': ['kitchen_renovation', 'bathroom_renovation'],
            'service_areas': ['Union County', 'Essex County', 'Middlesex County', 'Bergen County'],
            'license_number': '13VH13',
            'business_type': 'home_improvement',
            'lead_scoring_keywords': self.get('business.lead_scoring_keywords', DEFAULT_LEAD_KEYWORDS),
            'contact_info': self.get('business.contact_info', {})
        }

def load_config(config_path: str = 'config/production.json') -> Config:
    """
    Load configuration from file
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Config instance
    """
    return Config(config_path)

# Default lead scoring keywords for home improvement business
DEFAULT_LEAD_KEYWORDS = {
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
    'insured': 3
}

# Default configuration template for Top Notch New Jersey
DEFAULT_CONFIG = {
    "wordpress": {
        "url": "https://topnotchnj.com",
        "admin_user": "ENV:WP_ADMIN_USER",
        "admin_password": "ENV:WP_ADMIN_PASSWORD",
        "path": "/var/www/html",
        "database": {
            "host": "ENV:DB_HOST",
            "name": "ENV:DB_NAME", 
            "user": "ENV:DB_USER",
            "password": "ENV:DB_PASSWORD",
            "port": 3306
        }
    },
    "elementor": {
        "cache_optimization": True,
        "performance_monitoring": True,
        "auto_backup_before_fixes": True,
        "troubleshooting": {
            "auto_fix_common_issues": True,
            "notification_email": "info@topnotchnewjersey.com",
            "max_fix_attempts": 3
        },
        "home_renovation_optimizations": {
            "optimize_galleries": True,
            "before_after_widgets": True,
            "contact_form_optimization": True
        }
    },
    "webhooks": {
        "contact_forms": {
            "enrichment_api_key": "ENV:ENRICHMENT_API_KEY",
            "crm_webhook_url": "ENV:CRM_WEBHOOK_URL",
            "email_service_key": "ENV:EMAIL_SERVICE_KEY",
            "lead_scoring": True,
            "auto_followup": True
        },
        "integration_endpoints": [
            ".elementor-form",
            ".contact-form-7", 
            ".gravity-form"
        ]
    },
    "security": {
        "auto_hardening": True,
        "scan_frequency": "daily",
        "alert_email": "info@topnotchnewjersey.com"
    },
    "notifications": {
        "smtp_host": "ENV:SMTP_HOST",
        "smtp_port": 587,
        "smtp_user": "ENV:SMTP_USER", 
        "smtp_password": "ENV:SMTP_PASSWORD",
        "from_email": "noreply@topnotchnewjersey.com"
    },
    "business": {
        "company_name": "Top Notch New Jersey",
        "license_number": "13VH13",
        "specializations": ["kitchen_renovation", "bathroom_renovation"],
        "lead_scoring_keywords": DEFAULT_LEAD_KEYWORDS,
        "contact_info": {
            "phone": "ENV:BUSINESS_PHONE",
            "email": "info@topnotchnewjersey.com",
            "address": "Linden, NJ"
        }
    }
}
