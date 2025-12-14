---
tags:
  - authentication
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T00:11:16.123Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 21e4ade5-0282-4550-8e02-0adaf787aabc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-to-MoPub-Application

## Summary

This procedure establishes an authenticated session in the MoPub web application, providing access to protected features like custom report creation where vulnerabilities can be exploited.

## Description

The MoPub application requires user authentication to access dashboard functionalities. This step involves logging in with valid credentials to obtain a session cookie, enabling navigation to the custom reports section. It is a prerequisite for exploiting client-side vulnerabilities like XSS in authenticated contexts. Expected outcomes include a valid session allowing form submissions that trigger reflections.

## Requirements

1. Valid MoPub username and password
2. Web browser (e.g., Chrome, Firefox) with proxy support for Burp Suite
3. Internet access to https://app.mopub.com

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent credential-based access
- Monitor login attempts for anomalies using web application firewalls (WAF)
- Log and alert on unusual session creations from new IPs

## Objectives

1. Obtain an authenticated session token
2. Access the custom reports dashboard
3. Prepare for subsequent exploitation steps

## Instructions

### Step 1: Navigate to Login Page

**Context**: Direct the browser to the MoPub entry point to initiate authentication.

No specific command; manually enter https://app.mopub.com in the browser address bar.

> The login form should load, prompting for credentials.

### Step 2: Enter Credentials and Submit

**Context**: Provide authentication details to establish a session.

No specific command; fill in the username and password fields, then click 'Login'.

> Upon success, the browser redirects to the dashboard, and session cookies are set. Verify by checking network tab for 200 OK on protected resources.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[authentication]]
- [[web]]
