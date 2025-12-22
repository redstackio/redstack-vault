---
tags:
  - login
  - customer
  - authentication
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
updated_at: '2025-12-13T23:52:34.335Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d6dcf0a5-dbc6-4c0e-9c54-b3d0acd93a88
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-as-Customer-to-Access-Account

## Summary

This procedure authenticates a registered customer user to the WooCommerce My Account page, enabling access to features like address editing required for XSS payload injection.

## Description

Using valid customer credentials on a WooCommerce-enabled WordPress site, this step logs in the user to the /my-account/ endpoint. It assumes the account was created in a prior setup and focuses on gaining authenticated access without triggering any security alerts. This positions the attacker to interact with billing details or edit addresses where the vulnerable county field is exposed.

## Requirements

1. Valid customer username and password from prior registration.
2. Network access to the WordPress site (e.g., http://192.168.0.101/wordpress/).
3. Cookies/session handling enabled in the browser.

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for customer logins.
- Log and monitor login attempts from unusual IPs.
- Use session timeouts and rate limiting on authentication endpoints.

## Objectives

1. Establish an authenticated customer session.
2. Gain access to editable account sections.
3. Prepare for payload injection without logout.

## Instructions

### Step 1: Navigate to Login Page

**Context**: Direct the browser to the customer login endpoint.

Visit http://192.168.0.101/wordpress/my-account/ and click the login link if not already on the form.

> Expected: Login form displayed with fields for username/email and password.

### Step 2: Submit Credentials

**Context**: Authenticate to receive a session cookie.

Enter customer credentials and submit the form.

> Expected: Redirect to /my-account/dashboard/ with personalized content; verify by checking user profile elements.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[login]]
- [[customer]]
- [[authentication]]
