---
url: 'https://www.adobe.com/devnet/flex/flex-sdk-download.html'
tags:
  - compilation
  - flash
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: 'SDK for compiling ActionScript to SWF files, used to build Flash exploits.'
id: 15acda11-8905-4c6b-aafe-376dac0eab6a
created_at: '2025-12-14T17:27:29.667Z'
updated_at: '2025-12-14T17:27:29.667Z'
verified: false
validated: true
submitted: true
---
# Adobe-Flex-SDK

**Status**: Unverified

## Overview

Open-source SDK (version 4.6) for developing and compiling Flex applications into SWF for browser execution in attack payloads.

## Description

Compiles AS3 code for socket-based exploits, integrated with JS for CSRF chaining.

## Features

- Feature 1: mxmlc compiler for AS3
- Feature 2: Library support for networking
- Feature 3: Debugging tools

## Installation

### Requirements

- Java runtime

### Install Commands

```bash
wget http://download.macromedia.com/pub/developer/flex/sdk/flex_sdk_4.6.0.23201.zip
unzip flex_sdk_4.6.0.23201.zip
```

## Basic Usage

```bash
./bin/mxmlc exploit.as
```

### Common Options

| Option | Description |
|--------|-------------|
| -debug | Include debug symbols |

## Examples

### Example 1: Basic Usage

```bash
mxmlc -output=exploit.swf socket.as
```

### Example 2: Advanced Usage

With libraries

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- mxmlc process executions
- Generated SWF files

## Related Procedures

- [[procedures/Use-Adobe-Flash-for-Arbitrary-TCP-Connections]]

## Related Tools

- [[tools/Adobe-Flash]]

## References

- Adobe download archive
