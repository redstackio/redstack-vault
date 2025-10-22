---
id: 7d6252d6-e109-462a-9c6d-42718fb182f6
name: Linux - Suid Binary Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.934014+00:00'
updated_at: '2023-04-10T20:34:16.545366+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
sub_techniques:
- '[[Elevated Execution with Prompt|T1548.004 - Elevated Execution with Prompt]]'
tags:
- '[[Linux - Persistence]]'
- '[[Suid Binary]]'
---

# Linux - Suid Binary Persistence

## Summary

The Suid Binary Persistence procedure involves creating a SUID binary that will run with elevated privileges every time the system boots. This technique can be used by attackers to maintain persistence on the system even after a reboot. Attackers can create a SUID binary by copying an existing bina

## Description

# Description

The Suid Binary Persistence procedure involves creating a SUID binary that will run with elevated privileges every time the system boots. This technique can be used by attackers to maintain persistence on the system even after a reboot. Attackers can create a SUID binary by copying an existing binary with elevated privileges and modifying its code to include a backdoor. Once the binary is executed, the backdoor will be opened, giving the attacker remote access to the system.

From a technical perspective, SUID (Set User ID) is a special type of file permission that allows a user to run a program with the permissions of the file owner. By creating a SUID binary, an attacker can run a program with elevated privileges without needing to authenticate. This procedure can be used by attackers to gain access to sensitive files or execute malicious code with elevated privileges.

The business value of this procedure is that it allows attackers to maintain access to a compromised system even after a reboot. This can be used to steal sensitive data, install additional malware or use the system as a jumping-off point for further attacks.

## Requirements

1. Access to the target system with the ability to create files.

1. Knowledge of Linux command line and file permissions.

## Defense

1. Monitor the system for any new SUID binaries that are created.

1. Restrict access to sensitive files and directories.

1. Implement the principle of least privilege to limit the impact of a successful attack.

## Objectives

1. Create a SUID binary that will run with elevated privileges every time the system boots.

1. Maintain persistence on the system even after a reboot.

1. Gain access to sensitive files or execute malicious code with elevated privileges.

# Instructions

1. This command creates a setuid binary called 'croissant' in the /var/tmp directory. The binary is compiled from a C code which spawns a shell with root privileges. The binary is then given the setuid bit which allows any user to execute it with root privileges.

**Code**: [[TMPDIR2="/var/tmp"
echo 'int main(void){setresuid(]]

> The 'TMPDIR2' variable is set to '/var/tmp'. A C code is then written to a file called 'croissant.c' in the '/var/tmp' directory. The C code is compiled using gcc and the binary is named 'croissant'. The C code spawns a shell with root privileges using the 'setresuid(0, 0, 0);system("/bin/sh");' command. The 'croissant.c' file is then removed. The ownership of the 'croissant' binary is changed to 'root:root' and the setuid bit is set using 'chmod 4777'. This allows any user to execute the binary with root privileges.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]

### Sub-Techniques

- [[Elevated Execution with Prompt|T1548.004 - Elevated Execution with Prompt]]

## Tags

- [[Linux - Persistence]]
- [[Suid Binary]]
