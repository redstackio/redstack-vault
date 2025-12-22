---
tags:
  - xss
  - payload-injection
  - stored-xss
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
updated_at: '2025-12-14T03:46:26.586Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 76a3f383-b388-47f6-9dd9-9bec36ac93f4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Phone-Number-Field

## Summary

This procedure injects a stored XSS payload into the phone number field of the Shopify Email app settings, exploiting insufficient input validation to store malicious JavaScript for later execution.

## Description

The phone number field in Settings > General accepts arbitrary input without sanitization, allowing attackers to close HTML tags and inject script elements. The payload `1234567"><img src=a onerror=alert(1)>` breaks out of the input context and uses an onload error to execute JavaScript. This is a classic stored XSS, persisting the payload in the app's backend for rendering in user interfaces.

## Requirements

1. Installed Shopify Email app with access to Settings > General
2. Knowledge of basic HTML/JavaScript for payload crafting
3. Authenticated session as store admin

## Defense

Defensive measures and detection strategies:

- Implement server-side input sanitization (e.g., escape quotes, block script tags)
- Use Content Security Policy (CSP) to restrict inline scripts
- Log and monitor unusual input patterns in settings fields

## Objectives

1. Store unsanitized JavaScript in the phone number field
2. Ensure payload survives backend storage
3. Set up for execution in email rendering contexts

## Instructions

### Step 1: Navigate to Settings

**Context**: Access the vulnerable input field.

No specific command; in the Shopify Email app, click Settings > General.

> The page loads with form fields, including the phone number input.

### Step 2: Enter Payload

**Context**: Craft and input the malicious string to break out of the HTML attribute.

No specific command; in the phone number field, enter: `1234567"><img src=a onerror=alert(1)>`

> This appends `><img src=a onerror=alert(1)>` after the value, injecting an erroneous img tag that triggers on error.

### Step 3: Save Settings

**Context**: Persist the payload in storage.

No specific command; click the Save button.

> Settings update without errors; reload the page to confirm the payload is retained (may appear garbled if partially reflected).

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

