---
id: 4457ea25-e0c9-4e4e-81cb-0b7ced62f326
name: Test Alternative Nil Method POC in mruby
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:47.948Z'
updated_at: '2025-12-11T03:47:47.948Z'
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Endpoint Denial of Service]]'
sub_techniques: []
tags:
  - mruby
  - recursion
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

# Test Alternative Nil Method POC in mruby

## Summary

This procedure tests an alternative POC by defining a recursive method on nil with an ensure block to trigger stack overflow in mruby.

## Description

The script exploits recursion in ensure blocks, causing deep C-level calls and segfault. It crashes mruby but may not affect sandbox. Aimed at confirming the root cause in method definitions.

## Requirements

1. mruby installed
2. nil_method_ensure.rb script prepared

## Defense

Defensive measures and detection strategies:

- Update mruby to limit recursion
- Detect anomalous method definitions in scripts

## Objectives

1. Validate recursion via nil method
2. Cause process crash

## Instructions

### Step 1: Execute the Script

**Context**: Run the alternative POC.

**Command** ([[commands/mruby-nil-method-ensure]]):
```bash
mruby nil_method_ensure.rb
```

> This defines recursion in ensure block, leading to segfault.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Impact]] Impact

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/mruby-nil-method-ensure]]

## Tools Used

- #mruby

## Tags

- #recursion
- #dos
