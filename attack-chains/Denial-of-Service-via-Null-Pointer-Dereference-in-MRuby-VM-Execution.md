---
id: ac-mruby-dos-nullptr
tags:
  - dos
  - null-pointer-dereference
  - mrbuby
  - ruby
  - segmentation-fault
  - shopify
type: attack_chain
tools:
  - '[[tools/GCC]]'
  - '[[tools/ASAN]]'
  - '[[tools/GDB]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Linux
  - Ruby
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Download-and-Build-MRuby-for-Analysis]]'
  - '[[procedures/Execute-Proof-of-Concept-Script-in-MRuby-Sandbox]]'
  - '[[procedures/Analyze-Crash-Using-GDB-Debugger]]'
step_count: 3
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:26:30.760Z'
description: >-
  A multi-step process to demonstrate and exploit a null pointer dereference
  vulnerability in MRuby's mrb_vm_exec function, leading to a segmentation fault
  and denial of service in Ruby interpreters like those used in Shopify Scripts.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Denial of Service via Null Pointer Dereference in MRuby VM Execution

Multi-stage attack chain demonstrating the exploitation of a null pointer dereference in MRuby's virtual machine execution, resulting in a crash of the Ruby interpreter and potential denial of service in embedded applications like Shopify Scripts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Build and Prepare MRuby] --> B[Execute Malicious Script]
    B --> C[Analyze and Confirm Crash]
    C --> D[Denial of Service Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/GCC]]
- [[tools/ASAN]]
- [[tools/GDB]]

### Target Environment

- Linux x64 platform
- MRuby source code (version as of January 31, 2017)
- Ruby 2.3.1 or compatible interpreter environment

### Initial Access Requirements

- Access to a development environment for building and running MRuby
- No network access required; local sandboxed execution
- Proof-of-concept script (vm_exec.rb) prepared with malicious 'break' statement in NoMethodError context

## Detailed Attack Procedures

### Step 1: Prepare MRuby Environment
procedure: [[procedures/Download-and-Build-MRuby-for-Analysis]]

**Objective**: Download and compile MRuby with debugging tools to enable vulnerability analysis and reproduction.

**Instructions**: Download the MRuby source code and build it using GCC with AddressSanitizer enabled to detect memory issues.

**Expected Output**: Successfully built MRuby binary with ASAN instrumentation, ready for sandboxed execution.

**Success Indicators**:
- Build completes without errors
- ASAN reports no initial memory issues in clean runs

### Step 2: Trigger the Vulnerability
procedure: [[procedures/Execute-Proof-of-Concept-Script-in-MRuby-Sandbox]]

**Objective**: Run a crafted Ruby script in the MRuby sandbox to invoke the null pointer dereference during VM execution.

**Instructions**: Execute the vm_exec.rb script using the sandbox tool, which handles a 'break' statement in a method missing context, leading to improper range object access.

Use [[commands/sandbox-execute-poc]] to run the script:

```bash
./sandbox vm_exec.rb
```

**Expected Output**: Segmentation fault at address 0x00000000000000, with ASAN reporting a null pointer dereference.

**Success Indicators**:
- Interpreter crashes immediately
- Uncontrolled resource consumption observed prior to fault

### Step 3: Confirm Exploitation
procedure: [[procedures/Analyze-Crash-Using-GDB-Debugger]]

**Objective**: Debug the crash to verify the vulnerability location and understand the root cause for potential mitigation or further exploitation.

**Instructions**: Attach GDB to the crashing process and generate a backtrace to pinpoint the null pointer access.

Run [[commands/gdb-backtrace]] within GDB after the segfault:

```bash
bt
```

**Expected Output**: Backtrace showing frames from mrb_vm_exec (vm.c:1592) through method missing handling and range creation.

**Success Indicators**:
- Null pointer confirmed in mrb_vm_exec
- Root cause traced to 'break' handling in NoMethodError contexts

## Attack Chain Summary

### Key Achievements

1. Reproduced a critical null pointer dereference in MRuby VM, causing interpreter crashes
2. Demonstrated DoS impact on applications embedding MRuby, such as Shopify Scripts
3. Provided actionable debugging steps for verification and patching

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Impact

---

*Last updated: 2024-10-01T00:00:00Z*
