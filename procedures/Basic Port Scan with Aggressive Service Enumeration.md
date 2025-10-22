---
id: 0e6f716f-40a3-49ca-8935-dd395fc54b2a
name: Basic Port Scan with Aggressive Service Enumeration
type: procedure
verified: true
submitted: true
created_at: '2019-09-12T18:44:52.509187+00:00'
updated_at: '2023-05-26T00:42:42.415825+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Enumeration]]'
- '[[Network]]'
commands:
- '[[Nmap Aggressive Scan with Version and OS Detection]]'
---

# Basic Port Scan with Aggressive Service Enumeration

**Status**: ✓ Verified

## Summary

Launch a port scan, enumerating services, performing OS detection, and banner grabbing. 

## Description

# Description

Launch a port scan, enumerating services, performing OS detection, and banner grabbing.

# Instructions

**Command** ([[Nmap Aggressive Scan with Version and OS Detection]]):

```bash
nmap -A $_TARGET_IP
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Nmap Aggressive Scan with Version and OS Detection]]

## Tags

- [[Enumeration]]
- [[Network]]
