---
id: proc-authenticate-stocky-login
tags:
  - authentication
  - login-bypass-setup
  - phishing
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
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:31.255Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Authenticate-on-Stocky-Login-Page

## Summary

This procedure covers logging into the Stocky app using the crafted login URL, which preserves the malicious return_to parameter to enable the subsequent open redirect.

## Description

After loading the vulnerable login page, users enter credentials to authenticate. The app processes the login without sanitizing the return_to parameter, leading to a redirect upon success. This step is crucial in the phishing chain, as it requires victim interaction but confirms the vulnerability when combined with the malicious URL. Target environment: Web-based Shopify app login. Prerequisites include valid credentials.

## Requirements

1. Valid username and password for a Stocky app account.
2. The malicious login URL already loaded in the browser.
3. No additional network restrictions.

## Defense

Defensive measures and detection strategies:

- Log all login attempts with parameter details for anomaly detection.
- Enforce multi-factor authentication (MFA) to mitigate credential theft post-redirect.
- Alert on logins from unusual referrers or parameters.

## Objectives

1. Successfully authenticate without triggering errors.
2. Preserve the return_to parameter during form submission.
3. Initiate the redirect mechanism.

## Instructions

### Step 1: Enter Credentials

**Context**: Fill the login form with target account details to simulate victim login.

No command; use browser form:

- Username: [target-username]
- Password: [target-password]
- Click 'Login' or submit.

> The form submits via POST; monitor network tab for the request including return_to in query or hidden field.

### Step 2: Confirm Authentication

**Context**: Verify login success before redirect.

Check for session cookie set or brief dashboard load.

> Expected: HTTP 302 redirect response with Location header pointing to return_to.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.002]] Spearphishing Link

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- web-login
