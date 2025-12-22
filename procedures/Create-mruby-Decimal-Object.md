---
tags:
  - mruby
  - decimal
  - setup
type: procedure
tools:
  - '[[tools/GDB]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 9684a9bd-52a6-4d8c-aac1-08f5fa21a69c
created_at: '2025-12-11T03:47:48.076Z'
updated_at: '2025-12-11T03:47:48.076Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1203]]'
---
# Create mruby Decimal Object

## Summary

This procedure creates a new instance of the Decimal class in an mruby environment, setting up the object for further manipulation such as self-initialization to exploit vulnerabilities.

## Description

In mruby with mruby-mpdecimal, instantiating a Decimal object with no arguments prepares the object for method calls. This is the initial step in exploiting assertion failures by ensuring an instance exists to call initialize on. The procedure targets Linux environments running mruby and is used in denial of service attack chains.

## Requirements

1. Access to mirb interactive shell
2. mruby and mruby-mpdecimal libraries installed
3. Linux platform

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected mruby process crashes via logging
- Apply patches to mruby-mpdecimal to handle self-initialization gracefully

## Objectives

1. Create a Decimal instance without crashing
2. Prepare for vulnerability exploitation
3. Verify object creation in interactive shell

## Instructions

### Step 1: Launch mirb and Create Object

**Context**: Start the interactive mruby shell and instantiate the Decimal class.

**Command** ([[commands/decimal-new]]):
```bash
a = Decimal.new
```

> This command creates a new Decimal object with no arguments, returning the instance for further use.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used

- [[commands/decimal-new]]

## Tools Used

- #mirb

## Tags

- [[procedures/Create-mruby-Decimal-Object]]
- [[commands/decimal-new]]
- #setup
