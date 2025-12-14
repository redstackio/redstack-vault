---
tags:
  - strace
  - system-calls
  - debugging
type: procedure
tools:
  - '[[tools/strace]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/strace-trace-server]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:24:22.454Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: e0c42e59-5c01-4799-b23a-354113d48d15
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Trace-Server-System-Calls-with-strace

## Summary

This procedure employs strace to monitor system calls on a server (e.g., Burp Collaborator) during high-concurrency requests, confirming no server-side anomalies and attributing issues to the client (Burp Suite).

## Description

Attach strace to the server process while running multi-threaded requests from Burp Intruder. This traces network, file, and process syscalls to rule out server bugs like buffering errors. The scenario targets Linux servers in a local pentest lab, with outcomes validating clean server behavior and suspecting client async flaws. Prerequisites include server PID identification via ps or top.

## Requirements

1. Linux system with strace installed
2. Running server process (e.g., Collaborator or custom HTTP)
3. Concurrent load from Burp or similar

## Defense

Defensive measures and detection strategies:

- Log syscall anomalies for intrusion detection
- Use seccomp to restrict unnecessary syscalls in servers
- Regularly audit server processes under load

## Objectives

1. Verify server integrity during stress
2. Isolate anomalies to client tools
3. Provide evidence for vulnerability reproduction

## Instructions

### Step 1: Identify and Attach strace

**Context**: Find the server PID and trace relevant syscalls like network I/O.

**Command** ([[commands/strace-trace-server]]):
```bash
strace -p <server_pid> -e trace=network,read,write -o strace_collaborator.log
```

> Replace <server_pid> with actual PID (e.g., from ps aux | grep server); this captures syscalls without halting the process. Expected: Log file with timestamped calls showing normal accept/send/recv.

### Step 2: Induce Load and Review

**Context**: Trigger requests from Burp while tracing, then analyze for issues.

**Command** (Review Log):
```bash
cat strace_collaborator.log | grep -i error
```

> Run during Intruder attack; grep for errors or unusual patterns. Expected: No errors, confirming server-side cleanliness.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Disable or Modify Tools]] Impair Defenses: Disable or Modify Tools

### Sub-Techniques


## Commands Used

- [[commands/strace-trace-server]]

## Tools Used

- [[tools/strace]]

## Tags

- strace
- debugging
- linux
