---
id: d1a8ccd3-7f21-4106-92c5-ca9b7596182f
name: List Credentials in Windows Credential Manager Vault
type: procedure
verified: true
submitted: true
created_at: '2019-12-03T06:51:06.729791+00:00'
updated_at: '2023-05-25T19:42:09.815834+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
platforms:
- Windows
tags:
- '[[data exposure]]'
- '[[Service Attacks]]'
commands:
- '[[List Stored Windows Credentials (cmdkey.exe)]]'
- '[[List Stored Windows Credentials (vaultcmd.exe)]]'
- '[[vaultcmd.exe List Stored Windows Credentials]]'
---

# List Credentials in Windows Credential Manager Vault

**Status**: ✓ Verified

## Summary

Users often save credentials using Windows Credential Manager, allowing them to authenticate with applications and other systems without having to reenter their username and password. Attackers may be able to use these saved credentials for lateral movement across networks. 

## Description

# Description

Users often save credentials using Windows Credential Manager, allowing them to authenticate with applications and other systems without having to reenter their username and password. Attackers may be able to use these saved credentials for lateral movement across networks.

# Instructions

1. List the current user's credential vaults:

**Command** ([[List Stored Windows Credentials (vaultcmd.exe)]]):

```bash
vaultcmd.exe /list
```

2. List saved credentials in the "Windows Credentials" vault:

**Command** ([[vaultcmd.exe List Stored Windows Credentials]]):

```bash
vaultcmd.exe /listcreds:"Windows Credentials"
```

Alternately, cmdkey.exe can be used to enumerated saved credentials:

**Command** ([[List Stored Windows Credentials (cmdkey.exe)]]):

```bash
cmdkey.exe /list
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[List Stored Windows Credentials (cmdkey.exe)]]
- [[List Stored Windows Credentials (vaultcmd.exe)]]
- [[vaultcmd.exe List Stored Windows Credentials]]

## Tags

- [[data exposure]]
- [[Service Attacks]]
