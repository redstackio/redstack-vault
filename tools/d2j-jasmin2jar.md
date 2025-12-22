---
id: dce62801-0ede-48a6-9cf0-2f66701ae6f1
type: tool
verified: true
description: >-
  A utility within the dex2jar suite for assembling Jasmin bytecode files into
  Java JAR archives, used in Android reverse engineering.
url: 'https://github.com/pxb1988/dex2jar'
created_at: '2019-08-28T21:17:37.841490+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - reverse-engineering
  - android
  - mobile
  - dex2jar
validated: true
---

# d2j-jasmin2jar

**Status**: Unverified

## Overview

d2j-jasmin2jar is a component of the dex2jar toolkit, designed for converting Jasmin assembly bytecode (.j files) back into executable Java JAR files. It is primarily used in mobile security testing and reverse engineering of Android applications, allowing analysts to modify disassembled code (e.g., from smali) and reassemble it into a functional JAR for further analysis or repackaging into APKs.

## Description

dex2jar is a comprehensive set of tools for working with Android's Dalvik Executable (.dex and .odex) format. The d2j-jasmin2jar utility specifically handles the assembly of Jasmin files, which are human-readable representations of Java bytecode. This enables tasks like deobfuscation, patching vulnerabilities, or injecting code into Android apps. It integrates with other dex2jar components such as dex-reader (for parsing DEX), dex-translator (for DEX to JAR conversion), and dex-ir (intermediate representation). Unlike smali/baksmali, it supports escaped characters in type descriptors, making it suitable for complex obfuscated apps.

## Features

- Assembles Jasmin (.j) files to JAR archives
- Supports directory inputs for multi-file assembly
- Integrates with dex2jar's optimize pipeline for cleaner output
- Handles escaped Unicode in class/type names (e.g., "Lcom/dex2jar\t\u1234;")
- Lightweight API compatible with ASM for custom extensions

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher
- dex2jar suite (includes d2j-jasmin2jar.jar)

### Install Commands

On Kali Linux or Ubuntu:

```bash
# Download and extract dex2jar
wget https://github.com/pxb1988/dex2jar/releases/download/v2.1/dex2jar-2.1.zip
unzip dex2jar-2.1.zip -d /opt/dex2jar
cd /opt/dex2jar
chmod +x *.sh
```

On macOS with Homebrew:

```bash
brew install dex2jar
```

On Windows: Download the ZIP from GitHub, extract, and ensure Java is in PATH.

## Basic Usage

```bash
java -jar d2j-jasmin2jar.jar --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -o, --output | Specify output JAR file |
| -f, --force | Overwrite existing output |
| -v, --verbose | Enable verbose logging |

## Examples

### Example 1: Basic Usage

Assemble a single Jasmin file:

```bash
java -jar /opt/dex2jar/d2j-jasmin2jar.jar -o output.jar input.j
```

### Example 2: Advanced Usage

Assemble from a directory with verbose output:

```bash
java -jar /opt/dex2jar/d2j-jasmin2jar.jar -v -o rebuilt.jar jasmin_sources/
```

## Related Commands

- [[commands/d2j-jasmin2jar-convert]]

## References

- Official GitHub: https://github.com/pxb1988/dex2jar
- Dex2jar Documentation: Included in the release ZIP
