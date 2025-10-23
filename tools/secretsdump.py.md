---
id: 40eb3230-928e-4971-b67f-a701bf1547f9
name: secretsdump.py
type: tool
verified: true
created_at: '2020-03-16T03:14:52.907252+00:00'
updated_at: '2023-05-30T01:08:57.806518+00:00'
commands:
- '[[Dump Password Hashes from a Remote System (Authenticated)]]'
platforms:
- Windows
tags:
- '[[dump]]'
- '[[Network]]'
- '[[NTLM]]'
---

# secretsdump.py

**Status**: ✓ Verified

## Overview

Impacket's suite's secrestdump.py performs various techniques to dump hashes from the remote machine without executing any agent on the remote machine without executing any agent there. For SAM and LSA Secrets (including cached creds) it tries to read as much as it can from the registry and then sa

## Description

# Description

Impacket's suite's secrestdump.py performs various techniques to dump hashes from the remote machine without executing any agent on the remote machine without executing any agent there. For SAM and LSA Secrets (including cached creds) it tries to read as much as it can from the registry and then save the hives in the target system (%SYSTEMROOT%\\Temp dir) and read the rest of the data from there.



# Example



{{EMBEDDED_COMMAND_a87ed429-8db3-4bd4-8424-2ac200c81d5a}}



# Installation

## Install on Debian/Ubuntu









## Platforms

- Windows

## Services

- dcom-scm
- smb

## Commands (1)

- [[Dump Password Hashes from a Remote System (Authenticated)]]

## Tags

- [[dump]]
- [[Network]]
- [[NTLM]]


