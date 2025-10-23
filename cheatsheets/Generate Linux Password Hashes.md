---
id: 6ec819a0-fac5-40d0-92c7-2c04b4d5a297
name: Generate Linux Password Hashes
type: cheatsheet
verified: true
created_at: '2019-09-16T18:26:12.859898+00:00'
updated_at: '2023-05-30T20:10:41.684152+00:00'
---

# Generate Linux Password Hashes

**Status**: ✓ Verified

# Description

Steps to generate password hashes using Linux tools.



## mkpasswd

Available methods:





**Code**: [[sha512crypt     SHA-512
sha256crypt     SHA-256
md]]









**Command** ([[mkpasswd Generate a SHA512 Hash]]):

```bash
 mkpasswd -m sha-512 -S $_SALT $_PASSWORD
```







**Command** ([[mkpasswd Generate a MD5 Hash]]):

```bash
mkpasswd -5 -S $_SALT $_PASSWORD
```







## OpenSSL

Available methods:



**Code**: [[-6                  SHA512-based password algorith]]









**Command** ([[openssl Generate a SHA512 Hash]]):

```bash
 openssl passwd -6 -salt $_SALT $_PASSWORD
```









**Command** ([[openssl Generate a MD5 Hash]]):

```bash
openssl passwd -1 -salt $_SALT $_PASSWORD
```







**Command** ([[openssl View Available Hash Options]]):

```bash
openssl passwd --help
```








