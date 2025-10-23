---
id: 741681a9-daaf-4e34-b796-747004393dfc
name: SHA512 Hashes
type: cheatsheet
verified: true
created_at: '2019-09-16T22:24:57.477334+00:00'
updated_at: '2023-05-30T20:09:33.131084+00:00'
---

# SHA512 Hashes

**Status**: ✓ Verified

# Description

Generate SHA-512 Hashes to inject into a database or hashed password file.

Cracking SHA-512 Hashes to obtain the passwords



## SHA-512 Hash Format

> $6$16bytesXX16bytes$FXuYP0OI7qYB3K6u6.91Blr7rtvjLZmpcuAWuWVnTj4G2nVGny6k5yzaDbV3iQCwoSDMGgXePvFxddnxYkpa5/



## Generate Hashes





**Command** ([[mkpasswd Generate a SHA512 Hash]]):

```bash
 mkpasswd -m sha-512 -S $_SALT $_PASSWORD
```









**Command** ([[openssl Generate a SHA512 Hash]]):

```bash
 openssl passwd -6 -salt $_SALT $_PASSWORD
```





## Cracking Hashes





**Command** ([[John the Ripper Dictionary Attack a SHA-512 Hash]]):

```bash
john --format=sha512crypt --wordlist=$_WORDLIST $_HASH_FILE
```





Hashcat can be used in a virtual machine, but with a significant hit to speeds. Hashcat requires users specify the "--force" argument to brute force in a VM using CPU.





**Command** ([[Hashcat Dictionary Attack a SHA-512 Hash]]):

```bash
 hashcat -m 1800 -a0 -o $_OUTPUT.txt --remove $_HASH_FILE $_PASSWORD_LIST
```












