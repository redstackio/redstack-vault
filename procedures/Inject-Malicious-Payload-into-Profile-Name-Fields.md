---
tags:
  - xss
  - payload-injection
  - profile-manipulation
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
updated_at: '2025-12-14T03:15:47.144Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: fde38c56-f858-41d3-b8dd-5fb1611832c4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Profile-Name-Fields

## Summary

This procedure exploits the lack of proper escaping in the user profile name and lastname fields on marketplace.informatica.com, allowing injection of JavaScript payloads that are stored and later executed when profiles are viewed.

## Description

User input from name and lastname fields is concatenated directly into JavaScript code (e.g., `pageNameDTM` variable) without adequate quote escaping or sanitization, despite a partial regex replacement. The payload `'-alert(document.domain)-'` breaks out of the string, injecting `alert(document.domain)`. This stored XSS affects all viewers of the profile. Prerequisites include an authenticated session.

## Requirements

1. Authenticated session from prior login.
2. Access to profile editing interface.
3. Knowledge of JavaScript payloads suitable for the context.

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with proper escaping for JavaScript contexts (e.g., using JSON.stringify or libraries like DOMPurify).
- Implement Content Security Policy (CSP) to restrict inline script execution.
- Log and monitor profile updates for suspicious patterns like quote characters.

## Objectives

1. Store malicious JavaScript in the profile database.
2. Bypass any existing input validation.
3. Enable execution upon profile rendering.

## Instructions

### Step 1: Access Profile Editing

**Context**: Locate the form fields vulnerable to injection.

From the dashboard, navigate to the user profile settings page where name and lastname fields are editable.

> The fields should allow text input without immediate validation feedback.

### Step 2: Enter Payload and Save

**Context**: Insert the breakout payload to inject code.

In both 'name' and 'lastname' fields, input `'-alert(document.domain)-'`. Click save or update profile.

> The save should succeed, storing the payload. Inspect the page source to confirm insertion into JavaScript if possible.

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
- [[profile-manipulation]]
