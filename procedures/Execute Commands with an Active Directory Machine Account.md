---
id: aa18d5dc-b01d-4485-b37a-27ee522ae288
name: Execute Commands with an Active Directory Machine Account
type: procedure
verified: false
submitted: false
created_at: '2020-06-24T23:26:31.466498+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Pass the Hash|T1075 - Pass the Hash]]'
platforms:
- Windows
tags:
- '[[Active Directory]]'
- '[[NTLM]]'
- '[[privileges]]'
commands:
- '[[Mimikatz Spawn a Shell as an AD Machine Account]]'
---

# Execute Commands with an Active Directory Machine Account

## Summary

Use a domain computer's NTLM hash (or password) and Mimikatz to spawn a terminal which executes commands using the machine account. Because this technique spawns a new terminal for command execution, a local or RDP session is needed to execute the attack. 

## Description

# Description

Use a domain computer's NTLM hash (or password) and Mimikatz to spawn a terminal which executes commands using the machine account. Because this technique spawns a new terminal for command execution, a local or RDP session is needed to execute the attack.



# Instructions

1. Download [Mimikatz](https://github.com/gentilkiwi/mimikatz)  (or Impacket's Invoke Mimikatz) to the target system. 
2. Execute Mimikatz as Administrator, providing it with the computer's NTLM hash, domain, and the computer's account name (which ends in a "$" symbol).





**Command** ([[Mimikatz Spawn a Shell as an AD Machine Account]]):

```bash
Mimikatz.exe "sekurlsa::pth /user:$_MACHINE_NAME$ /domain:$_DOMAIN /ntlm:$_NTLM_HASH"
```



Note: if the command fails, try first running "privilege::debug" and "token::elevate"  before the "sekurl::pth" command.



## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Pass the Hash|T1075 - Pass the Hash]]

## Commands Used

- [[Mimikatz Spawn a Shell as an AD Machine Account]]

## Tags

- [[Active Directory]]
- [[NTLM]]
- [[privileges]]


