---
id: 4c6f6466-4bc4-4fbf-877b-7ecb67f36ee8
type: tool
verified: true
created_at: '2019-08-28T21:17:28.013080+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - reverse-engineering
  - deobfuscation
  - android
  - malware-analysis
url: 'https://github.com/pxb1988/dex2jar'
commands:
  - '[[commands/d2j-jar-remap-deobfuscate-jar]]'
validated: true
---

# d2j-jar-remap

**Status**: Unverified

## Overview

d2j-jar-remap is a component of the dex2jar toolkit designed for remapping obfuscated Java JAR files back to their original names using a mapping file. It is primarily used in Android reverse engineering and malware analysis to deobfuscate code protected by tools like ProGuard, making it easier to understand and analyze the structure of applications or malicious binaries.

## Description

The dex2jar project includes several components for working with Dalvik Executable (.dex and .odex) files from Android. d2j-jar-remap specifically handles the remapping of .class files within JAR archives. It reads a mapping file (often generated during the obfuscation process) and applies it to restore meaningful names for classes, methods, and fields. This tool is part of the broader dex-tools suite, which supports modifying APKs, deobfuscating JARs, and converting between dex and JAR formats. Common use cases include security testing of Android apps, identifying vulnerabilities in third-party libraries, and dissecting obfuscated malware samples.

## Features

- Feature 1: Remaps obfuscated JAR files using ProGuard-style mapping files to restore original identifiers.
- Feature 2: Supports force overwrite of output files and handles large archives efficiently.
- Feature 3: Integrates with other dex2jar tools for full dex-to-jar conversion workflows.
- Feature 4: Lightweight API for custom scripting and automation in reverse engineering pipelines.

## Installation

### Requirements

- Java 8 or higher (JDK recommended for full functionality).
- dex2jar toolkit (d2j-jar-remap is included in the main distribution).

### Install Commands

```bash
# Download the latest release from GitHub
wget https://github.com/pxb1988/dex2jar/releases/download/v2.1/dex2jar-2.1.zip

# Unzip the archive
unzip dex2jar-2.1.zip

# On Ubuntu/Kali (alternative via script or manual)
# The tool is not in standard repos; build from source if needed:
git clone https://github.com/pxb1988/dex2jar.git
dex2jar/build.sh
```

For Windows and macOS, download the ZIP and extract; no additional installation required beyond Java.

## Basic Usage

```bash
java -jar d2j-jar-remap-2.0.jar --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage. |
| -f, --force | Force overwrite of the output file if it exists. |
| -v, --verbose | Enable verbose output for debugging. |

## Examples

### Example 1: Basic Usage

Remap a simple obfuscated JAR using a mapping file:

```bash
java -jar dex2jar-2.0/d2j-jar-remap-2.0.jar -f obfuscated-app.jar proguard-mapping.txt deobfuscated-app.jar
```

### Example 2: Advanced Usage

Process with verbose output:

```bash
java -jar dex2jar-2.0/d2j-jar-remap-2.0.jar -f -v input.jar mapping.txt output.jar
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Software Packing]] Software Packing (deobfuscation aspect for analysis).
- [[JavaScript]] JavaScript (extended to Java bytecode analysis in mobile contexts).

### Tactics

- [[Discovery]] Discovery (uncovering hidden code structures in binaries).

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for Java processes invoking d2j-jar-remap JAR files in analysis environments.
- Detection method 2: File system changes showing remapped JARs or temporary dex2jar artifacts during reverse engineering.
- Detection method 3: Network downloads of dex2jar releases or GitHub clones in security toolchains.

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

- Official GitHub Repository: https://github.com/pxb1988/dex2jar
- Documentation: Included in the release ZIP or wiki on GitHub.
- Related Resources: ProGuard documentation for mapping file formats.
