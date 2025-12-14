---
tags:
  - interception
  - proxy
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
updated_at: '2025-12-14T03:16:19.875Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 567c5fbe-5453-49f6-bb98-ebea40b69292
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Intercept-Form-Submission-with-Burp-Suite

## Summary

This procedure uses Burp Suite to capture the POST request from the forum subscription form submission, allowing inspection and modification before it reaches the server.

## Description

The vulnerable form submits a POST to /██████_█████████, reflecting the redacted parameter without sanitization. By enabling interception in Burp Suite, the request is paused, revealing parameters like activeFlag and the target one. This is essential for injecting payloads in a controlled manner. The target environment is a PHP-based web app; assume proxy is already configured.

## Requirements

1. Burp Suite running and browser proxied
2. Authenticated session on the application
3. Form loaded at https://██████

## Defense

Defensive measures and detection strategies:

- Deploy client-side request inspection or CSP to block proxy tampering
- Log and alert on unusual request patterns via SIEM

## Objectives

1. Capture the exact POST request structure
2. Identify the vulnerable redacted parameter
3. Pause for safe modification without submission

## Instructions

### Step 1: Enable Interception

**Context**: Configure Burp to trap POST requests.

**Command** (Burp Configuration):

In Burp Proxy > Intercept, toggle 'Intercept is on' and filter for POST to /██████_█████████.

> Burp dashboard shows ready state. Expected output: No traffic until form submit.

### Step 2: Submit Form

**Context**: Trigger the request capture.

**Command** (Browser Action):

Fill minimal form data (e.g., test values) and click 'Submit'.

> Request halts in Burp Repeater/Proxy tab. Expected output: Full HTTP POST visible, including Content-Type: application/x-www-form-urlencoded and parameters like %25%25Surrogate_██████=1.

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

- interception
- proxy
