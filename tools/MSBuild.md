---
id: b8ff8e9d-9485-4651-a2d4-2d2f8680c5ef
name: MSBuild
type: tool
verified: true
created_at: '2020-03-03T02:41:11.369174+00:00'
updated_at: '2023-05-30T01:05:33.199877+00:00'
commands:
- '[[MSBuild Build Package from XML]]'
platforms:
- Windows
tags:
- '[[applocker]]'
- '[[Build]]'
- '[[Defense Bypass]]'
---

# MSBuild

**Status**: ✓ Verified

## Overview

MSBuild (Microsoft Build Engine) is a platform for building applications. It uses an XML schema to control how the platform processes and builds software (similar to Linux's make). MSBuild is a standalone program, and while Visual Studio uses it to compile software, it does not require Visual Studi

## Description

# Description

MSBuild (Microsoft Build Engine) is a platform for building applications. It uses an XML schema to control how the platform processes and builds software (similar to Linux's make). MSBuild is a standalone program, and while Visual Studio uses it to compile software, it does not require Visual Studio, and is often installed alongside .NET. Since MSBuild is a Microsoft signed binary, it can be used to execute commands and bypass AppLocker restrictions when AppLocker is configured to only run signed binaries.

# Example

# Installation

MSBuild can be installed with:

- .NET:  [https://dotnet.microsoft.com/download/dotnet-framework](https://dotnet.microsoft.com/download/dotnet-framework)

- Visual Studio: [https://visualstudio.microsoft.com/vs/community/](https://visualstudio.microsoft.com/vs/community/)

- Build Tools for Visual Studio: [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)

## Platforms

- Windows

## Commands (1)

- [[MSBuild Build Package from XML]]

## Tags

- [[applocker]]
- [[Build]]
- [[Defense Bypass]]
