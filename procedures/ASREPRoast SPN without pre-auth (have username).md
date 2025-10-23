---
id: 0a10cdd1-1117-4bec-ab86-a3ed64cd7ec6
name: ASREPRoast SPN without pre-auth (have username)
type: procedure
verified: false
submitted: false
created_at: '2023-01-11T20:48:08.611174+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Windows
tags:
- '[[ASEPRoast]]'
- '[[kerberoast]]'
- '[[kerberos]]'
commands:
- '[[Rubeus asreproast hashcat output]]'
---

# ASREPRoast SPN without pre-auth (have username)

## Summary

Active Directory try to get hash from username. Looking user without pre-auth attribute on Kerberos. Send AS_REQ to DC to receive encrypted user key to crack. Can achieve without domain account, just a username. 

## Description

# Description

Active Directory try to get hash from username. Looking user without pre-auth attribute on Kerberos. Send AS_REQ to DC to receive encrypted user key to crack.

Can achieve without domain account, just a username.



## Objective

1. Obtain a hash that can then be cracked for a password for valid credentials



# Instructions

Use Rubeus to get result with hashcat format to crack.





**Command** ([[Rubeus asreproast hashcat output]]):

```bash
rubeus.exe asreproast /format:hashcat
```





## Platforms

- Windows

## Commands Used

- [[Rubeus asreproast hashcat output]]

## Tags

- [[ASEPRoast]]
- [[kerberoast]]
- [[kerberos]]


