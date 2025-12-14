---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - dos
  - null-pointer-dereference
  - mrbuby
  - ruby
  - segmentation-fault
  - shopify-scripts
type: attack_chain
tools:
  - '[[tools/GDB]]'
  - '[[tools/ASAN]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Linux
  - MRuby
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-MRuby-Segmentation-Fault-with-PoC-Script]]'
step_count: 1
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:26:36.960Z'
description: >-
  Exploit a null pointer dereference in MRuby's mrb_obj_instance_eval to crash
  the Ruby process in Shopify Scripts sandbox, causing denial of service.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Command-Line Interface]]'
---
# Denial of Service via Null Pointer Dereference in MRuby instance_eval

Multi-stage attack chain demonstrating exploitation of a null pointer dereference in the MRuby engine used by Shopify Scripts, leading to a segmentation fault and denial of service.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare PoC Script] --> B[Execute in Sandbox]
    B --> C[Process Crash and DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/GDB]]
- [[tools/ASAN]]

### Target Environment

- Linux OS
- MRuby engine (version integrated with Ruby 2.3.1)
- Shopify Scripts sandbox service
- GCC compiler for building with ASAN

### Initial Access Requirements

- Access to execute scripts in the Shopify Scripts sandbox environment
- No network access required; local execution in the Ruby process
- Prior knowledge of MRuby internals for crafting the PoC

## Detailed Attack Procedures

### Step 1: Execute PoC Script in Sandbox
procedure: [[procedures/Trigger-MRuby-Segmentation-Fault-with-PoC-Script]]

**Objective**: Trigger the null pointer dereference in mrb_obj_instance_eval by evaluating malicious Ruby code, causing a segmentation fault that crashes the Ruby process and disrupts the scripting service.

**Instructions**: Prepare the eval.rb PoC script containing Ruby code that exploits the vulnerability during instance_eval. Then execute it using the sandbox command to simulate script evaluation in the Shopify Scripts environment.

First, ensure the MRuby build includes ASAN for detection:

Use [[commands/build-mruby-with-asan]] to compile if needed (prerequisite setup).

Then run the PoC:

```bash
./sandbox eval.rb
```

This invokes the sandbox_eval function, which calls mrb_obj_instance_eval and dereferences a null pointer at vm.c:522.

**Expected Output**: Segmentation fault (core dumped) with backtrace pointing to mrb_obj_instance_eval. ASAN may report: "heap-use-after-free" or null dereference details.

**Success Indicators**:
- Process crashes with SIGSEGV
- Backtrace shows failure in mrb_obj_instance_eval
- Scripting service becomes unresponsive, confirming DoS

## Attack Chain Summary

### Key Achievements

1. Successful reproduction of the null pointer dereference in MRuby.
2. Crash of the Ruby process handling Shopify Scripts.
3. Demonstration of denial of service impact on the sandboxed scripting environment.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Command-Line Interface]] Command and Scripting Interpreter

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
