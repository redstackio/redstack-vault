---
id: proc-uuid-003
tags:
  - xss-trigger
  - self-xss
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
updated_at: '2025-12-14T17:27:43.171Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS via Comment Edit

## Summary

This procedure triggers the stored XSS payload by loading the edit form, executing JavaScript in the browser context.

## Description

After injection, editing the comment reloads the form with the reflected payload, causing the <img onerror> to fire. This confirms the self-XSS in the attacker's session but highlights the risk for stored variants. Targets the same Demandware endpoint; requires prior payload submission.

## Requirements

1. Previously injected malicious comment
2. Access to wishlist edit UI
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Escape stored comments on output
- Validate edit requests with tokens
- Browser-based CSP enforcement

## Objectives

1. Execute injected JavaScript
2. Verify vulnerability impact
3. Simulate victim-side execution

## Instructions

### Step 1: Navigate to Edit

**Context**: Load the edit form for the comment.

**Command**:
```bash
# In browser: Click 'Edit Comments' on wishlist item
```

> Form loads with reflected payload.

### Step 2: Observe Execution

**Context**: Payload triggers on load.

**Command**:
```bash
# No command; monitor browser console/dev tools
```

> alert(1) pops; JS executes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- self-xss
