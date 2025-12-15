---
id: proc-dod-login-001
tags:
  - initial-access
  - authentication
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:29.414Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Log-into-DoD-Website-for-Initial-Access

## Summary

This procedure establishes an authenticated session on the U.S. Department of Defense website, providing the necessary access to the FTP push server management feature required for subsequent IDOR exploitation.

## Description

The DoD website requires user authentication to access sensitive features like FTP/sFTP push server configurations. By logging in with valid credentials, an attacker gains a session that can be leveraged to manipulate URLs for unauthorized access. This step is a prerequisite for the IDOR attack, as the vulnerability only affects authenticated users. Expected outcomes include session establishment and navigation to the target management interface, setting the stage for parameter tampering.

## Requirements

1. Valid login credentials for a DoD website account (e.g., username and password)
2. Web browser with internet access to https://██████████/██████████
3. No proxy or VPN restrictions blocking government sites

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent credential-based access
- Monitor login attempts for anomalies, such as logins from unusual IP addresses
- Use session timeouts and IP binding to limit session abuse

## Objectives

1. Achieve authenticated access to the FTP management section
2. Establish a valid session for URL manipulation
3. Validate access to own FTP configurations as a baseline

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the entry point for authentication on the DoD website.

Navigate to https://██████████/██████████ in your web browser.

> This loads the login or registration interface. If no account exists, create one via the registration functionality to obtain credentials.

### Step 2: Authenticate with Credentials

**Context**: Submit valid user details to establish a session.

Enter username and password in the login form and submit.

> Upon success, the browser redirects to the dashboard. Verify by checking for personalized elements or accessing the FTP section.

### Step 3: Access FTP Management

**Context**: Confirm access to the vulnerable feature.

From the dashboard, navigate to the FTP push server management area.

> Expected: Page loads with your own server configurations visible, including an ID in the URL (e.g., /filepush/ftp/303/).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- initial-access
- dod
- web-auth
