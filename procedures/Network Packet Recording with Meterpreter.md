---
id: e53ef3f3-7e8e-4364-8680-2b820d4b178f
name: Network Packet Recording with Meterpreter
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.433515+00:00'
updated_at: '2023-04-10T20:24:58.736284+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Sniffing|T1040 - Network Sniffing]]'
tags:
- '[[Metasploit]]'
- '[[Meterpreter - Basic]]'
- '[[Network Monitoring]]'
commands:
- '[[List interfaces using packetrecorder]]'
- '[[Record packets on interface 1 using packetrecorder]]'
---

# Network Packet Recording with Meterpreter

## Summary

This procedure is used to monitor network traffic by capturing packets on the target network. It is accomplished using the Packet Recorder Interface Listing and Recording command in Meterpreter. This technique can be used to gather information about the target network, such as identifying network t

## Description

# Description

This procedure is used to monitor network traffic by capturing packets on the target network. It is accomplished using the Packet Recorder Interface Listing and Recording command in Meterpreter. This technique can be used to gather information about the target network, such as identifying network topology and discovering hosts and services. It can also be used to capture sensitive information such as usernames and passwords, and to perform man-in-the-middle attacks.

The Packet Recorder Interface Listing and Recording command in Meterpreter provides a powerful tool for reconnaissance and attack. By capturing packets on the target network, an attacker can gain valuable information about the network and its hosts. This technique can be used to identify vulnerable hosts, discover open ports and services, and gather information about the network topology. Additionally, by capturing sensitive information such as usernames and passwords, an attacker can perform further attacks such as password cracking and privilege escalation. Finally, by performing man-in-the-middle attacks, an attacker can intercept and modify network traffic, allowing them to perform further attacks or exfiltrate sensitive data.

## Requirements

1. Meterpreter access to a target machine on the target network

1. Sufficient network access to capture desired traffic

## Defense

1. Implement network segmentation to limit access to sensitive systems and data

1. Use encrypted protocols such as HTTPS and SSH to protect sensitive information in transit

1. Monitor network traffic for suspicious activity and anomalous behavior

## Objectives

1. Capture network traffic on the target network

1. Identify hosts and services on the target network

1. Gather sensitive information such as usernames and passwords

1. Perform man-in-the-middle attacks

# Instructions

1. This command is used to list interfaces and record packets from a specific interface. 

To list all available interfaces, run the command 'run packetrecorder -li'. This will display a list of all available interfaces on your system.

To record packets from a specific interface, run the command 'run packetrecorder -i [interface_number]'. Replace [interface_number] with the number of the interface you want to record packets from. For example, if you want to record packets from interface number 1, run the command 'run packetrecorder -i 1'.

**Code**: [[# list interfaces
run packetrecorder -li

# record]]

> The '-li' option is used to list all available interfaces on your system.

The '-i' option is used to specify the interface from which packets will be recorded. Replace [interface_number] with the number of the interface you want to record packets from.

**Command** ([[List interfaces using packetrecorder]]):

```bash
run packetrecorder -li
```

**Command** ([[Record packets on interface 1 using packetrecorder]]):

```bash
run packetrecorder -i 1
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Sniffing|T1040 - Network Sniffing]]

## Commands Used

- [[List interfaces using packetrecorder]]
- [[Record packets on interface 1 using packetrecorder]]

## Tags

- [[Metasploit]]
- [[Meterpreter - Basic]]
- [[Network Monitoring]]
