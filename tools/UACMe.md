---
id: b68196f5-b992-4d0e-98e3-1bed06a98eb0
type: tool
verified: true
created_at: '2019-08-28T21:17:21.127446+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - uac-bypass
  - privilege-escalation
  - windows
url: 'https://github.com/hfiref0x/UACME'
commands:
  - '[[commands/uacme-fodhelper-bypass]]'
  - '[[commands/uacme-sdclt-bypass]]'
  - '[[commands/uacme-computerdefaults-bypass]]'
validated: true
---

# UACMe

**Status**: Unverified

## Overview

UACMe is an open-source assessment tool that implements numerous methods for bypassing Windows User Account Control (UAC). It is designed for security researchers, penetration testers, and red teams to evaluate UAC effectiveness across Windows versions from 7 to 11, focusing on privilege escalation techniques without triggering consent prompts.

## Description

UACMe compiles various proof-of-concept bypasses into a single executable, covering DLL hijacking, registry auto-elevation abuse, COM interface manipulation, and process injection. Each method targets specific Windows components (e.g., fodhelper.exe, sdclt.exe) and is numbered for selection. The tool auto-detects OS version compatibility and can run silently, making it useful for post-exploitation scenarios in controlled environments.

## Features

- Over 70 distinct UAC bypass methods
- OS version-specific compatibility checks
- Support for both x86 and x64 architectures
- Customizable source code for new methods
- Minimal footprint with no external dependencies

## Installation

### Requirements

- Windows 7 or later (for testing)
- Visual Studio 2019+ with C++ Desktop Development workload
- Windows SDK matching target OS

### Install Commands

```bash
# Clone the GitHub repository
git clone https://github.com/hfiref0x/UACME.git
cd UACME/Source

# Build using MSBuild (from Visual Studio Developer Command Prompt)
msbuild UACMe.sln /p:Configuration=Release /p:Platform=x64

# The executable will be in x64/Release/UACMe.exe
```

Pre-built binaries are available in the GitHub releases section for quick testing.

## Basic Usage

```cmd
UACMe.exe
```

Displays available methods and usage. Specify a method number to execute.

### Common Options

| Option | Description |
|--------|-------------|
| <method_number> | Execute specific bypass method (e.g., 41 for fodhelper) |
| -h | Show help and method list |
| --silent | Suppress output (if supported in custom builds) |

## Examples

### Example 1: Basic Usage

```cmd
UACMe.exe 41
```

Runs the fodhelper bypass method.

### Example 2: Advanced Usage

```cmd
UACMe.exe 3 --silent
```

Executes sdclt bypass quietly.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Bypass User Account Control]] Bypass User Account Control: Misconfigured/Abused Auto-Elevation

### Tactics

- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious child processes from trusted binaries (e.g., fodhelper.exe spawning cmd.exe)
- Temporary registry keys in HKCU\Software\Classes\ms-settings\Shell\Open\command
- Event logs showing UAC bypass attempts (Event ID 4672/4673 without prompt)
- File creation of UACMe.exe in temp directories

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/PrivescCheck]]
- [[tools/PowerUp]]

## References

- Official GitHub: https://github.com/hfiref0x/UACME
- UAC Bypass Research: https://pentestlab.blog/2017/06/07/uac-bypass/

*Last updated: 2023-10-01*
