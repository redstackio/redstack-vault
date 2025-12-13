---
url: ''
tags:
  - java
  - compile
type: tool
platforms:
  - Linux
  - Windows
description: Java compiler to compile the POC code
id: c50c3c63-4fa2-4ce6-9bbe-453cf8629d79
created_at: '2025-12-13T09:00:27.707Z'
updated_at: '2025-12-13T09:00:27.707Z'
verified: false
validated: true
submitted: true
---
# javac

**Status**: Unverified

## Overview

Javac is the Java compiler used to compile source code into bytecode for execution.

## Description

Essential for building custom Java POCs in security testing.

## Features

- Compiles Java code

## Installation

### Requirements

- JDK

### Install Commands

```bash
# Included in JDK
```

## Basic Usage

```bash
javac --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--help` | Show help |

## Examples

### Example 1: Basic Usage

```bash
javac QueryHive.java
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Compilation activity

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/java]]

## References

- Oracle JDK docs
