---
id: proc-uuid-1
tags:
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
updated_at: '2025-12-14T17:25:23.623Z'
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
# Authenticate-to-Zomato-Web-Application

## Summary

This procedure establishes a valid authenticated session on the Zomato web application, obtaining necessary session cookies and CSRF tokens required for subsequent API interactions in the IDOR exploitation chain.

## Description

In the context of exploiting the IDOR vulnerability in Zomato's treat subscriptions API, authentication is the initial step to gain a legitimate user session. This allows the attacker to mimic normal user behavior while preparing to manipulate API parameters. The target environment is the Zomato website (https://www.zomato.com), a PHP-based web application. Prerequisites include valid user credentials; expected outcomes are an active session enabling API calls without immediate detection.

## Requirements

1. Valid Zomato account credentials (email/password)
2. Web browser with developer tools enabled (e.g., Chrome)
3. Internet access to https://www.zomato.com

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to limit session abuse
- Monitor for unusual login patterns from known accounts
- Rate-limit login attempts to prevent credential guessing

## Objectives

1. Obtain a persistent authenticated session
2. Capture session artifacts (cookies, tokens) for API use
3. Ensure session validity for subsequent unauthorized requests

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the Zomato login interface to initiate authentication.

Open a browser and go to https://www.zomato.com. Click on the login button and enter your credentials.

**Expected Output**: Successful login and redirect to the user dashboard.

### Step 2: Capture Session Details

**Context**: Extract cookies and tokens from the authenticated session for reuse in API requests.

Open browser developer tools (F12), navigate to the Network tab, and inspect any request post-login to note the Cookie header (e.g., PHPSESSID) and any CSRF tokens in form data or headers.

**Expected Output**: Session cookie and CSRF token values copied for manual use.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- session-management
