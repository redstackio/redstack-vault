---
id: 8b5b6391-8eb5-4e83-9fb5-2b06c88ae7d8
name: Dump Kerberos Tickets
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.675644+00:00'
updated_at: '2023-04-10T20:26:27.746994+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Dump Kerberos Tickets]]'
- '[[Kerberos Tickets]]'
commands:
- '[[Dump one ticket using Rubeus.exe]]'
- '[[List available tickets using Rubeus.exe]]'
---

# Dump Kerberos Tickets

## Summary

Dumping Kerberos tickets is a technique used to extract Kerberos tickets from a compromised system. These tickets can be used to authenticate to other systems and services within the network. The process involves using tools such as Mimikatz to extract the tickets from memory or from the ticket cac

## Description

# Description

Dumping Kerberos tickets is a technique used to extract Kerberos tickets from a compromised system. These tickets can be used to authenticate to other systems and services within the network. The process involves using tools such as Mimikatz to extract the tickets from memory or from the ticket cache. This technique is often used in lateral movement and privilege escalation attacks.

Technical Explanation: Kerberos is the default authentication protocol used in Windows Active Directory environments. When a user logs into a system, a Kerberos ticket is created that can be used to authenticate the user to other systems and services within the network. These tickets are stored in memory or in the ticket cache. Dumping Kerberos tickets involves extracting these tickets from memory or from the ticket cache. This can be done using tools such as Mimikatz, which can bypass Windows security measures and extract the tickets.

Business Value: By dumping Kerberos tickets, an attacker can move laterally through the network and gain access to sensitive data and systems. This technique can be used to escalate privileges and gain access to critical systems and data.

## Requirements

1. Access to a compromised system

1. Privileged access to run Mimikatz or similar tool

## Defense

1. Implement credential hygiene best practices to reduce the impact of compromised credentials

1. Monitor for suspicious activity, such as the use of Mimikatz or other credential dumping tools

1. Implement network segmentation to limit lateral movement within the network

## Objectives

1. Extract Kerberos tickets from a compromised system

1. Authenticate to other systems and services within the network

1. Move laterally through the network

1. Escalate privileges

# Instructions

1. The 'Rubeus.exe' command is used to interact with Kerberos tickets. 

- To list available tickets, use the 'triage' flag. 
- To dump a specific ticket, use the 'dump' flag followed by the '/luid' argument and the value of the ticket's LUID (Locally Unique Identifier). 

Note: The output of the 'dump' command is in Kirbi format, which is a binary format used to represent Kerberos tickets.

**Code**: [[# List available tickets
Rubeus.exe triage

# Dump]]

> - 'Rubeus.exe': The command used to interact with Kerberos tickets. 
- 'triage': A flag used to list available tickets. 
- 'dump': A flag used to dump a specific ticket. 
- '/luid': An argument used with the 'dump' flag to specify the LUID of the ticket to dump. 
- '0x12d1f7': An example value of the LUID argument, which should be replaced with the actual LUID of the ticket to dump.

**Command** ([[List available tickets using Rubeus.exe]]):

```bash
Rubeus.exe triage
```

**Command** ([[Dump one ticket using Rubeus.exe]]):

```bash
Rubeus.exe dump /luid:0x12d1f7
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Dump one ticket using Rubeus.exe]]
- [[List available tickets using Rubeus.exe]]

## Tags

- [[Active Directory Attacks]]
- [[Dump Kerberos Tickets]]
- [[Kerberos Tickets]]
