---
id: proc-uuid-1
tags:
  - csrf
  - recon
  - web
type: procedure
tools: []
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
updated_at: '2025-12-14T17:27:15.766Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify CSRF Vulnerable Endpoint in Localize

## Summary

This procedure involves reconnaissance to identify the CSRF-vulnerable endpoint in the Localize platform's project watch settings, confirming lack of token validation.

## Description

In the Localize platform, the endpoint for modifying project watch or notifications settings fails to validate the anti-CSRF token. By analyzing the application's behavior, an attacker can send POST requests with an empty or missing CSRFToken and observe that the server processes them, allowing forged requests. This targets http://www.localize.io/watch/{project_id} and enables unauthorized changes to user settings, disrupting notifications.

## Requirements

1. Access to a web browser or proxy tool like Burp Suite for inspecting requests
2. Knowledge of the target project ID (e.g., 9s from testing)
3. Victim authentication not required for identification, but for full testing

## Defense

Defensive measures and detection strategies:

- Implement strict CSRF token validation on all state-changing endpoints
- Use SameSite cookies to mitigate cross-site requests
- Monitor for anomalous setting changes in user logs

## Objectives

1. Confirm the endpoint accepts requests without CSRF validation
2. Document parameters like watch[events] for exploitation
3. Assess potential impact on user notifications

## Instructions

### Step 1: Analyze Endpoint Behavior

**Context**: Intercept or craft a legitimate request to the watch settings endpoint and modify the CSRFToken to test validation.

Use browser developer tools or a proxy to send a POST request:

```http
POST /watch/9s HTTP/1.1
Host: www.localize.io
Content-Type: application/x-www-form-urlencoded

CSRFToken=&watch[events][1]=0&watch[events][2]=0
```

> If the request succeeds without a valid token, the vulnerability is confirmed. Expected output: Server response with 200 OK and settings updated.

### Step 2: Verify No Token Requirement

**Context**: Omit the CSRFToken entirely and resend the request to ensure processing.

Send the request without the token parameter:

```http
POST /watch/9s HTTP/1.1
Host: www.localize.io
Content-Type: application/x-www-form-urlencoded

watch[events][1]=0&watch[events][2]=0
```

> Success if settings change occurs, indicating no validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[recon]]
