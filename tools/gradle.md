---
id: uuid-t3
url: 'https://gradle.org/'
tags:
  - build
  - java
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.586Z'
validated: true
submitted: true
---
# Gradle

**Status**: Unverified

## Overview

Gradle is a build automation tool for Java projects, used to manage dependencies like Hive JDBC for custom exploitation POCs.

## Description

Automates downloading and classpath setup for Hive/Hadoop JARs via build scripts.

## Features

- Feature 1: Dependency management with Maven repos
- Feature 2: Custom tasks like getDeps
- Feature 3: Java plugin support

## Installation

### Requirements

- Java 8+

### Install Commands

```bash
# Via SDKMAN
sdk install gradle
```

## Basic Usage

```bash
gradle --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -v | Version info |

## Examples

### Example 1: Basic Usage

```bash
gradle build
```

### Example 2: Advanced Usage

```bash
gradle getDeps
```

## MITRE ATT&CK Mapping

### Techniques

- [[System Time Discovery]] System Binary Proxy Execution

### Tactics

- [[Execution]]

## Detection

- Gradle wrapper executions
- Network to repo1.maven.org

## Related Procedures

- [[procedures/Select-and-Configure-Hive-JDBC-Client]]

## Related Tools

- [[tools/javac]]

## References

- Official: https://gradle.org/guides/
