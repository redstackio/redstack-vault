---
type: tool
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - decompilation
  - reverse-engineering
  - java
url: 'http://www.varaneckas.com/jad/'
validated: true
---

# jad

**Status**: Unverified

## Overview

Jad is a command-line Java decompiler that converts compiled Java class files (.class) back into human-readable Java source code (.java). It is commonly used in offensive security for reverse engineering Java-based applications, such as web apps, Android APKs (after extraction), or enterprise software, to identify vulnerabilities, hardcoded credentials, or business logic flaws. Note that Jad is an older tool (last major update in the early 2000s) and may struggle with Java 1.5+ features like generics or annotations; for modern Java, consider alternatives like CFR or Procyon.

Category: Reverse Engineering

## Description

Jad analyzes Java bytecode and reconstructs the original source code as closely as possible, including methods, fields, and control structures. It supports decompiling single files, directories, or JAR archives and can handle basic obfuscation. In security testing, it's useful during source code review phases to understand application behavior without access to originals. Limitations include incomplete support for newer JVM features and potential inaccuracies in complex code.

## Features

- Feature 1: Decompiles .class files to .java with package structure preservation
- Feature 2: Supports recursive decompilation of inner classes and JAR contents
- Feature 3: Customizable output formatting (indentation, suffixes, comments)
- Feature 4: Basic error handling for corrupted or obfuscated bytecode
- Feature 5: No GUI; lightweight command-line interface for scripting

## Installation

### Requirements

- Java Runtime Environment (JRE) not required, as Jad is a native executable
- Works on 32/64-bit systems, but ensure architecture match

### Install Commands

```bash
# On Kali Linux/Debian/Ubuntu (jad is in repos, but may be outdated)
sudo apt update
sudo apt install jad

# On macOS with Homebrew
brew install jad

# Manual install (download binary from official site)
wget http://www.varaneckas.com/jad/jad158g.linux-i386.tar.gz
# Or for Windows: jad158g.win.zip
tar -xzf jad158g.linux-i386.tar.gz
sudo cp bin/jad /usr/local/bin/
chmod +x /usr/local/bin/jad
```

Verify installation:

```bash
jad -version
```

Expected: "Jad v1.5.8g. Copyright (c) 2001 Pavel Kouznetsov."

## Basic Usage

```bash
jad --help
```

Jad does not have a --help flag but supports options via man jad or jad (which shows usage).

### Common Options

| Option | Description |
|--------|-------------|
| -d <dir> | Output directory for decompiled files |
| -o | Don't verify dependencies (faster, but may miss errors) |
| -r | Decompile inner classes recursively |
| -s <suffix> | File extension for output (default .jad) |
| -t<n> | Indentation size (e.g., -t2 for 2 spaces) |
| -ff | Suppress comments in output |
| -safe | Enable safe mode to avoid exceptions on bad bytecode |

## Examples

### Example 1: Basic Usage

Decompile a single class:

```bash
jad -d ./output Example.class
```

### Example 2: Advanced Usage

Decompile entire JAR:

```bash
jad -d ./decompiled -r -o -t2 app.jar
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Software Packing]] Software Packing (for unpacking/decompiling obfuscated Java)
- [[JavaScript]] JavaScript (extended to Java for scripting analysis, but primarily reverse eng)

### Tactics

- [[Privilege Escalation]] Privilege Escalation (via vuln discovery in decompiled code)
- [[Discovery]] Discovery (application discovery through decompilation)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Process monitoring for 'jad' executable in task lists or logs
- Detection method 2: File system changes: sudden appearance of .jad or .java files in temp dirs from .class sources
- Detection method 3: Network logs if decompiled code reveals C2 endpoints; monitor for jad downloads
- Detection method 4: EDR alerts on binary execution matching jad signatures

## Related Procedures

- [[procedures/Decompile-Java-Application-for-Vulnerability-Analysis]]
- [[procedures/Extract-and-Analyze-JAR-Artifacts]]

## Related Tools

- [[CFR]] (Modern Java decompiler)
- [[JD-CLI]] (Command-line Java decompiler)
- [[Ghidra]] (Full reverse engineering suite)

## References

- Official site: http://www.varaneckas.com/jad/
- Kali Repo: https://packages.kali.org/j/jad
- Usage guide: man jad or online mirrors
