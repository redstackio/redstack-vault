---
url: 'https://wordpress.org/plugins/wp-mail-smtp/'
tags:
  - email
  - smtp
type: tool
verified: false
platforms:
  - Web
  - WordPress
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.685Z'
id: 8f56f0ab-04a9-4149-8d70-115fa389b2fe
validated: true
submitted: true
---
# wp-smtp

**Status**: Unverified

## Overview

WP Mail SMTP is a WordPress plugin that configures SMTP for reliable email delivery, essential for sending user registration notifications with login credentials in attacks relying on post-registration emails.

## Description

It overrides WordPress's default mail function to use external SMTP servers, preventing delivery failures. In offensive security, it's used to ensure attackers receive credentials after exploiting registration vulnerabilities like CSRF in bbPress.

## Features

- Feature 1: Supports multiple SMTP providers (Gmail, SendGrid, etc.)
- Feature 2: Test email functionality for verification
- Feature 3: Logging of email attempts for debugging

## Installation

### Requirements

- WordPress 4.0+
- Admin access

### Install Commands

No CLI; install via dashboard: Plugins > Add New > Search 'WP Mail SMTP' > Install.

## Basic Usage

Configure in WP admin: WP Mail SMTP > Settings > Select mailer and enter SMTP details.

### Common Options

| Option | Description |
|--------|-------------|
| Mailer | Choose SMTP provider |
| From Email | Sender address |
| SMTP Host/Port | Server details |

## Examples

### Example 1: Basic Usage

Set to Gmail SMTP: Host smtp.gmail.com, Port 587, TLS, auth with app password.

### Example 2: Advanced Usage

Enable logging: Check 'Enable Email Log' in settings for tracking.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exfiltration Over Web Service]] Exfiltration Over Web Service

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Check plugins list for 'WP Mail SMTP'
- Monitor SMTP traffic logs for unusual outbound emails

## Related Procedures


## Related Tools

- [[tools/bbPress]]

## References

- Official documentation: https://wpmailsmtp.com/docs/
- Related resources: WordPress Codex on wp_mail()
