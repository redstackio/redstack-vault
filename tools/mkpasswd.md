---
id: d63ca1a1-7a36-498c-bcc6-2612a73d6301
name: mkpasswd
type: tool
verified: true
created_at: '2020-02-21T02:30:15.150525+00:00'
updated_at: '2023-05-30T19:47:23.227969+00:00'
commands:
- '[[mkpasswd Generate a SHA512 Hash]]'
tags:
- '[[Cryptography]]'
- '[[Operating Systems]]'
---

# mkpasswd

**Status**: ✓ Verified

## Overview

mkpasswd generates hashed passwords from plain text, using popular formats found in /etc/passwd and /etc/shadow files. Available methods (-m <ALGO>): sha512crypt - SHA-512 sha256crypt - SHA-256 md5crypt - MD5 descrypt -  standard 56 bit DES-based crypt(3) 

## Description

# Description

mkpasswd generates hashed passwords from plain text, using popular formats found in /etc/passwd and /etc/shadow files.

Available methods (-m <ALGO>):

- sha512crypt - SHA-512

- sha256crypt - SHA-256

- md5crypt - MD5

- descrypt -  standard 56 bit DES-based crypt(3)

# Example

# Installation

## Install on Debian/Ubuntu

## Commands (1)

- [[mkpasswd Generate a SHA512 Hash]]

## Tags

- [[Cryptography]]
- [[Operating Systems]]
