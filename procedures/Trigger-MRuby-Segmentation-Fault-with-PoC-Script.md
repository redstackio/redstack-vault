---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - dos
  - null-pointer-dereference
  - mrbuby
  - ruby
  - segmentation-fault
type: procedure
tools:
  - '[[tools/GDB]]'
  - '[[tools/ASAN]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/sandbox-eval-poc]]'
verified: false
platforms:
  - Linux
  - MRuby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:26:36.954Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Command-Line Interface]]'
---
# Trigger-MRuby-Segmentation-Fault-with-PoC-Script

## Summary

This procedure exploits a null pointer dereference vulnerability in MRuby's mrb_obj_instance_eval function to cause a segmentation fault, crashing the Ruby process in the Shopify Scripts sandbox and resulting in denial of service.

## Description

The vulnerability occurs during Ruby code evaluation in the sandboxed environment of Shopify Scripts, where crafted input leads to unsafe object handling and a memory access violation at vm.c:522. By executing a proof-of-concept Ruby script (eval.rb), an attacker with script execution privileges can trigger the crash, preventing normal operation of the scripting service and causing uncontrolled resource consumption. This was discovered through fuzzing or targeted testing of the MRuby engine integrated with Ruby 2.3.1 on Linux.

## Requirements

1. Access to the MRuby sandbox execution environment (e.g., Shopify Scripts).
2. GCC compiler on Linux x64 for building MRuby with AddressSanitizer (ASAN).
3. The eval.rb PoC script containing malicious Ruby code that triggers instance_eval on a null object.
4. Optional: GDB for post-crash analysis.

## Defense

Defensive measures and detection strategies:

- Input validation and sanitization in mrb_obj_instance_eval to check for null pointers before dereferencing.
- Use of memory sanitizers like ASAN in development and staging builds to detect issues early.
- Runtime monitoring for segmentation faults in Ruby processes, with automatic restarts and logging.
- Fuzz testing of scripting engines to identify similar vulnerabilities.

## Objectives

1. Crash the MRuby process via segmentation fault to deny service to script evaluations.
2. Demonstrate impact on Shopify Scripts by preventing legitimate script execution.
3. Analyze the crash for root cause confirmation using debugging tools.

## Instructions

### Step 1: Build MRuby with ASAN

**Context**: Instrument the MRuby build to detect memory errors like null pointer dereferences during execution.

**Command** ([[commands/build-mruby-with-asan]]):
```bash
gcc -fsanitize=address -g -o mrb mrbgems/mruby-build/build/lib/libmruby.a vm.c
```

> This compiles MRuby with AddressSanitizer enabled on Linux x64 using GCC, enabling runtime detection of the vulnerability.

### Step 2: Prepare and Execute PoC Script

**Context**: Run the eval.rb script in the sandbox to trigger the null pointer dereference in mrb_obj_instance_eval.

**Command** ([[commands/sandbox-eval-poc]]):
```bash
./sandbox eval.rb
```

> The command executes the PoC Ruby script via the sandbox_eval function, leading to a crash. Expected output includes a segmentation fault at address 0x0000000000000003, with backtrace highlighting vm.c:522 in mrb_obj_instance_eval. Use GDB to attach and inspect registers if needed.

### Step 3: Analyze Crash with GDB

**Context**: Debug the segmentation fault to confirm the null pointer issue and examine the call stack.

**Command** (using [[tools/GDB]]):
```bash
gdb ./sandbox core
```

> Load the core dump to view backtrace (bt) and registers, verifying the dereference of a null pointer in the instance_eval path.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques


## Commands Used

- [[commands/build-mruby-with-asan]]
- [[commands/sandbox-eval-poc]]

## Tools Used

- [[tools/GDB]]
- [[tools/ASAN]]

## Tags

- dos
- null-pointer-dereference
- mrbuby
- ruby
- segmentation-fault
