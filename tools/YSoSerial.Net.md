---
id: uuid-placeholder-t1
url: 'https://github.com/pwntester/ysoserial.net'
tags:
  - deserialization
  - payload
type: tool
verified: false
platforms:
  - Windows
  - .NET
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.185Z'
validated: true
submitted: true
---
# ysoserial.net

**Status**: Unverified

## Overview

ysoserial.net is a .NET serialization payload generator for exploiting deserialization vulnerabilities, including DNN-specific chains.

## Description

It creates gadgets for various formatters like ObjectStateFormatter, targeting classes for RCE or file ops in apps like DNN. Used in offensive security for vuln validation.

## Features

- Feature 1: Multiple gadget chains (e.g., FileSystemUtils)
- Feature 2: Custom command execution
- Feature 3: DNN plugin support

## Installation

### Requirements

- .NET Framework 4.0+
- Windows or Mono

### Install Commands

```bash
# Clone repo
git clone https://github.com/pwntester/ysoserial.net.git
cd ysoserial.net
# Build
msbuild ysoserial.sln
```

## Basic Usage

```bash
ysoserial.exe -h
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p` | Payload type |
| `-g` | Gadget chain |
| `-f` | Formatter |

## Examples

### Example 1: Basic Usage

```bash
ysoserial.exe -p WindowsIdentity -g TypeConfuseDelegate
```

### Example 2: Advanced Usage

```bash
ysoserial.exe -p DNNPersonalization -c "calc.exe"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation of Remote Services]]
- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic with serialized payloads
- Process creation of ysoserial.exe

## Related Procedures

- [[procedures/Inject-Crafted-Deserialization-Payload-for-File-Write]]

## Related Tools

- [[Metasploit]]

## References

- GitHub repo
- .NET deserialization guides
