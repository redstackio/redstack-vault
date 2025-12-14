---
id: proc-uuid-456
tags:
  - csrf
  - web-vulnerability
  - token-reuse
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
updated_at: '2025-12-14T17:27:29.540Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-CSRF-Token-Non-Rotation

## Summary

This procedure verifies a CSRF token implementation flaw where tokens do not rotate per request in a web application session, such as drchrono.com's password change form. It enables attackers to reuse captured tokens for CSRF attacks, leading to unauthorized actions like account modifications.

## Description

In vulnerable applications like drchrono.com, CSRF tokens are generated once per session and remain static, allowing interception via XSS, MITM, or proxy tools. An attacker can capture the token during a legitimate request and replay it in a forged request to the POST endpoint (e.g., /profile/password-change), bypassing protections. This works even if the original session ID expires, as token validation is independent. The procedure involves logging in, navigating to the form, submitting twice with interception, and comparing tokens. Prerequisites include valid credentials and a proxy like Burp Suite for traffic capture. Expected outcomes: Confirmation of identical tokens and simulation of exploitation.

## Requirements

1. Valid user account credentials for the target web application (e.g., drchrono.com)
2. Proxy tool such as [[tools/Burp-Suite]] configured to intercept HTTPS traffic
3. Browser with developer tools or proxy support for form submission
4. Network access to the target site without restrictions

## Defense

Defensive measures and detection strategies:

- Rotate CSRF tokens per request or after each sensitive action to prevent reuse
- Implement token binding to session IDs and validate both on submission
- Monitor for anomalous POST requests to sensitive endpoints like password changes
- Use Content Security Policy (CSP) to mitigate XSS-based token theft

## Objectives

1. Confirm CSRF token non-rotation within a user session
2. Capture and compare tokens from multiple form submissions
3. Simulate token reuse to demonstrate CSRF exploitation potential

## Instructions

### Step 1: Establish Session and Access Form

**Context**: Log in to create a session and navigate to the vulnerable password change form to embed the CSRF token.

No specific command; perform manually in browser:

- Open drchrono.com and log in with credentials.
- Navigate to Settings > Profile > Change Password.
- Fill form fields with arbitrary new password values.

> This loads the form with the static CSRF token in the HTML or as a hidden input.

### Step 2: Intercept First Form Submission

**Context**: Submit the form while proxying traffic to capture the initial CSRF token in the POST request.

Configure [[tools/Burp-Suite]] proxy and submit the form.

No command; manual submission:

- Click 'Save' to trigger POST to the password change endpoint.
- In Burp, intercept and forward the request, then copy POST parameters including the CSRF token (e.g., csrf_token=abc123).

> Expected: POST data logged with token value.

### Step 3: Repeat Submission and Compare Tokens

**Context**: Submit the form again without logging out to verify token consistency.

Repeat form fill and submission:

- Refill and submit the password change form a second time.
- Intercept the second POST in Burp and extract the CSRF token.
- Compare tokens from both requests.

> Expected: Identical token values confirm non-rotation flaw.

### Step 4: Simulate Exploitation

**Context**: Use the captured token to craft a forged request demonstrating CSRF.

Manually craft a request:

- Create an HTML form with the reused token and malicious payload (e.g., new password).
- Submit to the endpoint: POST /profile/password-change with parameters including the static token.

> Expected: Request succeeds if targeted at a victim with valid session context.

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

- [[csrf]]
- [[web-vulnerability]]
- [[token-reuse]]
