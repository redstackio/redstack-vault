---
id: 0ba2acd0-7820-439d-b2b3-1ebe8454fb3b
name: Verify Payload Execution and RCE
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:13.229Z'
updated_at: '2025-12-11T06:10:13.229Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
sub_techniques: []
tags:
  - verification
  - rce
commands:
  - '[[commands/ruby-puts-hello]]'
  - '[[commands/ruby-echo-tmp-file]]'
  - '[[commands/git-clone-wiki-repo]]'
  - '[[commands/git-add-all]]'
  - '[[commands/git-commit-message]]'
  - '[[commands/git-push]]'
  - '[[commands/cat-tmp-vakzz]]'
  - '[[commands/ps-memory-injection]]'
  - '[[commands/ruby-echo-inject-tmp]]'
  - '[[commands/id]]'
  - '[[commands/hostname-a]]'
  - '[[commands/ps-auxww]]'
  - '[[commands/exit]]'
  - '[[commands/nc-reverse-shell]]'
platforms:
  - Linux
tools:
  - '[[tools/git]]'
  - '[[tools/Kramdown]]'
  - '[[tools/Rouge]]'
  - '[[tools/Redis-rb]]'
  - '[[tools/GetProcessMem]]'
  - '[[tools/GitHub::Markup]]'
  - '[[tools/nc]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---

# Verify Payload Execution and RCE

## Summary

Check logs and filesystem to confirm successful code execution from the payload.

## Description

Verification involves inspecting /tmp files and logs for evidence, or using reverse shell for further access.

## Requirements

1. Server access for verification (logs, shell)
2. Payload executed

## Defense

Defensive measures and detection strategies:

- Monitor /tmp for unexpected files
- Audit logs for rendering errors

## Objectives

1. Check logs
2. Verify file creation
3. Optional reverse shell

## Instructions

### Step 1: Check Logs

**Context**: Look for execution evidence in GitLab logs.

No command, review logs manually.

> Error messages indicate execution.

### Step 2: Verify File

**Context**: Cat the created file.

**Command** ([[commands/cat-tmp-vakzz]]):
```bash
cat /tmp/vakzz
```

> Output: vakzz was here

### Step 3: Command Injection Variant

**Context**: For GetProcessMem injection.

Use [[commands/ps-memory-injection]] or [[commands/ruby-echo-inject-tmp]].

> Injection successful.

### Step 4: Reverse Shell Commands

**Context**: If using reverse shell.

Execute [[commands/id]], [[commands/hostname-a]], [[commands/ps-auxww]], then [[commands/exit]].

```bash
id
hostname -a
ps auxww
exit
```

> Shell access verified.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/cat-tmp-vakzz]]
- [[commands/ps-memory-injection]]
- [[commands/ruby-echo-inject-tmp]]
- [[commands/id]]
- [[commands/hostname-a]]
- [[commands/ps-auxww]]
- [[commands/exit]]
- [[commands/nc-reverse-shell]]

## Tools Used

- [[tools/nc]]

## Tags

- [[verification]]
- [[rce]]
