---
id: ac-apache-prefork-root-esc
tags:
  - apache
  - php
  - uaf
  - privilege-escalation
  - local-root
  - memory-corruption
  - shared-memory
type: attack_chain
tools:
  - '[[tools/GDB]]'
  - '[[tools/proc-filesystem]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: high
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-PHP-Use-After-Free-for-Arbitrary-Memory-Read-Write]]'
  - '[[procedures/Locate-Apache-Shared-Memory-and-Bucket-Structures]]'
  - '[[procedures/Craft-Fake-prefork-child-Bucket-in-Shared-Memory]]'
  - >-
    [[procedures/Spray-Fake-Bucket-Addresses-by-Modifying-process-score-Buckets]]
  - '[[procedures/Trigger-Graceful-Restart-to-Execute-Arbitrary-Code-as-Root]]'
step_count: 5
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Process Injection]]'
updated_at: '2025-12-14T17:30:47.284Z'
description: >-
  Multi-stage local privilege escalation exploiting a PHP Use-After-Free to
  manipulate Apache shared memory, leading to an out-of-bounds access during
  graceful restart for arbitrary code execution as root.
skill_level: advanced
impact_level: critical
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Process Injection]]'
---
# Apache mod_prefork Out-of-Bounds Access for Local Root Privilege Escalation via PHP UAF

Multi-stage attack chain exploiting vulnerabilities in Apache HTTP Server's mod_prefork MPM and PHP to achieve local root privilege escalation from the www-data user.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~Several hours (awaiting restart) |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | Critical |

## Attack Flow Visualization

```mermaid
graph LR
    A[Exploit PHP UAF for Memory R/W] --> B[Locate SHM and Buckets]
    B --> C[Craft Fake Bucket Structure]
    C --> D[Spray Bucket Pointers]
    D --> E[Trigger Graceful Restart for Root Exec]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/GDB]]
- [[tools/proc-filesystem]]

### Target Environment

- Linux OS
- Apache HTTP Server 2.4.17-2.4.38 with mod_prefork MPM
- PHP 7.x with mod_php enabled
- Ports 80/443 open for Apache
- Local access as www-data (e.g., via compromised web shell)

### Initial Access Requirements

- Local execution privileges on a PHP-enabled Apache worker process (www-data user)
- Ability to trigger PHP code execution
- Knowledge of process PID for memory inspection

## Detailed Attack Procedures

### Step 1: Exploit PHP UAF for Memory Access
procedure: [[procedures/Exploit-PHP-Use-After-Free-for-Arbitrary-Memory-Read-Write]]

**Objective**: Gain arbitrary read/write access in the PHP worker process to target shared memory regions.

**Instructions**: Trigger a Use-After-Free in PHP's DateInterval/JsonSerializable to unset an object while retaining $this reference, converting to zend_string UAF for heap, SHM, and all_buckets manipulation.

**Expected Output**: Controlled memory writes confirming access to non-string regions.

**Success Indicators**:
- Successful UAF trigger without crash
- Read/write primitives established for SHM

### Step 2: Locate Bucket Indexes and all_buckets Address
procedure: [[procedures/Locate-Apache-Shared-Memory-and-Bucket-Structures]]

**Objective**: Identify locations of Apache shared memory (SHM) and prefork_child_bucket structures for targeting.

**Instructions**: Use [[commands/cat-proc-maps-grep-libphp-rw-p]] to find PHP heap and [[commands/cat-proc-maps-grep-rw-s]] for SHM. Scan memory patterns in GDB for mutex->meth pointing to libapr functions to locate all_buckets.

```bash
cat /proc/6318/maps | grep libphp | grep rw-p
cat /proc/6318/maps | grep rw-s
```

**Expected Output**: Addresses like 7f4a8f9f3000-7f4a8fa0a000 for heap and 7f4a9323e000-7f4a93252000 for SHM.

**Success Indicators**:
- SHM and heap addresses mapped
- all_buckets array located via pattern matching

### Step 3: Write Fake prefork_child_bucket Structure
procedure: [[procedures/Craft-Fake-prefork-child-Bucket-in-Shared-Memory]]

**Objective**: Overlay a fake structure in SHM to control function pointers for later execution.

**Instructions**: Use the UAF write primitive to superimpose prefork_child_bucket, apr_proc_mutex_t, and zend_object/zend_array. Set mutex->meth->child_init to zend_object_std_dtor, chaining to system() via pDestructor on a controlled string.

**Expected Output**: Fake structure written without detection, verifiable via GDB inspection like [[commands/gdb-print-ap-scoreboard-image]].

**Success Indicators**:
- Fake mutex and bucket structures in place
- Function pointer (child_init) controlled

### Step 4: Modify process_score Buckets to Point to Fake Structure
procedure: [[procedures/Spray-Fake-Bucket-Addresses-by-Modifying-process-score-Buckets]]

**Objective**: Ensure the fake structure is accessed post-restart by spraying pointers across possible all_buckets relocations.

**Instructions**: Alter multiple process_score->bucket indexes in SHM using UAF to point to the fake structure. Use negative offsets to cover memory regions and spray addresses for relocation robustness.

**Expected Output**: Multiple bucket indexes updated, inspectable via [[commands/gdb-print-process-score-parent-0]].

**Success Indicators**:
- process_score buckets modified to fake addresses
- Spray covers potential all_buckets shifts

### Step 5: Await and Trigger Graceful Restart
procedure: [[procedures/Trigger-Graceful-Restart-to-Execute-Arbitrary-Code-as-Root]]

**Objective**: Cause Apache to perform an out-of-bounds read leading to arbitrary function call as root.

**Instructions**: Wait for logrotate at 6:25AM to execute [[commands/apache2ctl-graceful]], or manually trigger it. This sends SIGUSR1 to workers, spawns new ones via make_child(), triggering OOB access to controlled bucket and apr_proc_mutex_child_init() call before privilege drop.

```bash
apache2ctl graceful
```

**Expected Output**: New workers spawn, root shell or command execution (e.g., via controlled system() call).

**Success Indicators**:
- Graceful restart completes
- Privilege escalation to root confirmed (e.g., id command shows uid=0)

## Attack Chain Summary

### Key Achievements

1. Arbitrary memory read/write via PHP UAF
2. Manipulation of Apache SHM for OOB control
3. Root privilege escalation during routine restart

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Process Injection]] Process Injection

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01T00:00:00Z*
