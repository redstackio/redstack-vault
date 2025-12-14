---
id: t1b2c3d4-e5f6-7890-abcd-ef1234567895
url: 'https://www.adobe.com/devnet/actionscript.html'
tags:
  - flash
  - compilation
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:09.975Z'
validated: true
submitted: true
---
# ActionScript Compiler

**Status**: Unverified

## Overview

The ActionScript Compiler (ASC) is used to compile ActionScript source code into SWF files for Flash applications, essential for creating PoC exploits involving Flash behaviors like file uploads.

## Description

ASC is Adobe's tool for building Flash content, supporting ActionScript 3.0. In offensive security, it's used to craft SWF files that exploit browser Flash implementations, such as handling redirects in uploads. It runs on multiple platforms and integrates with development environments.

## Features

- Feature 1: Compiles .as to .swf binaries
- Feature 2: Supports debugging and optimization flags
- Feature 3: Handles Flash API imports like FileReference

## Installation

### Requirements

- Java Runtime Environment (JRE)
- Adobe Flash Player SDK

### Install Commands

```bash
# Download and extract Adobe Flex SDK (includes ASC)
wget https://archive.apache.org/dist/flex/4.6.0/binaries/apache-flex-sdk-4.6.0-bin.tar.gz
tar -xzf apache-flex-sdk-4.6.0-bin.tar.gz
# Set PATH to bin/asc
```

## Basic Usage

```bash
asc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-O` | Optimize output |
| `-d` | Debug mode |

## Examples

### Example 1: Basic Usage

```bash
asc input.as -o output.swf
```

### Example 2: Advanced Usage

```bash
asc -O input.as -o optimized.swf
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of asc executable or SWF compilation artifacts
- Network downloads of Flex SDK

## Related Procedures


## Related Tools

- [[tools/PHP-Redirect-Server]]

## References

- Official documentation: https://www.adobe.com/devnet/actionscript.html
- Related resources: Adobe Flex SDK archives
