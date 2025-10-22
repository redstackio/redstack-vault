---
id: 5aa14c3c-6426-46bc-a6aa-5454d3fb84a2
name: Windows DPAPI Credential Theft
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.204797+00:00'
updated_at: '2023-04-10T20:37:12.504960+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Credentials from Password Stores|T1555 - Credentials from Password Stores]]'
sub_techniques:
- '[[Securityd Memory|T1555.002 - Securityd Memory]]'
tags:
- '[[Data Protection API]]'
- '[[Windows - DPAPI]]'
commands:
- '[[List all credentials in a specific vault]]'
- '[[List all credentials in Windows Credentials vault]]'
- '[[List all vault items]]'
---

# Windows DPAPI Credential Theft

## Summary

Windows Data Protection API (DPAPI) is a powerful tool that allows applications to store and retrieve sensitive information, such as passwords and keys, in a secure manner. However, if an attacker gains access to a user's DPAPI data, they can use it to steal valuable credentials and gain access to 

## Description

# Description

Windows Data Protection API (DPAPI) is a powerful tool that allows applications to store and retrieve sensitive information, such as passwords and keys, in a secure manner. However, if an attacker gains access to a user's DPAPI data, they can use it to steal valuable credentials and gain access to critical systems. This procedure involves using the 'List Credentials from Windows Credentials Manager' command to extract DPAPI data and decrypt it using a variety of techniques. By doing so, an attacker can quickly and easily gain access to sensitive information and use it to further their objectives.

## Requirements

1. Local access to a Windows system

1. Administrative or SYSTEM-level privileges

1. Access to the 'List Credentials from Windows Credentials Manager' command

## Defense

1. Implement strong access controls to limit local and remote access to sensitive systems

1. Monitor for suspicious activity, such as repeated failed login attempts or unusual network traffic

1. Use endpoint detection and response (EDR) tools to detect and respond to potential attacks in real-time

## Objectives

1. Extract and decrypt DPAPI data from a target system

1. Steal valuable credentials and gain access to critical systems

# Instructions

1. To list all credentials from the Windows Credentials Manager, run the following command:

vaultcmd /listcreds:"Windows Credentials" /all

To list credentials from a specific vault, run the following command:

VaultCmd /listcreds:<namevault>|<guidvault> /all

**Code**: [[vaultcmd /list

VaultCmd /listcreds:<namevault>|<g]]

> The command 'vaultcmd /listcreds' is used to list all credentials from a specific vault or from the Windows Credentials Manager. The '/all' flag is used to display all the credentials stored in the vault. The '<namevault>|<guidvault>' option is used to specify the name or GUID of the vault from which the credentials are to be listed. If no option is specified, the command will list all the vaults available on the system.

The command 'vaultcmd /list' is used to list all the vaults available on the system. It does not display any credentials.

**Command** ([[List all vault items]]):

```bash
vaultcmd /list
```

**Command** ([[List all credentials in a specific vault]]):

```bash
VaultCmd /listcreds:<namevault>|<guidvault> /all
```

**Command** ([[List all credentials in Windows Credentials vault]]):

```bash
vaultcmd /listcreds:"Windows Credentials" /all
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]

### Sub-Techniques

- [[Securityd Memory|T1555.002 - Securityd Memory]]

## Commands Used

- [[List all credentials in a specific vault]]
- [[List all credentials in Windows Credentials vault]]
- [[List all vault items]]

## Tags

- [[Data Protection API]]
- [[Windows - DPAPI]]
