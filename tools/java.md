---
id: uuid-t6
url: ''
tags:
  - runtime
  - java
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.578Z'
validated: true
submitted: true
---
# java

**Status**: Unverified

## Overview

java is the Java runtime, executing compiled classes like QueryHive for Hive queries and exploitation.

## Description

Runs bytecode with specified classpath and arguments for server and SQL.

## Features

- Feature 1: Classpath management
- Feature 2: Argument passing
- Feature 3: JVM options

## Installation

### Requirements

- JRE/JDK

### Install Commands

```bash
apt install openjdk-11-jre
```

## Basic Usage

```bash
java --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -cp | Classpath |

## Examples

### Example 1: Basic Usage

```bash
java -cp . MyClass
```

### Example 2: Advanced Usage

```bash
java -classpath '.:./runtime/*' QueryHive IP:10000 "SELECT 1"
```

## MITRE ATT&CK Mapping

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

- java processes with unusual classpaths

## Related Procedures

- [[procedures/Connect-to-Open-Apache-Hive-Database]]

## Related Tools

- [[tools/javac]]

## References

- Oracle Java docs
