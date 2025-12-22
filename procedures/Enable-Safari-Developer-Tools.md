---
id: proc-uuid-3
tags:
  - devtools
  - safari
type: procedure
tools:
  - '[[tools/Safari-JavaScript-Console]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:49.677Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Enable-Safari-Developer-Tools

## Summary

This procedure activates Safari's developer tools to access the JavaScript console for payload injection in the CSRF attack.

## Description

Safari's dev tools allow console execution, essential for dynamic form creation. Enable via preferences for Web Inspector access.

## Requirements

1. Safari on macOS
2. Administrative access to enable Develop menu

## Defense

Defensive measures and detection strategies:

- Disable dev tools in production environments if possible
- Monitor for console usage in client-side analytics

## Objectives

1. Access JavaScript execution environment
2. Prepare for payload injection
3. Inspect network requests

## Instructions

### Step 1: Configure Preferences

**Context**: Unlock the Develop menu.

Go to Safari > Preferences > Advanced, check "Show Develop menu".

> Expected: Develop menu appears in menu bar.

### Step 2: Open Inspector

**Context**: Launch tools on the malicious page.

Select Develop > Show Web Inspector, switch to Console tab.

> Expected: Console panel opens.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Safari-JavaScript-Console]]

## Tags

- devtools
- safari
