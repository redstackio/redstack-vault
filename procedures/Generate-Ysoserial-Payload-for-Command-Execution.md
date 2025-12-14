---
id: p-generate-ysoserial-cmd
tags:
  - rce
  - payload-generation
  - ysoserial
type: procedure
tools:
  - '[[tools/ysoserial]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ysoserial-generate-commonscollections-cmd]]'
verified: false
platforms:
  - Linux
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:23:42.656Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Generate Ysoserial Payload for Command Execution

## Summary

This procedure uses ysoserial to create serialized Java payloads exploiting deserialization vulnerabilities, specifically targeting JBoss invokers to execute Windows commands like cmd.exe.

## Description

Ysoserial generates gadget chains (e.g., CommonsCollections1) that, when deserialized, trigger code execution. In this scenario, the payload executes 'cmd.exe' on the target Windows server. Prerequisites include Java runtime and the ysoserial JAR. The output is binary data redirected to a file for HTTP transmission.

## Requirements

1. Java 8+ installed
2. Ysoserial JAR downloaded (v0.0.4-all.jar)
3. Knowledge of target OS commands (Windows here)

## Defense

Defensive measures and detection strategies:

- Disable unsafe deserialization libraries like CommonsCollections
- Use runtime application self-protection (RASP) tools
- Log and alert on deserialization attempts with anomalous gadgets

## Objectives

1. Create executable payload for RCE
2. Ensure compatibility with target gadget chain
3. Output serialized data for delivery

## Instructions

### Step 1: Run Ysoserial Command

**Context**: Generate the payload using the CommonsCollections1 chain for cmd.exe execution.

**Command** ([[commands/ysoserial-generate-commonscollections-cmd]]):
```bash
java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'cmd.exe' > serialdata
```

> This command invokes ysoserial with the specified gadget and command, redirecting binary output to serialdata. Expected: No console output; file contains ~1KB binary data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell

### Sub-Techniques


## Commands Used

- [[commands/ysoserial-generate-commonscollections-cmd]]

## Tools Used

- [[tools/ysoserial]]

## Tags

- rce
- deserialization
