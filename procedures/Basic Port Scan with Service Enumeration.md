---
id: 5758d331-ac13-44ca-afde-6476996867c4
name: Basic Port Scan with Service Enumeration
type: procedure
verified: true
submitted: true
created_at: '2019-09-12T18:24:17.694083+00:00'
updated_at: '2023-06-24T04:49:52.579043+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Enumeration]]'
- '[[Network]]'
commands:
- '[[Nmap Port Scan with Banner Enumeration]]'
---

# Basic Port Scan with Service Enumeration

**Status**: ✓ Verified

## Summary

Perform an Nmap port scan on a target and enumerate banners of ports 1-1024, as well as popular services (a full list can be found in /usr/share/nmap/nmap-services). 

## Description

# Description

Perform an Nmap port scan on a target and enumerate banners of ports 1-1024, as well as popular services (a full list can be found in /usr/share/nmap/nmap-services).





## Objectives

During a port scan with service enumeration, an adversary's primary objective is to identify the network ports that are open on a target system or network, as well as the services running on those ports. By identifying these services, the attacker can determine if any of them are vulnerable or misconfigured, with the ultimate goal of exploiting them to gain unauthorized access to the target system or network.



1. Scan the basic port range 1-1024 of the target







# Instructions





**Command** ([[Nmap Port Scan with Banner Enumeration]]):

```bash
nmap -sV $_TARGET_IP
```





## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Nmap Port Scan with Banner Enumeration]]

## Tags

- [[Enumeration]]
- [[Network]]


