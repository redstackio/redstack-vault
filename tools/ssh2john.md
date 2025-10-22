---
id: 9c1d35a1-c6e8-47b5-92ca-b069813e8c95
name: ssh2john
type: tool
verified: true
created_at: '2020-02-18T19:16:01.973601+00:00'
updated_at: '2023-05-30T19:48:54.799553+00:00'
commands:
- '[[ssh2john Extract the Hash from an Encrypted SSH Private Key]]'
platforms:
- Linux
- Windows
tags:
- '[[Brute Force]]'
- '[[Cryptography]]'
---

# ssh2john

**Status**: ✓ Verified

## Overview

Ssh2john is a Python script packaged with John the Ripper, which takes a private SSH key as input and outputs the hash, that can then be cracked with John. It's worth noting that John the Ripper must be used to crack the hash, and that the hashes are not supported by other programs such as Hashcat.

## Description

# Description

Ssh2john is a Python script packaged with John the Ripper, which takes a private SSH key as input and outputs the hash, that can then be cracked with John. It's worth noting that John the Ripper must be used to crack the hash, and that the hashes are not supported by other programs such as Hashcat. Ssh2john supports RSA, DSA, and EC keys.

# Example

# Installation

## Install on Debian/Ubuntu

ssh2john is included when installing John the Ripper, but can be downloaded directly from: https://github.com/magnumripper/JohnTheRipper/raw/bleeding-jumbo/run/ssh2john.py

## Platforms

- Linux
- Windows

## Services

- ssh
- ssh

## Commands (1)

- [[ssh2john Extract the Hash from an Encrypted SSH Private Key]]

## Tags

- [[Brute Force]]
- [[Cryptography]]
