---
id: proc-uber-set-payload-134124
name: Set-Malicious-Invite-Code-Payload
tags:
  - xss
  - payload-injection
  - uber
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
updated_at: '2025-12-14T03:15:26.607Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Set-Malicious-Invite-Code-Payload

## Summary

This procedure involves injecting a malicious JavaScript payload into the Uber invite code field on uber.com, exploiting the lack of input validation to store the payload for later execution on m.uber.com.

## Description

In the Uber platform, the invite code feature allows users to set custom codes in their personal area on uber.com. Due to insufficient sanitization, arbitrary HTML and JavaScript can be injected. The payload syncs to m.uber.com, where it is displayed unsanitized upon login, leading to self-XSS. This is particularly effective for obfuscated payloads hidden in long strings to evade casual detection. Prerequisites include an authenticated Uber account.

## Requirements

1. Authenticated access to uber.com personal area
2. Web browser for form submission
3. Knowledge of JavaScript payloads for XSS

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and HTML escaping for user-controlled fields
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for unusual invite code lengths or patterns indicating obfuscation

## Objectives

1. Store malicious JavaScript in the invite code field
2. Ensure payload syncs to mobile site
3. Prepare for execution without alerting the user

## Instructions

### Step 1: Access Personal Area

**Context**: Log into uber.com and navigate to the invite code settings to prepare for payload injection.

Navigate to uber.com, sign in, and go to the personal area or profile settings where the invite code can be edited.

### Step 2: Inject Payload

**Context**: Enter the malicious payload into the invite code field, leveraging unlimited length to obfuscate if needed.

Enter a payload such as `<script>alert(document.domain)</script>` for testing, or an obfuscated version like `EMPLOYEE_2016_04_oidkjnfkerjnoidkjnfkerjnoidkjnfkerjnoidkjnfkerjnoidkjnfkerjn<script>eval(atob('YWxlcnQoZG9jdW1lbnQuZG9tYWluKQ=='))</script>oidkjnfkerjnoidkjnfkerjnoidkjnfkerjnoidkjnfkerjnoidkjnfkerjn`. Submit and save the form.

> The form accepts the input without validation, storing it for display elsewhere.

### Step 3: Verify Storage

**Context**: Confirm the payload is saved by checking the profile or attempting a share.

Refresh the personal area page to ensure the code is updated with the injected content.

**Expected Output**: Payload visible in the invite code field, confirming storage.

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
- [[payload-injection]]
