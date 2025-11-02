---
id: e7ae7a92-f6d8-462c-a665-ee0823c768c7
name: Evil-WinRM
type: tool
verified: true
created_at: '2020-03-16T01:49:25.694116+00:00'
updated_at: '2023-05-30T19:59:15.025255+00:00'
commands:
- '[[evil-winrm.rb Connect to a WinRM Server (NTLM)]]'
- '[[evil-winrm.rb Connect to a WinRM Server]]'
platforms:
- Linux
- Windows
tags:
- '[[Defense Bypass]]'
- '[[shell]]'
---

# Evil-WinRM

**Status**: ✓ Verified

## Overview

Spawn a PowerShell instance on a remote Windows system using the WinRM protocol (usually port 5985). Evil-WinRM is written in Ruby and can be run on Linux or Windows systems. Notable features: Load in memory PowerShell scripts Load in memory DLL files to bypass some AV Load in memory C# to bypass s

## Description

# Description

Spawn a PowerShell instance on a remote Windows system using the WinRM protocol (usually port 5985). Evil-WinRM is written in Ruby and can be run on Linux or Windows systems.



Notable features:

- Load in memory PowerShell scripts

- Load in memory DLL files to bypass some AV

- Load in memory C# to bypass some AV

- Bypass AMSI

- Pass-the-hash support

- Kerberos authentication

- SSL with certificates

- Upload/download files



# Example



{{EMBEDDED_COMMAND_4a0275b1-f59a-49b6-baf8-ad85ca69e52e}}



# Installation

## Install on Debian/Ubuntu

1. Install Ruby and build tools



Note: When prompted by the installer to choose a toolchain, select either 1 or 3.



2. Install Evil-WinRM via gem





## Install on Windows

1. Install the latest version of Ruby + Devkit: [Download from rubyinstaller.org](https://rubyinstaller.org/downloads/)

2. Install Evil-WinRM using Ruby's package manager











## Platforms

- Linux
- Windows

## Services

- winrm
- winrm

## Commands (1)

- [[evil-winrm.rb Connect to a WinRM Server]]

## Tags

- [[Defense Bypass]]
- [[shell]]


