---
id: proc-uuid-2
name: Analyze-Request-with-Burp-Proxy
tags:
  - csrf
  - analysis
  - proxy
type: procedure
tools:
  - '[[tools/Burp-Proxy]]'
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
updated_at: '2025-12-14T17:27:22.564Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Analyze-Request-with-Burp-Proxy

## Summary

This procedure uses Burp Proxy to intercept and modify the album addition request, confirming that the X-CSRFToken is not enforced, thus validating the CSRF vulnerability.

## Description

After triggering the album addition, the request is intercepted via Burp Suite's Proxy tool. The headers reveal X-CSRFToken and sessionid, but removing the token and resending the request still results in successful album creation. This demonstrates the server's acceptance of forged requests, enabling CSRF attacks. Prerequisites include Burp Suite setup as a browser proxy and an active session.

## Requirements

1. Burp Suite Professional or Community Edition installed
2. Browser configured to use Burp as proxy (e.g., 127.0.0.1:8080)
3. Active login session on onpatient.com

## Defense

Defensive measures and detection strategies:

- Enforce CSRF token validation and reject requests without it
- Log and alert on requests missing CSRF tokens
- Use same-site cookie attributes to mitigate cross-site requests

## Objectives

1. Intercept the legitimate POST request
2. Analyze and modify headers to test token requirement
3. Confirm vulnerability by successful request without token

## Instructions

### Step 1: Configure and Intercept Request

**Context**: Set up interception to capture the album addition traffic.

Launch Burp Proxy and configure your browser to route traffic through it. Repeat the album addition action.

> In Burp, view the intercepted POST request to /photos/add_album/.

### Step 2: Modify and Resend Request

**Context**: Test the vulnerability by removing the CSRF token.

In the Burp Repeater tab, delete the X-CSRFToken header and forward the request.

> Expected: Server responds with success (e.g., 200 OK and new album ID), confirming no validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Proxy]]

## Tags

- [[csrf]]
- [[analysis]]
- [[proxy]]
