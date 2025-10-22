---
id: 48e4a8ea-7aad-4a4a-a288-2e196a50e181
name: SharpHound
type: tool
verified: false
created_at: '2019-08-28T21:17:32.038105+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[SharpHound Ingest AD Domain Information and Dump Results to File]]'
platforms:
- Windows
tags:
- '[[Active Directory]]'
- '[[Enumeration]]'
---

# SharpHound

## Overview

Bloodhound ingestor built in C# using .NET 4.5. Gathers information about an Active Directory environment and outputs files that can be processed by BloodHound. It must be run with domain user privileges, be that from the current user, using runas.exe, or the "ldapusername" and "ldappassword" argum

## Description

# Description

Bloodhound ingestor built in C# using .NET 4.5. Gathers information about an Active Directory environment and outputs files that can be processed by BloodHound. It must be run with domain user privileges, be that from the current user, using runas.exe, or the "ldapusername" and "ldappassword" arguments.

# Example

# Installation

## Download SharpHound

The latest pre-built version of SharpHound can be downloaded here: [SharpHound Ingestors](https://github.com/BloodHoundAD/BloodHound/tree/master/Ingestors)

## Build from Source (Windows)

SharpHound can be compiled using Microsoft Visual Studio Community 2019, with ".NET desktop development" , "ASP.NET and web development, and ".NET Core cross-platform development" installed.

1. Clone the repository

2. Open SharpHound.sln with Visual Studio
3. Set "Solutions Configuration" to "Release"
4. Select "Build" > "Rebuild Solution"

The compiled .exe and .ps1 can be found in <SharpHound Directory>/SharpHound/bin/Release/

## Platforms

- Windows

## Services

- ldap
- smb

## Commands (1)

- [[SharpHound Ingest AD Domain Information and Dump Results to File]]

## Tags

- [[Active Directory]]
- [[Enumeration]]
