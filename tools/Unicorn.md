---
type: tool
description: >-
  Unicorn is a tool for generating shellcode loaders that utilize PowerShell
  downgrade attacks to inject shellcode directly into memory, bypassing common
  antivirus detection.
url: 'https://github.com/trustedsec/Unicorn'
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - powershell
  - shellcode
  - injection
  - defense-evasion
commands:
  - '[[commands/unicorn-generate-powershell-loader]]'
  - '[[commands/unicorn-generate-csharp-loader]]'
validated: true
---

# Unicorn

**Status**: Unverified

## Overview

Unicorn is a lightweight Python-based tool designed for offensive security operations, specifically for creating shellcode loaders. It leverages PowerShell downgrade attacks to execute shellcode in memory without writing files to disk, making it useful for evading endpoint detection and response (EDR) solutions during red team engagements.

## Description

Unicorn generates executable code snippets in various languages (e.g., PowerShell, C#, Python) that perform reflective loading of shellcode. The core technique involves downgrading PowerShell to an unmonitored version (e.g., from 5.0 to 2.0) to avoid logging and then injecting the shellcode directly into the process memory. This tool is particularly effective in Windows environments for post-exploitation scenarios where stealth is required. It does not include shellcode generation; users must provide raw shellcode (e.g., from msfvenom).

## Features

- **PowerShell Downgrade Attack**: Bypasses modern PowerShell monitoring by forcing execution in an older, less logged version.
- **Multi-Language Output**: Supports generating loaders in PowerShell, C#, Python, Ruby, JavaScript, and VB.NET.
- **Reflective Loading**: Injects shellcode into memory without disk artifacts.
- **Customizable Options**: Allows specification of output file, architecture (x86/x64), and additional evasion flags.

## Installation

### Requirements

- Python 2.7 or 3.x (tested on Python 3)
- Git
- Windows target environment for execution (tool runs on Linux/macOS for generation)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/trustedsec/Unicorn.git
cd Unicorn

# No additional dependencies; runs with standard Python
python unicorn.py --help
```

On Kali Linux or Ubuntu:
```bash
sudo apt update
sudo apt install git python3
# Then clone as above
```

## Basic Usage

```bash
python unicorn.py <shellcode_file> <language> [options]
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-o <file>` | Specify output file name |
| `--arch <x86\|x64>` | Target architecture (default: x64) |

## Examples

### Example 1: Basic Usage

Generate a PowerShell loader from a shellcode file:

```bash
python unicorn.py shellcode.bin powershell -o loader.ps1
```

This creates `loader.ps1` that can be executed on a Windows target to inject the shellcode.

### Example 2: Advanced Usage

Generate a C# loader for x86 architecture:

```bash
python unicorn.py shellcode.bin csharp --arch x86 -o loader.cs
```

Compile and execute the resulting C# code on the target.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell
- [[Reflective Code Loading]] Reflective Code Loading
- [[Dynamic-link Library Injection]] Visual Basic

### Tactics

- [[Execution]] Execution
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- **Process Monitoring**: Look for PowerShell.exe spawning with command-line arguments indicating downgrade (e.g., `-Version 2` or `-ExecutionPolicy Bypass`).
- **Memory Scanning**: Anomalous memory allocations or reflective DLL loading in PowerShell processes.
- **File Artifacts**: Generated scripts like `.ps1` or `.cs` files with obfuscated shellcode loaders (though designed to avoid disk writes).
- **Network/Logging**: Enable PowerShell Script Block Logging and Module Logging to capture execution.
- **Behavioral Analytics**: Unusual parent-child process relationships, e.g., PowerShell spawning from non-interactive sessions.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit]] (for generating shellcode input)
- [[tools/PowerSploit]] (complementary PowerShell attack tools)

## References

- Official GitHub: https://github.com/trustedsec/Unicorn
- TrustedSec Blog: https://trustedsec.com/blog/unicorn-a-simple-tool-for-using-a-powershell-downgrade-attack-and-run-shellcode-in-memory
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1059/001/
