---
id: uuid-t1
url: 'https://www.jetbrains.com/datagrip/'
tags:
  - database
  - gui
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.591Z'
validated: true
submitted: true
---
# DataGrip

**Status**: Unverified

## Overview

DataGrip is a database IDE from JetBrains for managing and querying databases like Apache Hive, used here for executing SQL payloads against vulnerable servers.

## Description

Supports JDBC connections, custom drivers, and SQL execution; ideal for testing exploits in a GUI environment without custom coding.

## Features

- Feature 1: JDBC driver management for Hive 1.1.0
- Feature 2: SQL query console with result viewing
- Feature 3: Connection testing and schema exploration

## Installation

### Requirements

- Java 11+ runtime
- JetBrains account for trial

### Install Commands

```bash
# Download from website or use snap
snap install datagrip --classic
```

## Basic Usage

```bash
datagrip
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |
| --version | Display version |

## Examples

### Example 1: Basic Usage

Launch and create Hive connection with URI jdbc:hive2://IP:10000.

### Example 2: Advanced Usage

Add custom driver JARs and execute XXE queries in console.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to JetBrains update servers
- Process monitoring for datagrip.exe

## Related Procedures

- [[procedures/Connect-to-Open-Apache-Hive-Database]]

## Related Tools

- [[tools/Hive-JDBC]]

## References

- Official documentation: https://www.jetbrains.com/help/datagrip/connectivity.html
