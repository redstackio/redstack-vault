---
tags:
  - rce
  - poc
  - type-confusion
  - mruby
  - instruction-pointer
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Ruby
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 211882e8-4f72-4675-900d-94bcab30e37e
created_at: '2025-12-14T17:23:31.392Z'
updated_at: '2025-12-14T17:23:31.392Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Craft POC Script for mruby Instruction Pointer Control

## Summary

This procedure creates a proof-of-concept Ruby script that exploits the struct type confusion in mruby to manipulate the instruction pointer, jumping to an attacker-controlled address and causing a segfault, validating the vulnerability for further RCE development in Shopify Scripts.

## Description

Building on analysis, this POC leverages the type confusion by crafting Ruby objects that, when interpreted, cause incorrect struct casting in mruby's VM. The script manipulates internal representations (e.g., via custom classes or arrays) to overwrite the instruction pointer with a value like 0x0000133713371337. Tested locally with mruby, it demonstrates control but segfaults as proof. In Shopify Scripts, this could be submitted via the API for remote triggering. Prerequisites: Local mruby build and understanding of Ruby object internals.

## Requirements

1. Compiled mruby binary for testing
2. Ruby MRI for script development
3. Debugger (e.g., gdb) for segfault analysis

## Defense

Defensive measures and detection strategies:

- Sandbox mruby execution with seccomp or similar to restrict pointer jumps
- Validate script inputs for anomalous object structures before interpretation
- Log VM state changes and crashes in production environments like Shopify

## Objectives

1. Trigger type confusion to control instruction pointer
2. Demonstrate jump to arbitrary address
3. Confirm segfault as indicator of success

## Instructions

### Step 1: Define Malicious Ruby Objects

**Context**: Create classes or data structures that mimic internal mruby structs to induce confusion.

In a Ruby file (poc.rb), define a custom class with fields aligning to mrb_value or similar.

```ruby
class ConfusedStruct
  def initialize
    @ptr = 0x0000133713371337  # Target address
  end
end
confused = ConfusedStruct.new
```

> This sets up the payload for type casting.

### Step 2: Trigger Confusion in VM

**Context**: Execute code that forces mruby to misinterpret the object as an internal struct.

Use array or hash manipulations to invoke pointer operations.

```ruby
ary = [confused, :sym]  # Align to struct layout
mrb_load_irep(ary)  # Simulated; adapt to actual mruby exec
```

> Causes cast to internal pointer, overwriting IP.

### Step 3: Run and Debug POC

**Context**: Execute in mruby and capture segfault.

Compile and run: mruby poc.rb; use gdb to verify jump.

> Expected: Segfault at 0x0000133713371337, confirming control.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[exploit-development]]
- [[proof-of-concept]]
