---
id: 728a8253-4649-49f5-a715-2b356edf5e80
name: SharpUp
type: tool
verified: false
created_at: '2019-08-28T21:17:27.307699+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[PowerUp Enumerate for Privilege Escalation]]'
platforms:
- Windows
tags:
- '[[Enumeration]]'
---

# SharpUp

## Overview

SharpUp is a C# port of various PowerUp functions.  SharpUp has only implemented the more popular checks and no weaponization features have been added. Scans Include: Common privilege escalation paths Vulnerable services DLL hijacking opportunities Vulnerable registry settings 

## Description

# Description

SharpUp is a C# port of various PowerUp functions.  SharpUp has only implemented the more popular checks and no weaponization features have been added.

Scans Include:

- Common privilege escalation paths

- Vulnerable services

- DLL hijacking opportunities

- Vulnerable registry settings

# Example

# Installation

## Build from Source (Windows)

SharpUp can be compiled with Microsoft Visual Studio Community versions 2015 to 2019 with ".NET desktop development" installed.

1. Clone the repo

2. Open SharpUp.sln with Visual Studio

3. Set "Solutions Configuration" to "Release"

4. Select "Build" > ""Rebuild Solution"

The compiled .exe can be found in <SharpUp Directory>/SharpUp/bin/Release/SharpUp.exe

## Platforms

- Windows

## Commands (1)

- [[PowerUp Enumerate for Privilege Escalation]]

## Tags

- [[Enumeration]]
