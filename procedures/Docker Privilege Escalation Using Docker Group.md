---
id: d96906be-8cd0-491f-8571-e56a7be8da6c
name: Docker Privilege Escalation Using Docker Group
type: procedure
verified: true
submitted: true
created_at: '2019-10-09T19:15:07.945476+00:00'
updated_at: '2023-05-26T00:47:41.916274+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[File System Permissions Weakness|T1044 - File System Permissions Weakness]]'
tags:
- '[[Hypervisors]]'
- '[[known vulnerability]]'
- '[[misconfiguration]]'
commands:
- '[[Docker Mount a Host''s Root Directory in a Container]]'
---

# Docker Privilege Escalation Using Docker Group

**Status**: ✓ Verified

## Summary

Docker host systems with users who are part of the "docker" group are able to escalate privileges to root by mounting the root file system within a container, bypassing permissions on the host system. This is considered a misconfiguration, as non-admin users should never be added to this group. 

## Description

# Description

Docker host systems with users who are part of the "docker" group are able to escalate privileges to root by mounting the root file system within a container, bypassing permissions on the host system. This is considered a misconfiguration, as non-admin users should never be added to this group.





# Instructions

Mount the root file system within the Docker container



**Command** ([[Docker Mount a Host's Root Directory in a Container]]):

```bash
docker run -v /:/root_fs -i -t bash bash
```





## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[File System Permissions Weakness|T1044 - File System Permissions Weakness]]

## Commands Used

- [[Docker Mount a Host's Root Directory in a Container]]

## Tags

- [[Hypervisors]]
- [[known vulnerability]]
- [[misconfiguration]]


