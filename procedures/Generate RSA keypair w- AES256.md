---
id: 790b90a7-a2f7-4182-bb28-264a22a06983
name: Generate RSA keypair w/ AES256
type: procedure
verified: false
submitted: false
created_at: '2019-09-16T23:41:09.360012+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Linux
tags:
- '[[Setup]]'
commands:
- '[[Generate AES256 RSA keypair]]'
- '[[Generate Public Key from Private]]'
---

# Generate RSA keypair w/ AES256

## Summary

We suggest making RSA key's with a AES-256 encrypted passphrase to better secure your clients systems during a penetration test. 

## Description

# Description

We suggest making RSA key's with a AES-256 encrypted passphrase to better secure your clients systems during a penetration test.



# Instructions

1. Generate the private key





**Command** ([[Generate AES256 RSA keypair]]):

```bash
openssl genrsa -aes256 -out $RSA_KEY 4096
```





2. Generate a public key from the private





**Command** ([[Generate Public Key from Private]]):

```bash
openssl rsa -in $_KEY.priv -pubout > $_KEY.pub
```





## Platforms

- Linux

## Commands Used

- [[Generate AES256 RSA keypair]]
- [[Generate Public Key from Private]]

## Tags

- [[Setup]]


