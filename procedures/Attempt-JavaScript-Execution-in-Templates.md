---
id: proc-uuid-3
name: Attempt-JavaScript-Execution-in-Templates
tags:
  - xss
  - js-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/attempt-js-execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.263Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Attempt-JavaScript-Execution-in-Templates

## Summary

This procedure attempts to execute JavaScript directly within template expressions to probe for XSS, revealing blacklisted functions like alert() that block immediate exploitation.

## Description

In the context of CSTI exploitation, after confirming template evaluation, this step injects JS code like alert(1) inside {{}}. The target frontend blacklists common methods, preventing execution but confirming the injection path. This is crucial for identifying bypass needs in web pentesting, with outcomes showing blocked behavior and paving way for encoding techniques.

## Requirements

1. Confirmed template injection from prior step
2. Web browser with JS console for monitoring
3. Knowledge of common blacklisted JS functions

## Defense

Defensive measures and detection strategies:

- Blacklist and filter JS keywords in template inputs
- Use Content Security Policy (CSP) to restrict eval and inline scripts
- Monitor for failed JS executions in client logs

## Objectives

1. Test JS execution feasibility
2. Identify blacklisted methods
3. Confirm escalation potential

## Instructions

### Step 1: Inject Simple JS

**Context**: Use a basic alert to test execution, expecting blockage.

**Command** ([[commands/attempt-js-execution]]):
```bash
# Browser URL: www.███/News/Speeches?Search={{alert(1)}}
```

> No alert appears; page loads normally, indicating blacklist on alert().

### Step 2: Verify Blockage

**Context**: Check browser console for errors or suppressed output.

**Command** (Console Inspection):

Open dev tools and reload.

```bash
# Look for JS errors or silent failures in console
```

> Expected output: No popup, possible console warnings about blocked code.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/attempt-js-execution]]

## Tools Used


## Tags

- xss
- js-injection
