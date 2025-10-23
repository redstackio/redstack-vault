---
id: e688ac23-d622-4c35-bc4c-4342414cf0f0
name: linPEAS
type: tool
verified: true
created_at: '2020-02-29T01:35:57.840170+00:00'
updated_at: '2023-05-30T19:54:44.356865+00:00'
commands:
- '[[linPEAS Enumerate a Linux/Unix System with All Checks]]'
platforms:
- Linux
tags:
- '[[Enumeration]]'
- '[[privileges]]'
---

# linPEAS

**Status**: ✓ Verified

## Overview

linPEAS is a Linux enumeration script which focuses on finding privilege escalation paths. It performs many of the same checks as other enumeration scripts (LinEnum, lse, etc), including permission, SUIDs, misconfigurations, network/process enumeration, etc. It also color codes the results in order

## Description

# Description

linPEAS is a Linux enumeration script which focuses on finding privilege escalation paths. It performs many of the same checks as other enumeration scripts (LinEnum, lse, etc), including permission, SUIDs, misconfigurations, network/process enumeration, etc. It also color codes the results in order to draw attention to findings which warrant further investigation:



- RED/YELLOW: 99% a PE vector

- RED: You must take a look at it

- LightCyan: Users with console

- Blue: Users without console & mounted devs

- Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 

- LightMangenta: Your username



# Example



{{EMBEDDED_COMMAND_e8900666-a057-4077-a482-bf664b8caabd}}



# Installation

Clone the repository then copy linpeas.sh to the target









## Platforms

- Linux

## Commands (1)

- [[linPEAS Enumerate a Linux/Unix System with All Checks]]

## Tags

- [[Enumeration]]
- [[privileges]]


