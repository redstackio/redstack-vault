---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - idor
  - cookie
  - interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:23.676Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Intercept-Profile-Request-and-Identify-UID2-Cookie

## Summary

This procedure captures the HTTP request to the profile page using a proxy tool to inspect and identify the exposed user ID in the UID2 cookie, revealing the IDOR opportunity.

## Description

After logging in, navigating to the 'My Profile Page' triggers a request that includes the UID2 cookie with the user's numeric ID (e.g., 4820038). Without proper obfuscation, this allows direct reference manipulation. The target endpoint is a PHP-based profile handler in the DoD app.

## Requirements

1. Active session from prior login
2. Proxy tool (e.g., Burp Suite) configured with CA certificate for HTTPS interception
3. Knowledge of the profile URL post-login

## Defense

Defensive measures and detection strategies:

- Use indirect references (e.g., hashed IDs) instead of direct numeric UIDs in cookies
- Log and alert on anomalous cookie values in profile requests

## Objectives

1. Capture the profile request
2. Extract the UID2 cookie value
3. Confirm ID exposure for tampering

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception for all traffic to the target app.

Launch Burp Suite, configure the browser proxy to 127.0.0.1:8080, and install the CA certificate.

> Expected output: Proxy active, traffic routed through Burp.

### Step 2: Navigate to Profile

**Context**: Trigger the request to capture it.

With proxy intercept on, click to the 'My Profile Page' in the app.

> Expected output: Request paused in Burp Proxy tab, showing GET/POST to profile endpoint with headers including Cookie: UID2=4820038.

### Step 3: Inspect Cookie

**Context**: Analyze the request for vulnerabilities.

In Burp, view the Raw or Headers tab to locate and note the UID2 value.

> Expected output: UID2=4820038 visible, confirming direct object reference.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[interception]]
