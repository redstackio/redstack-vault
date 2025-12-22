---
tags:
  - mruby
  - segfault
  - dos
type: procedure
tools:
  - '[[tools/MRubyEngine]]'
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
commands:
  - '[[commands/(1..2)-dup-to_s]]'
  - '[[commands/mrubyengine-sandbox-eval-exploit]]'
platforms:
  - Ruby
  - mruby
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 91b55f33-fa1e-4550-8021-ff70d54fbe60
created_at: '2025-12-11T03:47:48.393Z'
updated_at: '2025-12-11T03:47:48.393Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1499]]'
---
# Duplicate Range Object and Trigger Segfault

## Summary

This procedure creates a Range object in mruby, duplicates it after method removal, and calls a method to trigger a null pointer dereference, resulting in a segfault and process crash for denial of service.

## Description

Following the removal of initialize_copy, duplicating a Range object allocates memory without initialization. Calling methods like to_s on this object dereferences a null pointer, crashing the process. This exploits a vulnerability in mruby's object handling, applicable in sandboxes like MRubyEngine, leading to high-impact DoS in services like shopify-scripts.

## Requirements

1. Prior removal of initialize_copy method
2. Ruby/mruby execution environment
3. Access to create and manipulate Range objects

## Defense

Defensive measures and detection strategies:

- Patch mruby to handle internal state copying before initialize_copy
- Monitor for segfaults and unusual object duplications in logs

## Objectives

1. Create uninitialized Range object via duplication
2. Trigger segfault through method call
3. Achieve denial of service via process crash

## Instructions

### Step 1: Duplicate and Call Method

**Context**: Duplicate the Range and invoke to_s to cause the crash.

**Command** ([[commands/(1..2)-dup-to_s]]):
```ruby
(1..2).dup.to_s
```

> This allocates an uninitialized object and attempts to convert it to string, leading to null pointer dereference. Expected output: Segfault and process termination.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used

- [[commands/(1..2)-dup-to_s]]

## Tools Used



## Tags

- #mruby
- #segfault
- #dos
