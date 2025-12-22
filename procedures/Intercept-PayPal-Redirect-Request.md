---
id: proc-intercept-paypal-redirect
tags:
  - intercept
  - proxy
  - paypal
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:20.354Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept PayPal Redirect Request

## Summary

This procedure captures the GET request from the Uzbey platform to PayPal's endpoint, allowing inspection of vulnerable payment parameters prior to modification.

## Description

Following order initiation, the Uzbey site generates a redirect to https://www.paypal.com/cgi-bin/webscr with parameters like cmd=_cart, amount_1, quantity_1, and item_name_1. Using a proxy, this request is intercepted to prevent direct submission, enabling the attacker to view and prepare for tampering. The vulnerability arises because these parameters are client-generated and trusted by PayPal without Uzbey server verification.

## Requirements

1. Proxy tool (e.g., Burp Suite) set up with browser traffic routing
2. Ongoing order completion from previous procedure
3. HTTPS interception enabled (requires CA certificate installation)
4. Knowledge of request parameters for PayPal cart API

## Defense

Defensive measures and detection strategies:

- Proxy detection via headers (e.g., block requests with X-Forwarded-For mismatches)
- Rate limiting on checkout endpoints to prevent repeated interceptions
- Log all redirect parameters and alert on proxy indicators (e.g., unusual User-Agent)
- Use token-based validation for payment requests

## Objectives

1. Pause the redirect request for analysis
2. Confirm presence of modifiable amount parameters
3. Maintain session integrity during interception

## Instructions

### Step 1: Configure Proxy for Interception

**Context**: Route traffic through the proxy to capture the exact moment of redirect.

In Burp Suite, set the browser proxy to 127.0.0.1:8080 and enable intercept mode on the Proxy tab. Ensure the scope includes paypal.com.

> Expected: All HTTPS traffic routed; CA cert trusted in browser.

### Step 2: Trigger and Capture Request

**Context**: Proceed with checkout to generate and intercept the request.

Submit the PayPal payment option on Uzbey. The request will pause in the proxy showing GET /cgi-bin/webscr?cmd=_cart&amount_1=10.00&quantity_1=1&item_name_1=128x128%20Square...

> Expected: Full parameter list visible, including multiple items if cart has them.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- intercept
- proxy
- paypal
