---
tags:
  - primitive
  - rce
  - mruby
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - mruby
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 3ac070ca-7806-479f-aed9-a9f49f838189
created_at: '2025-12-11T03:47:56.799Z'
updated_at: '2025-12-11T03:47:56.799Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Develop Arbitrary Read Write Primitive in mruby

## Summary

This procedure develops an arbitrary read/write primitive using the type confusion in mruby, enabling manipulation of internal data structures for full RCE.

## Description

Extend the PoC by implementing read and write operations via similar exploitation techniques. Demonstrate with functions like puts to show data manipulation in mruby, paving the way for arbitrary code execution and data disclosure.

## Requirements

1. Existing PoC for IP control
2. mruby test environment
3. Scripting knowledge to implement primitives

## Defense

Defensive measures and detection strategies:

- Update mruby to mitigate type confusion
- Implement runtime integrity checks for memory operations

## Objectives

1. Achieve arbitrary memory read/write
2. Manipulate internal structures
3. Enable full RCE capabilities

## Instructions

### Step 1: Extend PoC for Read/Write

**Context**: Modify the script to include read and write operations using type confusion.

> Implement primitives and test with simple data manipulation like outputting modified values via puts.

### Step 2: Validate Primitive

**Context**: Test the primitive in mruby to confirm arbitrary access.

> Execute and observe successful read/write without crashes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- primitive
- rce
- mruby
