---
tags:
  - uaf
  - mruby
  - array-setup
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/mruby-dos-poc]]'
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 0a6751e7-6ab4-427f-8166-29fc6b78a53a
created_at: '2025-12-14T17:26:48.778Z'
updated_at: '2025-12-14T17:26:48.778Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Setup-Global-Array-with-Malicious-Object

## Summary

This procedure initializes a global array in mruby containing an instance of the custom malicious class, positioning the object to invoke the faulty to_ary during Array#to_h iteration.

## Description

The global array $a is set to contain A.new, ensuring that when to_h is called, the iteration reaches the element and triggers to_ary, which clears $a (freeing memory and nulling ptr). This step is innocuous on its own but critical for chaining to the trigger, occurring in the mruby Ruby execution environment without requiring external access.

## Requirements

1. mruby runtime with class A already defined from prior procedure.
2. Permission to assign global variables.
3. No special privileges needed.

## Defense

Defensive measures and detection strategies:

- Sanitize inputs to Array#to_h to prevent custom to_ary overrides.
- Log array modifications during conversions.
- Use mruby's safe mode to restrict global variable access.

## Objectives

1. Create array with malicious element for UAF setup.
2. Maintain array integrity until trigger.
3. Prepare for DoS or corruption exploitation.

## Instructions

### Step 1: Initialize Global Array

**Context**: Assign [A.new] to $a, making the malicious object the sole or key element.

**Command** ([[commands/mruby-dos-poc]]):
```ruby
$a = [A.new]
```

> Sets up $a with length 1. Expected output: Array created; inspect with $a.length == 1.

### Step 2: Confirm Setup

**Context**: Verify the array holds the instance without invoking methods.

**Command** (inspection):
```ruby
p $a[0].class # Should show A
```

> Expected: Outputs A; confirms malicious object in place.

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
- global-array
- mruby
