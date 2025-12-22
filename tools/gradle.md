---
url: ''
tags:
  - build
  - java
type: tool
platforms:
  - Linux
  - Windows
description: Build tool to fetch and manage dependencies for Hive JDBC
id: 163b04e5-af19-4419-a33a-3a2273b44adc
created_at: '2025-12-13T09:00:27.721Z'
updated_at: '2025-12-13T09:00:27.721Z'
verified: false
validated: true
submitted: true
---
# gradle

**Status**: Unverified

## Overview

Gradle is a build automation tool used for managing Java dependencies, commonly in POCs for security reproductions.

## Description

Used to fetch Hive JDBC and Hadoop client dependencies for custom Java tools.

## Features

- Dependency management
- Build scripting

## Installation

### Requirements

- Java

### Install Commands

```bash
# Install via SDKMAN or package manager
```

## Basic Usage

```bash
gradle --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--help` | Show help |

## Examples

### Example 1: Basic Usage

```bash
gradle getDeps
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Build process monitoring

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/javac]]

## References

- Gradle official site
