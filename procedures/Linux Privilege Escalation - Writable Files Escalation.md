---
id: 73ad0400-d09b-4fc6-8012-b52620b6956a
name: Linux Privilege Escalation - Writable Files Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.149856+00:00'
updated_at: '2023-04-10T20:34:32.693736+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Clipboard Data|T1115 - Clipboard Data]]'
- '[[Code Signing|T1116 - Code Signing]]'
- '[[Component Firmware|T1109 - Component Firmware]]'
- '[[Email Collection|T1114 - Email Collection]]'
- '[[Execution through API|T1106 - Execution through API]]'
- '[[File Deletion|T1107 - File Deletion]]'
- '[[InstallUtil|T1118 - InstallUtil]]'
- '[[Redundant Access|T1108 - Redundant Access]]'
- '[[Regsvr32|T1117 - Regsvr32]]'
- '[[Remote File Copy|T1105 - Remote File Copy]]'
- '[[Screen Capture|T1113 - Screen Capture]]'
tags:
- '[[Linux - Privilege Escalation]]'
- '[[Writable files]]'
---

# Linux Privilege Escalation - Writable Files Escalation

## Summary

Writable files escalation is a common technique used in Linux privilege escalation attacks. This technique allows an attacker to escalate their privileges by modifying or adding files that are writable by privileged users. This could include modifying system files, adding new users with elevated pr

## Description

# Description

Writable files escalation is a common technique used in Linux privilege escalation attacks. This technique allows an attacker to escalate their privileges by modifying or adding files that are writable by privileged users. This could include modifying system files, adding new users with elevated privileges, or modifying configuration files to allow for persistence. This technique is often used in combination with other techniques to achieve full system compromise.

To perform this technique, the attacker first needs to identify writable files that can be used for escalation. This can be done using tools like Writable Files Finder, which scans the system for files that can be written to by privileged users. Once the attacker has identified a writable file, they can modify it to add their own code, or use it to escalate their privileges in other ways.

This technique can be very effective, as it allows an attacker to gain full control over a system. However, it can also be easily detected and prevented by implementing proper file permissions and monitoring.

 

## Requirements

1. Access to a Linux system with writable files

1. Writable Files Finder tool

 

## Defense

1. Implement proper file permissions to limit write access to critical files

1. Monitor system logs for suspicious file modifications

1. Use intrusion detection and prevention systems to detect and block privilege escalation attempts

 

## Objectives

1. Gain elevated privileges on the target system

1. Achieve persistence on the target system

 

# Instructions

1. The above commands can be used to find all writable files in the system. The first command searches for all files that are writable by anyone other than the current user and are not located in /proc/ or /sys/ directories. The second command searches for all files that have the setuid or setgid bit set and are writable by anyone. The third command searches for all files that are writable by anyone and are not located in /proc/ directory.

 



**Code**: [[find / -writable ! -user `whoami` -type f ! -path ]]



> Arguments:
- `find /`: Search for files starting from the root directory.
- `-writable`: Search for files that are writable.
- `! -user `whoami``: Search for files that are not owned by the current user.
- `-type f`: Search for regular files only.
- `! -path "/proc/*" ! -path "/sys/*"`: Exclude files located in /proc/ and /sys/ directories.
- `-exec ls -al {} \;`: Execute `ls -al` on each file found.
- `2>/dev/null`: Redirect error messages to null device.
- `-perm -2`: Search for files that have the setuid or setgid bit set.
- `! -path "*/proc/*"`: Exclude files located in /proc/ directory.
- `-print`: Print the file name.
- `2>/dev/null`: Redirect error messages to null device.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Command and Control|TA0011 - Command and Control]]
- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Clipboard Data|T1115 - Clipboard Data]]
- [[Code Signing|T1116 - Code Signing]]
- [[Component Firmware|T1109 - Component Firmware]]
- [[Email Collection|T1114 - Email Collection]]
- [[Execution through API|T1106 - Execution through API]]
- [[File Deletion|T1107 - File Deletion]]
- [[InstallUtil|T1118 - InstallUtil]]
- [[Redundant Access|T1108 - Redundant Access]]
- [[Regsvr32|T1117 - Regsvr32]]
- [[Remote File Copy|T1105 - Remote File Copy]]
- [[Screen Capture|T1113 - Screen Capture]]

## Tags

- [[Linux - Privilege Escalation]]
- [[Writable files]]


