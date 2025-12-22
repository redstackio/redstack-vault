---
url: ''
tags:
  - jdbc
  - hive
type: tool
platforms:
  - Linux
  - Windows
description: Driver for connecting to Hive database
id: 76189e31-3d4b-469d-a056-3881f4a4971a
created_at: '2025-12-13T09:00:27.665Z'
updated_at: '2025-12-13T09:00:27.665Z'
verified: false
validated: true
submitted: true
---
# Apache Hive JDBC Driver

**Status**: Unverified

## Overview

JDBC driver for Apache Hive, enabling Java applications to connect to Hive databases.

## Description

Custom compiled version 1.1.0 used for compatibility in exploitation POCs.

## Features

- Database connectivity
- Query execution

## Installation

### Requirements

- Java

### Install Commands

```bash
# Compile or download JAR
```

## Basic Usage

```bash
# Add to classpath
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | N/A |

## Examples

### Example 1: Basic Usage

```bash
# Use in Java application
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Driver loading logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/DataGrip]]

## References

- Apache Hive docs
