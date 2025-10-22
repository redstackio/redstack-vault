---
id: f72c836e-7e5e-4364-ac5d-f41d75e0995e
name: Crack krb5tgs hash for password
type: procedure
verified: false
submitted: false
created_at: '2023-01-11T21:03:47.343868+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Windows
tags:
- '[[hashcat]]'
- '[[john]]'
- '[[kerberos]]'
- '[[password cracking]]'
commands:
- '[[hashcat Kerberos 5 TGS (krb5-tgs)]]'
- '[[john crack Kerberos 5 TGS (krb5-tgs)]]'
---

# Crack krb5tgs hash for password

## Summary

Using hashcat to crack  krb5-tgs hash obtained from impacket or rubeus tools on DC. 

## Description

# Description

Using hashcat to crack  krb5-tgs hash obtained from impacket or rubeus tools on DC.

## Objective

1. Crack a Kerberos 5 TGS hash using a dictionary to obtain a password for valid credentials

# Instructions

## Use hashcat to crack krb5tgs

**Command** ([[hashcat Kerberos 5 TGS (krb5-tgs)]]):

```bash
hashcat -m 13100 -a 0 hash.txt password-list.txt
```

## Use john to crack krb5tgs

## 

**Command** ([[john crack Kerberos 5 TGS (krb5-tgs)]]):

```bash
john hash.txt --format=krb5tgs --wordlist=password-list.txt
```

## 

## Platforms

- Windows

## Commands Used

- [[hashcat Kerberos 5 TGS (krb5-tgs)]]
- [[john crack Kerberos 5 TGS (krb5-tgs)]]

## Tags

- [[hashcat]]
- [[john]]
- [[kerberos]]
- [[password cracking]]
