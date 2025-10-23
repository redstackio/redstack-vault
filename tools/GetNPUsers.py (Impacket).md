---
id: 16eb91f1-2b40-4ac0-a4b6-144b01cb5705
name: GetNPUsers.py (Impacket)
type: tool
verified: true
created_at: '2020-03-21T00:28:50.481347+00:00'
updated_at: '2023-05-30T19:52:36.162395+00:00'
commands:
- '[[GetNPUsers.py Brute force Users with "Do Not Require Preauth."]]'
platforms:
- Windows
tags:
- '[[Active Directory]]'
- '[[Enumeration]]'
- '[[Kernel Exploit]]'
---

# GetNPUsers.py (Impacket)

**Status**: ✓ Verified

## Overview

Impacket suite tool which attempts to list the ticket-granting tickets (TGTs) for users with the property "Do not require Kerberos preauthentication" set (UF_DONT_REQUIRE_PREAUTH), effectively getting password hashes without prior authentication. The resulting password hashes can be cracked using t

## Description

# Description

Impacket suite tool which attempts to list the ticket-granting tickets (TGTs) for users with the property "Do not require Kerberos preauthentication" set (UF_DONT_REQUIRE_PREAUTH), effectively getting password hashes without prior authentication. The resulting password hashes can be cracked using tools such as John the Ripper or Hashcat.



# Example



{{EMBEDDED_COMMAND_23c39a33-147b-4f0e-8776-9592377ed8b2}}



# Installation

## **Install using Python 3's pip (Windows/Linux)** 









## Platforms

- Windows

## Services

- smb

## Commands (1)

- [[GetNPUsers.py Brute force Users with "Do Not Require Preauth."]]

## Tags

- [[Active Directory]]
- [[Enumeration]]
- [[Kernel Exploit]]


