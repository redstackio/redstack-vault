---
id: 881bce42-157a-4a0d-9e98-83b4d20a8986
name: Scan Ports for Services with No Host Discovery
type: procedure
verified: false
submitted: false
created_at: '2019-09-12T18:53:18.223938+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Enumeration]]'
- '[[Network]]'
commands:
- '[[Nmap Service Scan with No Host Discovery]]'
---

# Scan Ports for Services with No Host Discovery

## Summary

Skip host discovery in cases where a host does not respond to ping, and enumerate banners. 

## Description

# Description

Skip host discovery in cases where a host does not respond to ping, and enumerate banners.

**Command** ([[Nmap Service Scan with No Host Discovery]]):

```bash
nmap -sV -Pn $_TARGET_IP
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Nmap Service Scan with No Host Discovery]]

## Tags

- [[Enumeration]]
- [[Network]]
