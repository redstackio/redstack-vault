---
id: cba96335-9a52-4223-9b90-22822bfc53a6
name: Intercept-and-Modify-CSRF-Token-via-Proxy
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:23.392Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - csrf
  - web
  - proxy
  - modification
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Intercept-and-Modify-CSRF-Token-via-Proxy

## Summary

This procedure uses a proxy tool to intercept the registration form submission, modify the CSRF token in both the cookie and form field to arbitrary values, and forward the request to bypass verification.

## Description

Targeting the Veris platform's Django-based registration endpoint, this exploits the lack of server-side CSRF token verification, where only a length check (up to 32 characters) is enforced. By setting the 'csrftoken' cookie and 'csrfmiddlewaretoken' form field to matching arbitrary strings, the request succeeds, proving weakened protection. This can enable CSRF attacks on unauthenticated flows by allowing forged requests with custom tokens.

## Requirements

1. Burp Suite or similar proxy configured and browser traffic routed through it
2. Completed registration form from prior access
3. Knowledge of HTTP request structure (cookies and POST data)

## Defense

Defensive measures and detection strategies:

- Enforce server-side CSRF token validation using secure random generation and comparison
- Rate-limit form submissions and monitor for proxy-intercepted traffic patterns
- Use HTTP-only, secure cookies for CSRF tokens to prevent client-side tampering

## Objectives

1. Capture and alter CSRF token values in transit
2. Demonstrate acceptance of non-standard tokens
3. Complete registration with bypassed protection

## Instructions

### Step 1: Intercept the Request

**Context**: Capture the POST request to the registration endpoint during form submission.

Configure Burp Suite Proxy to intercept HTTPS traffic, then submit the form.

> Intercepted request shows POST to /portal/register/ with csrftoken in Cookie header and csrfmiddlewaretoken in body.

### Step 2: Modify CSRF Token Values

**Context**: Change the token to an arbitrary string to test verification logic.

In Burp Repeater or Proxy, edit the Cookie header: set csrftoken to 'arbitrarytoken1234567890' (≤32 chars). Then, in the POST body, set csrfmiddlewaretoken to the same value.

> Ensure values match exactly; forward the request to observe server acceptance.

### Step 3: Forward and Observe Response

**Context**: Submit the tampered request and check for success.

Click Forward in Burp to send the modified request.

> Server returns 200 OK with successful registration message, confirming bypass.

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
- [[web]]
- [[proxy]]
- [[modification]]
