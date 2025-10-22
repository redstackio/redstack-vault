---
id: b4fc4ed5-f731-4e17-8f4e-25ff6af27f04
name: Responder
type: tool
verified: false
created_at: '2019-08-28T21:17:34.007997+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[Responder Intercept an NTLM Hash]]'
platforms:
- Linux
- Windows
tags:
- '[[LLMNR]]'
- '[[Man in the Middle]]'
- '[[Network]]'
- '[[NTLM]]'
---

# Responder

## Overview

Responder is an LLMNR, NBT-NS, and MDNS poisoning tool, which answers specific NBT-NS queries based on their name suffix. By default the tool will only answer to File Server Service requests for SMB. The concept behind Responder is to target and respond to specific queries, which helps improve stea

## Description

# Description

Responder is an LLMNR, NBT-NS, and MDNS poisoning tool, which answers specific NBT-NS queries based on their name suffix. By default the tool will only answer to File Server Service requests for SMB. The concept behind Responder is to target and respond to specific queries, which helps improve stealth and not impact other services.

Responder is also useful for capturing NTLM hashes, by running it on the attacker and either triggering or waiting for a system on the local network to attempt to authenticate with it. The resulting NTLM hash may be brute forced with other tools in an attempt to uncover the password.

# Example

# Installation

## Install on Kali

## Install on Debian/Ubuntu

## Platforms

- Linux
- Windows

## Services

- dns
- ftp
- http
- https
- imap
- kerberos
- ldap
- llmnr
- mdns
- ms-sql
- ms-sql
- netbios-dgm
- netbios-ns
- netbios-ss
- pop3
- rdp
- smb
- smtp
- smtp

## Commands (1)

- [[Responder Intercept an NTLM Hash]]

## Tags

- [[LLMNR]]
- [[Man in the Middle]]
- [[Network]]
- [[NTLM]]
