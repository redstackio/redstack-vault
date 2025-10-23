---
id: 49d3830a-114e-44cd-8ff0-38a1677a50c7
name: Brute Force Shadow Hashes
type: procedure
verified: true
submitted: true
created_at: '2020-01-20T20:42:02.745293+00:00'
updated_at: '2023-05-26T00:41:03.700936+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
platforms:
- Linux
tags:
- '[[Cryptography]]'
- '[[data exposure]]'
commands:
- '[[hashcat Brute Force Password Hashes]]'
- '[[Hashcat Find Hash Mode from Example Hashes]]'
---

# Brute Force Shadow Hashes

**Status**: ✓ Verified

## Summary

Linux systems store user passwords in the /etc/shadow file. While these passwords are hashed, attackers with read access to the shadow file may attempt a brute force attack in an attempt to uncover the original unhashed passwords. 

## Description

# Description

Linux systems store user passwords in the /etc/shadow file. While these passwords are hashed, attackers with read access to the shadow file may attempt a brute force attack in an attempt to uncover the original unhashed passwords.



# Instructions

## Identifying the Hash

This procedure will use Hashcat to brute force password hashes. Since Hashcat does not automatically detect the hash type, it must first be manually identified. Each hashed password starts with a "$" symbol, followed by one or two characters, then another "$", which designates the algorithm used.



**Code**: [[$1$ – MD5
$2a$ – Blowfish
$2y$ – Eksblowfish
$5$ –]]



For example, with the hash:



**Code**: [[$6$ngUYdXkcMLK$AI23a7brd9zZOgf336W.9a7/M2QstTHC/9E]]



The hashing algorithm is SHA-512. 



In order to use Hashcat to brute force a password, the "Mode" value must be found. This can be done by either searching their web page ([https://hashcat.net/wiki/doku.php?id=example_hashes](https://hashcat.net/wiki/doku.php?id=example_hashes)), or by searching Hashcat's built-in copy of example hashes. Often, it's easiest to use Hashcat's built-in copy, and grep the output.





**Command** ([[Hashcat Find Hash Mode from Example Hashes]]):

```bash
hashcat --example-hashes | grep -C 2 $_VALUE
```





## Brute Forcing Hashes

1. Create a file containing only the password hashes, removing the preceding usernames, and all information after the hash.

2. Execute Hashcat, specifying the mode value identified earlier, and a wordlist.





**Command** ([[hashcat Brute Force Password Hashes]]):

```bash
hashcat -m $_VALUE $_HASHES $_WORDLIST
```



Note: Cracking passwords within a Kali VM is generally slow and not recommended. Whenever possible crack passwords on a machine with a good graphics card, and leverage that to speed up cracking. If that is not possible, include the "**--force**" argument when running Kali in a VM, to force CPU usage.

## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[hashcat Brute Force Password Hashes]]
- [[Hashcat Find Hash Mode from Example Hashes]]

## Tags

- [[Cryptography]]
- [[data exposure]]


