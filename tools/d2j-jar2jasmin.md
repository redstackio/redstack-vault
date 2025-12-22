---
id: 69c70bf0-df94-46e8-8460-383fefa75785
name: d2j-jar2jasmin
type: tool
verified: true
created_at: '2019-08-28T21:17:33.416612+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - reverse-engineering
  - java
  - android
  - decompilation
url: 'https://github.com/pxb1988/dex2jar'
validated: true
---

# d2j-jar2jasmin

**Status**: Unverified

## Overview

d2j-jar2jasmin is a component of the dex2jar toolkit, designed for reverse engineering Java and Android applications. It specifically converts Java JAR files (containing bytecode) into Jasmin assembly format, which is a human-readable representation of bytecode. This tool is useful in security testing for analyzing, modifying, or deobfuscating Java-based applications, particularly in mobile app security assessments.

## Description

dex2jar is a broader suite that handles Dalvik Executable (.dex/.odex) files from Android, but d2j-jar2jasmin focuses on JAR-to-Jasmin conversion. It disassembles class files within a JAR into .j files using Jasmin syntax, enabling detailed inspection of bytecode logic without full decompilation to source code. Common use cases include identifying hardcoded secrets, analyzing control flows, or preparing for bytecode injection in offensive security operations.

## Features

- Converts JAR files to Jasmin assembly (.j files)
- Supports processing of individual classes or entire archives
- Integrates with other dex2jar components for end-to-end Android reverse engineering
- Lightweight and script-based for easy automation

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher
- Git for cloning the repository

### Install Commands

```bash
# Clone the dex2jar repository (d2j-jar2jasmin is included)
git clone https://github.com/pxb1988/dex2jar.git
cd dex2jar

# Build if necessary (pre-built binaries available in releases)
./gradlew dist

# Or download pre-built release from GitHub
wget https://github.com/pxb1988/dex2jar/releases/download/v2.1/dex2jar-2.1.zip
unzip dex2jar-2.1.zip
```

For Windows, use the .bat equivalents or WSL.

## Basic Usage

```bash
d2j-jar2jasmin.sh --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-f, --force` | Force overwrite of output files |
| `-o, --output` | Specify output directory |

## Examples

### Example 1: Basic Usage

```bash
d2j-jar2jasmin.sh myapp.jar ./output
```

This converts myapp.jar to Jasmin files in the ./output directory.

### Example 2: Advanced Usage

```bash
d2j-jar2jasmin.sh -f obfuscated.jar ./deobf-output
```

Forces conversion even if files exist, useful for iterative analysis.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Software Packing]] Software Packing (for unpacking/obfuscation analysis)
- [[JavaScript]] JavaScript (extended to Java bytecode analysis)

### Tactics

- [[Execution]] Execution (analyzing execution flows)
- [[Discovery]] Discovery (code discovery in binaries)

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of dex2jar scripts or Jasmin .j files in working directories
- Java processes invoking d2j-jar2jasmin.sh
- File system changes: JAR files being converted to assembly

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/dex2jar]]
- [[jadx]]
- [[procyon-decompiler]]

## References

- Official GitHub: https://github.com/pxb1988/dex2jar
- Dex2jar Documentation: Included in repository README
- Jasmin Assembler: http://jasmin.sourceforge.net/
