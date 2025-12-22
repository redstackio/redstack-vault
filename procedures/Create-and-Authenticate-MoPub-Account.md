---
id: proc-mopub-account-001
tags:
  - authentication
  - mopub
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:48.026Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-and-Authenticate-MoPub-Account

## Summary

This procedure establishes an authenticated session on the MoPub platform by creating a new account and logging in, providing the necessary cookies and tokens for subsequent API requests.

## Description

In the context of exploiting the IDOR vulnerability, initial authentication is required to access the orders endpoint. MoPub is a mobile advertising platform where users register to manage ad orders. This step simulates an attacker gaining legitimate but limited access to the platform before escalating to unauthorized data queries. Prerequisites include a web browser and internet access; no special tools are needed beyond standard registration.

## Requirements

1. Web browser (e.g., Firefox or Chrome)
2. Email address for registration
3. Internet access to https://app.mopub.com

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account creation
- Monitor for anomalous login patterns from new accounts
- Use CAPTCHA on registration to prevent automated sign-ups

## Objectives

1. Obtain valid session credentials for authenticated requests
2. Access the platform's orders management features
3. Prepare for order creation and API exploitation

## Instructions

### Step 1: Register New Account

**Context**: Visit the MoPub signup page to create a test account.

Navigate to https://app.mopub.com/signup and provide email, password, and company details.

**Expected Output**: Confirmation email and account activation.

### Step 2: Log In and Authenticate

**Context**: Log in to establish a session with necessary cookies.

Go to https://app.mopub.com/login, enter credentials, and submit.

**Expected Output**: Redirect to dashboard with sessionid and csrftoken cookies set.

**Success Indicators**:
- Access to /orders page
- Cookies visible in browser developer tools

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- mopub
