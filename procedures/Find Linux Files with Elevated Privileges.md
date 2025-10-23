---
id: ee1cf37e-c22b-44b0-93a5-99d6e2015434
name: Find Linux Files with Elevated Privileges
type: procedure
verified: true
submitted: true
created_at: '2019-10-11T21:24:57.127217+00:00'
updated_at: '2023-05-25T20:12:30.688031+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Setuid and Setgid|T1166 - Setuid and Setgid]]'
platforms:
- Linux
tags:
- '[[Linux]]'
- '[[vulnerability]]'
commands:
- '[[Find List All Files with Setuid Permissions Set]]'
- '[[Getcap List All Files with Capabilities Set]]'
---

# Find Linux Files with Elevated Privileges

**Status**: ✓ Verified

## Summary

Linux and *nix systems include features which allow certain programs to run with elevated privileges. This is a requirement for many system services, but occasionally these programs may allow attackers to execute arbitrary commands. Setuid - Programs with this permission set can run commands as the

## Description

# Description

Linux and *nix systems include features which allow certain programs to run with elevated privileges. This is a requirement for many system services, but occasionally these programs may allow attackers to execute arbitrary commands.



- Setuid - Programs with this permission set can run commands as the program's owner, often set as root.  

- File Capabilities - Programs with these permissions can run certain types of commands that bypass standard permission restrictions. File capabilities can be more specific than setuid permissions, allowing better control of some commands 



Both of these permissions can allow attackers to elevate privileges, and are vital to the Discovery phase.


# Instructions

## Search for Files with Setuid Permissions





**Command** ([[Find List All Files with Setuid Permissions Set]]):

```bash
find / -perm -4000 -ls 2>/dev/null
```





## Search for Files with Capabilities Set





**Command** ([[Getcap List All Files with Capabilities Set]]):

```bash
getcap -r / 2>/dev/null
```



A full list of file capabilities and their use can be found [here](http://man7.org/linux/man-pages/man7/capabilities.7.html)



## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Setuid and Setgid|T1166 - Setuid and Setgid]]

## Commands Used

- [[Find List All Files with Setuid Permissions Set]]
- [[Getcap List All Files with Capabilities Set]]

## Tags

- [[Linux]]
- [[vulnerability]]


