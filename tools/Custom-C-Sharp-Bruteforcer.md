---
id: j0k1l2m3-n4o5-6789-jklm-012345678901
url: null
tags:
  - brute-force
  - custom
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.899Z'
validated: true
submitted: true
---
# Custom-C-Sharp-Bruteforcer

**Status**: Unverified

## Overview

Custom-built C# application for brute-forcing 4-digit OTPs against the Grab API by iterating PUT requests.

## Description

Tool takes x-mts-ssid input and sends sequential requests with profileActivationCode from 1000-9999, logging until 204 response. Built for .NET 4.0, attached as tool.zip in report.

## Features

- Feature 1: Automated loop for 9000 combinations
- Feature 2: Response code checking (400 vs 204)
- Feature 3: Session header integration

## Installation

### Requirements

- Windows 7+, .NET Framework 4.0

### Install Commands

```bash
# Unzip tool.zip and run executable
# Compile: csc /target:exe bruteforcer.cs
```

## Basic Usage

```bash
# GUI or CLI: input session ID, run
bruteforcer.exe --session [ID]
```

### Common Options

| Option | Description |
|--------|-------------|
| --session | Input x-mts-ssid |
| --start | Start code (default 1000) |
| --end | End code (default 9999) |

## Examples

### Example 1: Basic Usage

Run with session: bruteforcer.exe --session abc123

### Example 2: Advanced Usage

Custom range: bruteforcer.exe --session abc123 --start 2000 --end 3000

## MITRE ATT&CK Mapping

### Techniques

- [[PowerShell]] PowerShell (adaptable to C#)

### Tactics

- [[Execution]] Execution

## Detection

- Monitor for high-volume PUT requests to /profiles/edit
- .NET process anomalies

## Related Procedures


## Related Tools

- [[tools/Hydra]]
- [[tools/Burp-Intruder]]

## References

- Custom tool from report
