---
id: proc-upchieve-intercept-001
tags:
  - intercept
  - modify-request
  - burp-suite
  - password-reset
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
updated_at: '2025-12-14T17:33:24.390Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-UPchieve-Password-Reset-Request

## Summary

This procedure intercepts the HTTP POST request for UPchieve's password reset, modifies the email parameter to an array including the attacker's email, and forwards it to exploit improper backend validation, resulting in a shared reset token.

## Description

The UPchieve password reset endpoint at https://app.upchieve.org/resetpassword accepts a JSON body with an 'email' field but fails to validate it as a single string, processing arrays instead. By using Burp Suite to tamper with the request, an attacker injects their email to receive the same token generated for the victim. This occurs in a web environment with email delivery services, requiring proxy interception capabilities. Prerequisites include knowing the victim's email and having Burp Suite configured.

## Requirements

1. Burp Suite installed and running as a proxy (e.g., browser proxy set to 127.0.0.1:8080)
2. Victim's email address
3. Attacker's email account for receiving the token
4. Network access to https://app.upchieve.org

## Defense

Defensive measures and detection strategies:

- Validate input parameters strictly as single strings on the backend
- Implement rate limiting on reset requests per IP/email
- Log and monitor anomalous request bodies (e.g., array inputs)
- Use CAPTCHA or secondary verification for resets

## Objectives

1. Intercept and alter the password reset request to include attacker's email
2. Trigger shared token generation without victim awareness
3. Enable subsequent account access

## Instructions

### Step 1: Access and Submit Reset Form

**Context**: Navigate to the reset page and submit the victim's email to generate an interceptable request.

Input the victim's email (e.g., victim@gmail.com) into the form at https://app.upchieve.org/resetpassword and submit.

> This triggers a POST request to the endpoint.

### Step 2: Intercept with Burp Suite

**Context**: Capture the request in transit for modification.

Ensure Burp Suite is proxying traffic; the request will be held in the Intercept tab.

> Request details: POST /resetpassword with JSON {"email": "victim@gmail.com"}.

### Step 3: Modify JSON Body

**Context**: Change the email field to an array to exploit the validation flaw.

In Burp's Repeater or Inspector, edit the body to {"email": ["victim@gmail.com", "attacker@gmail.com"]}.

> Verify JSON validity before proceeding.

### Step 4: Forward the Request

**Context**: Send the modified request to the server.

Click Forward in Burp Suite to release the request.

> Server responds with success, processing the array.

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

- [[intercept]]
- [[modify-request]]
- [[tools/Burp-Suite]]
- [[password-reset]]
