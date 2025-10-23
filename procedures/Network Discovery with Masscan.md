---
id: b20ac768-9d0d-468f-bede-789108368493
name: Network Discovery with Masscan
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.200662+00:00'
updated_at: '2023-04-10T20:25:05.850867+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Masscan]]'
- '[[Network Discovery]]'
---

# Network Discovery with Masscan

## Summary

Network Discovery with Masscan is a reconnaissance technique that allows an attacker to scan a network for open ports and services. Masscan is a high-speed tool that can scan large networks in a short amount of time. Once the attacker has identified open ports and services, they can use this inform

## Description

# Description

Network Discovery with Masscan is a reconnaissance technique that allows an attacker to scan a network for open ports and services. Masscan is a high-speed tool that can scan large networks in a short amount of time. Once the attacker has identified open ports and services, they can use this information to identify potential vulnerabilities and plan their attack. From a technical perspective, Masscan sends packets to the target network and listens for responses. The tool can scan a range of IP addresses and ports simultaneously. The business value of this procedure is that it allows an attacker to gain a better understanding of the target network and identify potential entry points for a successful attack.

 

## Requirements

1. Access to the target network

1. Masscan tool installed on the attacker's system

 

## Defense

1. Ensure that unnecessary ports and services are closed on the target network

1. Implement network segmentation to limit the attacker's access to critical systems

1. Monitor network traffic for suspicious activity

 

## Objectives

1. Identify open ports and services on the target network

1. Identify potential vulnerabilities on the target network

1. Plan an attack based on the information gathered

 

# Instructions

1. This command is used to perform a network scan and service enumeration. It uses masscan to scan for open ports, and then uses nmap to grab banners and service information for the open ports found.

The command has the following steps:
1. Scan the network for active machines using masscan.
2. Scan for open ports on a specific machine using masscan.
3. Use nmap to grab banners and service information for the open ports found.

The command takes in the following arguments:
- ips-online.txt: A file containing a list of IP addresses.
- $ROUTER_IP: The IP address of the router.
- $NETWORK: The network to scan.
- $MACHINE_IP: The IP address of the machine to scan.

Note that sudo privileges are required to run this command.

 



**Code**: [[masscan -iL ips-online.txt --rate 10000 -p1-65535 ]]



> This command is useful for identifying machines on a network and their open ports. It can help identify potential vulnerabilities and services that are running on the machines. The command can be used by security professionals and network administrators to perform regular network scans and identify potential security risks.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Tags

- [[Masscan]]
- [[Network Discovery]]


