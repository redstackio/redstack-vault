---
id: 9c2e6154-9aa4-4d6c-a595-2561fbb9f561
name: Ping Sweep a Subnet for Online Hosts
type: procedure
verified: true
submitted: true
created_at: '2019-09-11T20:46:03.582746+00:00'
updated_at: '2023-05-26T00:51:50.193820+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Remote System Discovery|T1018 - Remote System Discovery]]'
tags:
- '[[Enumeration]]'
- '[[Network]]'
commands:
- '[[Nmap Ping Sweep]]'
---

# Ping Sweep a Subnet for Online Hosts

**Status**: ✓ Verified

## Summary

Perform host discovery on an entire subnet, identifying online hosts using ping and queries to popular ports. 

## Description

# Description

Perform host discovery on an entire subnet, identifying online hosts using ping and queries to popular ports.



# Instructions





**Command** ([[Nmap Ping Sweep]]):

```bash
nmap -sn $_TARGET_IP/$_CIDR
```





## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Remote System Discovery|T1018 - Remote System Discovery]]

## Commands Used

- [[Nmap Ping Sweep]]

## Tags

- [[Enumeration]]
- [[Network]]


