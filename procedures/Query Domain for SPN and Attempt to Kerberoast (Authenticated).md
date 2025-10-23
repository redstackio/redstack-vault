---
id: 588255c0-9513-4cee-bdad-6eb2ed7c5da2
name: Query Domain for SPN and Attempt to Kerberoast (Authenticated)
type: procedure
verified: false
submitted: false
created_at: '2019-12-04T19:39:54.389336+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Kerberoasting|T1208 - Kerberoasting]]'
platforms:
- Windows
tags:
- '[[known vulnerability]]'
- '[[Network]]'
- '[[Service Attacks]]'
commands:
- '[[GetUserSPN.py Query Domain for SPNs and Dump Available Hashes]]'
---

# Query Domain for SPN and Attempt to Kerberoast (Authenticated)

## Summary

Sevrice principal names (SPN) are unique identifiers used by Kerberos authentication. Due to how Kerberos handles service tickets, attackers may be able to query a domain controller with valid credentials, make a request to the ticket granting service (TGT), and receive the hash of other accounts. 

## Description

# Description

Sevrice principal names (SPN) are unique identifiers used by Kerberos authentication. Due to how Kerberos handles service tickets, attackers may be able to query a domain controller with valid credentials, make a request to the ticket granting service (TGT), and receive the hash of other accounts.





# Instructions





**Command** ([[GetUserSPN.py Query Domain for SPNs and Dump Available Hashes]]):

```bash
GetUserSPNs.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DOMAIN_IP -request
```







## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Kerberoasting|T1208 - Kerberoasting]]

## Commands Used

- [[GetUserSPN.py Query Domain for SPNs and Dump Available Hashes]]

## Tags

- [[known vulnerability]]
- [[Network]]
- [[Service Attacks]]


