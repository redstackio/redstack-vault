---
tags:
  - authentication
  - token-acquisition
  - web
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
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:46:09.082Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: fdb2ef0d-505a-4683-9fe8-f0fafa34e3ac
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Chaturbate-and-Obtain-Tokens

## Summary

This procedure authenticates a user to Chaturbate and extracts the session cookie and CSRF token required for authenticated requests, such as the SSRF exploitation in push notifications.

## Description

In the context of exploiting the blind SSRF vulnerability, initial access requires a valid user session. Logging in via the web interface generates necessary tokens. The target environment is the public-facing Chaturbate web application. Prerequisites include valid credentials and a proxy like Burp Suite for token capture. Expected outcomes: Active session with extractable Cookie and X-CSRFToken for use in crafted requests.

## Requirements

1. Valid Chaturbate username and password
2. Web browser or HTTP proxy (e.g., Burp Suite) for traffic interception
3. Internet access to chaturbate.com

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on login attempts to prevent brute-force
- Monitor for unusual token extraction patterns in proxy logs
- Use multi-factor authentication (MFA) to secure sessions

## Objectives

1. Establish authenticated session to the target application
2. Capture CSRF token and session cookie for request forging
3. Prepare for subsequent exploitation steps without session expiration

## Instructions

### Step 1: Access and Authenticate

**Context**: Navigate to the login page and submit credentials to initiate a session.

No specific command; use browser to visit https://chaturbate.com/accounts/login/ and enter credentials.

> Successful login redirects to the dashboard, setting session cookies.

### Step 2: Trigger Token-Containing Request

**Context**: Perform an action to generate a request that exposes the CSRF token, such as viewing a profile.

Intercept traffic with Burp Suite Proxy.

> Visit a profile URL like https://chaturbate.com/princesscin/. Extract X-CSRFToken from headers and Cookie from the request.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- authentication
- web-session
