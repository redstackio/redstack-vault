---
id: uuid-t5
url: ''
tags:
  - compile
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.581Z'
validated: true
submitted: true
---
# javac

**Status**: Unverified

## Overview

javac is the Java compiler, used to build custom POC classes like QueryHive for Hive interactions.

## Description

Compiles .java files with JDBC imports into bytecode for execution.

## Features

- Feature 1: Source-to-class compilation
- Feature 2: Error reporting
- Feature 3: Classpath handling

## Installation

### Requirements

- JDK installed

### Install Commands

```bash
# Ubuntu
apt install openjdk-11-jdk
```

## Basic Usage

```bash
javac --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -cp | Classpath |

## Examples

### Example 1: Basic Usage

```bash
javac QueryHive.java
```

### Example 2: Advanced Usage

```bash
javac -cp libs/* MyClass.java
```

## MITRE ATT&CK Mapping

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

- javac process
- Compiled class files

## Related Procedures

- [[procedures/Select-and-Configure-Hive-JDBC-Client]]

## Related Tools

- [[tools/java]]

## References

- Oracle docs
