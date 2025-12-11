---
id: b86af473-2e61-465f-abc5-ca1d0ef1c45d
name: Execute Script in mruby to Trigger Stack Overflow
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:47.953Z'
updated_at: '2025-12-11T03:47:47.953Z'
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Endpoint Denial of Service]]'
sub_techniques: []
tags:
  - mruby
  - stack-overflow
  - dos
commands: []
platforms:
  - Linux
  - macOS
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1203]]'
  - '[[T1499]]'
---

# Execute Script in mruby to Trigger Stack Overflow

## Summary

This procedure executes a prepared recursive Ruby script in mruby or sandbox to induce a C-level stack overflow, causing a segmentation fault and denial of service.

## Description

By running the script, the attacker exploits the vulnerability in mruby's object.c (around line 561 for to_i), where recursion depth isn't limited at the C level. This crashes the process without hitting Ruby's stack limits. Targeted at mruby on Linux/macOS, expected outcome is a segfault.

## Requirements

1. mruby interpreter installed
2. Sandbox environment set up
3. Prepared recursive_to_i.rb script

## Defense

Defensive measures and detection strategies:

- Patch mruby to include recursion depth checks
- Monitor for segfaults in logs and restrict untrusted script execution

## Objectives

1. Trigger stack overflow in mruby
2. Achieve denial of service
3. Validate exploit in sandbox

## Instructions

### Step 1: Run in mruby

**Context**: Execute the script to cause recursion and crash.

**Command** ([[commands/mruby-recursive-to-i]]):
```bash
mruby recursive_to_i.rb
```

> This runs the script in vanilla mruby, leading to segfault.

### Step 2: Run in Sandbox

**Context**: Test in sandboxed environment.

**Command** ([[commands/sandbox-recursive-to-i]]):
```bash
sandbox recursive_to_i.rb
```

> This demonstrates the vulnerability in a limited environment, still causing crash.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Impact]] Impact

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/mruby-recursive-to-i]]
- [[commands/sandbox-recursive-to-i]]

## Tools Used

- #mruby
- #sandbox

## Tags

- #stack-overflow
- #dos
