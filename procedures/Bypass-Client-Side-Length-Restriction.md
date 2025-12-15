---
tags:
  - bypass
  - client-side
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: 4c4a19f4-e5a0-49ec-9d8c-2ac55b92dab9
created_at: '2025-12-14T17:32:01.986Z'
updated_at: '2025-12-14T17:32:01.986Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-Client-Side-Length-Restriction

## Summary

This procedure modifies the HTML source to remove the maxlength=30 attribute on the API key name input, allowing longer payloads for XSS exploitation.

## Description

The vulnerability stems from relying solely on client-side validation without server-side checks. Using browser dev tools, the attacker alters the DOM to bypass this, enabling injection of payloads longer than 30 characters in the web application.

## Requirements

1. Browser with developer tools (e.g., F12 in Chrome)
2. API key form loaded
3. Basic HTML inspection knowledge

## Defense

Defensive measures and detection strategies:

- Implement server-side length validation
- Use Content Security Policy (CSP) to mitigate DOM manipulation effects

## Objectives

1. Remove client-side input limits
2. Enable oversized payload entry
3. Exploit validation gap

## Instructions

### Step 1: Open Developer Tools

**Context**: Access inspection features.

**Action**: Press F12 or right-click and select 'Inspect' on the name input field.

> Dev tools panel opens, highlighting the input element.

### Step 2: Modify HTML Attribute

**Context**: Edit the maxlength property.

**Action**: In the Elements tab, locate <input maxlength="30" ...> and delete the maxlength attribute.

> Save changes (Ctrl+S in some tools); the input now accepts unlimited length.

### Step 3: Test Bypass

**Context**: Verify the modification works.

**Action**: Attempt to type more than 30 characters in the field.

> Input is accepted without truncation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[bypass]]
- [[client-side]]
- [[web]]
