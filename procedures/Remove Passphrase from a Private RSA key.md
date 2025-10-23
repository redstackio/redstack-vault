---
id: 52aed7ed-96b6-49ce-9984-574263a273f7
name: Remove Passphrase from a Private RSA key
type: procedure
verified: false
submitted: false
created_at: '2019-09-16T20:11:43.247738+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Linux
tags:
- '[[Setup]]'
commands:
- '[[openssl Remove Passphrase from RSA Key]]'
---

# Remove Passphrase from a Private RSA key

## Summary

Remove a known password from a password protected RSA key. 

## Description

# Description

Remove a known password from a password protected RSA key.



# Instructions





**Command** ([[openssl Remove Passphrase from RSA Key]]):

```bash
openssl rsa -in $_PRIVATE_KEY.enc -out $_PRIVATE_KEY
```





## Platforms

- Linux

## Commands Used

- [[openssl Remove Passphrase from RSA Key]]

## Tags

- [[Setup]]


