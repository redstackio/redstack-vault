---
id: 86968dcb-c057-4fd2-95b1-a231974be41e
name: List Domain Users and Groups with MS-RPC/SMB Service
type: procedure
verified: true
submitted: true
created_at: '2020-03-26T05:23:16.749793+00:00'
updated_at: '2023-05-25T19:46:08.899829+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Owner/User Discovery|T1033 - System Owner/User Discovery]]'
platforms:
- Windows
tags:
- '[[Enumeration]]'
- '[[Network]]'
commands:
- '[[List Domain Groups on an SMB/RPC Server]]'
- '[[List Domain Users on an SMB/RPC Server]]'
- '[[rpcclient Authenticate with an RPC Server]]'
---

# List Domain Users and Groups with MS-RPC/SMB Service

**Status**: ✓ Verified

## Summary

Connect to a Microsoft SMB server using rpcclient, and enumerate domain users and groups. 

## Description

# Description

Connect to a Microsoft SMB server using rpcclient, and enumerate domain users and groups.





## Objectives

Having a list of domain users and groups can help the attacker identify potential targets for reconnaissance and further information gathering. For example, the attacker might use the list of domain users and groups to identify individuals with privileged access, such as domain administrators or service accounts, and focus their efforts on obtaining their credentials or performing lateral movement.



1. Authenticate with an RPC service on a remote machine

2. Obtain a list of domain users

3. Obtain a list of domain groups



# Instructions

Instructions on how to complete the procedure. Typically multiple numbered lists with commands included, and may contain H2 subheadings.



1. Connect to the server using rpcclient. To attempt to authenticate without credentials (Null session), omit the username and password leaving only the empty quotes.





**Command** ([[rpcclient Authenticate with an RPC Server]]):

```bash
rpcclient -U "$_USERNAME%$_PASSWORD" $_TARGET_IP
```





2. Enumerate domain users.





**Command** ([[List Domain Users on an SMB/RPC Server]]):

```bash
enumdomusers
```





3. Enumerate domain groups.





**Command** ([[List Domain Groups on an SMB/RPC Server]]):

```bash
enumdomgroups
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Owner/User Discovery|T1033 - System Owner/User Discovery]]

## Commands Used

- [[List Domain Groups on an SMB/RPC Server]]
- [[List Domain Users on an SMB/RPC Server]]
- [[rpcclient Authenticate with an RPC Server]]

## Tags

- [[Enumeration]]
- [[Network]]


