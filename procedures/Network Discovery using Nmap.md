---
id: 0e777ad6-78e0-4dc6-8712-86343694ae95
name: Network Discovery using Nmap
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.017045+00:00'
updated_at: '2023-04-10T20:25:10.309187+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Application Window Discovery|T1010 - Application Window Discovery]]'
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Network Discovery]]'
- '[[Nmap]]'
commands:
- '[[Port Scan with nmap and searchsploit]]'
---

# Network Discovery using Nmap

## Summary

Network Discovery using Nmap is a process of identifying hosts and services on a network by sending packets and analyzing the responses. This procedure is commonly used by attackers to identify potential attack vectors and vulnerabilities on a network. Nmap is a powerful tool that can be used to pe

## Description

# Description

Network Discovery using Nmap is a process of identifying hosts and services on a network by sending packets and analyzing the responses. This procedure is commonly used by attackers to identify potential attack vectors and vulnerabilities on a network. Nmap is a powerful tool that can be used to perform a wide range of network scanning and reconnaissance tasks. It can be used to identify open ports, running services, and operating systems on a target network. By analyzing the results of a network scan, an attacker can identify potential vulnerabilities and misconfigurations that can be exploited to gain unauthorized access to a network.

## Requirements

1. Access to the target network

1. Nmap tool installed on the attacker's system

## Defense

1. Implement network segmentation to limit the impact of a successful network discovery

1. Monitor network traffic and log all network scans and reconnaissance activities

1. Implement access control measures to prevent unauthorized access to the target network

## Objectives

1. Identify hosts and services on a target network

1. Identify potential attack vectors and vulnerabilities on a network

1. Identify misconfigurations that can be exploited to gain unauthorized access to a network

# Instructions

1. This command performs a port scan on the specified IP address using nmap and saves the results in an XML file. It then uses the searchsploit tool to search for exploits related to the identified services and ports. 

**Code**: [[nmap -p- -sV -oX a.xml IP_ADDRESS; searchsploit --]]

> The nmap command performs a port scan on the specified IP address. The -p- option tells nmap to scan all ports. The -sV option enables version detection for each service that is found. The -oX option specifies that the results should be saved in an XML file named a.xml.

The searchsploit command searches the a.xml file for exploits related to the identified services and ports. The --nmap option tells searchsploit to use the nmap XML output format.

Note: This command requires the nmap and searchsploit tools to be installed on the system.

**Command** ([[Port Scan with nmap and searchsploit]]):

```bash
nmap -p- -sV -oX a.xml IP_ADDRESS; searchsploit --nmap a.xml
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Application Window Discovery|T1010 - Application Window Discovery]]
- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Port Scan with nmap and searchsploit]]

## Tags

- [[Network Discovery]]
- [[Nmap]]
