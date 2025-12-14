---
tags:
  - xss
  - stored-xss
  - javascript-injection
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.149Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: b5d04378-6b73-430d-8e16-11c75311ec2e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-VK-App-with-XSS-Payload

## Summary

This procedure creates a new application in the VK.com developer console with a malicious JavaScript payload embedded in the application name field, exploiting insufficient sanitization to store XSS that executes on page load for authorized users.

## Description

The VK.com developer page for the Login widget fails to properly sanitize the application name, allowing injection of JavaScript schemes like 'javascript:alert(1);//'. This stored payload persists and executes when admins view the app details, particularly via browser history navigation. The procedure requires a VK developer account and targets the app creation interface to set up the vulnerability.

## Requirements

1. Active VK.com account with developer access
2. Web browser for interface interaction
3. Knowledge of target victim's VK ID for later steps

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding for all user-controlled fields like app names
- Use Content Security Policy (CSP) to block inline JavaScript execution
- Monitor for anomalous app creations with script-like names

## Objectives

1. Inject and store a JavaScript payload in the app name
2. Prepare the app for admin assignment to victims
3. Enable persistent XSS for client-side attacks

## Instructions

### Step 1: Access Developer Console

**Context**: Log into VK.com and navigate to the developer section to create a new app.

Go to https://vk.com/dev and select the Login widget type.

### Step 2: Set Malicious Name

**Context**: During app creation, input the XSS payload in the name field to store it unsanitized.

Enter the name as `javascript:alert(1);//` or a more stealthy variant like `'><script>alert(document.cookie)</script>` if supported.

### Step 3: Complete App Creation

**Context**: Finalize the app setup to persist the payload.

Fill in other required fields (e.g., description) and submit the creation form.

**Expected Output**: App created with ID, visible in dashboard, payload stored in name.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
