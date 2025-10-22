---
id: b83d3105-5ed2-4c80-b2d7-58d67644c867
name: linuxprivcheck.py
type: tool
verified: true
created_at: '2020-02-22T02:53:00.013490+00:00'
updated_at: '2023-05-30T19:58:51.600877+00:00'
commands:
- '[[linuxprivchecker.py Scan a Linux Filesystem for Vulnerabilities]]'
platforms:
- Linux
tags:
- '[[Enumeration]]'
- '[[File System]]'
- '[[known vulnerability]]'
- '[[misconfiguration]]'
---

# linuxprivcheck.py

**Status**: ✓ Verified

## Overview

linuxprivchecker.py is a Linux privilege escalation check script which is run locally on a target to search for common privilege escalation vectors such as world writable files, misconfigurations, clear-text passwords, and applicable exploits. The exploit suggester is useful for older systems, but 

## Description

# Description

linuxprivchecker.py is a Linux privilege escalation check script which is run locally on a target to search for common privilege escalation vectors such as world writable files, misconfigurations, clear-text passwords, and applicable exploits. The exploit suggester is useful for older systems, but is unreliable at identifying newer exploits as the signatures were last updated in 2016.

# Example

Installation

Clone the repo and copy linuxprivchecker.py to the target

## Platforms

- Linux

## Commands (1)

- [[linuxprivchecker.py Scan a Linux Filesystem for Vulnerabilities]]

## Tags

- [[Enumeration]]
- [[File System]]
- [[known vulnerability]]
- [[misconfiguration]]
