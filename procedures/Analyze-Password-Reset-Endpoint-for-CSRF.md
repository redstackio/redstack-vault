---
id: proc-uuid-1
tags:
  - csrf
  - reconnaissance
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:50.272Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Analyze Password Reset Endpoint for CSRF

## Summary

This procedure involves inspecting the password reset functionality of web applications like accounts.firefox.com to detect missing CSRF protections, enabling the identification of vulnerabilities that allow forged requests for information disclosure.

## Description

In the context of Mozilla's accounts.firefox.com, the attacker creates an account and analyzes the /reset_password endpoint. Using tools like Burp Suite, they intercept requests and confirm that the email parameter is accepted without anti-CSRF tokens or origin validation. This allows cross-origin submissions, leading to reset emails that disclose the submitter's (victim's) IP, location, and browser details. Prerequisites include an attacker account and basic web proxy knowledge; expected outcome is validation of the flaw for PoC development.

## Requirements

1. Attacker account on the target service (e.g., accounts.firefox.com)
2. Web proxy tool like Burp Suite for request interception
3. Internet access to the target endpoint

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens or SameSite cookies on all state-changing endpoints
- Monitor for anomalous reset requests from unexpected origins or IPs
- Enable CORS policies to restrict cross-origin requests

## Objectives

1. Confirm lack of CSRF protection on password reset
2. Document request parameters for PoC crafting
3. Validate information disclosure in reset emails

## Instructions

### Step 1: Register and Initiate Reset

**Context**: Create an account to access the reset flow and inspect legitimate requests.

Navigate to https://accounts.firefox.com and register, then trigger a password reset by submitting your email.

**Expected Output**: Reset email received with your own details (IP, browser info) for baseline.

### Step 2: Intercept and Analyze Request

**Context**: Use a proxy to capture the request and check for CSRF protections.

Configure Burp Suite as a proxy in your browser, resubmit the reset form, and examine the POST to /reset_password for tokens or headers like Origin.

**Expected Output**: Request body shows email=attacker@example.com without csrf_token; response initiates email without validation errors.

### Step 3: Test Forged Request

**Context**: Manually forge a request to confirm vulnerability.

Using Burp Repeater, send a request from a different origin (e.g., localhost) with email=attacker@example.com and verify reset email is sent.

**Expected Output**: Successful reset email confirming no CSRF enforcement.

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

- [[csrf]]
- [[web]]
- [[Reconnaissance]]
