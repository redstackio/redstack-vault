---
id: a73e56ba-6b49-45b7-815b-c3af3e660c6e
name: mruby NoMethodError Overwrite to Cause Crash and Denial of Service
type: attack_chain
description: >-
  Exploitation of mruby vulnerability by overwriting NoMethodError class to
  trigger crashes and potential DoS
verified: false
submitted: true
step_count: 4
created_at: '2025-12-11T03:47:39.194Z'
updated_at: '2025-12-11T03:47:39.194Z'
procedures:
  - '[[procedures/Overwrite-mruby-NoMethodError-Class]]'
  - '[[procedures/Trigger-Undefined-Method-in-mruby]]'
  - '[[procedures/Execute-mruby-Script-in-Sandbox]]'
  - '[[procedures/Debug-mruby-Crash-with-GDB]]'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Endpoint Denial of Service]]'
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
tags:
  - mruby
  - crash
  - dos
  - memory-corruption
platforms:
  - Linux
tools: []
commands: []
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1059]]'
  - '[[T1499]]'
---

# mruby NoMethodError Overwrite to Cause Crash and Denial of Service

Multi-stage attack chain demonstrating exploitation of a vulnerability in mruby by overwriting the NoMethodError class, leading to crashes, memory corruption, and potential denial of service attacks on affected systems like web applications.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Overwrite Error Class] --> B[Trigger Error]
    B --> C[Run in Sandbox]
    C --> D[Debug Crash]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- #sandbox
- #gdb

### Target Environment

- Linux platform
- mruby-engine service running
- mruby and Ruby 2.3.3 tech stack

### Initial Access Requirements

- Ability to execute mruby scripts (e.g., via web application or local access)
- No specific credentials needed for local reproduction
- Network access not required for local testing

## Detailed Attack Procedures

### Step 1: Overwrite Error Class - [[procedures/Overwrite-mruby-NoMethodError-Class]]

**Procedure**: [[procedures/Overwrite-mruby-NoMethodError-Class]]

**Objective**: Overwrite the NoMethodError class with a builtin class like Fixnum to set up the vulnerability.

**Expected Output**: Successful assignment without immediate errors.

**Success Indicators**:
- NoMethodError is reassigned to Fixnum
- Script continues without crashing at this stage

First, in your mruby script, assign NoMethodError = Fixnum.

### Step 2: Trigger Undefined Method - [[procedures/Trigger-Undefined-Method-in-mruby]]

**Procedure**: [[procedures/Trigger-Undefined-Method-in-mruby]]

**Objective**: Invoke an undefined method to trigger the overwritten error handling.

**Expected Output**: Attempts to instantiate the error, leading to infinite recursion.

**Success Indicators**:
- Error handling is triggered
- Leads to potential stack overflow

In the script, invoke an undefined method like 'boom!'.

### Step 3: Execute in Sandbox - [[procedures/Execute-mruby-Script-in-Sandbox]]

**Procedure**: [[procedures/Execute-mruby-Script-in-Sandbox]]

**Objective**: Run the malicious script in a sandboxed environment to observe the crash.

**Expected Output**: Segmentation fault or engine time quota error.

**Success Indicators**:
- Application crashes
- Denial of service observed (e.g., website temporarily broken)

Use [[commands/sandbox-run-mruby-script]] to execute the script:

```bash
bin/sandbox new_crashes/fixnum_exception.mrb
```

Validate by checking for crash logs or segmentation faults.

### Step 4: Debug Crash - [[procedures/Debug-mruby-Crash-with-GDB]]

**Procedure**: [[procedures/Debug-mruby-Crash-with-GDB]]

**Objective**: Attach a debugger to analyze the crash and confirm memory corruption.

**Expected Output**: Backtrace showing infinite recursion and register dumps.

**Success Indicators**:
- GDB captures SIGSEGV
- Backtrace reveals stack overflow in error handling

Attach GDB using [[commands/gdb-attach-process]]:

```bash
gdb attach 5534
```

Then continue with [[commands/gdb-continue-execution]]:

```bash
c
```

Print backtrace with [[commands/gdb-print-backtrace]]:

```bash
bt
```

And get registers with [[commands/gdb-info-registers]]:

```bash
info registers
```

## Attack Chain Summary

### Key Achievements

1. Successful overwrite of error class leading to vulnerable state
2. Triggering of crash via undefined method invocation
3. Reproduction in sandbox confirming DoS potential
4. Detailed debugging to verify memory corruption

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Command-Line Interface]]
- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Impact]]

---

*Last updated: [TIMESTAMP]*
