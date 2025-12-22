---
id: proc-uuid-002
name: Intercept-Verification-Code-Submission
tags:
  - intercept-request
  - proxy-traffic
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:06.517Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Verification-Code-Submission

## Summary

This procedure involves submitting an incorrect verification code on the reset page while intercepting the resulting POST request using a proxy tool like Burp Suite, capturing the endpoint and parameters for later brute-forcing.

## Description

After receiving the code email, the attacker enters a deliberately wrong code to generate a verification request. Proxying the traffic reveals the POST endpoint (e.g., /verify-reset-code) and the 'code' parameter, which lacks protection against repeated submissions. This is key for identifying the brute-force target in vulnerable web apps.

## Requirements

1. Burp Suite configured as a proxy (browser traffic routed through it)
2. Access to the verification page post-reset initiation
3. Knowledge of the verification endpoint from traffic inspection

## Defense

Defensive measures and detection strategies:

- Enforce CAPTCHA or secondary factors after failed attempts
- Log and alert on multiple failed verifications from the same session/IP
- Use HTTPS and validate request origins

## Objectives

1. Capture the exact POST request structure
2. Identify the code parameter for payload positioning
3. Confirm error response for invalid codes

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept browser requests to the target site.

In Burp, go to Proxy > Intercept and ensure it's on; configure browser proxy to 127.0.0.1:8080.

> Navigate to the verification page; traffic will pause for inspection.

### Step 2: Submit Incorrect Code

**Context**: Enter a wrong code (e.g., 0000) to trigger the POST request.

Forward the intercepted request in Burp; observe the POST body with code=0000 and parameters like email.

> Expected response: 400/401 error like "Invalid code"; save the request for Intruder.

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

- [[intercept-request]]
- [[proxy-traffic]]
