---
id: 044edf5a-f7d3-4fb4-ba3c-8324a779d656
name: SID Enumeration and WMI Query for MS14-068 Checksum Validation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:02.589475+00:00'
updated_at: '2023-04-10T20:26:04.187922+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]'
- '[[Remote System Discovery|T1018 - Remote System Discovery]]'
tags:
- '[[Active Directory Attacks]]'
- '[[From CVE to SYSTEM shell on DC]]'
- '[[MS14-068 Checksum Validation]]'
commands:
- '[[Enumerating Group Memberships]]'
- '[[Enumerating Shares]]'
- '[[Enumerating Users]]'
---

# SID Enumeration and WMI Query for MS14-068 Checksum Validation

## Summary

This procedure focuses on validating MS14-068 checksums by performing SID enumeration and WMI queries. This attack allows an attacker to elevate privileges to SYSTEM on the domain controller. The attacker first performs SID enumeration to obtain the SID of the target user. Then, the attacker querie

## Description

# Description

This procedure focuses on validating MS14-068 checksums by performing SID enumeration and WMI queries. This attack allows an attacker to elevate privileges to SYSTEM on the domain controller. The attacker first performs SID enumeration to obtain the SID of the target user. Then, the attacker queries the WMI service on the domain controller for the user's password hash. The password hash can be used to generate a valid Kerberos ticket and authenticate as the target user, effectively elevating privileges to SYSTEM on the domain controller. This attack can be used to gain access to sensitive data and control of the entire Active Directory domain.

 

## Requirements

1. Authenticated access to the domain controller

1. RPC and WMI access to the domain controller

 

## Defense

1. Enforce the principle of least privilege by limiting the permissions of user accounts

1. Implement multi-factor authentication to prevent unauthorized access

1. Monitor and log all WMI and RPC activity to detect and respond to suspicious activity.

 

## Objectives

1. Obtain SYSTEM-level access on the domain controller

 

# Instructions

1. To use rpcclient for user SID enumeration, follow these steps:
1. Open a terminal and run the command 'rpcclient -U "" <IP_ADDRESS>'.
2. Once connected, run the command 'lookupnames <USERNAME>'.
3. The output will include the user's SID.

 



**Code**: [[rpcclient]]



> The rpcclient command is a tool for interacting with Microsoft's implementation of the DCE/RPC protocol. It can be used to perform various tasks, including user SID enumeration. The 'lookupnames' command is used to lookup the SID of a given username. By using this command, an attacker can obtain the SID of a user on the target system, which can be used in further attacks.



**Command** ([[Enumerating Users]]):

```bash
rpcclient -U "" -N 10.10.10.10 -c enumdomusers
```





**Command** ([[Enumerating Shares]]):

```bash
rpcclient -U "" -N 10.10.10.10 -c enumshares
```





**Command** ([[Enumerating Group Memberships]]):

```bash
rpcclient -U "" -N 10.10.10.10 -c 'querygroupmem 0x200'
```



2. Use the following command to query WMI remotely: 
wmic /node:<remote_computer_name> <command>

 



**Code**: [[wmi]]



> This command allows you to remotely query the Windows Management Instrumentation (WMI) service on another computer. The <remote_computer_name> parameter specifies the name of the remote computer, and the <command> parameter specifies the WMI query to execute. You must have administrative privileges on the remote computer to use this command.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]
- [[Remote System Discovery|T1018 - Remote System Discovery]]

## Commands Used

- [[Enumerating Group Memberships]]
- [[Enumerating Shares]]
- [[Enumerating Users]]

## Tags

- [[Active Directory Attacks]]
- [[From CVE to SYSTEM shell on DC]]
- [[MS14-068 Checksum Validation]]


