---
id: ac-php-pg-overflow-rce
tags:
  - php
  - postgresql
  - integer-overflow
  - heap-overflow
  - rce
  - memory-corruption
type: attack_chain
tools:
  - '[[tools/GDB]]'
  - '[[tools/PHP]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Linux
  - 32-bit
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - >-
    [[procedures/Review-PHP-Source-Code-for-Integer-Overflow-in-pg-escape-string]]
  - '[[procedures/Trigger-Heap-Overflow-with-PHP-Test-Script]]'
  - '[[procedures/Debug-PHP-Execution-to-Observe-Overflow-with-GDB]]'
  - '[[procedures/Exploit-Heap-Overflow-for-Arbitrary-Code-Execution-in-PHP]]'
step_count: 4
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Proc Memory]]'
updated_at: '2025-12-14T17:28:20.149Z'
description: >-
  Multi-stage exploitation of an integer overflow in PHP's pg_escape_string()
  function, causing heap buffer overflow and enabling arbitrary code execution
  on 32-bit systems.
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Proc Memory]]'
---
# Heap Overflow via Integer Overflow in PHP PostgreSQL Extension Leading to RCE

Multi-stage attack chain exploiting an integer overflow in the pg_escape_string() function of PHP's PostgreSQL extension, leading to heap buffer overflow, memory corruption, and arbitrary code execution on 32-bit Linux systems.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~30 minutes |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | Critical |

## Attack Flow Visualization

```mermaid
graph LR
    A[Code Review] --> B[Trigger Overflow]
    B --> C[Debug Overflow]
    C --> D[Exploit for RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/GDB]]
- [[tools/PHP]]

### Target Environment

- 32-bit Linux platform
- PHP 7.1 with PostgreSQL extension (vulnerable commit 931ea5c872a0a4455c5bbb8470c7a1d049bd8501)
- libpq.so.5 library
- No specific ports or services required beyond local PHP execution

### Initial Access Requirements

- Local access to a vulnerable PHP installation
- Source code access for review (e.g., from PHP GitHub repo)
- No network access or credentials needed; assumes developer or tester environment

## Detailed Attack Procedures

### Step 1: Code Review
procedure: [[procedures/Review-PHP-Source-Code-for-Integer-Overflow-in-pg-escape-string]]

**Objective**: Identify the integer overflow vulnerability in the pg_escape_string() function by analyzing the source code.

**Instructions**: Clone the PHP source repository and examine the file ext/pgsql/pgsql.c around line 4384. Look for the zend_string_alloc call without overflow checks.

**Expected Output**: Confirmation of vulnerable allocation: zend_string_alloc(ZSTR_LEN(from) * 2, 0) where ZSTR_LEN(from) can be PHP_INT_MAX (0x7FFFFFFF), causing wrap-around to small size (0x10 bytes).

**Success Indicators**:
- Overflow condition identified in code
- Potential for tiny allocation with large input noted

### Step 2: Trigger Overflow
procedure: [[procedures/Trigger-Heap-Overflow-with-PHP-Test-Script]]

**Objective**: Reproduce the vulnerability by creating a large input string and calling pg_escape_string() to cause the integer overflow and subsequent heap write overflow.

**Instructions**: Create a PHP script that sets unlimited memory and generates a string of 0x7FFFFFFF 'a's, then passes it to pg_escape_string(). Execute the script using [[commands/php-trigger-pg-escape-overflow]].

```php
<?php ini_set('memory_limit',-1); $s=str_repeat("a",0x7FFFFFFF); $escaped=pg_escape_string($s); ?>
```

**Expected Output**: Script execution leads to heap overflow, potentially crashing with SIGSEGV due to writing large data into small buffer.

**Success Indicators**:
- Script runs without immediate memory limit error
- Overflow occurs during escape processing

### Step 3: Debug Execution
procedure: [[procedures/Debug-PHP-Execution-to-Observe-Overflow-with-GDB]]

**Objective**: Use GDB to debug the PHP process, set breakpoints, and observe the overflow in allocation and write operations.

**Instructions**: Compile PHP in debug mode if needed, run the PHP script under GDB with breakpoint at ext/pgsql/pgsql.c:4384. Inspect registers to see overflowed size calculation: ((0x7fffffff * 2 + 0x14) & 0xfffffffc = 0x10). Continue to observe SIGSEGV in PQescapeStringInternal.

**Expected Output**: GDB shows small allocation (0x10 bytes) and large writes causing segmentation fault; memory corruption visible in heap inspection.

**Success Indicators**:
- Breakpoint hit and registers confirm overflow
- SIGSEGV traced to write in libpq.so.5

### Step 4: Develop Exploit
procedure: [[procedures/Exploit-Heap-Overflow-for-Arbitrary-Code-Execution-in-PHP]]

**Objective**: Craft an exploit script to leverage the overflow for memory corruption, ASLR/DEP bypass, EIP control, and RCE, spawning a shell.

**Instructions**: Based on debugging insights, develop a PHP exploit (e.g., pg_escape_string_exploit.php) that uses the overflow to leak memory, overwrite heap objects, and hijack control flow. Run on vulnerable PHP 7.1.

**Expected Output**: Exploit spawns /bin/sh shell, demonstrating full RCE.

**Success Indicators**:
- Memory leak bypasses ASLR and DEP
- EIP overwritten for code execution
- Interactive shell obtained

## Attack Chain Summary

### Key Achievements

1. Identified integer overflow in PHP PostgreSQL extension via code review
2. Reproduced heap overflow with crafted input string
3. Debugged and confirmed memory corruption mechanics
4. Achieved arbitrary code execution by spawning a shell

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Proc Memory]] Proc Memory Loading/Injection

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
