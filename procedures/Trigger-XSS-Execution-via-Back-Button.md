---
id: proc-shopify-xss-trigger-back-001
tags:
  - javascript-execution
  - browser-manipulation
  - xss-trigger
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
updated_at: '2025-12-13T23:56:03.516Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS Execution via Back Button

## Summary

This procedure triggers the reflected XSS by having the victim click the back button before full page load, executing the injected JavaScript in the admin context.

## Description

The vulnerability arises from the unsanitized href in the reflected anchor. Clicking back executes the javascript: protocol as the browser treats it as navigation. This runs in the high-privilege admin session, allowing data theft or actions. Requires precise timing.

## Requirements

1. Victim on the reflected page
2. Payload in anchor href
3. Victim follows instruction or habit to click back early

## Defense

Defensive measures and detection strategies:

- Sanitize all href attributes to strip protocols
- Disable or rewrite back button behaviors in admin apps
- Detect JavaScript execution anomalies via client-side monitoring

## Objectives

1. Execute arbitrary JavaScript
2. Access sensitive admin data or functions
3. Achieve impact like session hijacking

## Instructions

### Step 1: Position Victim for Trigger

**Context**: Ensure page is loading but not complete.

Instruct: "If the page looks off, try going back quickly."

### Step 2: Execute Back Button Click

**Context**: Trigger the href execution.

Victim clicks browser back button; the javascript: payload runs immediately.

**Expected Output**: Script executes, e.g., alert or network request to attacker.

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
- [[JavaScript]]
