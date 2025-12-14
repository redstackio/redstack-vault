---
tags:
  - gdb
  - debugging
  - integer-overflow
type: procedure
tools:
  - '[[tools/GDB]]'
  - '[[tools/PHP]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
  - PHP
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques: []
id: 00e08135-b8ca-4e22-841f-454f964ea684
created_at: '2025-12-14T17:28:20.068Z'
updated_at: '2025-12-14T17:28:20.068Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Debug-Execution-with-GDB-to-Observe-Overflow

## Summary

This procedure uses GDB to debug a PHP script execution, setting breakpoints to inspect the integer overflow in php_escape_html_entities_ex() and confirm small memory allocation.

## Description

Attach GDB to the PHP process running the trigger script. Break at line 1269 in ext/standard/html.c, step to 1272, and examine oldlen and maxlen values. On 32-bit systems, verify oldlen=0x7fffffff leads to maxlen=0xfffffffe and a tiny allocation in _emalloc(). Requires PHP built with debug symbols.

## Requirements

1. GDB installed on 32-bit Linux
2. PHP 7.1 compiled with -g flag for symbols
3. Trigger script from previous procedure

## Defense

Defensive measures and detection strategies:

- Harden PHP builds with address sanitizers (e.g., -fsanitize=address) to detect overflows at runtime
- Log debugger attachments or unusual process behaviors
- Use containerization to isolate PHP execution

## Objectives

1. Breakpoint and inspect vulnerable calculation
2. Verify integer wrap-around and allocation size
3. Document state for exploit refinement

## Instructions

### Step 1: Prepare and Launch GDB

**Context**: Start GDB with the PHP executable and script.

Run `gdb --args php trigger.php` to load the environment.

> Expected: GDB prompts for commands; PHP not yet executed.

### Step 2: Set Breakpoint and Run

**Context**: Place breakpoint at function entry and execute to hit it.

In GDB: `break ext/standard/html.c:1269` then `run`. Step with `next` to line 1272, print variables: `print oldlen` and `print maxlen`.

> Expected: oldlen=0x7fffffff, maxlen=0xfffffffe; trace zend_string_alloc() call showing small size.

### Step 3: Inspect Allocation

**Context**: Confirm the undersized buffer creation.

Use `print _emalloc(size)` or backtrace to see allocation path.

> Expected: Allocation of ~2MB instead of required 4GB.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GDB]]
- [[tools/PHP]]

## Tags

- [[debugging]]
- [[tools/GDB]]
- [[tools/PHP]]
