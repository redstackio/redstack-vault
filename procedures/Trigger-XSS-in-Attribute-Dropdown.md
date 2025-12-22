---
id: proc-003
tags:
  - xss
  - trigger
  - dropdown
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.291Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Attribute-Dropdown

## Summary

This procedure describes interacting with the UI to render the stored XSS payload from JSON keys, executing arbitrary JavaScript in the browser for potential session hijacking or data theft.

## Description

After payload injection, the JSON keys are displayed unsanitized in dropdown menus for attribute selection. Typing in fields like Primary or URL triggers autocomplete, parsing the malicious key as HTML and executing the JS (e.g., onerror alert). This is not self-XSS as it can be social-engineered via shared demo JSON files. Targets authenticated users; outcomes include JS execution in the victim's context, enabling cookie theft or further attacks.

## Requirements

1. Successfully injected JSON with payload
2. Access to attribute selection fields in UI Demo
3. Victim interaction (self or tricked user)

## Defense

Defensive measures and detection strategies:

- Escape all dynamic content in UI renders using libraries like DOMPurify
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor browser console for unexpected JS errors and alert on alert() calls

## Objectives

1. Render the malicious key in the dropdown
2. Execute the XSS payload in browser context
3. Achieve arbitrary JS for data exfiltration or hijacking

## Instructions

### Step 1: Locate Attribute Text Boxes

**Context**: Identify the input fields that trigger key rendering.

In the UI Demo configuration, find the text boxes labeled Primary, Secondary, Tertiary, Image, or URL.

> These fields provide autocomplete based on JSON keys.

### Step 2: Initiate Dropdown Interaction

**Context**: Force the UI to list and render JSON keys.

Click into one of the text boxes (e.g., Primary) and start typing any character to invoke the dropdown suggestions.

> The dropdown populates with JSON keys, including the malicious one.

### Step 3: Observe Payload Execution

**Context**: Confirm the XSS fires upon rendering.

As the malicious key appears in the dropdown, the <img> tag loads, fails src=1, and triggers onerror to execute alert(document.domain).

> An alert box appears, or replace with exfiltration payload (e.g., fetch to attacker server).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[trigger]]
- [[dropdown]]
- [[Execution]]
