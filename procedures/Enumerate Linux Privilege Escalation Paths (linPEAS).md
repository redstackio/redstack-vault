---
id: e5980341-1b7c-4e14-9ea8-9018f2ef6507
name: Enumerate Linux Privilege Escalation Paths (linPEAS)
type: procedure
verified: true
submitted: true
created_at: '2020-03-22T20:49:40.657781+00:00'
updated_at: '2023-05-26T00:46:59.578445+00:00'
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
- '[[Enumeration]]'
- '[[misconfiguration]]'
commands:
- '[[linPEAS Enumerate a Linux/Unix System with All Checks]]'
---

# Enumerate Linux Privilege Escalation Paths (linPEAS)

**Status**: ✓ Verified

## Summary

Automatically enumerate a Linux/BSD/Unix environment, scanning for vulnerabilities, misconfigurations, vulnerable software versions, etc. Pay close attention to any results appearing in red or red/yellow, as these indicate especially promising results. 

## Description

# Description

Automatically enumerate a Linux/BSD/Unix environment, scanning for vulnerabilities, misconfigurations, vulnerable software versions, etc. Pay close attention to any results appearing in red or red/yellow, as these indicate especially promising results.



# Instructions

1. Download linPEAS.sh and copy it to the target: [Download from GitHub](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS)

2. Execute linPEAS from a terminal.





**Command** ([[linPEAS Enumerate a Linux/Unix System with All Checks]]):

```bash
linpeas.sh -a
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

- [[linPEAS Enumerate a Linux/Unix System with All Checks]]

## Tags

- [[Enumeration]]
- [[misconfiguration]]


