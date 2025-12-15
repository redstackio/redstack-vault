---
tags:
  - rce
  - arbitrary-read-write
  - type-confusion
  - mruby
  - memory-manipulation
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
  - '[[Credential Dumping]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 384a2862-aaf3-4ea5-bd61-0cfccf43e104
created_at: '2025-12-14T17:23:31.289Z'
updated_at: '2025-12-14T17:23:31.289Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
  - '[[Credential Dumping]]'
---
# Develop Arbitrary Read/Write Primitive in mruby

## Summary

This procedure extends the POC to implement arbitrary read/write memory primitives using mruby's type confusion, allowing manipulation of internal data structures in the mruby VM and host MRI, enabling full RCE and sensitive data disclosure in Shopify Scripts.

## Description

Using the established instruction pointer control, this builds read/write functions by chaining type confusions to access arbitrary addresses. The primitive reads/writes via pointer arithmetic on confused structs, outputting via 'puts' for validation (limited in production mruby-engine). Targets include mruby's mrb_state or MRI globals for escalation. In Shopify, this facilitates code injection and exfiltration. Prerequisites: Working POC and memory layout knowledge from analysis.

## Requirements

1. Local mruby and MRI environments for testing
2. Hex editor or debugger for address validation
3. Script submission access to Shopify Scripts

## Defense

Defensive measures and detection strategies:

- Enforce memory protections like W^X in mruby embedding
- Runtime type verification with canary values in structs
- Anomaly detection on memory access patterns in script execution logs

## Objectives

1. Achieve arbitrary memory read/write
2. Manipulate VM internal structures
3. Enable RCE and data disclosure

## Instructions

### Step 1: Extend POC for Read Primitive

**Context**: Modify script to read from arbitrary address using confused pointer.

Add a read function leveraging type confusion.

```ruby
def arbitrary_read(addr)
  confused = ConfusedStruct.new
  confused.instance_variable_set(:@target, addr)
  # Trigger cast and deref
  puts confused.inspect  # Output read value
end
arbitrary_read(0xdeadbeef)
```

> Dumps memory at address via inspected struct.

### Step 2: Implement Write Primitive

**Context**: Chain to write data to target address.

Similar setup for overwrite.

```ruby
def arbitrary_write(addr, value)
  confused = ConfusedStruct.new
  confused.instance_variable_set(:@target, addr)
  confused.instance_variable_set(:@data, value)
  # Trigger write via operation
end
arbitrary_write(0xdeadbeef, 0x41414141)
```

> Overwrites memory, altering structures.

### Step 3: Test on Internal Structures

**Context**: Target mruby/MRI internals for validation.

Run in local VM, verify changes with debugger.

> Expected: Successful manipulation, e.g., altered globals leading to code exec.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Credential Dumping]] OS Credential Dumping

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[memory-exploitation]]
- [[primitive-development]]
