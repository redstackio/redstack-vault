---
id: proc-nextcloud-access-smtp-001
tags:
  - ssrf
  - nextcloud
  - admin-access
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - Nextcloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:02.086Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Nextcloud-Admin-SMTP-Settings

## Summary

This procedure outlines how an authenticated Nextcloud administrator navigates to the email configuration settings and enables SMTP mode, setting the stage for SSRF-based network probing via the server address field.

## Description

In Nextcloud, administrators can configure email settings through the web interface. Selecting SMTP mode exposes a field for the SMTP server address, which lacks input validation and allows internal IPs. This procedure assumes admin login and focuses on accessing the relevant form. The target environment is a standard Nextcloud deployment, and outcomes include readiness for SSRF exploitation to reveal internal network details.

## Requirements

1. Valid administrator credentials for the Nextcloud instance
2. Web browser with access to the Nextcloud URL (e.g., https://demo.nextcloud.com)
3. No additional tools; uses built-in web interface

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit admin privileges
- Monitor admin setting changes via audit logs for unusual email configurations
- Validate and sanitize all input fields in admin panels to block internal IPs

## Objectives

1. Gain access to the SMTP configuration interface
2. Enable SMTP mode for probing
3. Prepare for network reconnaissance without triggering alerts

## Instructions

### Step 1: Log In as Administrator

**Context**: Authenticate to the Nextcloud instance to access admin-only features.

Enter admin credentials at the login page.

> Successful login redirects to the dashboard.

### Step 2: Navigate to Admin Settings

**Context**: Locate the additional settings page where email configuration resides.

Access the URL: https://target.nextcloud.com/settings/admin/additional.

> The admin settings page loads, showing various configuration options.

### Step 3: Select SMTP Mode

**Context**: Switch to SMTP to expose the vulnerable server address field.

Choose "SMTP" from the email mode dropdown and save if prompted.

> SMTP fields appear, including server address and port, ready for input.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[nextcloud]]
- [[admin-access]]
