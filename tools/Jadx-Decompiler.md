---
url: 'https://github.com/skylot/jadx'
tags:
  - decompiler
  - android
  - reverse-engineering
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.209Z'
description: Command-line and GUI tool for decompiling Android APKs into Java source code.
id: 1ca3bd6b-de3a-4946-bebf-c40a68863723
validated: true
submitted: true
---
# Jadx-Decompiler

**Status**: Unverified

## Overview

Jadx is a dex to java decompiler for Android APKs, useful for static analysis in security testing to uncover vulnerabilities like insecure intent handling.

## Description

Supports decompiling Dalvik bytecode to Java, viewing resources, and searching code. Commonly used in offensive security for app reverse engineering.

## Features

- Feature 1: CLI and GUI modes
- Feature 2: Smali and resource viewing
- Feature 3: Search and navigation in decompiled code

## Installation

### Requirements

- Java 8+
- Build tools (Maven)

### Install Commands

```bash
# Clone and build
wget https://github.com/skylot/jadx/releases/download/v1.4.7/jadx-1.4.7.zip
unzip jadx-1.4.7.zip
# Or via brew: brew install jadx
```

## Basic Usage

```bash
jadx --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-d <dir>` | Output directory |
| `--deobf` | Deobfuscate names |
| `-v` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
jadx app.apk -d output
```

### Example 2: Advanced Usage

```bash
jadx -Xmx2g app.apk --deobf -d src
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Jadx processes in task manager
- Decompiled directories on analyst machines

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Apktool]]
- [[Dex2jar]]

## References

- Official documentation: https://github.com/skylot/jadx
