---
id: proc-glassdoor-2fa-bypass-blank
name: Bypass-Glassdoor-2FA-with-Blank-Code
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.641Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Modify Authentication Process]]'
sub_techniques: []
tags:
  - 2fa-bypass
  - authentication-bypass
  - web
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Modify Authentication Process]]'
---

# Bypass-Glassdoor-2FA-with-Blank-Code

## Summary

This procedure exploits an improper authentication vulnerability in Glassdoor's 2FA system by intercepting the OTP verification POST request and removing the 'code' parameter, causing a blank submission that bypasses null checks and allows unauthorized login despite 2FA being enabled.

## Description

The attack targets a flaw where the server fails to validate null or empty OTP codes before comparison, enabling attackers with initial credential access to bypass 2FA. It requires proxying traffic through a tool like Burp Suite to modify requests during login. The target environment is the Glassdoor web application, specifically the 2FA endpoint. Expected outcomes include full account takeover, potentially leading to data exfiltration or account manipulation. Prerequisites include valid login credentials and network access to glassdoor.com.

## Requirements

1. Valid Glassdoor account credentials for initial setup.
2. Burp Suite installed and configured as a proxy for the browser.
3. Internet access to https://www.glassdoor.com.
4. Basic knowledge of HTTP request interception.

## Defense

Defensive measures and detection strategies:

- Implement strict null and empty string validation on all input parameters in authentication flows.
- Log and monitor for requests with missing or blank OTP parameters, alerting on anomalies during 2FA verification.
- Use client-side validation to prevent blank submissions, combined with server-side enforcement.
- Rate-limit login attempts and monitor proxy-like traffic patterns.

## Objectives

1. Bypass 2FA verification to gain unauthorized account access.
2. Demonstrate the impact of improper input validation in authentication.
3. Enable further post-exploitation actions like data access.

## Instructions

### Step 1: Setup and Enable 2FA

**Context**: Prepare the account by enabling 2FA to activate the vulnerable flow.

Log in to Glassdoor at https://www.glassdoor.com using credentials, navigate to https://www.glassdoor.com/member/account/securitySettings_input.htm, and enable 2FA via authenticator or SMS. Verify setup with the initial code.

> After enabling, log out to reset the session.

### Step 2: Initiate Login and Intercept OTP Request

**Context**: Trigger the 2FA prompt and capture the verification request.

Configure browser proxy to Burp Suite (default: 127.0.0.1:8080). Attempt login with credentials, enter an incorrect OTP when prompted, and enable intercept in Burp to capture the POST request to the 2FA endpoint.

> The request will include a 'code' parameter; inspect but do not forward yet.

### Step 3: Modify and Submit Blank Code

**Context**: Exploit the vulnerability by emptying the code parameter.

In Burp's Intercept tab, remove the 'code' parameter from the POST body (e.g., delete 'code=123456'). Forward the modified request.

> The server will process the blank code without validation, completing the login.

### Step 4: Verify Access

**Context**: Confirm the bypass success.

Disable intercept, refresh the page, and check for full account access (e.g., dashboard loaded).

> Successful bypass indicated by no further prompts and active session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Modify Authentication Process]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[2fa-bypass]]
- [[authentication-bypass]]
