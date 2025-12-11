---
url: 'https://jfrog.com/cli/'
tags:
  - artifactory
  - devops
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: 'Command-line interface for JFrog products, including Artifactory.'
id: 207343e9-c260-4457-a758-87ddc9e968d8
created_at: '2025-12-11T03:47:56.492Z'
updated_at: '2025-12-11T03:47:56.492Z'
verified: false
validated: true
submitted: true
---
# JFrog CLI

**Status**: Unverified

## Overview

JFrog CLI is used for interacting with Artifactory, including uploading, downloading, and managing artifacts.

## Description

Provides commands for configuration, searching, and deploying artifacts, useful in supply chain attacks.

## Features

- Repository management
- Artifact search and upload
- Integration with CI/CD

## Installation

### Requirements

- Go or direct binary

### Install Commands

```bash
curl -fL https://getcli.jfrog.io | sh
```

## Basic Usage

```bash
jfrog --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `rt config` | Configure server |
| `rt upload` | Upload files |

## Examples

### Example 1: Basic Usage

```bash
jfrog rt ping
```

### Example 2: Advanced Usage

```bash
jfrog rt upload file repo/
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Supply Chain Compromise]]

### Tactics

- [[Persistence]]

## Detection

Indicators and methods for detecting this tool's usage:

- Logs of jfrog commands
- Network traffic to Artifactory endpoints

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Curl]]

## References

- https://jfrog.com/help/r/jfrog-cli
