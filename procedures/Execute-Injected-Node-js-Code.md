---
tags:
  - rce
  - execution
type: procedure
tools:
  - '[[tools/Node-js]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:53.839Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 7f2c821a-4e74-4aeb-87b8-d782668ecd60
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-Injected-Node-js-Code

## Summary

This procedure runs the Burp-generated Node.js code, triggering the injected payload to achieve remote code execution on the local machine.

## Description

Pasting and executing the code in a Node.js environment causes the child_process module to spawn calc.exe due to the code injection from the cookie. This demonstrates RCE with user interaction (pasting and running).

## Requirements

1. Node.js installed and in PATH
2. Generated code from previous step
3. Terminal or IDE for execution

## Defense

Defensive measures and detection strategies:

- Never execute unverified generated code
- Run in sandboxed environments
- Monitor process creation events (e.g., Sysmon for calc.exe)

## Objectives

1. Execute the script without syntax errors
2. Trigger the injected command
3. Confirm RCE capability

## Instructions

### Step 1: Prepare Script

**Context**: Save the generated code to a file.

**Instructions**: Paste clipboard content into `request.js`.

### Step 2: Run Node.js Code

**Context**: Execute the script to invoke the payload.

**Instructions**: Open terminal and run `node request.js`.

> The script sends the HTTP request but executes the injected `exec('calc.exe')` immediately due to string breakout. Expected: No errors, request sent, calc launches.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Node-js]]

## Tags

- rce
- execution
