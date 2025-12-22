---
id: 31f9eb21-b5ba-4d5c-8efb-5c77c443349a
name: Execute mruby Script in Sandbox
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:39.185Z'
updated_at: '2025-12-11T03:47:39.185Z'
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Endpoint Denial of Service]]'
sub_techniques:
  - '[[Application or System Exploitation]]'
tags:
  - mruby
  - sandbox
commands: []
platforms:
  - Linux
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1059]]'
  - '[[T1499]]'
---

# Execute mruby Script in Sandbox

## Summary

This procedure runs the malicious mruby script in a sandboxed environment to safely reproduce and observe the crash.

## Description

Using the sandbox tool, execute the script containing the overwrite and trigger, leading to observable segmentation faults and potential DoS, as demonstrated by breaking the mruby.science website temporarily.

## Requirements

1. Sandbox tool available
2. Script file (e.g., fixnum_exception.mrb)
3. Linux environment with mruby

## Defense

Defensive measures and detection strategies:

- Isolate script execution in sandboxes
- Monitor for engine crashes

## Objectives

1. Reproduce the crash safely
2. Confirm DoS impact
3. Validate exploitation

## Instructions

### Step 1: Run Script in Sandbox

**Context**: Execute the script to trigger the crash.

**Command** ([[commands/sandbox-run-mruby-script]]):
```bash
bin/sandbox new_crashes/fixnum_exception.mrb
```

> This runs the script and should produce a segmentation fault or quota error.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Impact]]

### Techniques

- [[Command-Line Interface]]
- [[Endpoint Denial of Service]]

### Sub-Techniques

- [[Application or System Exploitation]]

## Commands Used

- [[commands/sandbox-run-mruby-script]]

## Tools Used

- #sandbox

## Tags

- [[commands/sandbox-run-mruby-script]]
- #sandbox
