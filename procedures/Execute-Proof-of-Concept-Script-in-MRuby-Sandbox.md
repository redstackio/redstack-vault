---
id: proc-mruby-execute-poc
tags:
  - dos
  - poc
  - sandbox
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/sandbox-execute-poc]]'
verified: false
platforms:
  - Linux
  - Ruby
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:26:30.748Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Execute-Proof-of-Concept-Script-in-MRuby-Sandbox

## Summary

This procedure executes a proof-of-concept Ruby script (vm_exec.rb) in the MRuby sandbox to trigger a null pointer dereference in the mrb_vm_exec function, causing a segmentation fault and demonstrating denial of service in the interpreter.

## Description

The vulnerability arises from improper handling of 'break' statements within NoMethodError contexts during virtual machine execution, leading to null pointer access when creating range objects or accessing methods. The PoC script is designed to invoke this path in a sandboxed environment, resulting in uncontrolled resource consumption and a crash. This is particularly impactful for applications like Shopify Scripts that embed MRuby. The target is a locally built MRuby on Linux x64 with ASAN enabled.

## Requirements

1. Built MRuby binary with ASAN from previous procedure
2. vm_exec.rb PoC script containing malicious 'break' in method missing handler
3. Sandbox executable in the MRuby build directory

## Defense

Defensive measures and detection strategies:

- Implement bounds checking in VM execution paths for method missing and break handling
- Monitor for segmentation faults in logs and restart interpreters with resource limits
- Use fuzzing tools like American Fuzzy Lop to test interpreter robustness pre-deployment

## Objectives

1. Trigger the null pointer dereference to crash the MRuby interpreter
2. Observe DoS effects such as resource exhaustion
3. Validate the vulnerability in a controlled sandbox

## Instructions

### Step 1: Prepare PoC Script

**Context**: Ensure the vm_exec.rb script is in the current directory, crafted to hit the vulnerable code path involving range creation in NoMethodError.

No command; manually create or place the script.

> Expected: Script file ready for execution.

### Step 2: Run Script in Sandbox

**Context**: Invoke the sandbox_eval function via the sandbox binary to execute the script and trigger the VM crash.

Execute [[commands/sandbox-execute-poc]]:

```bash
./sandbox vm_exec.rb
```

> This runs the script, leading to a null pointer dereference in mrb_vm_exec during method handling. Expected output: Segmentation fault (core dumped) at 0x00000000000000, with ASAN heap-use-after-free or null-deref report.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/sandbox-execute-poc]]

## Tools Used


## Tags

- dos
- poc
- sandbox
