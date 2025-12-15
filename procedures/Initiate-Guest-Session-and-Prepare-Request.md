---
id: proc-guest-session-prep
tags:
  - web
  - recon
  - session-prep
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
updated_at: '2025-12-14T17:25:18.236Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate Guest Session and Prepare Request

## Summary

This procedure establishes an unauthenticated guest session on the target website by adding a product to the basket and extracting CSRF tokens and cookies, preparing for exploitation of the registration endpoint.

## Description

In the context of theperfumeshop.com, this step simulates a guest checkout to obtain session artifacts without logging in. It targets the e-commerce flow to capture dynamic tokens required for authenticated-like requests, setting up the IDOR exploitation. Expected outcomes include a valid session ready for POST requests, with no persistent changes to the target.

## Requirements

1. Browser access to https://theperfumeshop.com
2. Burp Suite configured as a proxy for traffic interception
3. No prior authentication or credentials needed

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on basket additions to detect automated probing
- Monitor for unusual token extraction patterns in proxy logs

## Objectives

1. Establish guest session without authentication
2. Extract CSRF token and cookies for request forging
3. Prepare for IDOR exploitation in registration

## Instructions

### Step 1: Navigate to Target and Add Product

**Context**: Open the website in a browser proxied through Burp Suite to capture all traffic.

Intercept the request when adding a product to the basket.

> No specific command; use browser UI to select and add any product (e.g., a perfume item) to initiate the guest flow.

### Step 2: Extract CSRF Token and Cookies

**Context**: From the intercepted basket addition request/response, copy the CSRF token from headers or forms and session cookies.

Use Burp Suite to view and export these values.

> Expected output: CSRF token as a string (e.g., 'abc123...') and cookies like 'JSESSIONID=xyz'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[web]]
- [[recon]]
