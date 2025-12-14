---
tags:
  - code-generation
  - node-js
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Copy-as-Node-Request]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Java
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:53.851Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 543a12b6-1301-4140-bfbb-94f90aaf5934
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Copy-Request-as-Node-js-Code

## Summary

This procedure uses the vulnerable extension to generate Node.js code from an intercepted request, embedding the malicious cookie payload due to improper sanitization.

## Description

Right-clicking the request invokes the extension, which formats cookies in single quotes without escaping them (flaw in escapeQuotes function). The payload breaks out, injecting `require('child_process').exec('calc.exe')` into the executable code.

## Requirements

1. Intercepted request with malicious cookie
2. 'Copy as Node Request' extension loaded
3. Clipboard access

## Defense

Defensive measures and detection strategies:

- Patch extensions or review source code on GitHub
- Scan generated code for injections before execution
- Use linters for Node.js code

## Objectives

1. Generate injectable Node.js code
2. Confirm payload embedding
3. Prepare for execution

## Instructions

### Step 1: Select Copy Option

**Context**: Access the extension's functionality on the intercepted request.

**Instructions**: In Burp's Proxy > HTTP history or Intercept, right-click the request and choose 'Copy as Node.js Request'.

### Step 2: Inspect Generated Code

**Context**: Verify the output contains the injection.

**Instructions**: Paste from clipboard into a text editor.

> Look for unescaped single quotes in the cookie string, e.g., the code should include something like `'test='/require('child_process').exec('calc.exe')//'` which executes on run.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Copy-as-Node-Request]]

## Tags

- code-generation
- node-js
