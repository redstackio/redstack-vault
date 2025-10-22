---
id: 02af3d7c-4e91-4a51-b2ee-b02824d028fd
name: Basic Nmap Scan Procedure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.964588+00:00'
updated_at: '2023-04-10T20:25:04.645566+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Network Discovery]]'
- '[[Nmap]]'
commands:
- '[[Nmap initial scan with service and version detection and scripts enabled]]'
---

# Basic Nmap Scan Procedure

## Summary

The Basic Nmap Scan Procedure is a network reconnaissance technique that leverages the Nmap tool to identify active hosts and open ports on a network. It is commonly used by attackers to gather information on a target network and identify potential vulnerabilities that can be exploited. From a tech

## Description

# Description

The Basic Nmap Scan Procedure is a network reconnaissance technique that leverages the Nmap tool to identify active hosts and open ports on a network. It is commonly used by attackers to gather information on a target network and identify potential vulnerabilities that can be exploited. From a technical perspective, Nmap sends packets to target hosts and analyzes the responses to determine which ports are open and which services are running. This procedure can provide valuable insights into a network's topology and configuration, which can be used to plan further attacks. From a business perspective, this procedure can help organizations identify weaknesses in their security posture and take steps to improve their defenses.

## Requirements

1. Access to the target network

1. Nmap tool installed on the system

## Defense

1. Implement network segmentation to limit the impact of a successful network scan

1. Use firewalls to block unnecessary traffic and restrict access to sensitive systems

1. Regularly monitor network traffic and logs for signs of suspicious activity

## Objectives

1. Identify active hosts on a network

1. Determine which ports are open on target hosts

1. Identify services running on open ports

# Instructions

1. Run the above command to perform a basic Nmap scan on a target IP address. This command will probe open ports to determine service/version information, enable scripts and save the results to a file. You can add "-p-" to run a full scan while you work with the previous result.

**Code**: [[nmap -sV -sC -oA ~/nmap-initial 192.168.1.1

-sV :]]

> The 'nmap' command is a network exploration tool and security scanner that can be used to discover hosts and services on a computer network, thus creating a 'map' of the network. The '-sV' option is used to probe open ports to determine service/version information. The '-sC' option is used to enable scripts, which can be used to automate various tasks. The '-oA' option is used to save the results of the scan in multiple formats. By default, Nmap scans the most common 1,000 ports. Adding '-p-' to the command will scan all ports.

**Command** ([[Nmap initial scan with service and version detection and scripts enabled]]):

```bash
nmap -sV -sC -oA ~/nmap-initial 192.168.1.1
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Nmap initial scan with service and version detection and scripts enabled]]

## Tags

- [[Network Discovery]]
- [[Nmap]]
