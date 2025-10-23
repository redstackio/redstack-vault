---
id: fdbd2d83-7a46-4eab-944a-e76ca03e62ff
name: Network Discovery with Nmap Full Scan
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.991137+00:00'
updated_at: '2023-04-10T20:25:08.706963+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
- '[[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]'
tags:
- '[[Network Discovery]]'
- '[[Nmap]]'
commands:
- '[[Nmap scan with OS detection, version detection, script scanning, and traceroute]]'
---

# Network Discovery with Nmap Full Scan

## Summary

Network Discovery is the process of identifying hosts, services, and other characteristics of a network. Nmap is a popular tool used for network discovery. A full scan with OS detection and version detection can provide valuable information about the network, including which hosts are active, which

## Description

# Description

Network Discovery is the process of identifying hosts, services, and other characteristics of a network. Nmap is a popular tool used for network discovery. A full scan with OS detection and version detection can provide valuable information about the network, including which hosts are active, which services are running, and which operating systems are in use. This information can be used by attackers to identify potential vulnerabilities and plan further attacks.

From a technical perspective, Nmap sends packets to hosts on the network and analyzes the responses. The OS detection and version detection features use various techniques to identify the operating system and software in use on each host.

From a business perspective, network discovery can help organizations understand their network topology and identify potential security risks. By identifying all hosts and services on the network, organizations can ensure that they have proper security controls in place to protect their assets.

 

## Requirements

1. Access to the network

1. Permission to scan hosts

 

## Defense

1. Limit network access to only authorized users and devices

1. Implement network segmentation to limit the impact of a potential breach

1. Regularly monitor network traffic for suspicious activity

 

## Objectives

1. Identify all hosts and services on the network

1. Identify potential vulnerabilities and security risks

1. Understand the network topology

 

# Instructions

1. To perform a full scan with OS detection and version detection, run the following command:

 



**Code**: [[nmap -A -T4 scanme.nmap.org
• -A: Enable OS detect]]



> This command uses the nmap tool to perform a full scan of the target host 'scanme.nmap.org'. The '-A' option enables OS detection, version detection, script scanning, and traceroute. The '-T4' option defines the timing for the task, with higher values being faster. This command is useful for gathering detailed information about the target host, including its operating system, open ports, and running services.



**Command** ([[Nmap scan with OS detection, version detection, script scanning, and traceroute]]):

```bash
nmap -A -T4 scanme.nmap.org
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]
- [[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]

## Commands Used

- [[Nmap scan with OS detection, version detection, script scanning, and traceroute]]

## Tags

- [[Network Discovery]]
- [[Nmap]]


