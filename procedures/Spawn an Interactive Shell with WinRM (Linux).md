---
id: e732ce42-b42b-4f1e-9288-b71befcd80f1
name: Spawn an Interactive Shell with WinRM (Linux)
type: procedure
verified: true
submitted: true
created_at: '2019-11-22T22:40:14.550466+00:00'
updated_at: '2023-05-25T19:42:05.411624+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Windows Remote Management|T1028 - Windows Remote Management]]'
platforms:
- Windows
tags:
- '[[Network]]'
commands:
- '[[evil-winrm.rb Connect to a WinRM Server]]'
---

# Spawn an Interactive Shell with WinRM (Linux)

**Status**: ✓ Verified

## Summary

Spawn a PowerShell session  on a remote system using the WinRM service (usually port 5985).  See the Evil-WinRM tools page for installation instructions. 

## Description

# Description

Spawn a PowerShell session  on a remote system using the WinRM service (usually port 5985).  See the Evil-WinRM tools page for installation instructions.

## Objectives

This technique is commonly used in post-exploitation activities to move laterally within a network by gaining access to additional systems. It is particularly effective when combined with other techniques such as pass-the-hash, where the attacker can use stolen credentials to authenticate to the target system via WinRM.

1. Connect to a remote WinRM service using credentials

# Instructions

**Command** ([[evil-winrm.rb Connect to a WinRM Server]]):

```bash
evil-winrm.rb -i $_TARGET_IP -u $_USER -p $_PASS
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Windows Remote Management|T1028 - Windows Remote Management]]

## Commands Used

- [[evil-winrm.rb Connect to a WinRM Server]]

## Tags

- [[Network]]
