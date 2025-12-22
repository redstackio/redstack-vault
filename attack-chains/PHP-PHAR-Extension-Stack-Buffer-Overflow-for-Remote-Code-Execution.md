---
tags:
  - buffer-overflow
  - phar
  - php
  - rce
  - memory-corruption
type: attack_chain
tools:
  - '[[tools/Valgrind]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Linux
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-and-Test-Malicious-PHAR-Archive]]'
  - '[[procedures/Execute-PHP-Script-to-Load-Malicious-PHAR]]'
  - '[[procedures/Analyze-Crash-Output-for-Overflow-Confirmation]]'
step_count: 3
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:19.594Z'
description: >-
  Multi-stage exploitation of a stack-based buffer overflow in PHP's PHAR
  extension to achieve remote code execution via malicious archive processing.
skill_level: intermediate
impact_level: high
id: de2a49bb-5399-4f09-9cb2-565e87fa578a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# PHP PHAR Extension Stack Buffer Overflow for Remote Code Execution

Multi-stage attack chain demonstrating exploitation of a stack-based buffer overflow in PHP's PHAR extension, allowing EIP manipulation and potential remote code execution when processing untrusted PHAR archives.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious PHAR] --> B[Load Archive in PHP]
    B --> C[Trigger Overflow and Analyze]
    C --> D[RCE Achievement]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Valgrind]]

### Target Environment

- Linux OS
- PHP with PHAR extension enabled
- SPL (Standard PHP Library)

### Initial Access Requirements

- Access to a PHP environment for testing
- Ability to compile or use a custom PHP binary
- No network access required for local testing

## Detailed Attack Procedures

### Step 1: Create and Test Malicious PHAR Archive
procedure: [[procedures/Create-and-Test-Malicious-PHAR-Archive]]

**Objective**: Craft a malformed PHAR archive with manipulated filepath to trigger buffer overflow in phar_fix_filepath.

**Instructions**: Use scripting tools to generate the PHAR file with oversized or corrupted filepath data. Test under Valgrind to detect initial memory issues.

Execute the Valgrind command to run PHP and process the archive:

```bash
valgrind ./out/php phar_test.php
```

**Expected Output**: Valgrind reports invalid reads in zend_mm_alloc_small and phar_fix_filepath.

**Success Indicators**:
- Malicious PHAR file created without errors
- Initial memory corruption detected in Valgrind output

### Step 2: Execute PHP Script to Load Malicious PHAR
procedure: [[procedures/Execute-PHP-Script-to-Load-Malicious-PHAR]]

**Objective**: Load the malicious PHAR via PHP's Phar::__construct and SPL filesystem functions to propagate the overflow.

**Instructions**: Write a PHP script that opens the PHAR as a directory stream using spl_filesystem_dir_open. Run it under Valgrind.

Use the following Valgrind-wrapped execution:

```bash
valgrind ./out/php load_phar.php
```

**Expected Output**: SIGSEGV at corrupted address like 0xdbdbdbdbdbdbdbdb, with stack trace through phar_parse_url and Phar::__construct.

**Success Indicators**:
- Segmentation fault triggered
- EIP register manipulation observed in crash

### Step 3: Analyze Crash Output for Overflow Confirmation
procedure: [[procedures/Analyze-Crash-Output-for-Overflow-Confirmation]]

**Objective**: Examine Valgrind logs to confirm stack overflow, invalid memory reads, and potential RCE path.

**Instructions**: Review the Valgrind output for specific errors like invalid read of size 8 and general protection faults. Correlate with PHP source locations.

Parse the logs from the previous Valgrind run:

```bash
grep -i "invalid read" valgrind.log
```

**Expected Output**: Details on faults in zend_alloc.c:1291 and phar.c:2080, full stack trace involving PHAR wrapper.

**Success Indicators**:
- Buffer overflow confirmed via memory access violations
- Path to RCE validated through EIP control

## Attack Chain Summary

### Key Achievements

1. Successful creation of malicious PHAR triggering overflow
2. Reproduction of segmentation faults and EIP manipulation
3. Identification of RCE potential in untrusted input scenarios

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
