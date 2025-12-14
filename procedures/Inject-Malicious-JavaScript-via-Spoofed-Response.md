---
id: proc-js-injection-mitm
tags:
  - javascript-injection
  - mitm
  - cors
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:57.771Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-JavaScript-via-Spoofed-Response

## Summary

This procedure involves replacing the body of an intercepted HTTP response during a MITM attack with malicious JavaScript that, when executed in the victim's browser, sets up XMLHttpRequest objects for cross-origin attacks leveraging the spoofed CORS origin.

## Description

Following origin spoofing, the attacker modifies the response from the spoofed domain to include JavaScript code. This code runs in the context of the trusted origin, allowing it to make AJAX requests to sensitive endpoints like /profile with withCredentials=true, including session cookies. The attack relies on the server's CORS policy permitting credentials from the spoofed origin. Expected outcomes include arbitrary JS execution in the victim's session.

## Requirements

1. Established MITM position from prior procedure
2. Burp Suite for response modification
3. Knowledge of target endpoint (https://g-mail.grammarly.com/profile)
4. Victim's browser must execute the injected JS

## Defense

Defensive measures and detection strategies:

- Implement Content-Security-Policy (CSP) to block inline scripts
- Validate and sanitize all responses for unexpected JS
- Use HTTPS to prevent MITM tampering
- Browser extensions or network firewalls to detect proxy interference

## Objectives

1. Deliver and execute JS payload in victim's browser
2. Prepare for credentialed cross-origin requests
3. Maintain session hijacking via cookies

## Instructions

### Step 1: Intercept Response

**Context**: After spoofing the origin, capture the response to the spoofed domain.

**Instructions**: In Burp Suite's Proxy, forward the request but intercept the response.

### Step 2: Replace Response Body with JS

**Context**: Insert JavaScript that initializes XMLHttpRequest for profile access.

**Instructions**: Edit the response body to:

```html
<html><body><div id="response-node"></div><script>/* JS code for XHR setup */</script></body></html>
```

> The JS targets the /profile endpoint, setting withCredentials=true to attach cookies like profileToken. Server's reflective CORS allows the requests.

**Expected Output**: Victim's browser loads the page, executes JS, and console shows no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- javascript-injection
- mitm
- cors
