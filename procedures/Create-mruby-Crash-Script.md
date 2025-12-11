---
tags:
  - buffer-overflow
  - mruby
type: procedure
tools:
  - '[[tools/ASAN]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - macOS
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 245337c9-832c-4464-85de-e7fa7df7f02b
created_at: '2025-12-11T03:47:48.033Z'
updated_at: '2025-12-11T03:47:48.033Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1203]]'
---
# Create mruby Crash Script

## Summary

This procedure creates a Ruby script that exploits a buffer overflow in mruby by instantiating a Time object with extreme negative second values, triggering a crash when to_s is called during error handling.

## Description

The script uses an invalid Time.new call with a large negative value, causing a NoMethodError that invokes mrb_time_asctime, leading to buffer overflow and segmentation faults or invalid outputs. This is useful for demonstrating denial of service in mruby-based applications.

## Requirements

1. Access to a text editor to create the script
2. mruby environment for later execution
3. Knowledge of basic Ruby syntax

## Defense

Defensive measures and detection strategies:

- Implement input validation on Time object creation
- Monitor for segmentation faults in mruby processes

## Objectives

1. Create a script that reliably triggers the vulnerability
2. Demonstrate potential for DoS attacks
3. Prepare for debugging and patching

## Instructions

### Step 1: Write the Crash Script

**Context**: Define the Ruby code that creates an invalid Time object and triggers an error.

**Command** ([[commands/time-new-crash]]):
```ruby
Time.new(-0XD00000000000000) & 0
```

> This code attempts to create a Time with extreme negative seconds, then performs an invalid operation to raise NoMethodError, calling the vulnerable function.

Save the code to a file named 'crash.rb'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used

- [[commands/time-new-crash]]

## Tools Used

- #mruby

## Tags

- #buffer-overflow
- #mruby
