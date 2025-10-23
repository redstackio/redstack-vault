---
id: 1fce62e4-778b-4a93-b78c-572637ee1edd
name: Thorough Port Scan with Service Enumeration
type: procedure
verified: true
submitted: true
created_at: '2019-10-11T19:37:17.178400+00:00'
updated_at: '2023-05-26T00:40:33.582175+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
tags:
- '[[Enumeration]]'
- '[[Network]]'
commands:
- '[[Nmap Full Port Scan with Service Enumeration]]'
- '[[Nmap Scan with Service Enumeration]]'
- '[[Nmap UDP Scan with Service Enumeration]]'
---

# Thorough Port Scan with Service Enumeration

**Status**: ✓ Verified

## Summary

Query a computer's services by probing the ports on which it listens. Since each system potentially has 65,535 ports for TCP and UDP, it's often best to perform multiple scans, each focusing on a different technique or port range. 

## Description

# Description

Query a computer's services by probing the ports on which it listens. Since each system potentially has 65,535 ports for TCP and UDP, it's often best to perform multiple scans, each focusing on a different technique or port range. 



# Instructions

Each of the following scans become progressively more noisy and intrusive as they enumerate more in depth. Running all of the scans is generally not necessary, but may be required if initial scans show no useful information. 



1. Perform an initial SYN scan targeting popular ports, grabbing banners, and outputting the results to a file.





**Command** ([[Nmap Scan with Service Enumeration]]):

```bash
nmap -sV $_TARGET_IP -oN $_OUTPUT
```





2. Perform a UDP port scan and output the results to a file





**Command** ([[Nmap UDP Scan with Service Enumeration]]):

```bash
nmap -sU -sV $_TARGET_IP -oN $_OUTPUT
```





3.  Perform a full TCP port scan. This scan will take longer than others, as it queries all ports.





**Command** ([[Nmap Full Port Scan with Service Enumeration]]):

```bash
nmap -sV -p- $TARGET_IP -oN $OUTPUT
```





## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]

## Commands Used

- [[Nmap Full Port Scan with Service Enumeration]]
- [[Nmap Scan with Service Enumeration]]
- [[Nmap UDP Scan with Service Enumeration]]

## Tags

- [[Enumeration]]
- [[Network]]


