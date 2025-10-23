---
id: 6df4d650-03a1-4f95-a080-c000ae27883e
name: Brute Force Private SSH Key Password
type: procedure
verified: false
submitted: false
created_at: '2019-10-25T19:09:24.280004+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
platforms:
- Linux
tags:
- '[[Cryptography]]'
commands:
- '[[John the Ripper Brute Force a Hash File]]'
- '[[openssl Remove Passphrase from RSA Key]]'
- '[[ssh2john Extract the Hash from an Encrypted SSH Private Key]]'
---

# Brute Force Private SSH Key Password

## Summary

SSH keys are often protected by a password as a security measure. Even with this precaution, without a strong password attackers who are able to copy the key can perform an offline brute force attack against the password hash. 

## Description

# Description

SSH keys are often protected by a password as a security measure. Even with this precaution, without a strong password attackers who are able to copy the key can perform an offline brute force attack against the password hash.



# Instructions

1. Extract the password hash from the SSH key.





**Command** ([[ssh2john Extract the Hash from an Encrypted SSH Private Key]]):

```bash
python ssh2john.py $_PRIVATE_KEY.enc > $_OUTPUT.txt
```





2. Perform a dictionary brute force attack against the password hash





**Command** ([[John the Ripper Brute Force a Hash File]]):

```bash
john --wordlist=$_WORDLIST $_HASH_FILE
```





3. (Optional) Remove the password from the original SSH key.





**Command** ([[openssl Remove Passphrase from RSA Key]]):

```bash
openssl rsa -in $_PRIVATE_KEY.enc -out $_PRIVATE_KEY
```







## Platforms

- Linux

## Products

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[John the Ripper Brute Force a Hash File]]
- [[openssl Remove Passphrase from RSA Key]]
- [[ssh2john Extract the Hash from an Encrypted SSH Private Key]]

## Tags

- [[Cryptography]]


