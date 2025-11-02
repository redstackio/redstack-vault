---
id: 97f92a38-5c30-4899-b2e9-d1b94ae3328d
name: CrackMapExec
type: tool
verified: false
created_at: '2019-08-28T21:17:33.126811+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[CrackMapExec Authenticate with SMB Using an NTLM Hash]]'
- '[[CrackMapExec Brute Force SMB Usernames and Passwords]]'
- '[[CrackMapExec Brute Force SMB Users Using RID]]'
- '[[CrackMapExec Dictionary Brute Force Remote Desktop Protocol (RDP)]]'
- '[[crackmapexec scan smb ip range]]'
platforms:
- Linux
- Windows
tags:
- '[[Brute Force]]'
- '[[pass the hash]]'
---

# CrackMapExec

## Overview

CrackMapExec (CME) is a post-exploitation tool that helps automate assessing the security of Active Directory networks. CME is typically used to brute force valid usernames and passwords using wordlists from services including: SMB/CIFS, HTTP, WinRM, SSH, and MySQL. CME can also be used for Pass-th

## Description

# Description

CrackMapExec (CME) is a post-exploitation tool that helps automate assessing the security of Active Directory networks. CME is typically used to brute force valid usernames and passwords using wordlists from services including: SMB/CIFS, HTTP, WinRM, SSH, and MySQL. CME can also be used for Pass-the-Hash attacks, using a password hash instead of the actual password.



# Example



{{EMBEDDED_COMMAND_4fc0ee9c-a0b1-4198-9099-1184c8b25805}}



# Installation

## Copy Latest Compiled Binary

Due to complex dependencies, it is often easiest to use the pre-built binaries from GitHub.

1. Navigate to: [https://github.com/byt3bl33d3r/CrackMapExec/actions](https://github.com/byt3bl33d3r/CrackMapExec/actions)

2. Select an appropriate build from the  "Workflows" and download a single CrackMapExec binary.



## Install on Kali











## Platforms

- Linux
- Windows

## Services

- http
- http
- https
- https
- ms-sql
- rdp
- smb
- ssh
- winrm

## Commands (1)

- [[CrackMapExec Brute Force SMB Usernames and Passwords]]

## Tags

- [[Brute Force]]
- [[pass the hash]]


