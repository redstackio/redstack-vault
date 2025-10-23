---
id: d6a7ff81-3b42-46e1-be74-48201307705d
name: Intercept NTLMv2 Hashes via LLMNR and NetBIOS Requests (Windows)
type: procedure
verified: false
submitted: false
created_at: '2020-07-06T23:40:45.767101+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[LLMNR/NBT-NS Poisoning and Relay|T1171 - LLMNR/NBT-NS Poisoning and Relay]]'
platforms:
- Windows
tags:
- '[[Network]]'
- '[[NTLM]]'
commands:
- '[[Inveigh Intercept and Log NTLMv2 Hashes via LLMNR and NetBIOS Requests]]'
---

# Intercept NTLMv2 Hashes via LLMNR and NetBIOS Requests (Windows)

## Summary

Use the Inveigh PowerShell module to capture and log NTLMv2 hashes. By specifying the "LLMNR" and "NBNS" arguments, Inveigh can sniff and respond to those services without elevated privileges. 

## Description

# Description

Use the Inveigh PowerShell module to capture and log NTLMv2 hashes. By specifying the "LLMNR" and "NBNS" arguments, Inveigh can sniff and respond to those services without elevated privileges.



# Instructions

1. Download and import Inveigh: [Download from GitHub](https://github.com/Kevin-Robertson/Inveigh).

2. Execute the listener.





**Command** ([[Inveigh Intercept and Log NTLMv2 Hashes via LLMNR and NetBIOS Requests]]):

```bash
Invoke-Inveigh -LLMNR Y -NBNS Y -IP $_LISTEN_IP -ConsoleOutput Y
```



Note: When finished, execute "Stop-Inveigh" to exit the listener.

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[LLMNR/NBT-NS Poisoning and Relay|T1171 - LLMNR/NBT-NS Poisoning and Relay]]

## Commands Used

- [[Inveigh Intercept and Log NTLMv2 Hashes via LLMNR and NetBIOS Requests]]

## Tags

- [[Network]]
- [[NTLM]]


