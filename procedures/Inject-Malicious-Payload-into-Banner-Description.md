---
tags:
  - xss
  - payload-injection
  - javascript
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
updated_at: '2025-12-13T23:52:24.130Z'
sub_techniques: []
id: 17ccac86-8591-4806-a598-b9d44c1d4116
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Inject-Malicious-Payload-into-Banner-Description

## Summary

This procedure details the injection of a malicious JavaScript payload into the description field of a banner block in Stripo's template editor, leveraging the lack of input sanitization to store executable code for later XSS execution.

## Description

Targeting the stored XSS vulnerability in the banner block's description field, this step involves editing the block properties and inserting a payload such as `"><img src=1 onerror=alert(document.domain)>`. The field stores HTML without escaping, allowing the script to persist and execute when the template is rendered. This is performed in the web editor interface and assumes the template with banner block is already created. Outcomes include successful storage of the payload, enabling attacks like cookie theft when victims view the template.

## Requirements

1. Existing template with banner block from prior procedure
2. Active editing session in the template editor
3. Knowledge of basic HTML/JavaScript for payload crafting

## Defense

Defensive measures and detection strategies:

- Enforce server-side HTML escaping and sanitization on all input fields
- Use Content Security Policy (CSP) to restrict inline script execution
- Log and review all description field updates for anomalous patterns

## Objectives

1. Store unsanitized malicious HTML/JavaScript in the description
2. Ensure payload evasion of any client-side checks
3. Set up for execution in subsequent template views

## Instructions

### Step 1: Edit Banner Block Properties

**Context**: Access the description field within the banner block settings.

Select the banner block on the canvas, then open its properties panel (usually on the right sidebar). Locate the "Description" or "Alt Text" field.

> The properties panel expands, showing editable fields including the vulnerable description input.

### Step 2: Insert and Save Payload

**Context**: Enter the XSS payload and persist it in the backend.

In the description field, input: `"><img src=1 onerror=alert(document.domain)>`. Click "Save" or "Apply" to update the block, then save the entire template.

> The payload is stored without execution at this stage; no errors occur if sanitization is absent.

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
- [[JavaScript]]
