---
tags:
  - mruby
  - ruby
  - type-confusion
  - dos
  - segmentation-fault
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - mruby
  - Ruby
complexity: low
procedures:
  - '[[procedures/Exploit-mruby-Range-Type-Confusion-for-DoS]]'
step_count: 2
techniques:
  - '[[Command-Line Interface]]'
description: >-
  Exploits a type confusion vulnerability in mruby's Range constructor to cause
  a segmentation fault and crash the interpreter
skill_level: beginner
impact_level: medium
id: 5744e1ec-5b67-4f53-be22-af700f040611
created_at: '2025-12-11T03:47:48.649Z'
updated_at: '2025-12-11T03:47:48.649Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# mruby Range Type Confusion Leading to Denial of Service

Multi-stage attack chain demonstrating exploitation of a type confusion vulnerability in mruby's Range constructor, leading to a Denial of Service by crashing the interpreter. This attack redefines the Range class and triggers a segmentation fault through type confusion.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Redefine Range Class] --> B[Trigger Type Confusion]
    B --> C[Denial of Service]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None

### Target Environment

- mruby interpreter
- Ruby-compatible environment (e.g., Shopify Scripts)
- Ability to execute Ruby code

### Initial Access Requirements

- Access to execute code in the mruby environment
- No specific credentials needed
- Local or embedded script execution context

## Detailed Attack Procedures

### Step 1: Redefine Range Class - [[procedures/Exploit-mruby-Range-Type-Confusion-for-DoS]]

**Procedure**: [[procedures/Exploit-mruby-Range-Type-Confusion-for-DoS]]

**Objective**: Override the Range class to point to another class like Array, setting up for type confusion.

**Expected Output**: No visible output; prepares the environment for exploitation.

**Success Indicators**:
- Range constant is successfully redefined without errors
- Subsequent range literals use the redefined class

First, redefine the Range constant using [[commands/redefine-range-to-array]]:

```ruby
Range = Array
```

This exploits runtime constant lookup in mruby.

### Step 2: Trigger Type Confusion and Crash - [[procedures/Exploit-mruby-Range-Type-Confusion-for-DoS]]

**Procedure**: [[procedures/Exploit-mruby-Range-Type-Confusion-for-DoS]]

**Objective**: Create a range object using literal syntax and call an instance method to cause a segmentation fault due to struct field confusion.

**Expected Output**: Segmentation fault, crashing the mruby interpreter.

**Success Indicators**:
- Interpreter crashes with a segfault
- Potential for further RCE exploration (not demonstrated)

Execute [[commands/trigger-range-type-confusion]] to trigger the vulnerability:

```ruby
(1..2).inspect
```

This misinterprets RRange struct fields, leading to the crash.

## Attack Chain Summary

### Key Achievements

1. Successful redefinition of core Range class in mruby
2. Triggering of type confusion leading to DoS
3. Demonstration of vulnerability in mrb_range_new function

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Execution]]

*Last updated: [TIMESTAMP]*
