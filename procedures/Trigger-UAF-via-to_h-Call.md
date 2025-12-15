---
tags:
  - uaf
  - dos
  - mruby
type: procedure
tools:
  - '[[tools/GDB]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/mruby-dos-poc]]'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Endpoint Denial of Service]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 02556e67-56ef-41ee-b512-bc773e368df6
created_at: '2025-12-14T17:26:48.775Z'
updated_at: '2025-12-14T17:26:48.775Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Endpoint Denial of Service]]'
---
# Trigger-UAF-via-to_h-Call

## Summary

This procedure invokes Array#to_h on the prepared global array to trigger the use-after-free, resulting in a null pointer dereference and process crash for denial of service.

## Description

Calling $a.to_h invokes mrb_ary_to_h, which iterates over elements calling to_ary; the custom implementation clears $a (nulling RARRAY_PTR(ary)), but the loop continues without length recheck, accessing invalid memory in exception handling (e.g., mrb_obj_classname on null). This causes a crash in array.c:130. For verification, attach GDB to the mruby process.

## Requirements

1. mruby process running with $a setup from prior steps.
2. GDB for debugging the crash.
3. Source access to array.c for analysis.

## Defense

Defensive measures and detection strategies:

- Update mruby to patched version rechecking array length post-callback.
- Deploy runtime protections like heap canaries or ASLR.
- Detect crashes via process monitoring and alert on mruby terminations.

## Objectives

1. Cause DoS by null dereference in to_h iteration.
2. Validate UAF for further exploitation potential.
3. Observe crash in GDB for root cause confirmation.

## Instructions

### Step 1: Execute to_h Call

**Context**: Trigger the vulnerability by converting the array to hash, invoking the malicious to_ary.

**Command** ([[commands/mruby-dos-poc]]):
```ruby
class A; def to_ary; $a.clear; nil; end; end; $a=[A.new]; $a.to_h
```

> Full PoC execution. Expected output: Segmentation fault or null access crash.

### Step 2: Debug with GDB

**Context**: Attach GDB to mruby process before execution to trace the fault.

**Command** (GDB usage):
```bash
gdb --args mruby script.rb
(gdb) run
(gdb) bt  # After crash
```

> Expected: Backtrace showing fault in mrb_ary_to_h or RARRAY_PTR access.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/mruby-dos-poc]]

## Tools Used

- [[tools/GDB]]

## Tags

- uaf-trigger
- dos
- gdb-debug
