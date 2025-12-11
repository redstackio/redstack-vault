---
tags:
  - rce
  - jenkins
  - script-console
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Jenkins
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques:
  - '[[AppleScript]]'
id: f64de76c-b281-427b-93b4-37c3bf6342c9
created_at: '2025-12-11T06:10:15.833Z'
updated_at: '2025-12-11T06:10:15.833Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Execute Arbitrary Code via Script Console

## Summary

This procedure uses Jenkins' Script Console to execute arbitrary Groovy scripts, achieving RCE on the server.

## Description

The Script Console is a default feature for admins but accessible due to misconfiguration, allowing script execution that can compromise the host system.

## Requirements

1. Authenticated access to Jenkins with Script Console enabled.
2. Knowledge of Groovy scripting.
3. Caution to avoid detection or damage.

## Defense

Defensive measures and detection strategies:

- Disable Script Console or restrict to admins only.
- Monitor for script executions in Jenkins logs.

## Objectives

1. Run test scripts to confirm RCE.
2. Execute commands for system access.
3. Achieve persistence or exfiltration if needed.

## Instructions

### Step 1: Access Script Console

**Context**: Navigate to the console endpoint.

Go to /script in the Jenkins interface.

> Expected: Script input form appears.

### Step 2: Execute Script

**Context**: Input and run Groovy code.

Enter a script like 'println "Hello".reverse()' and submit.

> Expected: Output confirming execution, e.g., 'olleH'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- [[AppleScript]]

## Commands Used

None

## Tools Used

None

## Tags

- rce
- jenkins
- script-console
