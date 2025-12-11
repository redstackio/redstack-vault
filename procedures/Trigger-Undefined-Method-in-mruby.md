---
id: e0453199-b0dc-4671-853a-e1b5a7f0ba2c
name: Trigger Undefined Method in mruby
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:39.189Z'
updated_at: '2025-12-11T03:47:39.189Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
sub_techniques: []
tags:
  - mruby
  - trigger
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
mitre_techniques:
  - '[[T1059]]'
---

# Trigger Undefined Method in mruby

## Summary

This procedure triggers an undefined method in mruby after class overwrite, causing the vulnerable error handling to activate and lead to a crash.

## Description

After overwriting NoMethodError, calling an undefined method like 'boom!' attempts to create a new instance of the overwritten class, resulting in infinite recursion due to missing 'new' method, ultimately causing stack overflow and memory corruption.

## Requirements

1. mruby script with class overwrite already set
2. Execution environment ready
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Implement safe error handling in mruby
- Log and alert on undefined method calls

## Objectives

1. Activate the vulnerability
2. Induce infinite recursion
3. Achieve application crash

## Instructions

### Step 1: Invoke Undefined Method

**Context**: Add code to call a non-existent method.

> Invoke 'boom!' in the script, triggering error handling.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[commands/sandbox-run-mruby-script]]
- #trigger
