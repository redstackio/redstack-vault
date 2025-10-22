---
id: 947caf48-e5cf-4a22-ae68-851706f04af3
name: Basic Port Scan and Scripted Service Enumeration
type: procedure
verified: true
submitted: true
created_at: '2019-09-12T18:35:43.404781+00:00'
updated_at: '2023-05-26T00:52:19.234580+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Enumeration]]'
- '[[Network]]'
commands:
- '[[Nmap Service Scan with Default Scripts]]'
---

# Basic Port Scan and Scripted Service Enumeration

**Status**: ✓ Verified

## Summary

Launch a SYN scan against a target and run basic enumeration scripts to identify services. 

## Description

# Description

Launch a SYN scan against a target and run basic enumeration scripts to identify services.

# Instructions

**Command** ([[Nmap Service Scan with Default Scripts]]):

```bash
nmap -sV -sC $_TARGET_IP
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Nmap Service Scan with Default Scripts]]

## Tags

- [[Enumeration]]
- [[Network]]
