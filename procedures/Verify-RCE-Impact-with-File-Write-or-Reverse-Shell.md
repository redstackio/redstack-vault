---
id: proc-uuid-5
tags:
  - verification
  - reverse-shell
  - file-write
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/echo-vakzz-file-write]]'
  - '[[commands/id-display-user]]'
  - '[[commands/hostname-show-aliases]]'
  - '[[commands/ps-list-processes]]'
  - '[[commands/spawn-ruby-reverse-shell]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
  - '[[Web Protocols]]'
updated_at: '2025-12-14T17:24:14.937Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
  - '[[Web Protocols]]'
---
# Verify-RCE-Impact-with-File-Write-or-Reverse-Shell

## Summary

Confirm successful RCE by checking for payload effects, such as file creation in /tmp or establishing a reverse shell connection to execute reconnaissance commands as the 'git' user.

## Description

The payload executes as 'git' user on the GitLab server. For simple PoC, verify file write; for advanced, receive a Ruby-based reverse shell allowing commands like id, hostname, and ps to enumerate the environment (Ruby 2.7.2, PostgreSQL 12.6, etc.).

## Requirements

1. Server access or listener setup (nc for shell)
2. Knowledge of payload type (echo or reverse_shell)
3. Tools for checking /tmp or network listener

## Defense

Defensive measures and detection strategies:

- Monitor /tmp for unexpected files
- Block outbound connections from 'git' user processes
- Use EDR to detect anomalous Ruby or Perl executions
- Alert on reverse shell patterns in network traffic

## Objectives

1. Validate code execution and user context
2. Enumerate server environment via shell
3. Confirm impact like file writes or persistence

## Instructions

### Step 1: Check File Write for Echo PoC

**Context**: Verify simple command execution.

SSH to server and check:

```bash
ls -la /tmp/vakzz
cat /tmp/vakzz
```

> Expected: File exists with 'vakzz' content, created by [[commands/echo-vakzz-file-write]].

### Step 2: Set Up Listener for Reverse Shell PoC

**Context**: Prepare to receive the incoming connection.

Run netcat listener:

```bash
nc -lvnp 12345
```

> Expected: Connection from GitLab server IP.

### Step 3: Interact with Shell and Run Commands

**Context**: Execute recon commands over the shell.

In listener, send:

```bash
id
hostname -a
ps auxww
```

> Expected: uid=500(git), hostname like web-09-sv-gprd, process list showing puma/nginx/exiftool, linking to [[commands/id-display-user]], [[commands/hostname-show-aliases]], [[commands/ps-list-processes]]. The shell is spawned by [[commands/spawn-ruby-reverse-shell]].

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Command and Scripting Interpreter: Perl
- [[Web Protocols]] Application Layer Protocol: Web Protocols (for reverse shell)

### Sub-Techniques


## Commands Used

- [[commands/echo-vakzz-file-write]]
- [[commands/id-display-user]]
- [[commands/hostname-show-aliases]]
- [[commands/ps-list-processes]]
- [[commands/spawn-ruby-reverse-shell]]

## Tools Used


## Tags

- rce-verification
- reverse-shell
- enumeration
