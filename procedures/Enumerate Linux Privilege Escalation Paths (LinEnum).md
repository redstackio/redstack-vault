---
id: 38adc8a2-8350-4e66-9bdf-b3aca59ece32
name: Enumerate Linux Privilege Escalation Paths (LinEnum)
type: procedure
verified: true
submitted: true
created_at: '2019-10-25T23:13:00.366945+00:00'
updated_at: '2023-05-25T20:11:43.504159+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
- '[[File System Permissions Weakness|T1044 - File System Permissions Weakness]]'
- '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
- '[[Process Discovery|T1057 - Process Discovery]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
- '[[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]'
- '[[System Service Discovery|T1007 - System Service Discovery]]'
platforms:
- BSD
- Linux
tags:
- '[[misconfiguration]]'
- '[[Service Attacks]]'
commands:
- '[[LinEnum.sh Thorough File System Scan]]'
- '[[Scan a Linux Filesystem for Vulnerabilities (LinEnum)]]'
---

# Enumerate Linux Privilege Escalation Paths (LinEnum)

**Status**: ✓ Verified

## Summary

Automatically enumerate a Linux or Unix file environment, scanning for vulnerabilities such as permission issues, security misconfigurations, vulnerable software versions, etc. 

## Description

# Description

Automatically enumerate a Linux or Unix file environment, scanning for vulnerabilities such as permission issues, security misconfigurations, vulnerable software versions, etc. 

# Instructions

1. Download LinEnum and copy it to the target: [Download here](https://github.com/rebootuser/LinEnum)

2. Execute a basic LinEnum scan

**Command** ([[Scan a Linux Filesystem for Vulnerabilities (LinEnum)]]):

```bash
LinEnum.sh
```

3. Perform a thorough scan.

**Command** ([[LinEnum.sh Thorough File System Scan]]):

```bash
LinEnum.sh -t 1
```

## Platforms

- BSD
- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[File System Permissions Weakness|T1044 - File System Permissions Weakness]]
- [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]
- [[Process Discovery|T1057 - Process Discovery]]
- [[System Information Discovery|T1082 - System Information Discovery]]
- [[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]
- [[System Service Discovery|T1007 - System Service Discovery]]

## Commands Used

- [[LinEnum.sh Thorough File System Scan]]
- [[Scan a Linux Filesystem for Vulnerabilities (LinEnum)]]

## Tags

- [[misconfiguration]]
- [[Service Attacks]]
