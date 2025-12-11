---
tags:
  - dos
  - mruby
  - segmentation-fault
  - ruby
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - mruby
  - Ruby
  - C
complexity: low
procedures:
  - '[[procedures/Create-mruby-Crash-Script]]'
  - '[[procedures/Execute-mruby-Crash-Script]]'
step_count: 2
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Application or System Exploitation]]'
description: >-
  Exploitation of a vulnerability in mruby's argument handling leading to
  segmentation fault and potential denial of service
skill_level: beginner
impact_level: medium
id: 466e5dcc-6936-40af-96be-3f2a914dc3c5
created_at: '2025-12-11T03:47:47.914Z'
updated_at: '2025-12-11T03:47:47.914Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1499]]'
  - '[[T1499.004]]'
---
# mruby Denial of Service via Excessive Method Arguments

Multi-stage attack chain demonstrating exploitation of a logic error in mruby's gen_values function, causing a segmentation fault when a method is called with exactly 127 arguments, enabling denial of service attacks.

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
    A[Create Crash Script] --> B[Execute Script]
    B --> C[Trigger Segfault]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- #mruby
- #sandbox

### Target Environment

- mruby or mruby_engine environment
- No specific ports required
- Local access to run scripts

### Initial Access Requirements

- Ability to execute Ruby scripts in the target mruby environment
- No credentials needed
- Local or embedded system access

## Detailed Attack Procedures

### Step 1: Prepare Exploit Script - [[procedures/Create-mruby-Crash-Script]]

**Procedure**: [[procedures/Create-mruby-Crash-Script]]

**Objective**: Create a Ruby script that defines a method call with exactly 127 arguments to trigger the vulnerability.

**Expected Output**: A file named crash.rb containing the exploit code.

First, create the script file crash.rb with the following content:

```ruby
def x(a1, a2, a3, ..., a127) # Use line continuations for 127 arguments, all set to 0
end
x(0, 0, 0, ..., 0) # Call with exactly 127 zeros
```

**Success Indicators**:
- Script file is saved successfully
- The script contains a method call with precisely 127 arguments

### Step 2: Trigger Vulnerability - [[procedures/Execute-mruby-Crash-Script]]

**Procedure**: [[procedures/Execute-mruby-Crash-Script]]

**Objective**: Run the exploit script in mruby or sandbox to cause a segmentation fault.

**Expected Output**: Segmentation fault error from mruby or sandbox.

Execute the script using [[commands/mruby-run-script]]:

```bash
mruby crash.rb
```

Alternatively, use [[commands/sandbox-run-script]]:

```bash
sandbox crash.rb
```

This triggers the logic error in gen_values, leading to a null pointer dereference in array.c.

**Success Indicators**:
- mruby crashes with segmentation fault
- Denial of service achieved on the mruby process

## Attack Chain Summary

### Key Achievements

1. Creation of exploit script targeting mruby's argument limit
2. Successful crash of mruby interpreter
3. Demonstration of denial of service potential

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]
- [[Application or System Exploitation]]

### MITRE ATT&CK Tactics

- [[Impact]]

*Last updated: [TIMESTAMP]*
