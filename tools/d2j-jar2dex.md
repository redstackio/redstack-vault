---
id: 6410beae-eb23-44ac-b877-7e78f36e4320
type: tool
verified: true
description: >-
  A component of the dex2jar suite for converting JAR files to DEX format, used
  in Android reverse engineering and bytecode analysis.
url: 'https://github.com/pxb1988/dex2jar'
created_at: '2019-08-28T21:17:24.662173Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - android
  - reverse-engineering
  - decompilation
  - bytecode
commands:
  - '[[commands/d2j-jar2dex-convert-jar-to-dex]]'
  - '[[commands/d2j-jar2dex-convert-with-force]]'
validated: true
---

# d2j-jar2dex

**Status**: Unverified

## Overview

d2j-jar2dex is a tool from the dex2jar project designed to convert Java Archive (JAR) files into Dalvik Executable (DEX) format. It is primarily used in Android security testing, reverse engineering, and malware analysis to transform standard Java bytecode into the format executable on Android devices. This enables further disassembly, deobfuscation, or repackaging of Android applications.

## Description

dex2jar is a comprehensive suite for handling Dalvik and Java bytecode conversions. The d2j-jar2dex component specifically handles JAR to DEX translation by reading JAR contents, processing classes through an intermediate representation (dex-ir), optimizing, and writing to DEX. It supports features like handling obfuscated code and is lightweight with an API similar to ASM for bytecode manipulation. Common use cases include preparing JARs for Android APK integration, analyzing decompiled apps, or modifying bytecode for testing purposes.

## Features

- JAR to DEX conversion with optimization passes
- Support for obfuscated or complex bytecode structures
- Integration with other dex2jar tools for full reverse engineering workflows
- Command-line interface for batch processing
- API for programmatic use in custom tools

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher
- Git for cloning the repository

### Install Commands

```bash
# Clone the dex2jar repository
git clone https://github.com/pxb1988/dex2jar.git
cd dex2jar

# Build using Gradle (requires Gradle installed)
./gradlew dist

# Or download pre-built binaries from releases
wget https://github.com/pxb1988/dex2jar/releases/download/v2.1/dex2jar-2.1.zip
unzip dex2jar-2.1.zip

# For Kali/Ubuntu, install via apt if available, or use the above method
sudo apt update && sudo apt install default-jre
git clone https://github.com/pxb1988/dex2jar.git
cd dex2jar && ./gradlew dist
```

Add the lib directory to your PATH for easy access to scripts like d2j-jar2dex.sh.

## Basic Usage

```bash
d2j-jar2dex.sh --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -f, --file | Specify input JAR file |
| -o, --output | Specify output DEX file |
| -force | Overwrite existing output files |
| -v, --verbose | Enable verbose logging |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Convert a JAR to DEX:

```bash
d2j-jar2dex.sh -f /path/to/input.jar -o /path/to/output.dex
```

### Example 2: Advanced Usage

Convert with force overwrite and verbose output:

```bash
d2j-jar2dex.sh -f app.jar -o app.dex -force -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Software Packing]] Software Packing (for repackaging analyzed malware)
- [[JavaScript]] JavaScript (extended to Java bytecode manipulation)

### Tactics

- [[Execution]] Execution (enabling execution in Android environments)
- [[Defense Evasion]] Defense Evasion (deobfuscation and repackaging)

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of dex2jar binaries or scripts in process lists
- File system artifacts like .dex files generated from .jar inputs
- Java processes invoking dex2jar classes (monitor via ps aux | grep dex2jar)
- Network downloads of dex2jar from GitHub during incident response

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/jadx]] (Android DEX decompiler)
- [[tools/apktool]] (APK reverse engineering)
- [[tools/bytecode-viewer]] (Multi-framework bytecode viewer)

## References

- Official GitHub: https://github.com/pxb1988/dex2jar
- dex2jar Documentation: https://sourceforge.net/p/dex2jar/wiki/Home/
- Android Reverse Engineering Guide: https://developer.android.com/studio/debug
