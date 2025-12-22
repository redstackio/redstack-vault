---
id: 0d351a9b-bf12-48e5-9083-4871a2b0e438
type: tool
verified: true
created_at: '2019-08-28T21:17:33.509491+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - reverse-engineering
  - android
  - disassembler
  - assembler
url: 'https://github.com/JesusFreke/smali'
commands:
  - '[[commands/baksmali-disassemble-dex-file]]'
  - '[[commands/smali-assemble-smali-files]]'
validated: true
---

# smali

**Status**: Unverified

## Overview

smali/baksmali is a suite of tools for disassembling and assembling Android DEX (Dalvik Executable) files. It is essential for reverse engineering Android applications, allowing security researchers to analyze, modify, and repackage APKs. Commonly used in mobile penetration testing to identify vulnerabilities, hardcoded secrets, or manipulate app behavior.

## Description

The smali project provides baksmali for disassembly (converting DEX bytecode to readable smali assembly) and smali for reassembly (converting edited smali back to DEX). The syntax is based on Jasmin and dedexer, supporting full DEX features like annotations, debug info, and line numbers. It operates on extracted DEX files from APKs and is Java-based, making it cross-platform.

## Features

- Feature 1: Full DEX disassembly to editable smali code with debug information preservation.
- Feature 2: Smali assembly supporting experimental features and API level specifications.
- Feature 3: Handles multi-DEX APKs and integrates with tools like apktool for full APK manipulation.

## Installation

### Requirements

- Java 8 or higher (OpenJDK recommended).
- For APK handling, pair with [[tools/apktool]].

### Install Commands

```bash
# Download latest release from GitHub
wget https://github.com/JesusFreke/smali/releases/download/v2.5.2/baksmali-2.5.2.jar
wget https://github.com/JesusFreke/smali/releases/download/v2.5.2/smali-2.5.2.jar

# Or clone and build
apt install default-jdk ant  # On Ubuntu/Debian
git clone https://github.com/JesusFreke/smali.git
cd smali
ant dist
```

On Kali Linux, smali is available via apt:

```bash
apt update && apt install smali
```

## Basic Usage

```bash
java -jar baksmali.jar --help
java -jar smali.jar --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -o, --output | Specify output directory or file |
| --debug-info | Include debug information in disassembly |
| --api-levels | Target specific Android API levels |
| --experimental | Enable experimental features during assembly |

## Examples

### Example 1: Basic Usage

Disassemble a DEX file:

```bash
java -jar baksmali.jar disassemble classes.dex -o smali_out/
```

Assemble back:

```bash
java -jar smali.jar assemble smali_out/ -o classes.dex
```

### Example 2: Advanced Usage

Disassemble with debug info:

```bash
java -jar baksmali.jar disassemble --debug-info classes.dex -o smali_out/
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1420]] Codecorking (for Android app analysis in mobile intrusions)
- [[T1407]] Structure Consumption (analyzing app structures)

### Tactics

- [[Initial Access]] Initial Access (via mobile app exploitation)
- [[Discovery]] Discovery (app reconnaissance)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for Java processes invoking baksmali.jar or smali.jar in forensics.
- Detection method 2: Look for modified APKs with tampered DEX signatures in app stores or endpoints.
- Detection method 3: File system artifacts like temporary smali directories during reverse engineering.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/apktool]]
- [[jadx]]
- [[tools/dex2jar]]

## References

- Official GitHub: https://github.com/JesusFreke/smali
- Documentation: https://github.com/JesusFreke/smali/wiki
- Android Reverse Engineering Guide: https://developer.android.com/studio/debug

*Last updated: 2023-10-01T00:00:00+00:00*
