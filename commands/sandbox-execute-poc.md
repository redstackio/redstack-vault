---
id: cmd-sandbox-poc
data: |
  |
    ./sandbox vm_exec.rb
tags:
  - dos
  - poc
type: command
output: |-
  Segmentation fault (core dumped)
  AddressSanitizer: null-dereference on address 0x00000000000000
executor: bash
platforms:
  - Linux
  - Ruby
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.739Z'
verified: false
validated: true
submitted: true
---
# sandbox-execute-poc

## Command

```bash
./sandbox vm_exec.rb
```

## Description

Executes the proof-of-concept Ruby script (vm_exec.rb) in the MRuby sandbox environment, triggering a null pointer dereference in mrb_vm_exec and causing a segmentation fault. Used to demonstrate the DoS vulnerability in embedded Ruby interpreters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| vm_exec.rb | Path to the PoC script file containing the malicious 'break' in NoMethodError context | Yes |

## Examples

### Basic Usage

```bash
./sandbox vm_exec.rb
```

### Advanced Usage

Run under strace for additional tracing:

```bash
strace ./sandbox vm_exec.rb
```

## Expected Output

Segmentation fault at 0x00000000000000 with backtrace showing crash in mrb_vm_exec. ASAN may report: "AddressSanitizer: attempting to access null pointer."

## Related

- [[commands/gdb-backtrace]]
- [[procedures/Execute-Proof-of-Concept-Script-in-MRuby-Sandbox]]
