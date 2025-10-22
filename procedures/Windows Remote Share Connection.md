---
id: 1ca12e81-54e0-4f8b-b164-fccfa55b505f
name: Windows Remote Share Connection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.346921+00:00'
updated_at: '2023-04-10T20:37:55.945400+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]'
tags:
- '[[Mount a remote share]]'
- '[[Other methods]]'
- '[[Windows - Using credentials]]'
commands:
- '[[Connect to network share]]'
---

# Windows Remote Share Connection

## Summary

The Windows Remote Share Connection procedure is a method for accessing a remote server share. This procedure is commonly used in lateral movement attacks, allowing an attacker to move laterally within a network after gaining access to a system. To use this procedure, the attacker must have valid c

## Description

# Description

The Windows Remote Share Connection procedure is a method for accessing a remote server share. This procedure is commonly used in lateral movement attacks, allowing an attacker to move laterally within a network after gaining access to a system. To use this procedure, the attacker must have valid credentials to access the remote share.

This procedure works by mounting a remote share on the local system, allowing the attacker to access files and directories on the remote system as if they were on the local system. This can be done using the 'Connect to remote server share' command.

The business value of this procedure is that it allows attackers to move laterally within a network, potentially accessing sensitive data and systems.

## Requirements

1. Valid credentials to access remote share

1. Network access to remote share

## Defense

1. Limit access to remote shares to only authorized users

1. Implement network segmentation to limit lateral movement

1. Use strong passwords and multi-factor authentication to protect credentials

## Objectives

1. Access remote server share

1. Move laterally within network

1. Potentially access sensitive data and systems

# Instructions

1. To connect to a remote server share, use the 'net use' command followed by the UNC path of the share and the appropriate username and password. In this example, we are connecting to the C$ share on server 'srv01.domain.local' using the username 'username' and password 'password'.

**Code**: [[PS C:\> net use \\srv01.domain.local /user:DOMAIN\]]

> The 'net use' command is used to connect to or disconnect from a shared resource on a network. The command can be used to map a network drive or connect to a printer. The '/user' parameter is used to specify the username and password to use for the connection. The 'C$' share is a hidden administrative share on Windows systems that provides access to the root of the system drive.

**Command** ([[Connect to network share]]):

```bash
net use \\srv01.domain.local /user:DOMAIN\username password C$
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]

## Commands Used

- [[Connect to network share]]

## Tags

- [[Mount a remote share]]
- [[Other methods]]
- [[Windows - Using credentials]]
