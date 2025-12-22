---
id: ee044b8d-5bf2-48e0-919b-b6aae49eb375
name: mruby C-Level Recursion Stack Overflow via Recursive Ruby Methods
type: attack_chain
description: >-
  Exploits lack of C-level recursion limits in mruby to cause stack overflow and
  denial of service through crafted Ruby scripts
verified: false
submitted: true
step_count: 4
created_at: '2025-12-11T03:47:47.961Z'
updated_at: '2025-12-11T03:47:47.961Z'
procedures:
  - '[[procedures/Save-and-Prepare-Recursive-Ruby-POC-Script]]'
  - '[[procedures/Execute-Script-in-mruby-to-Trigger-Stack-Overflow]]'
  - '[[procedures/Test-Alternative-Nil-Method-POC-in-mruby]]'
  - '[[procedures/Test-Alternative-Module-New-POC-in-mruby]]'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Endpoint Denial of Service]]'
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
tags:
  - mruby
  - stack-overflow
  - dos
  - recursion
  - ruby
platforms:
  - Linux
  - macOS
tools: []
commands: []
complexity: low
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1203]]'
  - '[[T1499]]'
---

# mruby C-Level Recursion Stack Overflow via Recursive Ruby Methods

Multi-stage attack chain demonstrating how to exploit C-level recursion vulnerabilities in mruby by crafting recursive Ruby methods, leading to process stack overflow and segmentation fault without triggering Ruby's built-in stack limits. This results in a denial of service by crashing the mruby process or sandbox environment.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare POC Script] --> B[Execute in mruby/Sandbox]
    B --> C[Test Nil Method POC]
    C --> D[Test Module New POC]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- #mruby
- #sandbox

### Target Environment

- Linux or macOS
- mruby interpreter (commit b84e005fc36a3c669586cc66ab3c87630d7a5509 or similar)
- Sandbox environment with default limits (4 MB, 100ms, 100k instructions)

### Initial Access Requirements

- Local access to run mruby or sandbox
- Ability to create and execute Ruby scripts

## Detailed Attack Procedures

### Step 1: Prepare POC Script - [[procedures/Save-and-Prepare-Recursive-Ruby-POC-Script]]

**Procedure**: [[procedures/Save-and-Prepare-Recursive-Ruby-POC-Script]]

**Objective**: Create a proof-of-concept Ruby script that induces C-level recursion in mruby via method redefinition and string multiplication.

**Expected Output**: A file named recursive_to_i.rb containing the recursive code.

**Success Indicators**:
- Script file is created successfully
- Code defines a recursive to_i method without syntax errors

### Step 2: Execute in mruby or Sandbox - [[procedures/Execute-Script-in-mruby-to-Trigger-Stack-Overflow]]

**Procedure**: [[procedures/Execute-Script-in-mruby-to-Trigger-Stack-Overflow]]

**Objective**: Run the prepared script in mruby or sandbox to trigger the stack overflow and cause a segmentation fault.

**Expected Output**: Process crashes with segmentation fault.

First, execute using [[commands/mruby-recursive-to-i]]:

```bash
mruby recursive_to_i.rb
```

Then, test in sandbox using [[commands/sandbox-recursive-to-i]]:

```bash
sandbox recursive_to_i.rb
```

**Success Indicators**:
- mruby process terminates with segfault
- No Ruby stack overflow exception is raised

### Step 3: Test Nil Method POC - [[procedures/Test-Alternative-Nil-Method-POC-in-mruby]]

**Procedure**: [[procedures/Test-Alternative-Nil-Method-POC-in-mruby]]

**Objective**: Use an alternative POC exploiting recursion in nil method with ensure block to confirm the vulnerability.

**Expected Output**: mruby crashes with segmentation fault.

Execute using [[commands/mruby-nil-method-ensure]]:

```bash
mruby nil_method_ensure.rb
```

**Success Indicators**:
- Crashes mruby but may not affect sandbox
- Deep C-level recursion observed

### Step 4: Test Module New POC - [[procedures/Test-Alternative-Module-New-POC-in-mruby]]

**Procedure**: [[procedures/Test-Alternative-Module-New-POC-in-mruby]]

**Objective**: Use another POC with recursive module creation to validate the stack overflow issue.

**Expected Output**: Segmentation fault in mruby.

Execute using [[commands/mruby-module-new-do]]:

```bash
mruby module_new_do.rb
```

**Success Indicators**:
- Process stack overflow leads to crash
- Confirms lack of recursion depth limits

## Attack Chain Summary

### Key Achievements

1. Demonstrated denial of service via stack overflow in mruby
2. Bypassed Ruby's stack limits by exploiting C-level recursion
3. Validated vulnerability across multiple POC scripts and environments

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Impact]] Impact

---

*Last updated: 2023-10-01*
