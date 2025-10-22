---
id: 48c68642-611b-410c-aa8e-96bd2bf67926
name: psexec.py (Impacket)
type: tool
verified: false
created_at: '2019-08-28T21:17:26.315589+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[psexec.py Connect and Spawn a Command Shell]]'
platforms:
- Windows
tags:
- '[[administrator]]'
- '[[Network]]'
- '[[NTLM]]'
---

# psexec.py (Impacket)

## Overview

Impacket suite implementation of PSEXEC, a remote access tool which allows Administrators to interact with the system's command prompt. This tool requires the user have full access to the target's SMB admin share, as it copies a .SVC file to the share, launches a service to run the file, then uses 

## Description

# Description

Impacket suite implementation of PSEXEC, a remote access tool which allows Administrators to interact with the system's command prompt. This tool requires the user have full access to the target's SMB admin share, as it copies a .SVC file to the share, launches a service to run the file, then uses named pipes to connect to the session.

# Example

# Installation

## **Install using Python 3's pip (Windows/Linux)**

## Platforms

- Windows

## Services

- smb

## Commands (1)

- [[psexec.py Connect and Spawn a Command Shell]]

## Tags

- [[administrator]]
- [[Network]]
- [[NTLM]]
