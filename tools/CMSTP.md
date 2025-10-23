---
id: fdce6099-d49d-4606-98d7-8d987924826d
name: CMSTP
type: tool
verified: false
created_at: '2019-08-28T21:17:37.410908+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[cmstp Run an INF file]]'
platforms:
- Windows
tags:
- '[[applocker]]'
- '[[Defense Bypass]]'
---

# CMSTP

## Overview

The Microsoft Connection Manager Profile Installer (CMSTP.exe) is a command line utility used to install Connection Manager service profiles via INF files. Attackers can craft INF files to load and execute DLLs and/or COM scripts (SCT) from remote servers. This technique may act as an AppLocker byp

## Description

# Description

The Microsoft Connection Manager Profile Installer (CMSTP.exe) is a command line utility used to install Connection Manager service profiles via INF files. Attackers can craft INF files to load and execute DLLs and/or COM scripts (SCT) from remote servers. This technique may act as an AppLocker bypass, if AppLocker is configured to only execute signed Microsoft binaries.



# Example



{{EMBEDDED_COMMAND_b5428658-adfc-4265-be49-f8c7a295a246}}



# Installation

CMSTP.exe is installed with Windows







## Platforms

- Windows

## Commands (1)

- [[cmstp Run an INF file]]

## Tags

- [[applocker]]
- [[Defense Bypass]]


