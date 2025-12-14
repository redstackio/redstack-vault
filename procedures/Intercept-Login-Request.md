---
tags:
  - intercept
  - http-proxy
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ddb0cf48-e001-429f-9d50-d4ab10b13e2e
created_at: '2025-12-14T17:33:11.952Z'
updated_at: '2025-12-14T17:33:11.952Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Login-Request

## Summary

This procedure captures the HTTP POST request to the login endpoint of a web application, such as the Mars website, using a proxy tool to enable subsequent manipulation for authentication bypass.

## Description

In scenarios involving improper access control, intercepting login requests allows attackers to observe and alter server responses without needing valid credentials. This is particularly effective against endpoints lacking server-side validation of response integrity. The target environment is a web application accessible via HTTP/HTTPS, and the outcome is preparation for faking a successful login, leading to potential account takeover.

## Requirements

1. Proxy tool like Burp Suite installed and configured
2. Network access to intercept traffic (e.g., browser proxy settings)
3. Target website login form accessible

## Defense

Defensive measures and detection strategies:

- Implement HSTS and certificate pinning to prevent proxy interception
- Monitor for anomalous proxy traffic patterns in network logs
- Use client-side integrity checks on responses (e.g., HMAC signatures)

## Objectives

1. Capture exact login request structure
2. Identify response format for modification
3. Enable seamless transition to response tampering

## Instructions

### Step 1: Configure Proxy

**Context**: Set up the interception tool to route traffic through it.

In Burp Suite, configure the proxy listener on localhost:8080 and set the browser to use this proxy.

> Navigate to the Mars website and attempt a login to trigger the request.

### Step 2: Trigger and Capture Request

**Context**: Perform a login action to send the request, which gets intercepted.

Submit invalid credentials on the login form; the tool will pause the request for inspection.

> View the POST request to the login endpoint (e.g., /login), noting headers, body (username/password), and any CSRF tokens.

### Step 3: Forward Request

**Context**: Allow the request to proceed to the server to receive the authentic response for modification in the next procedure.

Forward the intercepted request to the server.

> Expected: Server responds with failure (e.g., 401), ready for alteration.

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
- [[http-proxy]]
- [[web]]
