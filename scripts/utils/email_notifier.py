"""
Email Notification System for Top Notch New Jersey Scripts
=========================================================

Automated email notifications for script execution results,
security alerts, and business events related to lead generation
and website maintenance.

Features:
- SMTP integration with multiple providers
- HTML email templates for professional appearance
- Business-specific notification types
- Lead generation alerts
- Security incident notifications
- Performance reports

Author: Top Notch New Jersey Development Team
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from typing import Dict, Any, List, Optional
import logging
from pathlib import Path

from .logger import get_logger

class EmailNotifier:
    """Email notification system for Top Notch New Jersey automation"""
    
    def __init__(self, config):
        """
        Initialize email notifier with configuration
        
        Args:
            config: Configuration object containing SMTP settings
        """
        self.config = config
        self.logger = get_logger(__name__)
        
        # SMTP configuration
        self.smtp_host = config.get('notifications.smtp_host', 'smtp.gmail.com')
        self.smtp_port = config.get('notifications.smtp_port', 587)
        self.smtp_user = config.get('notifications.smtp_user', '')
        self.smtp_password = config.get('notifications.smtp_password', '')
        self.from_email = config.get('notifications.from_email', 'noreply@topnotchnewjersey.com')
        
        # Business information
        self.company_name = "Top Notch New Jersey"
        self.company_tagline = "Kitchen & Bathroom Renovation Specialists"
        self.license_number = "13VH13"
        
        # Default recipients
        self.default_recipients = [
            config.get('business.contact_info.email', 'info@topnotchnewjersey.com')
        ]
    
    def send_execution_report(self, results: Dict[str, Any], recipients: Optional[List[str]] = None):
        """
        Send script execution report
        
        Args:
            results: Execution results dictionary
            recipients: Email recipients (uses default if None)
        """
        if recipients is None:
            recipients = self.default_recipients
        
        subject = f"🔧 {self.company_name} - Automation Report"
        
        # Determine status
        status = "✅ SUCCESS" if not results.get('tasks_failed') else "⚠️ PARTIAL SUCCESS"
        if len(results.get('tasks_failed', [])) == len(results.get('tasks_completed', [])) + len(results.get('tasks_failed', [])):
            status = "❌ FAILED"
        
        # Create HTML content
        html_content = self._create_execution_report_html(results, status)
        
        # Create text content
        text_content = self._create_execution_report_text(results, status)
        
        self._send_email(
            recipients=recipients,
            subject=subject,
            text_content=text_content,
            html_content=html_content
        )
        
        self.logger.info(f"Execution report sent to {len(recipients)} recipients")
    
    def send_security_alert(self, alert_data: Dict[str, Any], recipients: Optional[List[str]] = None):
        """
        Send security alert notification
        
        Args:
            alert_data: Security alert information
            recipients: Email recipients (uses default if None)
        """
        if recipients is None:
            recipients = self.default_recipients
        
        severity = alert_data.get('severity', 'medium').upper()
        subject = f"🚨 {self.company_name} - Security Alert [{severity}]"
        
        html_content = self._create_security_alert_html(alert_data)
        text_content = self._create_security_alert_text(alert_data)
        
        self._send_email(
            recipients=recipients,
            subject=subject,
            text_content=text_content,
            html_content=html_content,
            priority='high' if severity in ['HIGH', 'CRITICAL'] else 'normal'
        )
        
        self.logger.warning(f"Security alert sent: {alert_data.get('issue_type', 'Unknown')}")
    
    def send_lead_notification(self, lead_data: Dict[str, Any], recipients: Optional[List[str]] = None):
        """
        Send new lead notification
        
        Args:
            lead_data: Lead information
            recipients: Email recipients (uses default if None)
        """
        if recipients is None:
            recipients = self.default_recipients
        
        lead_score = lead_data.get('lead_score', 0)
        renovation_type = lead_data.get('renovation_type', 'General Inquiry')
        
        subject = f"🏠 New Lead - {renovation_type} (Score: {lead_score})"
        
        html_content = self._create_lead_notification_html(lead_data)
        text_content = self._create_lead_notification_text(lead_data)
        
        priority = 'high' if lead_score >= 50 else 'normal'
        
        self._send_email(
            recipients=recipients,
            subject=subject,
            text_content=text_content,
            html_content=html_content,
            priority=priority
        )
        
        self.logger.info(f"Lead notification sent: {lead_data.get('email', 'Unknown')} (Score: {lead_score})")
    
    def _send_email(
        self,
        recipients: List[str],
        subject: str,
        text_content: str,
        html_content: str = None,
        attachments: List[str] = None,
        priority: str = 'normal'
    ):
        """
        Send email using SMTP
        
        Args:
            recipients: List of recipient email addresses
            subject: Email subject
            text_content: Plain text content
            html_content: HTML content (optional)
            attachments: List of file paths to attach (optional)
            priority: Email priority (normal, high)
        """
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['From'] = self.from_email
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject
            
            # Set priority
            if priority == 'high':
                msg['X-Priority'] = '1'
                msg['X-MSMail-Priority'] = 'High'
            
            # Add text content
            text_part = MIMEText(text_content, 'plain', 'utf-8')
            msg.attach(text_part)
            
            # Add HTML content if provided
            if html_content:
                html_part = MIMEText(html_content, 'html', 'utf-8')
                msg.attach(html_part)
            
            # Add attachments if provided
            if attachments:
                for file_path in attachments:
                    self._add_attachment(msg, file_path)
            
            # Send email
            context = ssl.create_default_context()
            
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                server.starttls(context=context)
                if self.smtp_user and self.smtp_password:
                    server.login(self.smtp_user, self.smtp_password)
                
                server.send_message(msg)
            
            self.logger.debug(f"Email sent successfully to {len(recipients)} recipients")
            
        except Exception as e:
            self.logger.error(f"Failed to send email: {e}")
            raise
    
    def _add_attachment(self, msg: MIMEMultipart, file_path: str):
        """Add file attachment to email message"""
        try:
            file_path = Path(file_path)
            if not file_path.exists():
                self.logger.warning(f"Attachment file not found: {file_path}")
                return
            
            with open(file_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {file_path.name}'
            )
            
            msg.attach(part)
            
        except Exception as e:
            self.logger.error(f"Failed to add attachment {file_path}: {e}")
    
    def _create_execution_report_html(self, results: Dict[str, Any], status: str) -> str:
        """Create HTML content for execution report"""
        execution_time = results.get('execution_time', 0)
        tasks_completed = results.get('tasks_completed', [])
        tasks_failed = results.get('tasks_failed', [])
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .header {{ background-color: #2c3e50; color: white; padding: 20px; text-align: center; }}
                .content {{ padding: 20px; }}
                .status {{ font-size: 24px; font-weight: bold; margin: 20px 0; }}
                .success {{ color: #27ae60; }}
                .warning {{ color: #f39c12; }}
                .error {{ color: #e74c3c; }}
                .section {{ margin: 20px 0; }}
                .task-list {{ list-style-type: none; padding: 0; }}
                .task-item {{ padding: 10px; margin: 5px 0; border-left: 4px solid #3498db; background-color: #ecf0f1; }}
                .footer {{ background-color: #34495e; color: white; padding: 15px; text-align: center; font-size: 12px; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>{self.company_name}</h1>
                <p>{self.company_tagline}</p>
                <p>Licensed Home Improvement Contractor</p>
            </div>
            
            <div class="content">
                <div class="status">{status}</div>
                
                <div class="section">
                    <h3>📊 Execution Summary</h3>
                    <p><strong>Execution Time:</strong> {execution_time:.2f} seconds</p>
                    <p><strong>Tasks Completed:</strong> {len(tasks_completed)}</p>
                    <p><strong>Tasks Failed:</strong> {len(tasks_failed)}</p>
                    <p><strong>Timestamp:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                </div>
                
                {self._create_task_list_html('✅ Completed Tasks', tasks_completed, 'success')}
                {self._create_task_list_html('❌ Failed Tasks', tasks_failed, 'error')}
            </div>
            
            <div class="footer">
                <p>Top Notch New Jersey - Automated Website Management</p>
                <p>This is an automated message from your WordPress maintenance system.</p>
            </div>
        </body>
        </html>
        """
        
        return html
    
    def _create_task_list_html(self, title: str, tasks: List, css_class: str) -> str:
        """Create HTML task list section"""
        if not tasks:
            return ""
        
        html = f'<div class="section"><h3>{title}</h3><ul class="task-list">'
        
        for task in tasks:
            if isinstance(task, tuple):  # Failed task with error
                task_name, error = task
                html += f'<li class="task-item {css_class}"><strong>{task_name.title()}</strong><br><small>{error}</small></li>'
            else:  # Completed task
                html += f'<li class="task-item {css_class}">{task.title()}</li>'
        
        html += '</ul></div>'
        return html
    
    def _create_execution_report_text(self, results: Dict[str, Any], status: str) -> str:
        """Create plain text content for execution report"""
        execution_time = results.get('execution_time', 0)
        tasks_completed = results.get('tasks_completed', [])
        tasks_failed = results.get('tasks_failed', [])
        
        text = f"""
TOP NOTCH NEW JERSEY - AUTOMATION REPORT
{self.company_tagline}
Licensed Home Improvement Contractor

STATUS: {status}

EXECUTION SUMMARY:
- Execution Time: {execution_time:.2f} seconds
- Tasks Completed: {len(tasks_completed)}
- Tasks Failed: {len(tasks_failed)}
- Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

COMPLETED TASKS:
{chr(10).join(f"✅ {task.title()}" for task in tasks_completed) if tasks_completed else "None"}

FAILED TASKS:
{chr(10).join(f"❌ {task[0].title()}: {task[1]}" if isinstance(task, tuple) else f"❌ {task}" for task in tasks_failed) if tasks_failed else "None"}

---
This is an automated message from your WordPress maintenance system.
        """
        
        return text.strip()
    
    def _create_security_alert_html(self, alert_data: Dict[str, Any]) -> str:
        """Create HTML content for security alert"""
        # Implementation would be similar to execution report
        # Simplified for brevity
        return f"<h1>Security Alert: {alert_data.get('issue_type', 'Unknown')}</h1>"
    
    def _create_security_alert_text(self, alert_data: Dict[str, Any]) -> str:
        """Create plain text content for security alert"""
        return f"Security Alert: {alert_data.get('issue_type', 'Unknown')}"
    
    def _create_lead_notification_html(self, lead_data: Dict[str, Any]) -> str:
        """Create HTML content for lead notification"""
        # Implementation would be similar to execution report
        # Simplified for brevity
        return f"<h1>New Lead: {lead_data.get('name', 'Unknown')}</h1>"
    
    def _create_lead_notification_text(self, lead_data: Dict[str, Any]) -> str:
        """Create plain text content for lead notification"""
        return f"New Lead: {lead_data.get('name', 'Unknown')}"
