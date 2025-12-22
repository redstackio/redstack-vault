---
id: b723c3a7-aa47-4750-8d06-36e77c4c4bb1
type: tool
verified: true
created_at: '2019-08-28T21:17:30.248944+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - android
  - reverse-engineering
  - deobfuscation
  - dex2jar
url: 'https://github.com/pxb1988/dex2jar'
validated: true
---

# d2j-init-deobf

**Status**: Unverified

## Overview

d2j-init-deobf is a component of the dex2jar toolkit designed for initializing deobfuscation processes on Android Dalvik Executable (.dex/.odex) and JAR files. It is used in mobile application reverse engineering to restore readable names to obfuscated code, making analysis easier for security testers and researchers. Common use cases include analyzing potentially malicious Android apps or recovering logic from obfuscated APKs during penetration testing.

## Description

dex2jar is a comprehensive toolkit for working with Android bytecode. d2j-init-deobf specifically handles the initialization of deobfuscation mappings, often using ProGuard or similar mapping files to rename obfuscated classes, methods, and fields. It integrates with other dex2jar components like dex-reader (for parsing DEX files), dex-translator (for converting to JAR), and dex-ir (intermediate representation). This tool is essential for post-exploitation analysis in mobile security assessments.

## Features

- Initialization of deobfuscation mappings from ProGuard files
- Generation of default mappings for apps without explicit mappings
- Integration with dex2jar pipeline for full DEX to JAR conversion with deobf
- Support for escaping in type descriptors (e.g., "Lcom/dex2jar\t\u1234;")
- Light-weight API similar to ASM for custom scripting

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher
- Git (for cloning the repository)

### Install Commands

```bash
# Clone the dex2jar repository
git clone https://github.com/pxb1988/dex2jar.git
cd dex2jar

# Build the JAR (requires Apache Ant)
ant dist

# Or download pre-built JAR from releases
wget https://sourceforge.net/projects/dex2jar/files/dex2jar-2.0/dex2jar-2.0.zip
unzip dex2jar-2.0.zip
```

For Windows, use the .bat scripts provided in the distribution.

## Basic Usage

```bash
java -jar d2j.jar d2j-init-deobf --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose logging |
| -f, --file | Specify input file |
| --mapping | Provide mapping file path |

## Examples

### Example 1: Basic Usage

Initialize deobfuscation for a DEX file:

```bash
java -jar d2j.jar d2j-init-deobf -f app.dex -o output --mapping proguard.map
```

### Example 2: Advanced Usage

Generate and apply default mapping:

```bash
java -jar d2j.jar d2j-init-deobf --generate-default -o default.map
java -jar d2j.jar d2j-dex2jar -f app.dex -o app-deobf.jar --deobf default.map
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1422]] Code Signing (for analyzing signed Android apps)
- [[T1407]] Structure and Logic Discovery (deobfuscating app logic)

### Tactics

- [[Privilege Escalation]] Privilege Escalation (in mobile post-exploitation)
- [[Discovery]] Discovery (app component discovery)

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of dex2jar JAR files or output directories in analysis environments
- Java processes invoking d2j.jar with deobf flags
- Generated mapping files (.map) in working directories
- Network downloads of dex2jar from GitHub or SourceForge

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
- SourceForge Downloads: https://sourceforge.net/projects/dex2jar/
- Dex2jar Documentation: Included in repository README
