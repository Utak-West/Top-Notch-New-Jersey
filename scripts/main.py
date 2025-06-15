#!/usr/bin/env python3
"""
Top-Notch New Jersey Site Management Script
==========================================

Main entry point for all WordPress/Elementor maintenance tasks
Designed specifically for kitchen and bathroom renovation business needs

Usage:
    python main.py --task all                    # Run all maintenance tasks
    python main.py --task elementor              # Elementor troubleshooting only
    python main.py --task webhooks               # Webhook integration setup
    python main.py --task maintenance            # WordPress maintenance
    python main.py --dry-run                     # Preview changes without executing
    python main.py --config config/staging.json # Use specific configuration

Author: Top Notch New Jersey Development Team
License: MIT
"""

import argparse
import sys
import logging
import time
from pathlib import Path
from typing import Dict, Any

# Import our modules
from config.settings import load_config
from elementor.troubleshooter import ElementorTroubleshooter
from webhooks.integration_manager import WebhookIntegrationManager
from wordpress.maintenance import WordPressMaintenance
from utils.logger import setup_logging
from utils.email_notifier import EmailNotifier

def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(
        description='Top-Notch New Jersey Site Management',
        epilog='Specialized for kitchen and bathroom renovation lead generation'
    )
    parser.add_argument(
        '--task', 
        choices=['elementor', 'webhooks', 'maintenance', 'security', 'all'],
        default='all',
        help='Task to execute (default: all)'
    )
    parser.add_argument(
        '--config', 
        default='config/production.json',
        help='Configuration file path (default: config/production.json)'
    )
    parser.add_argument(
        '--dry-run', 
        action='store_true',
        help='Preview changes without executing'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    parser.add_argument(
        '--email-report',
        action='store_true',
        help='Send email report after completion'
    )
    
    args = parser.parse_args()
    
    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    setup_logging(level=log_level)
    logger = logging.getLogger(__name__)
    
    # Banner
    print_banner()
    
    try:
        # Load configuration
        logger.info(f"Loading configuration from: {args.config}")
        config = load_config(args.config)
        
        # Initialize results tracking
        results = {
            'start_time': time.time(),
            'tasks_completed': [],
            'tasks_failed': [],
            'summary': {}
        }
        
        # Execute tasks based on selection
        if args.task in ['elementor', 'all']:
            logger.info("🔧 Starting Elementor troubleshooting...")
            try:
                troubleshooter = ElementorTroubleshooter(config)
                elementor_results = troubleshooter.run_diagnostics(dry_run=args.dry_run)
                results['summary']['elementor'] = elementor_results
                results['tasks_completed'].append('elementor')
                logger.info("✅ Elementor troubleshooting completed")
            except Exception as e:
                logger.error(f"❌ Elementor troubleshooting failed: {e}")
                results['tasks_failed'].append(('elementor', str(e)))
            
        if args.task in ['webhooks', 'all']:
            logger.info("🔗 Managing webhook integrations...")
            try:
                webhook_manager = WebhookIntegrationManager(config)
                webhook_results = webhook_manager.setup_integrations(dry_run=args.dry_run)
                results['summary']['webhooks'] = webhook_results
                results['tasks_completed'].append('webhooks')
                logger.info("✅ Webhook integration completed")
            except Exception as e:
                logger.error(f"❌ Webhook integration failed: {e}")
                results['tasks_failed'].append(('webhooks', str(e)))
            
        if args.task in ['maintenance', 'all']:
            logger.info("🛠 Running WordPress maintenance...")
            try:
                maintenance = WordPressMaintenance(config)
                maintenance_results = maintenance.run_maintenance(dry_run=args.dry_run)
                results['summary']['maintenance'] = maintenance_results
                results['tasks_completed'].append('maintenance')
                logger.info("✅ WordPress maintenance completed")
            except Exception as e:
                logger.error(f"❌ WordPress maintenance failed: {e}")
                results['tasks_failed'].append(('maintenance', str(e)))
        
        # Calculate execution time
        results['execution_time'] = time.time() - results['start_time']
        
        # Print summary
        print_summary(results, args.dry_run)
        
        # Send email report if requested
        if args.email_report:
            try:
                notifier = EmailNotifier(config)
                notifier.send_execution_report(results)
                logger.info("📧 Email report sent successfully")
            except Exception as e:
                logger.warning(f"Email report failed: {e}")
        
        # Exit with appropriate code
        if results['tasks_failed']:
            logger.error("Some tasks failed. Check logs for details.")
            sys.exit(1)
        else:
            logger.info("🎉 All tasks completed successfully!")
            sys.exit(0)
            
    except Exception as e:
        logger.error(f"💥 Critical error: {e}")
        sys.exit(1)

def print_banner():
    """Print application banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                 TOP NOTCH NEW JERSEY                         ║
    ║              WordPress Automation Suite                      ║
    ║                                                              ║
    ║        🏠 Kitchen & Bathroom Renovation Specialists         ║
    ║        ⚡ Licensed Home Improvement Contractor              ║
    ║        🔧 Automated Site Management & Lead Generation       ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def print_summary(results: Dict[str, Any], dry_run: bool):
    """Print execution summary"""
    mode = "DRY RUN" if dry_run else "EXECUTION"
    
    print(f"\n{'='*60}")
    print(f"EXECUTION SUMMARY - {mode}")
    print(f"{'='*60}")
    print(f"⏱  Execution Time: {results['execution_time']:.2f} seconds")
    print(f"✅ Tasks Completed: {len(results['tasks_completed'])}")
    print(f"❌ Tasks Failed: {len(results['tasks_failed'])}")
    
    if results['tasks_completed']:
        print(f"\n✅ Successful Tasks:")
        for task in results['tasks_completed']:
            print(f"   • {task.title()}")
    
    if results['tasks_failed']:
        print(f"\n❌ Failed Tasks:")
        for task, error in results['tasks_failed']:
            print(f"   • {task.title()}: {error}")
    
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
