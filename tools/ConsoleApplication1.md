---
id: tool-uuid-2
url: 'https://github.com/l00ph0le/CVE-2019-0604'
tags:
  - poc
  - encoder
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:31.940Z'
validated: true
submitted: true
---
# ConsoleApplication1

**Status**: Unverified

## Overview

ConsoleApplication1 is a custom C# executable from the CVE-2019-0604 PoC that encodes XAML payloads for SharePoint deserialization exploits.

## Description

Built from the PoC repository, it reads a t.xml file containing malicious XAML and outputs a base64-encoded string for injection, enabling RCE via ObjectDataProvider and cmd.exe.

## Features

- Feature 1: XAML to encoded string conversion
- Feature 2: Support for custom command strings in templates
- Feature 3: Simple CLI interface

## Installation

### Requirements

- .NET Framework
- Visual Studio for building

### Install Commands

```bash
# Clone repo and build: cd ConsoleApplication1; msbuild ConsoleApplication1.csproj
```

## Basic Usage

```cmd
ConsoleApplication1.exe --help
```

### Common Options

| Option | Description |
|--------|-------------|
| input_file | Path to t.xml | Required |

## Examples

### Example 1: Basic Usage

```cmd
ConsoleApplication1.exe c:/path/t.xml
```

### Example 2: Advanced Usage

N/A (single-argument tool)

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Command Shell]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for execution of unknown .exe in PoC directories
- Scan for strings starting with '__' in memory or files

## Related Procedures

- [[procedures/Generate-Encoded-XAML-Payload]]

## Related Tools

- [[tools/Git]]

## References

- PoC repo: https://github.com/l00ph0le/CVE-2019-0604
