---
id: ac-mruby-dos-instanceexec
tags:
  - dos
  - null-pointer
  - mruby
  - shopify
  - vulnerability-exploit
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - mruby
  - Shopify Scripts
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Analyze-mruby-Source-Code-for-Null-target-class-Issue]]'
  - '[[procedures/Exploit-mruby-instance-exec-with-Class-Definition-for-DoS]]'
step_count: 2
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:26:48.387Z'
description: >-
  Attack chain exploiting a null pointer dereference in mruby's
  Object#instance_exec method to crash the VM in Shopify Scripts environment,
  resulting in denial of service.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Command-Line Interface]]'
---
# mruby Null Pointer Dereference DoS in Shopify Scripts via instance_exec

Multi-stage attack chain demonstrating the exploitation of a null pointer dereference vulnerability in mruby's Object#instance_exec method, leading to a crash of the scripting VM used in Shopify Scripts. This DoS attack disrupts the scripting environment by causing a segfault when attempting to define a class within an instance_exec block on certain objects like Fixnum.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Source Code Analysis] --> B[Exploit Execution]
    B --> C[VM Crash and DoS]

    style A fill:#f39c12
    style B fill:#e74c3c
    style C fill:#e74c3c
```

## Prerequisites & Requirements

### Required Tools

- mruby interpreter or Shopify Scripts environment access
- Source code access to mruby (e.g., via git clone)

### Target Environment

- mruby VM (version prior to fix)
- Shopify Scripts platform
- Embedded Ruby environment

### Initial Access Requirements

- Access to execute scripts in Shopify Scripts
- Ability to analyze mruby source code
- No network access required; local or controlled environment

## Detailed Attack Procedures

### Step 1: Source Code Analysis
procedure: [[procedures/Analyze-mruby-Source-Code-for-Null-target-class-Issue]]

**Objective**: Identify the null pointer dereference vulnerability in the Object#instance_exec method by reviewing the mruby source code.

**Instructions**: Clone the mruby repository and examine the relevant file in mrbgems/mruby-object-ext/src/object.c. Look for the logic in instance_exec where the VM's target_class is set to NULL on singleton class creation failure, and note the lack of null checks in subsequent opcodes like OP_CLASS and OP_MODULE.

**Expected Output**: Confirmation of the vulnerability through code review, highlighting the unsafe dereference.

**Success Indicators**:
- Identified target_class set to NULL without validation
- Noted opcode assumptions of non-null pointer

### Step 2: Exploit Execution
procedure: [[procedures/Exploit-mruby-instance-exec-with-Class-Definition-for-DoS]]

**Objective**: Trigger the null pointer dereference by executing a Ruby block via instance_exec that defines a class, causing a segfault and VM crash.

**Instructions**: In the mruby environment or Shopify Scripts, execute the Ruby code using [[commands/mruby-instance-exec-class-definition]] to run the block on a Fixnum object like 1, which fails singleton class creation and leads to the dereference.

```ruby
1.instance_exec { class X; end }
```

**Expected Output**: Segfault or immediate crash of the mruby VM.

**Success Indicators**:
- VM crashes with null pointer dereference error
- Denial of service confirmed in scripting environment

## Attack Chain Summary

### Key Achievements

1. Discovered null pointer vulnerability through static code analysis
2. Demonstrated reliable DoS via simple Ruby script execution
3. Highlighted impact on Shopify Scripts VM stability

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Command-Line Interface]] Command and Scripting Interpreter

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
