---
id: 6a89ae29-4a3a-4d10-b75f-fae1ff0017e9
name: baksmali
type: tool
verified: true
created_at: '2019-08-28T21:17:24.619284+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - reverse-engineering
  - android
  - mobile
  - disassembly
  - assembly
url: 'https://github.com/JesusFreke/smali'
validated: true
---

# baksmali

**Status**: Unverified

## Overview

baksmali is a disassembler for the DEX (Dalvik Executable) format used by Android's Dalvik virtual machine. It converts compiled Android bytecode into readable smali assembly code, enabling reverse engineers to analyze, modify, and understand Android applications. It is commonly used in mobile security testing for vulnerability research, malware analysis, and app modification.

## Description

smali/baksmali is a pair of tools: baksmali for disassembly and smali for assembly. The syntax is based on Jasmin and dedexer, supporting full DEX features like annotations, debug info, and line numbers. It is essential for low-level Android reverse engineering, allowing security professionals to inspect app logic, identify hardcoded secrets, or patch behaviors without decompiling to higher-level languages like Java.

## Features

- Feature 1: Full DEX disassembly to smali code with debug information preservation
- Feature 2: Support for multiple API levels and experimental features for newer Android versions
- Feature 3: Integration with tools like apktool for complete APK reverse engineering workflows

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher
- Git (for cloning the repository)

### Install Commands

```bash
# Clone the repository
mkdir -p ~/tools && cd ~/tools
git clone https://github.com/JesusFreke/smali.git
cd smali

# Build the JAR files (requires Maven)
mvn clean package

# Or download pre-built JARs from releases
wget https://github.com/JesusFreke/smali/releases/download/v2.5.2/baksmali-2.5.2.jar
wget https://github.com/JesusFreke/smali/releases/download/v2.5.2/smali-2.5.2.jar
```

For Kali Linux/Ubuntu:
```bash
# Install Java if needed
sudo apt update && sudo apt install default-jre maven git
# Then follow the clone/build steps above
```

## Basic Usage

```bash
java -jar baksmali.jar --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--help` or `-h` | Show help message and usage |
| `--version` or `-v` | Display version information |
| `--api-levels` | Specify Android API levels for compatibility |
| `--no-debug-info` | Strip debug information from output |

## Examples

### Example 1: Basic Usage

Extract DEX from APK and disassemble:
```bash
# First, unzip APK to get classes.dex (or use apktool d app.apk)
unzip app.apk classes.dex

# Disassemble
java -jar baksmali.jar disassemble classes.dex -o smali_code
```

### Example 2: Advanced Usage

Disassemble with specific output and API level:
```bash
java -jar baksmali.jar disassemble classes.dex -o output_dir --api-levels 30
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1422]] Code Signing (for analyzing Android app signatures and modifications)
- [[T1407]] Structure and Enumeration (for mobile application reverse engineering)

### Tactics

- [[Reconnaissance]] Reconnaissance (gathering app internals)
- [[Discovery]] Discovery (examining app components)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Presence of smali directories or baksmali.jar in forensic analysis of analyst machines
- Detection method 2: Modified APKs with tampered DEX files in app distribution monitoring
- Detection method 3: Java processes invoking baksmali.jar in process monitoring on analysis environments

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
- [[tools/jadx]]
- [[tools/dex2jar]]

## References

- Official GitHub: https://github.com/JesusFreke/smali
- Documentation: Included in JAR help or repo README
- Android Reverse Engineering Guide: https://developer.android.com/studio/command-line
