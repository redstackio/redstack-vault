---
id: proc-inject-xss-001
tags:
  - xss
  - header-injection
  - burp-suite
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:50.106Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inject-XSS-Payload-into-X-Forwarded-Host

## Summary

This procedure modifies a captured HTTP request in Burp Suite by injecting a malicious JavaScript payload into the X-Forwarded-Host header, exploiting reflection vulnerabilities to enable XSS on the target website.

## Description

Targeting https://www.omise.co/, the server reflects the X-Forwarded-Host header value directly into the response without sanitization. The payload 'bing.com'><img src/onerror=prompt(document.cookie)> closes any open HTML tags and injects an img element that executes JavaScript on error, prompting cookie data. This step assumes the request is already captured and sent to Repeater.

## Requirements

1. Captured request from previous step in Burp Repeater
2. Knowledge of HTML/JS for payload crafting
3. Burp Suite with Repeater module active

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all HTTP headers before reflection in responses
- Implement Content Security Policy (CSP) to block inline script execution
- Log and monitor unusual header values for anomaly detection

## Objectives

1. Craft and insert XSS payload into the header
2. Ensure payload bypasses any basic filtering
3. Prepare request for execution to steal session data

## Instructions

### Step 1: Send to Repeater

**Context**: Transfer the intercepted request for editing.

No command; Burp action:
- In Intercept tab, click "Forward" until the request is processed, then right-click the history entry and select "Send to Repeater".

> This loads the request into Repeater for modification.

### Step 2: Add Malicious Header

**Context**: Insert the X-Forwarded-Host with XSS payload below the Host header.

No command; manual edit in Repeater:
- In the Raw request view, add a new line after Host: www.omise.co: X-Forwarded-Host: bing.com'><img src/onerror=prompt(document.cookie)>

> Expected: Header added; preview shows the payload integrated into the request.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[header-injection]]
