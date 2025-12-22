---
id: tool-001
url: 'https://www.eclipse.org/mat/'
tags:
  - memory-analysis
  - java
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.357Z'
validated: true
submitted: true
---
# Eclipse-Memory-Analyzer

**Status**: Unverified

## Overview

Eclipse Memory Analyzer (MAT) is a Java heap analysis tool used to inspect memory dumps for leaks, performance issues, and sensitive data extraction in security contexts.

## Description

MAT parses .hprof files to provide visualizations of heap contents, including object graphs and string searches, ideal for finding credentials in exploited dumps from Spring Boot applications.

## Features

- Feature 1: Heap dump parsing and leak detection
- Feature 2: Query language for searching strings and objects
- Feature 3: Report generation for exported findings

## Installation

### Requirements

- Java 8 or higher
- Eclipse IDE (optional)

### Install Commands

```bash
# Download from official site and extract
wget https://download.eclipse.org/mat/1.14/mat-1.14.0-win32.win32.x86_64.zip
unzip mat-1.14.0-win32.win32.x86_64.zip
```

## Basic Usage

```bash
# Launch via ParseHeapDump.sh or GUI
./ParseHeapDump.sh heapdump.hprof
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose parsing output |

## Examples

### Example 1: Basic Usage

```bash
# Open GUI and load file
MemoryAnalyzer
```

### Example 2: Advanced Usage

```bash
# Command-line parsing
java -jar org.eclipse.mat.api.jar -parse heapdump.hprof
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for mat.exe or Java with MAT jars
- File access logs showing .hprof parsing

## Related Procedures


## Related Tools

- [[tools/VisualVM]]

## References

- Official documentation: https://wiki.eclipse.org/MemoryAnalyzer
