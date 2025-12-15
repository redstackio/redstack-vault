---
id: proc-craft-fake-bucket
tags:
  - apache
  - shared-memory
  - function-pointer
type: procedure
tools:
  - '[[tools/GDB]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/gdb-ptype-apr-proc-mutex-unix-lock-methods-t]]'
  - '[[commands/gdb-print-ap-scoreboard-image]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:30:47.278Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
---
# Craft Fake prefork_child_bucket in Shared Memory

## Summary

This procedure uses the PHP UAF primitive to write a superimposed fake prefork_child_bucket structure into Apache SHM, including apr_proc_mutex_t and zend_object elements, to control the child_init function pointer for root execution.

## Description

Overlay structures in SHM: set fake prefork_child_bucket with mutex->meth->child_init pointing to zend_object_std_dtor, which chains to system() via a controlled pDestructor string. This prepares for OOB access during restart. Requires prior UAF R/W and SHM location.

## Requirements

1. Established UAF read/write primitive
2. Known SHM address from previous procedure
3. GDB for structure verification

## Defense

Defensive measures and detection strategies:

- Patch Apache to 2.4.39+ with bounds checks
- Use memory integrity checks (e.g., PaX)
- Audit SHM access logs

## Objectives

1. Write controlled mutex and bucket in SHM
2. Hijack child_init to arbitrary code
3. Chain to system() for escalation

## Instructions

### Step 1: Define and Write Fake Structure

**Context**: Use UAF to write the superimposed structure acting as prefork_child_bucket, apr_proc_mutex_t, and zend_object/zend_array.

No direct command; leverage PHP UAF script to write at SHM offset (e.g., from 0x7f4a9323e020).

> Set fields: mutex->meth->child_init = zend_object_std_dtor; pDestructor = controlled string for system().

### Step 2: Verify Structure Types and Placement

**Context**: Use GDB to confirm types and inspect write.

**Command** ([[commands/gdb-ptype-apr-proc-mutex-unix-lock-methods-t]]):
```bash
(gdb) ptype apr_proc_mutex_unix_lock_methods_t
```

> Outputs: apr_proc_mutex_unix_lock_methods_t { ... apr_status_t (*child_init)(apr_proc_mutex_t **, apr_pool_t *, const char *); ... }

**Command** ([[commands/gdb-print-ap-scoreboard-image]]):
```bash
(gdb) p *ap_scoreboard_image
```

> Verify fake structure at parent/servers offsets.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow

### Sub-Techniques

-

## Commands Used

- [[commands/gdb-ptype-apr-proc-mutex-unix-lock-methods-t]]
- [[commands/gdb-print-ap-scoreboard-image]]

## Tools Used

- [[tools/GDB]]

## Tags

- fake-structure
- mutex-hijack
