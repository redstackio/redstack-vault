---
id: 07f2c348-a675-41ce-b82e-8f83942f9301
name: SMB Beacon Payload with Command Line Interactions
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.340572+00:00'
updated_at: '2023-04-10T20:36:22.162395+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Data Encoding|T1132 - Data Encoding]]'
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
tags:
- '[[Cobalt Strike]]'
- '[[Payloads]]'
- '[[SMB Beacon]]'
---

# SMB Beacon Payload with Command Line Interactions

## Summary

The SMB Beacon payload with command line interactions is a technique used by attackers to establish a foothold in a target network. The payload is delivered via Cobalt Strike and establishes a communication channel with the attacker's command and control server. The SMB Beacon is designed to blend 

## Description

# Description

The SMB Beacon payload with command line interactions is a technique used by attackers to establish a foothold in a target network. The payload is delivered via Cobalt Strike and establishes a communication channel with the attacker's command and control server. The SMB Beacon is designed to blend in with normal network traffic, making it difficult to detect. Once the payload is established, the attacker can use command line interactions to execute commands on the compromised system, allowing them to move laterally within the network and perform reconnaissance. This technique is often used in advanced persistent threat (APT) attacks.

## Requirements

1. Access to the target network

1. Cobalt Strike software

## Defense

1. Implement network segmentation to limit lateral movement

1. Use endpoint detection and response (EDR) software to detect and respond to malicious activity

1. Enforce least privilege access controls to limit the impact of a compromised system

## Objectives

1. Establish a foothold in the target network

1. Maintain persistence on the compromised system

1. Move laterally within the network

1. Perform reconnaissance on the target network

# Instructions

1. The following are the details for the commands:
link - This command creates a connection between the host and the specified pipe name. 
connect - This command establishes a connection between the host and the specified port. 
unlink - This command removes the connection between the host and the specified PID. 
jump - This command executes the specified executable on the host and connects it to the specified pipe.

**Code**: [[link [host] [pipename]
connect [host] [port]
unlin]]

> The arguments for each command are as follows:
link - [host] - the host to connect to, [pipename] - the name of the pipe to connect to.
connect - [host] - the host to connect to, [port] - the port to connect to.
unlink - [host] - the host to disconnect from, [PID] - the process ID to disconnect from.
jump - [exec] - the executable to execute on the host, [host] - the host to connect to, [pipe] - the name of the pipe to connect to.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Data Encoding|T1132 - Data Encoding]]
- [[Remote Access Tools|T1219 - Remote Access Tools]]

## Tags

- [[Cobalt Strike]]
- [[Payloads]]
- [[SMB Beacon]]
