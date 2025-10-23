---
id: 099d05fb-ad74-41f2-8afd-ae16bbb7069a
name: Monitor Processes and Commands
type: procedure
verified: true
submitted: true
created_at: '2019-10-22T18:03:37.431650+00:00'
updated_at: '2023-05-26T00:44:20.693676+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Service Discovery|T1007 - System Service Discovery]]'
platforms:
- Linux
tags:
- '[[Enumeration]]'
- '[[Service Attacks]]'
commands:
- '[[pspy Monitor Processes and Commands]]'
---

# Monitor Processes and Commands

**Status**: ✓ Verified

## Summary

Pspy is a utility that can monitor and  report on commands run on the system. This can allow a low privilege user to view commands run by other higher privilege users, cron jobs, system processes, etc. 

## Description

# Description

Pspy is a utility that can monitor and  report on commands run on the system. This can allow a low privilege user to view commands run by other higher privilege users, cron jobs, system processes, etc.



# Instructions

1. Download  pspy (static version) which matches the target architecture: [Download from Github](https://github.com/DominicBreuker/pspy)

2. Copy the binary to the target system.
3. Run pspy with no arguments.





**Command** ([[pspy Monitor Processes and Commands]]):

```bash
pspy
```





## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Service Discovery|T1007 - System Service Discovery]]

## Commands Used

- [[pspy Monitor Processes and Commands]]

## Tags

- [[Enumeration]]
- [[Service Attacks]]


