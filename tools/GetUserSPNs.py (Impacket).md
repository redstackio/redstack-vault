---
id: 0bd559ef-80fe-4ab2-b8a0-6937f6c6ff95
name: GetUserSPNs.py (Impacket)
type: tool
verified: true
created_at: '2020-03-06T21:48:07.585987+00:00'
updated_at: '2023-05-30T19:53:26.451873+00:00'
commands:
- '[[GetUserSPN.py Query Domain for SPNs and Dump Available Hashes]]'
platforms:
- Windows
tags:
- '[[Active Directory]]'
- '[[Enumeration]]'
- '[[kerberoast]]'
---

# GetUserSPNs.py (Impacket)

**Status**: ✓ Verified

## Overview

Impacket suite tool used to find Service Principal Names that are associated with normal user account and make a TGS request. Since the TGS request will encrypt the ticket with the account the SPN is running under, this retrieves that user's password hash which John the Ripper or Hashcat can brute 

## Description

# Description

Impacket suite tool used to find Service Principal Names that are associated with normal user account and make a TGS request. Since the TGS request will encrypt the ticket with the account the SPN is running under, this retrieves that user's password hash which John the Ripper or Hashcat can brute force.



# Example



{{EMBEDDED_COMMAND_cfe8a48e-084c-42b7-b6b5-b66fba573639}}



# Installation

## **Install using Python 3's pip (Windows/Linux)**









## Platforms

- Windows

## Services

- ldap
- netbios-ss
- smb

## Commands (1)

- [[GetUserSPN.py Query Domain for SPNs and Dump Available Hashes]]

## Tags

- [[Active Directory]]
- [[Enumeration]]
- [[kerberoast]]


