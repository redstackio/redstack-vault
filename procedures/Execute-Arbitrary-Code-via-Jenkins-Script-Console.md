---
tags:
  - rce
  - groovy
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Jenkins
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques:
  - '[[AppleScript]]'
id: 70ed4614-b88a-4293-89f6-0a7f93b302d1
created_at: '2025-12-11T03:47:56.621Z'
updated_at: '2025-12-11T03:47:56.621Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Execute Arbitrary Code via Jenkins Script Console

## Summary

This procedure uses the Jenkins Script Console to run arbitrary Groovy scripts for remote code execution.

## Description

The Script Console allows administrators to execute Groovy code directly on the server, which can be abused if accessible to unauthorized users, leading to full system compromise.

## Requirements

1. Authenticated access with script execution permissions
2. Knowledge of Groovy scripting
3. Access to /script endpoint

## Defense

Defensive measures and detection strategies:

- Disable Script Console or restrict access
- Monitor console usage logs for anomalies

## Objectives

1. Execute test scripts to confirm RCE
2. Achieve system-level access
3. Perform post-exploitation actions

## Instructions

### Step 1: Access Script Console

**Context**: Navigate to the console endpoint.

Go to https://jenkins.target.com/script.

### Step 2: Run Groovy Script

**Context**: Enter and execute a test script.

**Command** ([[commands/groovy-rce-test]]):

```groovy
println System.getProperty("os.name")
```

> Submit the script and review the output to confirm execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- [[AppleScript]]

## Commands Used

- [[commands/groovy-rce-test]]

## Tools Used

- [[tools/Browser]]

## Tags

- [[commands/groovy-rce-test]]
- [[commands/groovy-rce-test]]
