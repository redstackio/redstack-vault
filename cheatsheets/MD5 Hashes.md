---
id: 33cbc7cc-dd43-4b74-8f59-f2b8886432dd
name: MD5 Hashes
type: cheatsheet
verified: true
created_at: '2019-09-16T19:37:40.329940+00:00'
updated_at: '2023-05-30T20:12:10.336974+00:00'
---

# MD5 Hashes

**Status**: ✓ Verified

# Description

Generate MD5 Hashes to inject into a database or hashed password file.

Cracking MD5 Hashes to obtain the passwords.



## MD5 Hash Format

> $1$8BytesXX$dXGg2H2MnwNoiq6UuVkws/

## 

## Generate Hashes



**Command** ([[mkpasswd Generate a MD5 Hash]]):

```bash
mkpasswd -5 -S $_SALT $_PASSWORD
```









**Command** ([[openssl Generate a MD5 Hash]]):

```bash
openssl passwd -1 -salt $_SALT $_PASSWORD
```





## Cracking Hashes





**Command** ([[John the Ripper Dictionary Attack Against MD5 Hashes]]):

```bash
john --format=md5crypt --wordlist=$_PASSWORD_FILE $_HASH_FILE
```











**Command** ([[hashcat Dictionary Attack Against MD5 Hashes]]):

```bash
hashcat -m 500 -a 0 -o $_OUTPUT.txt $_HASH_FILE $_PASSWORD_FILE
```










