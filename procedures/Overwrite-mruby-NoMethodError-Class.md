---
id: 2855d84e-9e8a-438f-995c-ed0451092c15
name: Overwrite mruby NoMethodError Class
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:39.191Z'
updated_at: '2025-12-11T03:47:39.191Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
sub_techniques: []
tags:
  - mruby
  - overwrite
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

# Overwrite mruby NoMethodError Class

## Summary

This procedure overwrites the NoMethodError class in mruby with a builtin class like Fixnum, setting up a vulnerability that causes infinite recursion and crashes when an undefined method is called.

## Description

In mruby, assigning NoMethodError = Fixnum replaces the error class with one lacking a 'new' method. When an undefined method is invoked, the error handling attempts to instantiate this class, leading to infinite recursion, stack overflow, and segmentation faults. This can be exploited for denial of service, as seen in crashing web applications like mruby.science.

## Requirements

1. Access to execute mruby scripts (local or via web app)
2. mruby environment installed
3. Script file to modify (e.g., fixnum_exception.mrb)

## Defense

Defensive measures and detection strategies:

- Restrict class overwriting in scripting environments
- Monitor for unexpected crashes in error handling code

## Objectives

1. Prepare the mruby environment for crash exploitation
2. Set up conditions for memory corruption
3. Enable denial of service attacks

## Instructions

### Step 1: Assign Overwrite in Script

**Context**: Modify the mruby script to perform the class overwrite.

> Assign NoMethodError = Fixnum in the script code.

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
- #overwrite
