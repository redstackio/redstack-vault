---
id: proc-001
tags:
  - 2fa-bypass
  - auth-bypass
  - business-logic
  - api-manipulation
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
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:31:52.846Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
---
# Bypass-2FA-Disable-Password-with-Burp-Suite

## Summary

This procedure exploits a business logic vulnerability in the Localize application's 2FA disable process by intercepting and modifying API requests with Burp Suite, allowing an attacker to disable 2FA and reconfigure it to an SMS number under their control without providing the account password, using only stolen session cookies.

## Description

The attack targets the /api/user/two-factor/set endpoint, which handles 2FA configuration changes. While the UI requires password confirmation for disabling 2FA, the backend API does not validate the password parameter if omitted, enabling direct manipulation. This leads to unauthorized 2FA reconfiguration, facilitating account takeover. Prerequisites include a valid logged-in session (via stolen cookies) and network access to the web app. Expected outcomes: 2FA disabled on the original method and enabled on attacker's SMS, confirmed via API response and login attempts.

## Requirements

1. Valid session cookies for the target Localize account (e.g., obtained via session hijacking)
2. Burp Suite installed and configured as a proxy for the browser
3. Access to the target's 2FA settings page (https://localizestaging.com account settings)
4. Knowledge of a phone number for SMS reconfiguration (e.g., +62-hacker-phone-number)

## Defense

Defensive measures and detection strategies:

- Implement server-side password validation for all sensitive API endpoints, regardless of request origin
- Enforce CSRF tokens and rate limiting on 2FA change endpoints to prevent automated abuse
- Monitor for anomalous API calls omitting expected parameters (e.g., via WAF logs) and session cookie usage from unusual IPs
- Require multi-factor confirmation (e.g., email + password) for 2FA changes

## Objectives

1. Disable existing 2FA without password authentication
2. Reconfigure 2FA to SMS on attacker's phone for control
3. Achieve full account takeover by bypassing security controls

## Instructions

### Step 1: Set Up Burp Suite Interception

**Context**: Configure Burp to capture traffic from the browser to intercept the 2FA disable request.

In Burp Suite, navigate to the Proxy tab, enable Intercept mode, and configure your browser to use Burp as the proxy (e.g., 127.0.0.1:8080). Log in to the Localize app with the stolen session cookies and go to the 2FA settings page.

### Step 2: Trigger and Intercept the Disable Request

**Context**: Attempt a disable action with a wrong password to capture the full request structure without succeeding in the UI.

Click the 'Disable two factor' button in the UI, entering an incorrect password to trigger the POST request. In the Intercept tab, forward the request after noting the body (which includes the password parameter) and copy all headers, including session cookies.

### Step 3: Prepare Modified Request in Repeater

**Context**: Create a clean request omitting the password to bypass validation.

Switch to the Repeater tab in Burp, paste the target URL (https://localizestaging.com/api/user/two-factor/set), method (POST), and headers. Set the request body to `method=sms&phone=%2B62-hacker-phone-number` (ensure + is URL-encoded as %2B).

### Step 4: Execute the Bypassed Request

**Context**: Send the modified request to trigger the unauthorized 2FA change.

Click 'GO' in Repeater to send the request. The server processes it without password check, disabling current 2FA and setting up SMS on the new number.

### Step 5: Validate the Reconfiguration

**Context**: Confirm the bypass by checking the response and app state.

Review the response for success (e.g., JSON confirming set method). Refresh the 2FA page or attempt login to receive an SMS code on the attacker's phone.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Modify Authentication Process]] Modify Authentication Process

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- 2fa-bypass
- auth-bypass
- business-logic
- api-manipulation
