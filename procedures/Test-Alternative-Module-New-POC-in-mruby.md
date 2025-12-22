---
id: 707455cf-7891-4b16-bcd0-0c17b27c7a67
name: Test Alternative Module New POC in mruby
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:47.943Z'
updated_at: '2025-12-11T03:47:47.943Z'
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

# Test Alternative Module New POC in mruby

## Summary

This procedure uses a POC with recursive module creation to trigger stack overflow in mruby.

## Description

The script creates a new Module with a recursive call, exploiting the vulnerability in Module.new handling. Results in segfault due to unchecked recursion.

## Requirements

1. mruby installed
2. module_new_do.rb script prepared

## Defense

Defensive measures and detection strategies:

- Enforce recursion limits in mruby
- Scan for recursive structures in Ruby code

## Objectives

1. Exploit via module creation
2. Induce denial of service

## Instructions

### Step 1: Execute the Script

**Context**: Run the module creation POC.

**Command** ([[commands/mruby-module-new-do]]):
```bash
mruby module_new_do.rb
```

> This creates recursive modules, causing stack overflow.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Impact]] Impact

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/mruby-module-new-do]]

## Tools Used

- #mruby

## Tags

- #recursion
- #dos
