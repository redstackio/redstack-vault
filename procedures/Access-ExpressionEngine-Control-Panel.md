---
id: proc-access-ee-control-panel
tags:
  - authentication
  - expressionengine
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:26:17.470Z'
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
# Access-ExpressionEngine-Control-Panel

## Summary

This procedure outlines logging into the ExpressionEngine control panel using valid credentials to gain access to administrative features, a prerequisite for exploiting internal vulnerabilities like LFI in developer tools.

## Description

ExpressionEngine is a PHP-based CMS with a web-based control panel for management. This procedure assumes possession of legitimate credentials for a user with control panel access. It establishes an authenticated session, enabling navigation to restricted areas such as developer utilities. In an attack scenario, stolen or weak credentials can be used; outcomes include session hijacking risks if not properly secured.

## Requirements

1. Valid username and password for an ExpressionEngine admin user
2. Network access to the web server hosting ExpressionEngine (HTTP/HTTPS)
3. Web browser or proxy tool like Burp Suite for request handling

## Defense

Defensive measures and detection strategies:

- Enforce strong password policies and multi-factor authentication (MFA) for admin accounts
- Monitor login attempts for anomalies (e.g., unusual IP addresses) using web application firewalls (WAF)
- Log all authentication events and review for brute-force patterns

## Objectives

1. Establish an authenticated session to the control panel
2. Verify permissions for developer utilities access
3. Position for subsequent exploitation steps

## Instructions

### Step 1: Navigate to Login Page

**Context**: Locate and access the control panel login endpoint to initiate authentication.

Open a web browser and navigate to the ExpressionEngine admin login, typically `https://target.com/admin.php` or `/system/login`.

**Expected Output**: Login form loads with fields for username, password, and CAPTCHA if enabled.

### Step 2: Submit Credentials

**Context**: Provide valid credentials to authenticate and create a session.

Enter the username and password, then submit the form. If using [[tools/Burp-Suite]], intercept the POST request to `/admin.php/login` and ensure cookies are handled properly.

**Expected Output**: Redirect to the control panel dashboard (`/admin.php` or similar) with a successful login message.

> Upon success, session cookies (e.g., `exp_sessionid`) are set, confirming access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- authentication
- expressionengine
