---
id: c0a1c1e5-c457-44c3-b371-b6962a6bfdd7
name: Mimikatz
type: tool
verified: false
created_at: '2019-08-28T21:17:38.065570+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[.NET Load a remote executable into memory]]'
- '[[Extract Windows LM/NTLM Hashes From LSASS]]'
- '[[Mimikatz Capture Windows Logins to a File]]'
- '[[Mimikatz Create a Golden Ticket with the krbtgt hash]]'
- '[[Mimikatz Decrypt a User''s Masterkey with the Domain''s Private key]]'
- '[[Mimikatz Dump Masterkeys in Memory]]'
- '[[Mimikatz Export a Domain''s Private Key]]'
- '[[Mimikatz Extract Chrome Credentials from the Current User''s Session]]'
- '[[Mimikatz Extract Chrome Credentials with the Masterkey]]'
- '[[Mimikatz Extract Windows LM/NTLM Hashes From SAM]]'
- '[[Mimikatz Extract Windows Saved Credentials from Vault]]'
- '[[Mimikatz Extract a User''s Masterkey using their Password]]'
- '[[Mimikatz Forge an Internal AD Forest Trust Ticket]]'
- '[[Mimikatz Spawn a Shell as an AD Machine Account]]'
- '[[cmd-ae14bc4f]]'
platforms:
- Windows
tags:
- '[[Cryptography]]'
- '[[extract]]'
- '[[NTLM]]'
- '[[pass the hash]]'
---

# Mimikatz

## Overview

Mimikatz is a post exploitation tool which aids in the extraction of hashed and cleartext passwords, PIN codes, and Kerberos tickets from memory. It can also be used for pass-the-hash attacks, pass-the-ticket, or build Golden tickets. 

## Description

# Description

Mimikatz is a post exploitation tool which aids in the extraction of hashed and cleartext passwords, PIN codes, and Kerberos tickets from memory. It can also be used for pass-the-hash attacks, pass-the-ticket, or build Golden tickets.



# Example



{{EMBEDDED_COMMAND_92396b13-6d83-4737-ae7b-c5b8260ba77a}}



# Installation

## Compile mimikatz.exe on Windows 10

1. Download and install MS Visual Studio 2013: [https://visualstudio.microsoft.com/vs/older-downloads/](https://visualstudio.microsoft.com/vs/older-downloads/)

2. Download and install the Windows Driver Kit 7.1: [https://github.com/gentilkiwi/mimikatz.git](https://github.com/gentilkiwi/mimikatz.git)

3. Clone the mimikatz repository



4. Open "mimikatz.sln" with Visual Studio.
5. Set the "Solution Platform" to match the target (generally x64 or Win32)
6. Select "Build" > "Rebuilt Solution"
7. The compiled files are in .\mimikatz\x64







## Platforms

- Windows

## Commands (1)

- [[Extract Windows LM/NTLM Hashes From LSASS]]

## Tags

- [[Cryptography]]
- [[extract]]
- [[NTLM]]
- [[pass the hash]]


