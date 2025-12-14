---
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
updated_at: '2025-12-14T03:16:07.927Z'
sub_techniques: []
id: 9eee2d0c-7878-4f76-9a4a-0099985b75e5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Template-with-XSS-Payload

## Summary

This procedure injects a malicious JavaScript payload into a template field name in Drchrono's form builder, exploiting the lack of escaping to store XSS for later execution.

## Description

The advanced form builder allows user-supplied field names without HTML/JS sanitization, enabling storage of payloads like SVG tags with onload events. This stored XSS persists when the template is shared publicly, executing on victim browsers. The procedure focuses on crafting and inserting the payload during template creation.

## Requirements

1. Access to the advanced form builder interface
2. Knowledge of effective XSS payloads (e.g., cross-browser compatible)
3. Browser developer tools for testing payload acceptance

## Defense

Defensive measures and detection strategies:

- Input validation and HTML escaping on all user-supplied fields
- Content Security Policy (CSP) to block inline script execution
- Audit logs for template creation with suspicious content (e.g., < > tags)

## Objectives

1. Insert unsanitized HTML/JS into a field name
2. Ensure payload survives template validation
3. Prepare for storage and sharing without immediate trigger

## Instructions

### Step 1: Add New Field in Builder

**Context**: Initiate field creation to access the vulnerable name input.

In the form builder, click 'Add Field' or equivalent button.

> Select field type if prompted, then focus on the name input area.

### Step 2: Inject XSS Payload

**Context**: Enter the malicious string to exploit the escaping flaw.

Type `<svg onload=alert(document.domain)>` directly into the field name box.

> Press enter or tab; confirm no auto-escaping occurs (raw tags remain visible).

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
