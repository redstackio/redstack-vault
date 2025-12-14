---
id: uuid-t2
url: ''
tags:
  - jdbc
  - database
type: tool
verified: false
platforms:
  - Java
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.588Z'
validated: true
submitted: true
---
# Hive-JDBC

**Status**: Unverified

## Overview

Hive JDBC is the Java Database Connectivity driver for Apache Hive, enabling SQL queries over Thrift protocol; version 1.1.0 used to connect to vulnerable servers.

## Description

Provides org.apache.hive.jdbc.HiveDriver for URI-based connections; critical for protocol compatibility in exploitation.

## Features

- Feature 1: Thrift-based remote query execution
- Feature 2: Support for unauthenticated connections
- Feature 3: Integration with Java apps for POC

## Installation

### Requirements

- Apache Hive 1.1.0 JARs
- Java classpath setup

### Install Commands

```bash
# Download via Maven or Gradle as in build.gradle
dependencies { implementation 'org.apache.hive:hive-jdbc:1.1.0' }
```

## Basic Usage

```bash
# Via Java code: Class.forName("org.apache.hive.jdbc.HiveDriver");
```

### Common Options

| Option | Description |
|--------|-------------|
| URI | jdbc:hive2://host:port | 

## Examples

### Example 1: Basic Usage

Connection: DriverManager.getConnection("jdbc:hive2://IP:10000", "hive", "");

### Example 2: Advanced Usage

Execute statements with XXE payloads.

## MITRE ATT&CK Mapping

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

- JDBC traffic on port 10000
- Hive query logs

## Related Procedures

- [[procedures/Select-and-Configure-Hive-JDBC-Client]]

## Related Tools

- [[tools/DataGrip]]

## References

- Hive docs: https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Clients
