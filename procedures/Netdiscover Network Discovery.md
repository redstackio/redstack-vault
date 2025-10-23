---
id: 1916ed79-da75-416f-a25b-849b2a80bc64
name: Netdiscover Network Discovery
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.247259+00:00'
updated_at: '2023-04-10T20:25:08.347945+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Netdiscover]]'
- '[[Network Discovery]]'
commands:
- '[[Scan network for hosts]]'
---

# Netdiscover Network Discovery

## Summary

Netdiscover is a tool used for active scanning and network discovery. It sends ARP packets to discover live hosts on the network, and can also identify the IP and MAC addresses of hosts. This tool can be used by attackers to map out a network and identify potential targets for further attacks. From

## Description

# Description

Netdiscover is a tool used for active scanning and network discovery. It sends ARP packets to discover live hosts on the network, and can also identify the IP and MAC addresses of hosts. This tool can be used by attackers to map out a network and identify potential targets for further attacks. From a defensive perspective, Netdiscover can also be used by security teams to identify unauthorized hosts on the network and detect potential security breaches.

From a technical standpoint, Netdiscover works by sending ARP packets and analyzing the responses. It can be run from the command line and provides a simple interface for scanning networks. The business value of this tool is in its ability to help organizations identify potential security risks and take proactive measures to mitigate them.

 

## Requirements

1. Access to the network being scanned

1. Permission from the network owner to perform the scan

1. Netdiscover tool installed on the system performing the scan

 

## Defense

1. Limit network access to only authorized users and devices

1. Monitor network traffic for suspicious activity

1. Implement network segmentation to limit the impact of a potential breach

 

## Objectives

1. Identify live hosts on a network

1. Map out the network topology

1. Identify potential targets for further attacks

 

# Instructions

1. This command is used to discover hosts on a network. The '-i' flag is used to specify the interface to use and '-r' flag is used to specify the range of IP addresses to scan. The output shows the IP addresses, MAC addresses, count, length, and vendor name of the discovered hosts.

 



**Code**: [[netdiscover -i eth0 -r 192.168.1.0/24
Currently sc]]



> The command 'netdiscover' is used to discover hosts on a network. The '-i' flag is used to specify the interface to use and '-r' flag is used to specify the range of IP addresses to scan. The output shows the IP addresses, MAC addresses, count, length, and vendor name of the discovered hosts. This command can be useful in identifying all the hosts on a network and can be used for security purposes. For example, it can be used to identify unauthorized devices on a network. Additionally, it can be used to troubleshoot network issues by identifying the devices on a network and their respective IP addresses.



**Command** ([[Scan network for hosts]]):

```bash
netdiscover -i eth0 -r 192.168.1.0/24
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Scan network for hosts]]

## Tags

- [[Netdiscover]]
- [[Network Discovery]]


