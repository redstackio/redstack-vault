---
id: 89e279ef-50f3-4702-bbd6-adb6da444995
name: Network Discovery Responder
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.278115+00:00'
updated_at: '2023-04-10T20:25:10.716121+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]'
tags:
- '[[Network Discovery]]'
- '[[Responder]]'
commands:
- '[[Run responder and save output to file]]'
- '[[Run responder without responding to NBT-NS, BROWSER, LLMNR requests]]'
---

# Network Discovery Responder

## Summary

The Network Discovery Responder procedure involves using the Responder tool to capture and respond to LLMNR and NBT-NS requests, which are typically used for name resolution on local networks. By responding to these requests with spoofed information, an attacker can trick a target system into revea

## Description

# Description

The Network Discovery Responder procedure involves using the Responder tool to capture and respond to LLMNR and NBT-NS requests, which are typically used for name resolution on local networks. By responding to these requests with spoofed information, an attacker can trick a target system into revealing sensitive information such as usernames and passwords. Additionally, by relaying SMB authentication attempts to an attacker-controlled system, an attacker can gain access to network resources and escalate privileges.

This procedure is typically used as a first step in a larger attack campaign, as it allows an attacker to gather valuable information about the target network and potentially gain a foothold on one or more systems.

 

## Requirements

1. Access to the target network

1. Ability to run Responder on a system on the target network

 

## Defense

1. Disable LLMNR and NBT-NS on all systems on the network

1. Use strong passwords and implement two-factor authentication to reduce the risk of credential theft

1. Monitor network traffic for signs of LLMNR/NBT-NS poisoning and SMB relay attacks

 

## Objectives

1. Identify vulnerable systems on the target network

1. Capture usernames and passwords transmitted over the network

1. Gain access to network resources and escalate privileges

 

# Instructions

1. Use the responder command with the following parameters:
-I: Specify the interface to listen on.
-A: Analyze incoming requests without responding.
-w: Enable the WPAD rogue proxy server.
-r: Enable the NBT-NS, BROWSER, and LLMNR poisoner.
-f: Force Responder to use SMBv1 instead of SMBv2/v3.

 



**Code**: [[responder -I eth0 -A # see NBT-NS, BROWSER, LLMNR ]]



> This command allows you to discover devices on a network by analyzing incoming network requests without responding to them. The -w parameter enables the WPAD rogue proxy server which can be used to intercept and manipulate web traffic. The -r parameter enables the NBT-NS, BROWSER, and LLMNR poisoner which can be used to intercept and manipulate network traffic. The -f parameter forces Responder to use SMBv1 instead of SMBv2/v3 which can be useful for compatibility with older systems.



**Command** ([[Run responder without responding to NBT-NS, BROWSER, LLMNR requests]]):

```bash
responder -I eth0 -A
```





**Command** ([[Run responder and save output to file]]):

```bash
responder.py -I eth0 -wrf
```



## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]

## Commands Used

- [[Run responder and save output to file]]
- [[Run responder without responding to NBT-NS, BROWSER, LLMNR requests]]

## Tags

- [[Network Discovery]]
- [[Responder]]


