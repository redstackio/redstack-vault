---
id: 1973b52d-79ba-48d9-8e67-85234a505dca
name: Network Discovery with Nmap Service Version Detection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.040013+00:00'
updated_at: '2023-05-26T00:58:41.239584+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Network Discovery]]'
- '[[Nmap]]'
---

# Network Discovery with Nmap Service Version Detection

## Summary

Network Discovery with Nmap Service Version Detection is a technique used to identify active hosts, open ports and running services on a network. This technique can be used by attackers to map out the network topology and identify potential attack vectors. Nmap is a popular tool used for network sc

## Description

# Description

Network Discovery with Nmap Service Version Detection is a technique used to identify active hosts, open ports and running services on a network. This technique can be used by attackers to map out the network topology and identify potential attack vectors. Nmap is a popular tool used for network scanning and reconnaissance. It can be used to identify hosts, open ports and services running on those ports. By using Nmap's service version detection feature, an attacker can identify the exact version of the service running on a port, which can be useful for identifying known vulnerabilities and exploits. 

From a technical perspective, this technique involves sending packets to a range of IP addresses and ports on a network and analyzing the responses. Nmap uses various techniques such as TCP SYN scan, TCP connect scan, UDP scan and others to identify open ports and services. Once the open ports and services are identified, Nmap sends probes to those ports to identify the exact version of the service running on that port. 

The business value of this technique is that it can help organizations identify potential vulnerabilities and weaknesses in their network infrastructure before attackers can exploit them. By identifying open ports and services, organizations can take proactive measures to secure those services and prevent attackers from gaining unauthorized access.

## Requirements

1. Access to the network being scanned

1. Permission from the network owner

1. Nmap tool installed on the scanning machine

## Defense

1. Implement network segmentation to limit the attack surface

1. Use firewalls to restrict access to sensitive services

1. Regularly scan the network for open ports and services to identify potential vulnerabilities

## Objectives

1. Identify active hosts on a network

1. Identify open ports and services running on those ports

1. Identify the exact version of the service running on a port

# Instructions

1. This command uses Nmap to perform a scan on the specified IP address, with service version detection enabled. The '-oX' flag saves the output in XML format to a file called 'scan.xml'. The '&&' operator is used to chain the next command, which uses 'xsltproc' to convert the XML output to an HTML report file with the current date appended to the file name.

**Code**: [[nmap -sV IP_ADDRESS -oX scan.xml && xsltproc scan.]]

> The 'nmap' command is a network exploration and security auditing tool. The '-sV' flag enables service version detection, which attempts to determine the version of the service running on the specified IP address. The '-oX' flag specifies the output format as XML and saves the output to a file called 'scan.xml'. The '&&' operator is used to chain the next command, which executes 'xsltproc' to convert the XML output to an HTML report file. The '-o' flag specifies the output file name, which includes the current date in the format 'mmddyy'.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Tags

- [[Network Discovery]]
- [[Nmap]]
