---
tags:
  - mruby
  - ruby
  - method-removal
type: procedure
tools:
  - '[[tools/MRubyEngine]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/(1..2)-dup-to_s]]'
  - '[[commands/mrubyengine-sandbox-eval-exploit]]'
platforms:
  - Ruby
  - mruby
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3176e6bf-1806-4f90-8e81-3bd0c5088f1f
created_at: '2025-12-11T03:47:48.401Z'
updated_at: '2025-12-11T03:47:48.401Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1203]]'
---
# Remove Initialize Copy Method from Range Class

## Summary

This procedure removes the initialize_copy method from mruby's Range class, setting up the conditions for creating uninitialized Range objects that can lead to null pointer dereferences when duplicated and manipulated.

## Description

In mruby environments, the Range class's initialize_copy method is responsible for properly initializing duplicated objects. By removing this method using Ruby's remove_method, subsequent duplications fail to initialize the object, leading to vulnerabilities like segfaults on method calls. This is typically used in exploit chains targeting mruby sandboxes, such as in Shopify's mruby-engine. The procedure requires execution access in a Ruby/mruby runtime and results in a modified class state.

## Requirements

1. Access to a Ruby/mruby interpreter or sandbox
2. Ability to execute arbitrary Ruby code
3. Target environment running mruby, such as shopify-scripts

## Defense

Defensive measures and detection strategies:

- Monitor for method removals or modifications in critical classes like Range
- Implement sandbox restrictions preventing method removal on built-in classes

## Objectives

1. Prevent proper initialization during object duplication
2. Prepare for null pointer dereference exploitation
3. Achieve class modification without detection

## Instructions

### Step 1: Execute Method Removal

**Context**: Remove the initialize_copy method to disable proper duplication handling.

**Command** ([[commands/remove-range-initialize-copy]]):
```ruby
Range.remove_method(:initialize_copy)
```

> This command eliminates the method from the Range class, allowing uninitialized objects to be created on dup calls. Expected output: None, but the method is no longer available.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used

- [[commands/remove-range-initialize-copy]]

## Tools Used



## Tags

- #mruby
- [[Ruby]]
- #method-removal
