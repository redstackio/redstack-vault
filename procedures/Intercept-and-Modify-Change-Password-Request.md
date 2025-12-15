---
id: proc-uuid-002
tags:
  - csrf
  - bypass
  - intercept
  - django
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
updated_at: '2025-12-14T17:27:03.230Z'
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
# Intercept-and-Modify-Change-Password-Request

## Summary

This procedure intercepts the POST request for changing a password in Veris View, removes the CSRF middleware token parameter, and forwards the modified request to exploit missing server-side validation, allowing the change to succeed without the token.

## Description

The vulnerability stems from Django's CSRF protection being generated client-side but not enforced server-side in the change password endpoint (likely /settings/password_change/). By using Burp Suite to proxy and edit the request, the csrfmiddlewaretoken is deleted from the form data (e.g., old_password, new_password1, new_password2). This simulates a CSRF attack where an attacker could craft a malicious form on another site to trigger the action. Prerequisites include an active session; outcomes include successful password update without token, confirming the flaw.

## Requirements

1. Active authenticated session from prior login
2. Burp Suite running as proxy (e.g., browser set to 127.0.0.1:8080)
3. Access to the settings page and filled password form

## Defense

Defensive measures and detection strategies:

- Enforce server-side CSRF token validation in Django views using @csrf_protect decorator
- Log and alert on password change requests missing CSRF tokens
- Implement Content Security Policy (CSP) to prevent cross-site form submissions

## Objectives

1. Bypass CSRF protection to perform unauthorized password changes
2. Demonstrate impact on authenticated users via tricked submissions
3. Validate the endpoint's lack of token enforcement

## Instructions

### Step 1: Navigate to Settings and Initiate Change

**Context**: Access the password change form to prepare the legitimate request for interception.

No command; GET /settings/ in browser, enter old_password, new_password1, new_password2, and submit.

> The form includes csrfmiddlewaretoken automatically. Expected output: Request captured in Burp if proxied.

### Step 2: Intercept and Edit Request

**Context**: Capture the POST request and remove the vulnerable parameter.

In Burp Suite Repeater or Proxy, inspect the POST body and delete the line 'csrfmiddlewaretoken: [token_value]'.

> Retain other parameters like old_password=oldpass&new_password1=newpass&new_password2=newpass. Expected output: Cleaned request ready for forwarding.

### Step 3: Forward Modified Request

**Context**: Send the altered request to the server to test validation.

Click 'Forward' in Burp Suite.

> Expected output: 200 OK with 'Password changed Successfully' message, no CSRF error.

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
- [[bypass]]
- [[intercept]]
- [[django]]
