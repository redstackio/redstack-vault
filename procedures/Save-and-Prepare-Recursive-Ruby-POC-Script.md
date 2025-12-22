---
id: a5c22311-9625-4867-8713-abaa0f48b0da
name: Save and Prepare Recursive Ruby POC Script
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:47.957Z'
updated_at: '2025-12-11T03:47:47.957Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploitation for Client Execution]]'
sub_techniques: []
tags:
  - mruby
  - recursion
  - poc
commands: []
platforms:
  - Linux
  - macOS
tools: []
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1203]]'
---

# Save and Prepare Recursive Ruby POC Script

## Summary

This procedure involves creating and saving a proof-of-concept Ruby script that redefines the to_i method to cause tight C-level recursion in mruby, leading to stack overflow without consuming the Ruby stack.

## Description

The script exploits mruby's lack of C-level recursion depth tracking by using recursive string multiplication with self-reference. This is targeted at mruby interpreters on Linux or macOS, resulting in a segmentation fault and denial of service. Prerequisites include access to a text editor and basic Ruby knowledge.

## Requirements

1. Text editor to create Ruby script
2. Local file system access
3. Understanding of Ruby method redefinition

## Defense

Defensive measures and detection strategies:

- Implement C-level recursion limits in mruby
- Monitor for unexpected process crashes in mruby environments

## Objectives

1. Prepare a POC script for recursion exploit
2. Ensure script induces deep recursion
3. Set up for execution in mruby

## Instructions

### Step 1: Create the Script File

**Context**: Define a recursive to_i method using string multiplication.

Create a file named recursive_to_i.rb with the following content:

```ruby
class Integer
  def to_i
    (self * "x").to_i
  end
end
1.to_i
```

> This code causes recursion by multiplying the integer with a string referencing self, triggering C-level calls.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- #mruby
- #recursion
