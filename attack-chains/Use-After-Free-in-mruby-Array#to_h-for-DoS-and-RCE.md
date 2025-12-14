---
tags:
  - uaf
  - mruby
  - ruby
  - dos
  - rce
  - memory-corruption
type: attack_chain
tools:
  - '[[tools/GDB]]'
  - '[[tools/jmlb337]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/mruby-dos-poc]]'
  - '[[commands/mruby-memory-corruption-poc]]'
  - '[[commands/mruby-rce-full-exploit]]'
platforms:
  - Embedded Ruby (mruby)
  - Linux
complexity: high
procedures:
  - '[[procedures/Define-Custom-Class-for-UAF-Trigger]]'
  - '[[procedures/Setup-Global-Array-with-Malicious-Object]]'
  - '[[procedures/Trigger-UAF-via-to_h-Call]]'
  - '[[procedures/Advanced-Exploitation-with-Memory-Leak-and-Corruption]]'
step_count: 4
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Command-Line Interface]]'
  - '[[Endpoint Denial of Service]]'
description: >-
  Exploits a use-after-free vulnerability in mruby's Array#to_h function to
  cause denial of service via null pointer dereference and achieve remote code
  execution through memory corruption primitives.
skill_level: advanced
impact_level: critical
id: 15114d42-a2dc-482e-8d47-0292a8c2af7e
created_at: '2025-12-14T17:26:48.783Z'
updated_at: '2025-12-14T17:26:48.783Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Command-Line Interface]]'
  - '[[Endpoint Denial of Service]]'
---
# Use-After-Free in mruby Array#to_h for DoS and RCE

Multi-stage attack chain exploiting a use-after-free vulnerability in mruby's Array#to_h function. The attack begins with defining a custom class that modifies the array during to_ary conversion, leading to out-of-bounds access and null dereference for DoS. Advanced stages leverage memory leaks from a related String#lines bug to build arbitrary read/write primitives, enabling RCE by overwriting a Proc object's function pointer.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | Critical |

## Attack Flow Visualization

```mermaid
graph LR
    A[Define Custom Class] --> B[Setup Array] --> C[Trigger to_h] --> D[Leak and Corrupt Memory]
    D --> E[RCE via Proc Overwrite]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/GDB]]
- [[tools/jmlb337]]

### Target Environment

- mruby interpreter (embedded Ruby runtime)
- Linux platform for debugging with GDB
- Access to mruby source or binary for analysis

### Initial Access Requirements

- Code execution environment in mruby (e.g., script execution in an application using mruby)
- No network access required; local to the mruby process
- Prior knowledge of mruby internals for advanced exploitation

## Detailed Attack Procedures

### Step 1: Define Custom Class for UAF Trigger
procedure: [[procedures/Define-Custom-Class-for-UAF-Trigger]]

**Objective**: Create a malicious class that overrides to_ary to clear the target array during conversion, setting up the use-after-free condition.

**Instructions**: Define class A with to_ary method that clears the global array $a and returns nil to trigger exception handling in mrb_ary_to_h.

Execute the class definition using [[commands/mruby-dos-poc]] (initial part):

```ruby
class A; def to_ary; $a.clear; nil; end; end
```

**Expected Output**: Class defined without errors; prepares for array setup.

**Success Indicators**:
- Class A is successfully defined and overrides to_ary.
- No immediate crash; vulnerability triggered later.

### Step 2: Setup Global Array with Malicious Object
procedure: [[procedures/Setup-Global-Array-with-Malicious-Object]]

**Objective**: Populate a global array with an instance of the custom class to position the malicious object for the to_h iteration.

**Instructions**: Create the global array $a containing A.new as the element that will invoke the faulty to_ary.

Execute using [[commands/mruby-dos-poc]] (setup part):

```ruby
$a = [A.new]
```

**Expected Output**: Array created with one element; ready for to_h call without visible issues.

**Success Indicators**:
- Global array $a holds the instance of A.
- Array length is 1, confirming setup.

### Step 3: Trigger UAF via to_h Call
procedure: [[procedures/Trigger-UAF-via-to_h-Call]]

**Objective**: Invoke Array#to_h to iterate over the array, calling to_ary on the element, which clears the array (nullifying ptr) and causes out-of-bounds read on null pointer during exception handling.

**Instructions**: Call to_h on $a to trigger mrb_ary_to_h, leading to null dereference in RARRAY_PTR(ary)[i] access.

Execute the full DoS PoC with [[commands/mruby-dos-poc]]:

```ruby
class A; def to_ary; $a.clear; nil; end; end; $a=[A.new]; $a.to_h
```

**Expected Output**: Null memory access crash terminating the mruby process.

**Success Indicators**:
- Process crashes with segmentation fault or null dereference.
- GDB backtrace shows fault in array.c around mrb_ary_to_h or mrb_obj_classname.

### Step 4: Advanced Exploitation with Memory Leak and Corruption
procedure: [[procedures/Advanced-Exploitation-with-Memory-Leak-and-Corruption]]

**Objective**: Combine with String#lines bug for memory leak, then use UAF to corrupt structures for arbitrary read/write, targeting Proc for RCE.

**Instructions**: First, leak RString structure using String#lines. Then, in to_ary, manipulate arrays for overlap and corrupt IV table. Use GDB to inspect.

Execute memory corruption PoC with [[commands/mruby-memory-corruption-poc]] for disclosure, then full RCE with [[commands/mruby-rce-full-exploit]]:

```ruby
# Excerpt from RCE PoC: Setup leak with $lines.lines, then trigger UAF in $uaf.to_h
$lines = placeholder *1; $lines[0]="\n"; $lines.lines do|l| ... end;
# Followed by class A definition and $uaf.to_h
```

**Expected Output**: Leaked pointers (e.g., str_obj), corrupted memory leading to arbitrary read/write, and Proc function pointer overwrite (e.g., 0x4141414141414141) for control flow hijack.

**Success Indicators**:
- Valid memory leak (e.g., $str_ptr unpacked correctly).
- Successful arbitrary write confirmed via GDB inspection of Proc at code_addr.
- RCE achieved with code.call executing hijacked flow.

## Attack Chain Summary

### Key Achievements

1. Triggered DoS via null pointer dereference in Array#to_h.
2. Demonstrated memory disclosure using chained String#lines bug.
3. Built arbitrary read/write primitives through UAF-induced corruption.
4. Achieved RCE by overwriting Proc function pointer.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01*
