---
tags:
  - dos
  - assertion-failure
  - mruby
  - decimal
type: attack_chain
tools:
  - '[[tools/GDB]]'
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
commands: []
platforms:
  - Linux
complexity: low
procedures:
  - '[[procedures/Create-mruby-Decimal-Object]]'
  - '[[procedures/Initialize-Decimal-with-Itself-for-Crash]]'
  - '[[procedures/Debug-mruby-Crash-with-GDB]]'
step_count: 3
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Endpoint Denial of Service]]'
description: >-
  Multi-stage attack chain exploiting an assertion failure in mruby's Decimal
  class to cause a denial of service crash
skill_level: beginner
impact_level: medium
id: b7479392-fdca-41d3-ace7-a9777c539da2
created_at: '2025-12-11T03:47:48.087Z'
updated_at: '2025-12-11T03:47:48.087Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1203]]'
  - '[[T1499]]'
---
# mruby Decimal Self-Initialization Assertion Failure Leading to Denial of Service

Multi-stage attack chain demonstrating a complete workflow to exploit an assertion failure in the mruby Decimal class by initializing an instance with itself, causing a program crash and denial of service. This vulnerability affects the mruby-mpdecimal library, leading to an empty mpd_t structure access during to_s calls. A patch was deployed to return self in such cases.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Decimal Object] --> B[Self-Initialize for Crash]
    B --> C[Debug Crash]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/GDB]]
- #mirb

### Target Environment

- Linux platform
- mruby and mruby-mpdecimal installed
- No specific services or ports required

### Initial Access Requirements

- Local access to run mirb interactive shell
- No credentials or network position needed

## Detailed Attack Procedures

### Step 1: Create Decimal Object - [[procedures/Create-mruby-Decimal-Object]]

**Procedure**: [[procedures/Create-mruby-Decimal-Object]]

**Objective**: Instantiate a new Decimal object in the mruby environment to set up for the self-initialization exploit.

**Expected Output**: A new Decimal object is created without errors.

**Success Indicators**:
- Decimal object 'a' is successfully instantiated
- No immediate crash occurs

First, launch mirb and create the object using [[commands/decimal-new]]:

```bash
a = Decimal.new
```

This instantiates the Decimal class with no arguments.

### Step 2: Self-Initialize for Crash - [[procedures/Initialize-Decimal-with-Itself-for-Crash]]

**Procedure**: [[procedures/Initialize-Decimal-with-Itself-for-Crash]]

**Objective**: Call the initialize method on the Decimal object with itself as the argument to trigger the assertion failure and crash.

**Expected Output**: The application crashes with SIGABRT due to assertion failure in mpd_msword.

**Success Indicators**:
- Assertion failure is triggered
- Program exits with denial of service

Execute [[commands/decimal-initialize-self]] to trigger the vulnerability:

```bash
a.initialize a
```

This creates an empty mpd_t structure and attempts access via to_s, causing the crash.

### Step 3: Debug Crash - [[procedures/Debug-mruby-Crash-with-GDB]]

**Procedure**: [[procedures/Debug-mruby-Crash-with-GDB]]

**Objective**: Attach GDB to the mirb process to analyze the crash, including backtrace and register inspection.

**Expected Output**: GDB captures the SIGABRT, providing backtrace and register details showing the assertion in mpd_msword.

**Success Indicators**:
- GDB attaches successfully
- Backtrace confirms the root cause in Decimal.initialize

Attach to the process using [[commands/gdb-attach]] (replace 10251 with actual PID):

```bash
gdb attach 10251
```

Continue execution with [[commands/gdb-continue]]:

```bash
c
```

Inspect the backtrace with [[commands/gdb-backtrace]]:

```bash
bt
```

View registers with [[commands/gdb-info-registers]]:

```bash
info registers
```

## Attack Chain Summary

### Key Achievements

1. Successful instantiation of vulnerable Decimal object
2. Triggered assertion failure leading to DoS
3. Detailed crash analysis via debugging

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]]
- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Impact]]

*Last updated: 2023-10-01*
