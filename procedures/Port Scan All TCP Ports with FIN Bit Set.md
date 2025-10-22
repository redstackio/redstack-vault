---
id: 6be0a602-f92b-446a-b7f6-53d330b4d9f4
name: Port Scan All TCP Ports with FIN Bit Set
type: procedure
verified: true
submitted: true
created_at: '2019-09-12T19:01:25.720362+00:00'
updated_at: '2023-05-26T00:47:29.774295+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Enumeration]]'
- '[[Network]]'
commands:
- '[[Nmap FIN Scan with Service Enumeration]]'
---

# Port Scan All TCP Ports with FIN Bit Set

**Status**: ✓ Verified

## Summary

Firewalls may not disclose all listening ports to a SYN scan, and other scans are needed. A FIN scan monitors different aspects of a TCP handshake, and may discover more ports. 

## Description

# Description

Firewalls may not disclose all listening ports to a SYN scan, and other scans are needed. A FIN scan monitors different aspects of a TCP handshake, and may discover more ports.

# Instructions

**Command** ([[Nmap FIN Scan with Service Enumeration]]):

```bash
nmap -sV -sF -p- $_TARGET_IP
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Nmap FIN Scan with Service Enumeration]]

## Tags

- [[Enumeration]]
- [[Network]]
