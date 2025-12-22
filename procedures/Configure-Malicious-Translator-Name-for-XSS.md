---
id: proc-uuid-001
tags:
  - xss
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.808Z'
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
# Configure Malicious Translator Name for XSS

## Summary

This procedure involves setting a translator's name in the Localize platform to a malicious XSS payload, exploiting lack of input sanitization to prepare for reflection in admin interfaces.

## Description

In the context of Localize's project management system, the translator name field is user-controlled but not properly escaped when displayed in the admin's invite review page. By injecting HTML and JavaScript, such as an SVG onload handler, the payload breaks out of the expected context and executes in the victim's browser. This step requires a valid translator account and sets up the vector for subsequent exploitation, potentially leading to arbitrary code execution in the admin's session.

## Requirements

1. Active Localize account with translator role
2. Access to profile editing features
3. Basic knowledge of XSS payloads and HTML/JS injection

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and HTML escaping (e.g., using libraries like DOMPurify) on all user-controlled fields displayed in admin views
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous join requests with suspicious characters in names

## Objectives

1. Inject unsanitized payload into translator profile
2. Ensure payload survives storage and transmission
3. Prepare for reflection without triggering client-side validation

## Instructions

### Step 1: Access Profile Settings

**Context**: Log in and navigate to the area where translator details can be edited to insert the payload.

No specific command required; use the web interface:

- Log in to Localize at the platform URL.
- Go to 'My Profile' or 'Account Settings'.
- Locate the 'Name' or 'Display Name' field.

### Step 2: Inject Payload

**Context**: Enter the malicious string to close tags and inject executable content.

Update the name field with:

```"><svg onload="prompt(/xss/);">
```

> This payload terminates any enclosing attribute or tag (e.g., <span class="name">) and inserts an SVG element. The onload attribute executes JavaScript when rendered, displaying a prompt to confirm XSS.

### Step 3: Save and Verify

**Context**: Persist the change and check for immediate issues.

- Click 'Save' or 'Update Profile'.
- View your profile source in browser dev tools to confirm the payload is stored as-is.

> Expected output: Profile saves without error; source shows raw payload.

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
- [[injection]]
