---
id: proc-2
tags:
  - interception
  - proxy
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:24.823Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Forgot-Password-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept HTTP requests to the forgot password endpoint, capturing the POST submission with an invalid email payload for further analysis and automation.

## Description

Burp Suite's Proxy Interceptor allows capturing traffic between the browser and the server. In this scenario, after submitting an arbitrary input like %0a to /users/forgot_password, the request is captured, revealing the data[User][email] parameter. This step is crucial for preparing payloads for automated testing. The target environment is a PHP web application with database backend.

## Requirements

1. Burp Suite installed and running
2. Browser configured to use Burp as proxy (e.g., 127.0.0.1:8080)
3. Access to the target URL

## Defense

Defensive measures and detection strategies:

- Monitor for proxy-like traffic patterns or unusual User-Agent strings
- Enforce HTTPS with HSTS to complicate interception
- Rate limit proxy-detected IPs

## Objectives

1. Capture the exact request structure
2. Identify injectable parameters
3. Prepare for fuzzing without manual repetition

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up interception to capture outgoing requests.

Launch Burp Suite, ensure the Proxy tab is active, and turn on Intercept in the Interceptor sub-tab.

### Step 2: Submit Request from Browser

**Context**: Trigger the capture by submitting a forgot password form with invalid input.

In the browser, go to https://affiliates.nordvpn.com/users/forgot_password, enter %0a in the email field, and submit.

**Expected Output**: Burp displays the intercepted POST request with body like data[User][email]=%0a.

### Step 3: Forward and Analyze

**Context**: Inspect the request details before forwarding.

Review headers and body in Burp, then forward the request to complete the submission.

**Expected Output**: Server response captured, showing database query execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- request-interception
- burp-suite
