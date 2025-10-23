---
id: 761a0091-36fd-441c-ab52-5e708870d53e
name: Network Discovery with Nmap
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.909410+00:00'
updated_at: '2023-04-10T20:25:09.453398+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
- '[[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]'
tags:
- '[[Network Discovery]]'
- '[[Nmap]]'
commands:
- '[[Host Discovery using nmap]]'
---

# Network Discovery with Nmap

## Summary

Network discovery is an essential first step in any offensive operation. Nmap is a powerful tool for discovering live hosts on a network. It can be used to scan a range of IP addresses and identify hosts that are up and responding to network traffic. This information can be used to identify potenti

## Description

# Description

Network discovery is an essential first step in any offensive operation. Nmap is a powerful tool for discovering live hosts on a network. It can be used to scan a range of IP addresses and identify hosts that are up and responding to network traffic. This information can be used to identify potential targets for further exploitation.

Technically, Nmap sends packets to the target network and analyzes the responses. It can detect hosts that are up by sending ICMP echo requests (ping), TCP SYN packets, or UDP packets. Nmap can also identify open ports and services running on the target hosts.

From a business perspective, network discovery can help an organization identify potential vulnerabilities and improve their overall security posture.

 

## Requirements

1. Access to the target network

1. Permission to perform network scanning

1. Nmap installed on the attacker's system

 

## Defense

1. Segment your network to limit the scope of the scan

1. Use intrusion detection systems to detect and alert on Nmap scans

1. Implement network access controls to limit access to sensitive systems

 

## Objectives

1. Identify live hosts on a network

1. Identify open ports and services on target hosts

1. Identify potential targets for further exploitation

 

# Instructions

1. Use this command to discover live hosts on the network.

 



**Code**: [[nmap -sn -n --disable-arp-ping 192.168.1.1-254 | g]]



> This command uses nmap to perform a host discovery scan on the specified IP range. The '-sn' flag disables port scanning and only performs host discovery. The '-n' flag disables DNS resolution. The output is then piped to grep to remove any lines containing 'host down', which indicates that the host is not live. This command is useful for identifying active hosts on a network.



**Command** ([[Host Discovery using nmap]]):

```bash
nmap -sn -n --disable-arp-ping 192.168.1.1-254 | grep -v "host down"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]
- [[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]

## Commands Used

- [[Host Discovery using nmap]]

## Tags

- [[Network Discovery]]
- [[Nmap]]


