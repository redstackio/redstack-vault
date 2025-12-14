---
tags:
  - debugging
  - decompile
  - bapp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Desktop
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:24:22.420Z'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques: []
id: 45f9b889-21f2-4820-a1b9-4398829fd77f
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Analyze-JSBeautifier-BApp-for-Root-Cause

## Summary

This procedure enables debug mode in the JSBeautifier BApp, decompiles key functions, and logs async processing to confirm the race condition in HTTP response beautification.

## Description

Within Burp, activate JSBeautifier's debug logging and reproduce bursts from prior steps. Decompile processHttpMessage to reveal calls to jsBeautifierFunctions.beautifyIt without locks, causing interleaving on shared buffers for '<!'-starting JS/HTML. Environment: Burp Suite Extender with BApp loaded. Outcomes: Logs evidencing unsynchronized concurrency, triggered by malformed lengths.

## Requirements

1. JSBeautifier BApp installed in Burp
2. Debug access (file logging enabled)
3. Repro setup from previous procedures

## Defense

Defensive measures and detection strategies:

- Patch BApps or use verified versions
- Implement mutexes in extension code
- Audit logs for race indicators like interleaved timestamps

## Objectives

1. Pinpoint async flaw in beautification
2. Confirm triggers (Content-Length, doctype)
3. Document for reporting

## Instructions

### Step 1: Enable Debug Mode

**Context**: Turn on logging in BApp preferences to capture processing details.

**Command** (Burp GUI):
```bash
# Extender > BApp Store > JSBeautifier > Options > Enable debug mode > Set log file path
```

> Restart Burp if needed; logs to specified file on response processing.

### Step 2: Reproduce and Decompile

**Context**: Run burst repro and review logs/code.

**Command** (Analysis):
```bash
# Use JD-GUI or similar to decompile Burp JAR: Look for processHttpMessage > if (response starts with '<!') > beautifyIt async
```

> Logs show overlapping beautifyIt calls; expected: Evidence of no synchronization primitives.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Disable or Modify Tools]] Impair Defenses: Disable or Modify Tools

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- bapp-analysis
- race-debug
- decompile
