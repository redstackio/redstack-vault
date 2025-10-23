---
id: 375d0d9c-2b9d-40eb-8a48-34bcb8224cde
name: Network Reconnaissance Procedure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.222746+00:00'
updated_at: '2023-04-10T20:25:06.545309+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Network Discovery]]'
- '[[Reconnoitre]]'
---

# Network Reconnaissance Procedure

## Summary

The Network Reconnaissance Procedure is used to discover and map out the target network. This procedure is typically used in the initial stages of an attack to gather information about the target network, such as IP addresses, open ports, and services running on those ports. Active scanning techniq

## Description

# Description

The Network Reconnaissance Procedure is used to discover and map out the target network. This procedure is typically used in the initial stages of an attack to gather information about the target network, such as IP addresses, open ports, and services running on those ports. Active scanning techniques such as port scanning and service enumeration are used to identify potential vulnerabilities that can be exploited. Passive scanning techniques such as sniffing network traffic can also be used to gather information without alerting the target network.

From a technical perspective, this procedure involves the use of various tools and techniques to scan and map the target network. These tools include Nmap, Netcat, and Wireshark, among others. The information gathered during this procedure can be used to plan and execute further attacks on the target network.

The business value of this procedure lies in its ability to identify potential vulnerabilities in the target network. By identifying these vulnerabilities, organizations can take steps to patch and secure their systems, thereby reducing the risk of a successful attack.

 

## Requirements

1. Access to the target network

1. Tools such as Nmap, Netcat, and Wireshark

 

## Defense

1. Implement network segmentation to limit the scope of the attack

1. Use intrusion detection and prevention systems to detect and block malicious traffic

1. Regularly patch and update systems to address known vulnerabilities

 

## Objectives

1. Discover and map out the target network

1. Identify potential vulnerabilities that can be exploited

1. Gather information for further attacks

 

# Instructions

1. This command performs network reconnaissance by scanning a range of IP addresses and gathering information about the hosts including hostnames and services running on them. To use this command, you must have Nmap, Python 2.7, and Git installed on your system.

 



**Code**: [[python2.7 ./reconnoitre.py -t 192.168.1.2-252 -o .]]



> -t: specifies the target IP address range to scan
-o: specifies the output directory for the scan results
--pingsweep: performs a ping sweep to determine which hosts are up
--hostnames: performs DNS resolution to determine hostnames
--services: performs service detection to determine which services are running on the hosts
--quick: performs a quick scan by skipping some of the more time-consuming scans

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Tags

- [[Network Discovery]]
- [[Reconnoitre]]


