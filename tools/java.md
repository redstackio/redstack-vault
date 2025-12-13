---
url: ''
tags:
  - java
  - runtime
type: tool
platforms:
  - Linux
  - Windows
description: Runtime to execute the compiled Java POC for querying Hive
id: 4287c3a8-9ca2-40a3-9e85-c114b71c5e55
created_at: '2025-12-13T09:00:27.702Z'
updated_at: '2025-12-13T09:00:27.702Z'
verified: false
validated: true
submitted: true
---
# java

**Status**: Unverified

## Overview

Java runtime environment for executing compiled Java code.

## Description

Used to run custom POCs that interact with databases like Hive.

## Features

- Executes Java bytecode
- Classpath management

## Installation

### Requirements

- JRE/JDK

### Install Commands

```bash
# Install JDK
```

## Basic Usage

```bash
java --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-classpath` | Set classpath |

## Examples

### Example 1: Basic Usage

```bash
java -classpath '.:./runtime/*' QueryHive ████████:10000 "SELECT 1"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Java process monitoring

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

- Oracle Java docs
