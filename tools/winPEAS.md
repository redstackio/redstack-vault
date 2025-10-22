---
id: b075d77e-0007-4f83-b697-b6db5f795b18
name: winPEAS
type: tool
verified: true
created_at: '2020-03-06T05:51:58.563727+00:00'
updated_at: '2023-10-10T18:30:49.995974+00:00'
commands:
- '[[Enumeate Windows for Privilesge Escalation Paths]]'
platforms:
- Windows
tags:
- '[[Enumeration]]'
- '[[privileges]]'
---

# winPEAS

**Status**: ✓ Verified

## Overview

Windoes Privilege Escalation Awesome Script (winPEAS) enumerates a Windows host for potential privilege escalation paths. This program comes in two versions, a simple .bat file, and a more robust .exe which requires .NET 4+ to run. 

## Description

# Description

Windoes Privilege Escalation Awesome Script (winPEAS) enumerates a Windows host for potential privilege escalation paths. This program comes in two versions, a simple .bat file, and a more robust .exe which requires .NET 4+ to run.

# Example

# Installation

## Download the .BAT

Download a copy of the .BAT script: [Download here](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/blob/master/winPEAS/winPEASbat/winPEAS.bat)

## Download the .EXE

Download a pre-built and obfuscated copy of winPEAS.exe: [Download here](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS/winPEASexe/winPEAS/bin/Obfuscated%20Releases)

## Build the .EXE from Source (Windows)

winPEAS can be compiled with Microsoft Visual Studio Community 2019 with ".NET desktop development" installed.

1. Clone the repository

2. Open winPEAS.sln" with Visual Studio
3. Set the "Solutions Configuration" to "Release"
4. Set the "Solution Platform" to the target's architecture
5. Select "Build" > "Rebuild Solution"

The compiled .exe can be find ount <PEASDirectory>\winPEAS\winPEASexe\winPEAS\bin\x64\Release\winPEAS.exe

winPEAS may be identified as malware due to its capabilities. The makers of winPEAS suggest installing Visual Studio's dotfuscator module. [Click here for instructions](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS/winPEASexe) 

The .EXE variant of winPEAS supports a number of arguments:

## Platforms

- Windows

## Commands (1)

- [[Enumeate Windows for Privilesge Escalation Paths]]

## Tags

- [[Enumeration]]
- [[privileges]]
