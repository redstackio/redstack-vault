---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
name: Intercept-Resend-Email-Request-in-Stripo
tags:
  - csrf
  - recon
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:35.760Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Intercept-Resend-Email-Request-in-Stripo

## Summary

This procedure involves logging into an unverified Stripo account and intercepting the POST request triggered by the 'Resend it' link to identify the vulnerable endpoint lacking CSRF protection.

## Description

In the context of testing Stripo's email confirmation feature, an attacker or tester logs into an unverified account via https://my.stripo.email. Navigating to the account cabinet and clicking 'Resend it' sends a POST request to /cabinet/stripeapi/v1/resendEmailConfirmation. Unlike other protected endpoints, this one does not require CSRF tokens or specific content-types like application/json, making it susceptible to forgery. Interception reveals an empty request body {}, confirming the vulnerability. This step is crucial for understanding the attack surface before crafting exploits.

## Requirements

1. Access to a web browser with developer tools (e.g., Chrome DevTools) or a proxy tool like Burp Suite
2. Valid unverified Stripo account credentials
3. Network access to https://my.stripo.email

## Defense

Defensive measures and detection strategies:

- Implement CSRF token validation on all state-changing endpoints
- Enforce strict content-type checks (e.g., require application/json for APIs)
- Monitor for anomalous POST requests to resend endpoints from non-standard referers

## Objectives

1. Capture the exact request details for replication
2. Verify absence of CSRF protections
3. Identify bypassable same-origin policy elements

## Instructions

### Step 1: Login to Unverified Account

**Context**: Establish an authenticated session to access the resend feature.

Log into https://my.stripo.email with unverified account credentials. Navigate to the account settings or cabinet where the email verification status is shown.

### Step 2: Trigger and Intercept Request

**Context**: Simulate the resend action while capturing the network traffic to analyze the endpoint.

Click the 'Resend it' link or button. Use browser developer tools (F12 > Network tab) or a configured proxy to intercept the outgoing POST request.

**Expected Output**: Intercepted request showing:
- Method: POST
- URL: https://my.stripo.email/cabinet/stripeapi/v1/resendEmailConfirmation
- Body: {}
- No CSRF token in headers or body
- Content-Type not enforced

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[recon]]
