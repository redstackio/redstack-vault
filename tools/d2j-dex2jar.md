---
id: 33c29ec5-c220-44e2-b746-308cb378e339
type: tool
verified: true
created_at: '2019-08-28T21:17:31.820601+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - reverse-engineering
  - android
  - dex
  - jar
  - mobile
url: 'https://github.com/pxb1988/dex2jar'
commands:
  - '[[commands/d2j-dex2jar-convert-dex-to-jar]]'
  - '[[commands/d2j-dex2jar-convert-apk-to-jar]]'
validated: true
---

# d2j-dex2jar

**Status**: Unverified

## Overview

d2j-dex2jar is a lightweight tool for converting Android Dalvik Executable (DEX) and Optimized DEX (ODEX) files to standard Java Archive (JAR) files. It is part of the dex2jar suite, commonly used in mobile security testing for reverse engineering Android applications by translating Dalvik bytecode to Java bytecode for further analysis with tools like JD-GUI or Fernflower.

## Description

dex2jar is a set of tools designed to work with Android's DEX format. Key components include:

- **dex-reader**: Reads DEX/ODEX files with a lightweight API similar to ASM for bytecode manipulation.
- **dex-translator**: Converts DEX instructions to an intermediate representation (dex-ir), optimizes it, and outputs ASM-compatible format.
- **dex-ir**: Intermediate representation used internally for instruction handling.
- **dex-tools**: Utilities for working with resulting .class files, such as modifying APKs or deobfuscating JARs.
- **d2j-smali**: Disassembles DEX to smali files and assembles back, supporting advanced syntax like escaped type descriptors.
- **dex-writer**: Writes DEX files in a manner compatible with dex-reader.

This tool is essential for offensive security operations involving Android app analysis, such as identifying vulnerabilities, extracting secrets, or understanding app behavior without running the application.

## Features

- Feature 1: Direct conversion of DEX/ODEX to JAR for Java decompilers.
- Feature 2: Support for APK files by extracting embedded DEX.
- Feature 3: Optimization passes during translation to improve readability.
- Feature 4: Integration with smali for low-level bytecode editing.
- Feature 5: Cross-platform compatibility via Java runtime.

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher.
- unzip utility for extracting the download.

### Install Commands

```bash
# Download the latest release from GitHub
wget https://github.com/pxb1988/dex2jar/releases/download/v2.1/dex2jar-2.1.zip

# Unzip the archive
unzip dex2jar-2.1.zip

# Make scripts executable (Linux/macOS)
chmod +x d2j-dex2jar.sh

# For Windows, use d2j-dex2jar.bat
```

On Kali Linux, it may be available via apt:

```bash
apt update && apt install dex2jar
```

## Basic Usage

```bash
sh d2j-dex2jar.sh --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -f, --force | Force overwrite of output files |
| -o, --output | Specify output file path |
| --deobf | Attempt deobfuscation if mappings available |
| -v, --verbose | Enable verbose logging |

## Examples

### Example 1: Basic Usage

Convert a DEX file to JAR:

```bash
sh d2j-dex2jar.sh classes.dex -o classes.jar
```

### Example 2: Advanced Usage

Convert an APK with force and verbose output:

```bash
sh d2j-dex2jar.sh -f -v app.apk -o app.jar
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1420]] - Codec Information (for Android app analysis in reverse engineering)
- [[Software Discovery]] - Software Discovery (identifying app components and dependencies)

### Tactics

- [[Privilege Escalation]] - Privilege Escalation (via app vulnerability discovery)
- [[Discovery]] - Discovery (app structure and secrets enumeration)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Presence of dex2jar JAR files or scripts in temporary directories.
- Detection method 2: Java processes invoking dex2jar classes (e.g., via `ps aux | grep dex2jar`).
- Detection method 3: Generated JAR files from DEX in analysis environments.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/jadx]]
- [[tools/apktool]]

## References

- Official GitHub: https://github.com/pxb1988/dex2jar
- Documentation: Included in release ZIP or wiki on GitHub
