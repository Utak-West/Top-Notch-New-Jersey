"""
Logging Configuration for Top Notch New Jersey Scripts
=====================================================

Centralized logging setup with business-specific formatting
and multiple output destinations for comprehensive monitoring.

Features:
- Structured logging with business context
- Multiple log levels and handlers
- File and console output
- Email alerts for critical issues
- Performance tracking integration

Author: Top Notch New Jersey Development Team
"""

import logging
import logging.handlers
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional

# Create logs directory if it doesn't exist
LOGS_DIR = Path(__file__).parent.parent / 'logs'
LOGS_DIR.mkdir(exist_ok=True)

class BusinessContextFilter(logging.Filter):
    """Add business context to log records"""
    
    def filter(self, record):
        record.company = 'Top Notch New Jersey'
        record.business_type = 'Home Improvement'
        record.specialization = 'Kitchen & Bathroom Renovation'
        return True

class ColoredFormatter(logging.Formatter):
    """Colored console formatter for better readability"""
    
    # ANSI color codes
    COLORS = {
        'DEBUG': '\033[36m',    # Cyan
        'INFO': '\033[32m',     # Green
        'WARNING': '\033[33m',  # Yellow
        'ERROR': '\033[31m',    # Red
        'CRITICAL': '\033[35m', # Magenta
        'RESET': '\033[0m'      # Reset
    }
    
    def format(self, record):
        # Add color to levelname
        if record.levelname in self.COLORS:
            record.levelname = (
                f"{self.COLORS[record.levelname]}"
                f"{record.levelname}"
                f"{self.COLORS['RESET']}"
            )
        
        return super().format(record)

def setup_logging(
    level: int = logging.INFO,
    log_file: Optional[str] = None,
    console_output: bool = True,
    max_file_size: int = 10 * 1024 * 1024,  # 10MB
    backup_count: int = 5
):
    """
    Setup comprehensive logging for Top Notch New Jersey scripts
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Custom log file path (optional)
        console_output: Enable console output
        max_file_size: Maximum log file size before rotation
        backup_count: Number of backup files to keep
    """
    
    # Create root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    
    # Clear existing handlers
    root_logger.handlers.clear()
    
    # Add business context filter
    business_filter = BusinessContextFilter()
    
    # Console handler with colors
    if console_output:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        
        console_formatter = ColoredFormatter(
            fmt='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
            datefmt='%H:%M:%S'
        )
        
        console_handler.setFormatter(console_formatter)
        console_handler.addFilter(business_filter)
        root_logger.addHandler(console_handler)
    
    # File handler with rotation
    if log_file is None:
        timestamp = datetime.now().strftime('%Y%m%d')
        log_file = LOGS_DIR / f'topnotch_automation_{timestamp}.log'
    
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=max_file_size,
        backupCount=backup_count,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)  # Always capture debug in files
    
    file_formatter = logging.Formatter(
        fmt='%(asctime)s | %(levelname)s | %(company)s | %(name)s | %(funcName)s:%(lineno)d | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler.setFormatter(file_formatter)
    file_handler.addFilter(business_filter)
    root_logger.addHandler(file_handler)
    
    # Error file handler for critical issues
    error_log_file = LOGS_DIR / f'topnotch_errors_{datetime.now().strftime("%Y%m%d")}.log'
    error_handler = logging.handlers.RotatingFileHandler(
        error_log_file,
        maxBytes=max_file_size,
        backupCount=backup_count,
        encoding='utf-8'
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(file_formatter)
    error_handler.addFilter(business_filter)
    root_logger.addHandler(error_handler)
    
    # Log startup message
    logger = logging.getLogger(__name__)
    logger.info("🚀 Top Notch New Jersey automation logging initialized")
    logger.info(f"📁 Log files: {LOGS_DIR}")
    logger.info(f"📊 Log level: {logging.getLevelName(level)}")

def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance with business context
    
    Args:
        name: Logger name (typically __name__)
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    
    # Add business-specific context
    if not hasattr(logger, '_business_context_added'):
        logger._business_context_added = True
        
        # Add extra context for this logger
        old_factory = logging.getLogRecordFactory()
        
        def record_factory(*args, **kwargs):
            record = old_factory(*args, **kwargs)
            record.business_context = {
                'company': 'Top Notch New Jersey',
                'industry': 'Home Improvement',
                'specialization': 'Kitchen & Bathroom Renovation',
                'license': '13VH13'
            }
            return record
        
        logging.setLogRecordFactory(record_factory)
    
    return logger

def log_performance(func):
    """
    Decorator to log function performance
    
    Usage:
        @log_performance
        def my_function():
            pass
    """
    import functools
    import time
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = get_logger(func.__module__)
        start_time = time.time()
        
        logger.debug(f"⏱ Starting {func.__name__}")
        
        try:
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            logger.info(f"✅ {func.__name__} completed in {execution_time:.2f}s")
            return result
            
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"❌ {func.__name__} failed after {execution_time:.2f}s: {e}")
            raise
    
    return wrapper

def log_business_event(event_type: str, details: dict):
    """
    Log business-specific events for analytics
    
    Args:
        event_type: Type of business event (lead_captured, form_submitted, etc.)
        details: Event details dictionary
    """
    logger = get_logger('business_events')
    
    event_data = {
        'event_type': event_type,
        'timestamp': datetime.now().isoformat(),
        'company': 'Top Notch New Jersey',
        **details
    }
    
    logger.info(f"📊 Business Event: {event_type}", extra={'event_data': event_data})

# Pre-configured loggers for common use cases
def get_elementor_logger():
    """Get logger for Elementor operations"""
    return get_logger('elementor')

def get_webhook_logger():
    """Get logger for webhook operations"""
    return get_logger('webhooks')

def get_security_logger():
    """Get logger for security operations"""
    return get_logger('security')

def get_maintenance_logger():
    """Get logger for maintenance operations"""
    return get_logger('maintenance')
