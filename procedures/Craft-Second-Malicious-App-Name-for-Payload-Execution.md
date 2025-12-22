---
id: proc-craft-second-app-execution-2024
tags:
  - xss
  - javascript-uri
  - eval-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/eval-jquery-text]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.485Z'
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
# Craft Second Malicious App Name for Payload Execution

## Summary

This procedure forges the second javascript: URI in a Chaturbate app name to evaluate the stored room title payload using jQuery, completing the split XSS chain.

## Description

Building on the first app's variable setup, this app uses eval to execute the text from the #roomtitle element. The unfiltered '|' in app names allows URI forgery in the chat header links, leading to JS execution on click.

## Requirements

1. First app already created and variable set
2. jQuery loaded in the target page (as in Chaturbate)
3. App creation interface access

## Defense

Defensive measures and detection strategies:

- Block eval() and dynamic code execution in browser context
- Sanitize app names to prevent URI schemes
- Use strict CSP to restrict script sources

## Objectives

1. Reference variable from first payload
2. Retrieve and execute stored code
3. Trigger arbitrary JS for account control

## Instructions

### Step 1: Access App Creation Again

**Context**: Create a new dummy app after the first one.

**Instructions**: Ensure broadcast room is prepared.

### Step 2: Set Execution App Name

**Context**: Craft name for eval execution.

**Command** ([[commands/eval-jquery-text]]):

Use app name: `2|javascript:eval($(b).text())`

> Forges <a href="javascript:eval($(b).text())">. Relies on `b` from first click. Expected output: On click, executes room title code, e.g., alert popup. Test in victim session.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/eval-jquery-text]]

## Tools Used


## Tags

- [[xss]]
- [[eval-execution]]
