---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - persistent-xss
  - input-injection
type: procedure
tools: []
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
updated_at: '2025-12-14T03:16:08.081Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Class-Name-for-XSS

## Summary

This procedure exploits the lack of proper escaping in Khan Academy's class creation feature by injecting a cross-site scripting payload into the class name field, allowing it to persist and execute JavaScript when rendered in subsequent views.

## Description

The class creation form accepts user input for the class name without adequate sanitization for HTML or JSON contexts. By crafting a payload that closes an existing script tag and injects an executable script, an attacker can store malicious code that executes for any user viewing pages where the class name is rendered, such as coach reports. This persistent XSS enables client-side attacks like stealing session cookies or keystrokes from victims with coach access.

## Requirements

1. Valid Khan Academy user account with class creation permissions
2. Web browser for manual input and navigation
3. Knowledge of XSS payloads targeting script tag breakouts

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and HTML/JSON escaping (e.g., using libraries like DOMPurify)
- Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript alerts or network requests from reports pages

## Objectives

1. Persist malicious JavaScript via unsanitized class name input
2. Set up conditions for execution on rendered reports
3. Enable potential data theft from viewing users

## Instructions

### Step 1: Access Class Creation

**Context**: Log in and navigate to the class creation interface to prepare for payload injection.

Navigate to Khan Academy's class management section and select the option to create a new class.

### Step 2: Inject Payload

**Context**: Enter the crafted XSS payload into the class name field to exploit the escaping flaw.

Enter the following payload in the class name input field:

```
'</script>"><img src=x onerror=alert(0)>
```

Submit the form to create and save the class. The payload breaks out of any containing `<script>` tag and injects an `<img>` tag that executes `alert(0)` on error.

> This step succeeds if the class is created without validation errors, storing the payload server-side.

### Step 3: Verify Persistence

**Context**: Confirm the payload is stored by checking the class dashboard.

Return to your classes list and inspect the new class entry. No execution occurs here, but the name should display the injected HTML without sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[persistent-xss]]
- [[JavaScript]]
