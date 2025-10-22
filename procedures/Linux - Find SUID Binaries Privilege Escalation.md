---
id: 329beb02-6453-42a4-9316-58cff93604af
name: Linux - Find SUID Binaries Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.822508+00:00'
updated_at: '2023-04-10T20:34:27.113361+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Setuid and Setgid|T1166 - Setuid and Setgid]]'
tags:
- '[[Find SUID binaries]]'
- '[[Linux - Privilege Escalation]]'
- '[[SUID]]'
---

# Linux - Find SUID Binaries Privilege Escalation

## Summary

The Linux Find SUID Binaries Privilege Escalation procedure involves searching for SUID binaries in order to gain escalated privileges. SUID binaries are executables that are owned by a privileged user and have the SUID bit set, which allows anyone who runs the binary to temporarily run it with the

## Description

# Description

The Linux Find SUID Binaries Privilege Escalation procedure involves searching for SUID binaries in order to gain escalated privileges. SUID binaries are executables that are owned by a privileged user and have the SUID bit set, which allows anyone who runs the binary to temporarily run it with the privileges of the file owner. This can be used by attackers to gain elevated privileges and access to sensitive data.

To perform this procedure, the user must first identify potential SUID binaries on the target system. Once identified, the user can analyze the binaries to determine if they can be leveraged to escalate privileges. This procedure can be used as a reconnaissance step in a larger attack.

The business value of this procedure is that it can help identify potential weaknesses in the system and allow for proactive security measures to be taken before an attacker can exploit them.

## Requirements

1. Access to the target system

1. Ability to run commands on the target system

## Defense

1. Regularly review and audit SUID binaries on the system

1. Limit the use of SUID binaries to only necessary executables

1. Implement least privilege access control to limit the potential impact of SUID binary exploitation

## Objectives

1. Identify potential SUID binaries on the target system

1. Analyze the binaries to determine if they can be leveraged to escalate privileges

# Instructions

1. To find all the SUID and SGID files on a system, run this command in the terminal.

**Code**: [[find / -perm -4000 -type f -exec ls -la {} 2>/dev/]]

> This command uses the `find` utility to search for files that have the SUID or SGID bit set. The `-perm -4000` option searches for files with the SUID bit set, and the `-perm -2000` option searches for files with the SGID bit set. The `-type f` option ensures that only files are returned, and not directories. The `-exec ls -la {}` option executes the `ls -la` command on each file found, displaying detailed information about the file. The `2>/dev/null` option redirects any error messages to the null device, suppressing any error messages that may occur. The `\;` option terminates the `find` command.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Setuid and Setgid|T1166 - Setuid and Setgid]]

## Tags

- [[Find SUID binaries]]
- [[Linux - Privilege Escalation]]
- [[SUID]]
