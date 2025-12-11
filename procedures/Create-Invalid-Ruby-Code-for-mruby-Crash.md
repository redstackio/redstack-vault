---
tags:
  - mruby
  - code-generation
  - exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Embedded Ruby
  - Linux
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 1520d158-0780-4fb9-8a32-13e8dedd7b5e
created_at: '2025-12-11T03:47:47.890Z'
updated_at: '2025-12-11T03:47:47.890Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1203]]'
---
# Create Invalid Ruby Code for mruby Crash

## Summary

This procedure involves crafting invalid Ruby code using the ||= operator with constants, break, and while loops to trigger a code generation bug in mruby, leading to invalid bytecode and crashes.

## Description

The attack exploits a vulnerability in mruby's codegen.c where NODE_OP_ASGN handling for ||= with constants inside loops fails to pop the LOOP_RESCUE context, causing incorrect jump offsets. This is used in embedded Ruby environments like Shopify Scripts to cause segfaults or potential RCE.

## Requirements

1. Access to a text editor for writing Ruby code
2. Knowledge of Ruby syntax
3. mruby interpreter for testing

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected crashes in mruby VM
- Validate input scripts for invalid constructs before execution

## Objectives

1. Create code that crashes mruby
2. Demonstrate vulnerability trigger
3. Prepare for further analysis

## Instructions

### Step 1: Write Crashing Code Snippet

**Context**: Construct the minimal invalid code to trigger the bug.

Write and save the following in crash.rb:

```ruby
A ||= break while break
```

> This uses a constant (A), ||=, break, and while loop to cause invalid bytecode generation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used



## Tools Used

- #mruby

## Tags

- #mruby
- [[Exploit]]
