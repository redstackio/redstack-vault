---
id: proc-line-zip-execution-001
tags:
  - rce
  - user-execution
  - macos
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Malicious File]]'
updated_at: '2025-12-14T17:26:29.926Z'
skill_level: low
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Malicious File]]'
---
# Trigger-Execution-via-Zip-Handling

## Summary

This procedure relies on the victim interacting with the malicious zip in the LINE Mac client, triggering the path traversal in filename parsing to execute the pre-placed .terminal file, leading to arbitrary code execution if Gatekeeper is disabled.

## Description

When the victim clicks the zip, the LINE client's logic error resolves the traversal filename to the .terminal path in ~/Downloads, launching it as if it were the zip handler. .terminal files execute Terminal commands directly. Success depends on Gatekeeper not blocking unsigned executables.

## Requirements

1. Victim's LINE Mac client vulnerable
2. .terminal in ~/Downloads
3. Gatekeeper disabled on victim machine

## Defense

Defensive measures and detection strategies:

- Enable and enforce Gatekeeper for all app executions
- Update LINE client to patched version fixing parsing
- Monitor for unexpected app launches from chat clients

## Objectives

1. Cause client to resolve traversal path
2. Execute .terminal payload
3. Achieve RCE without further interaction

## Instructions

### Step 1: Victim Interaction

**Context**: Prompt or wait for victim to click the zip.

The victim receives the zip message and clicks to open/handle it in LINE.

**Expected Output**: Client parses filename and navigates to target path.

### Step 2: Execution Confirmation

**Context**: Verify payload runs.

Observe effects like app launch (e.g., Calculator) or file creation from payload.

**Expected Output**: Commands from .terminal execute.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Malicious File]] User Execution: Malicious File

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- malicious-file
