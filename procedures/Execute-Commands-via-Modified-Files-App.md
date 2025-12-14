---
tags:
  - rce
  - command-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/access-rce-url]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:26:22.480Z'
sub_techniques:
  - '[[JavaScript]]'
id: b4fab719-9d50-4a0f-8c92-dbc48cca9ae9
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Execute-Commands-via-Modified-Files-App

## Summary

Use the overwritten App.php in the files app to execute arbitrary commands via URL parameters, achieving RCE as www-data.

## Description

The modified App.php processes poc_cmd parameter by executing it on the server (e.g., via system() in PHP). Accessing /apps/files/?dir=/&poc_cmd=whoami runs the command, outputting results directly. This grants full control: file read/write, PII access, and further escalation.

## Requirements

1. Successful file overwrite
2. Web access to the host
3. URL encoding knowledge for complex commands

## Defense

Defensive measures and detection strategies:

- Input sanitization in app code
- Disable or audit URL parameters
- Server-side logging of command executions

## Objectives

1. Verify RCE with simple command
2. Execute arbitrary payloads
3. Access/modify installation files and PII

## Instructions

### Step 1: Test RCE

**Context**: Confirm overwrite by running a basic command.

Visit https://[host]/apps/files/?dir=/&poc_cmd=whoami using [[commands/access-rce-url]].

### Step 2: Run Advanced Commands

**Context**: Demonstrate full compromise.

Replace poc_cmd with id, cat /etc/passwd, or custom scripts.

**Expected Output**: Command stdout, e.g., 'www-data www-data'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques

- [[JavaScript]] JavaScript (adapted for PHP execution)

## Commands Used

- [[commands/access-rce-url]]

## Tools Used


## Tags

- rce
- command-execution
