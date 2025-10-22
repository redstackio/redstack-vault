---
id: 07ac6a4f-9131-4513-a485-fe436d976f0e
name: gpp-decrypt
type: tool
verified: false
created_at: '2019-08-28T21:17:38.502874+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[gpp-decrypt Extract Password from a GPP Encrypted String]]'
platforms:
- Windows
tags:
- '[[Cryptography]]'
- '[[known vulnerability]]'
---

# gpp-decrypt

## Overview

gpp-decrypt is a Ruby script used for decrypting passwords encrypted in Microsoft Group Policy Preferences (GPP) files, often found in Active Directory environments on the SYSVOL share. Though the passwords contained in GPP files are encrypted, Microsoft disclosed the key, making decryption  trivia

## Description

# Description

gpp-decrypt is a Ruby script used for decrypting passwords encrypted in Microsoft Group Policy Preferences (GPP) files, often found in Active Directory environments on the SYSVOL share. Though the passwords contained in GPP files are encrypted, Microsoft disclosed the key, making decryption  trivial with tools like gpp-decrypt.

# Example

# Installation

## Requirements

- Ruby

## Install on Debian/Ubuntu

## Platforms

- Windows

## Commands (1)

- [[gpp-decrypt Extract Password from a GPP Encrypted String]]

## Tags

- [[Cryptography]]
- [[known vulnerability]]
