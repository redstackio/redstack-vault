---
id: 042082b6-661e-405e-bad0-e415586db243
name: wmiexec.py (Impacket)
type: tool
verified: true
created_at: '2020-03-06T03:07:31.483816+00:00'
updated_at: '2023-05-30T19:52:02.602585+00:00'
commands:
- '[[wmiexec.py Connect and Spawn a Command Shell]]'
platforms:
- Windows
tags:
- '[[administrator]]'
- '[[Network]]'
---

# wmiexec.py (Impacket)

**Status**: ✓ Verified

## Overview

Impacket suite tool which uses WMI to execute commands on a remote system. While similar to smbexec.py, wmiexec runs as Administrator rather than SYSTEM, and leaves fewer traces in events logs, though it requires access to the machine's DCOM ports. 

## Description

# Description

Impacket suite tool which uses WMI to execute commands on a remote system. While similar to smbexec.py, wmiexec runs as Administrator rather than SYSTEM, and leaves fewer traces in events logs, though it requires access to the machine's DCOM ports.

# Example

# Installation

## **Install using Python 3's pip (Windows/Linux)**

## Platforms

- Windows

## Services

- dcom-scm
- smb

## Commands (1)

- [[wmiexec.py Connect and Spawn a Command Shell]]

## Tags

- [[administrator]]
- [[Network]]
