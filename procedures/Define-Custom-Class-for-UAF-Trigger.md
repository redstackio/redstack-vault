---
tags:
  - uaf
  - mruby
  - ruby
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/mruby-dos-poc]]'
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a3b2a634-a372-446a-8d7f-56f045ce0ada
created_at: '2025-12-14T17:26:48.781Z'
updated_at: '2025-12-14T17:26:48.781Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Define-Custom-Class-for-UAF-Trigger

## Summary

This procedure defines a custom Ruby class in mruby that overrides the to_ary method to clear a global array during conversion, setting up the use-after-free condition in Array#to_h without immediate detection.

## Description

In the mruby environment, the vulnerability arises because mrb_ary_to_h does not recheck the array length after calling to_ary on elements, allowing modifications like array.clear() to nullify the pointer (ptr). This procedure creates class A where to_ary executes $a.clear and returns nil, triggering an exception in mrb_ary_to_h that leads to out-of-bounds access on the freed memory. It is the foundational step for both DoS and advanced exploitation, requiring mruby execution context.

## Requirements

1. Access to mruby interpreter or embedded runtime.
2. Ability to execute Ruby code snippets.
3. Global variable $a must be accessible for later steps.

## Defense

Defensive measures and detection strategies:

- Patch mruby to version fixing CVE or add length checks in mrb_ary_to_h.
- Use AddressSanitizer (ASan) in builds to detect UAF at runtime.
- Monitor for crashes in mruby processes and audit custom class definitions.

## Objectives

1. Establish malicious to_ary override to modify array during iteration.
2. Prepare for UAF trigger without alerting defenses.
3. Enable subsequent array setup for exploitation.

## Instructions

### Step 1: Define the Custom Class

**Context**: Override to_ary in class A to clear the target array and return a non-array value, forcing exception handling that accesses freed memory.

**Command** ([[commands/mruby-dos-poc]]):
```ruby
class A; def to_ary; $a.clear; nil; end; end
```

> This defines class A. Expected output: No errors; class is ready. Verify with A.new succeeding.

### Step 2: Verify Class Behavior

**Context**: Test the override indirectly by checking if $a.clear would affect a sample array, but defer full trigger.

**Command** (manual check):
```ruby
$a = [1,2]; obj = A.new; # Simulate but don't call to_ary yet
```

> Ensures setup; expected: Array intact until to_ary invoked.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/mruby-dos-poc]]

## Tools Used


## Tags

- uaf
- mruby
- custom-class
