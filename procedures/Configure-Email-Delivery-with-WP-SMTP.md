---
tags:
  - email
  - smtp
  - wordpress
type: procedure
tools:
  - '[[tools/wp-smtp]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Web Service]]'
updated_at: '2025-12-14T17:30:18.692Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 44fbbbb0-8d75-47e7-9bb9-afb5c914d1b5
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Web Service]]'
---
# Configure-Email-Delivery-with-WP-SMTP

## Summary

This procedure installs and configures the WP-SMTP plugin to ensure WordPress can send registration notification emails, delivering login credentials to the attacker's email after CSRF exploitation.

## Description

WordPress default email delivery often fails; WP-SMTP routes through external SMTP servers like Gmail or SendGrid. This is crucial for the attack as bbPress sends credentials post-registration. Configure with valid SMTP details to guarantee delivery during the exploit.

## Requirements

1. WordPress admin access
2. Valid SMTP server credentials (e.g., Gmail app password)
3. Internet access

## Defense

Defensive measures and detection strategies:

- Disable or monitor SMTP plugin configurations
- Use email logging to track registrations
- Implement CAPTCHA on registration to prevent automated sign-ups

## Objectives

1. Enable reliable email sending from WordPress
2. Test delivery for new user registrations
3. Ensure credentials reach attacker post-exploit

## Instructions

### Step 1: Install WP-SMTP Plugin

**Context**: Add the plugin to handle SMTP.

**Instructions**: In WordPress admin: Plugins > Add New > Search 'WP Mail SMTP' > Install and Activate.

> Expected output: Plugin active in plugins list.

### Step 2: Configure SMTP Settings

**Context**: Set up mailer to use external SMTP.

**Instructions**: Go to WP Mail SMTP > Settings > Mailer: Other SMTP > Enter SMTP Host (e.g., smtp.gmail.com), Port 587, Encryption TLS, Authentication Yes, Username/Password.

> Expected output: Settings saved without errors.

### Step 3: Test Email Configuration

**Context**: Verify emails can be sent.

**Instructions**: Use the plugin's 'Send a Test Email' feature to an address like attacker@email.com.

> Expected output: Test email received successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exfiltration Over Web Service]] Exfiltration Over Web Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/wp-smtp]]

## Tags

- email
- smtp
- configuration
