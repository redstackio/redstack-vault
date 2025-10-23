---
id: 5e2d35cd-13cf-40f0-aedd-06ef55cf693f
name: Connect to WinRM from a Linux System (Pass-the-Hash)
type: procedure
verified: true
submitted: true
created_at: '2020-03-16T02:05:05.244733+00:00'
updated_at: '2023-05-25T19:44:35.252518+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Pass the Hash|T1075 - Pass the Hash]]'
- '[[Windows Remote Management|T1028 - Windows Remote Management]]'
platforms:
- Windows
tags:
- '[[Network]]'
- '[[pass the hash]]'
- '[[shell]]'
commands:
- '[[evil-winrm.rb Connect to a WinRM Server (NTLM)]]'
---

# Connect to WinRM from a Linux System (Pass-the-Hash)

**Status**: ✓ Verified

## Summary

Spawn a PowerShell instance on a remote system using the WinRM service (usuallyport 5985) using an NTLM password hash instead of a password. 

## Description

# Description

Spawn a PowerShell instance on a remote system using the WinRM service (usuallyport 5985) using an NTLM password hash instead of a password.



## Objectives

This technique is commonly used in post-exploitation activities to move laterally within a network by gaining access to additional systems. It is particularly effective when combined with other techniques such as pass-the-hash, where the attacker can use stolen credentials to authenticate to the target system via WinRM.



1. Use a Users NTLM hash to authenticate through the WinRM service on a remote machine as that target user and obtain a shell on the target machine.



# Instructions





**Command** ([[evil-winrm.rb Connect to a WinRM Server (NTLM)]]):

```bash
evil-winrm.rb -i $_TARGET -u $_USER -H $_NTLM
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Pass the Hash|T1075 - Pass the Hash]]
- [[Windows Remote Management|T1028 - Windows Remote Management]]

## Commands Used

- [[evil-winrm.rb Connect to a WinRM Server (NTLM)]]

## Tags

- [[Network]]
- [[pass the hash]]
- [[shell]]


