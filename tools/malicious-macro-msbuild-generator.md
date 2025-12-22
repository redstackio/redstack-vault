---
id: 26b58ef2-2211-4bbb-9c9b-c1701ce61e9a
name: malicious-macro-msbuild-generator
type: tool
verified: true
created_at: '2019-08-28T21:17:42.178955+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - macro-generation
  - msbuild-bypass
  - phishing
  - evasion
url: 'https://github.com/related-repo/malicious-macro-msbuild-generator'
validated: true
---

# Malicious Macro MSBuild Generator

**Status**: Unverified

## Overview

The Malicious Macro MSBuild Generator is a specialized tool for creating VBA macros in Microsoft Office documents that execute PowerShell scripts or shellcode by leveraging MSBuild as a proxy execution mechanism. This bypasses application whitelisting policies like AppLocker, making it useful for red team simulations involving phishing attachments and initial access via Office files.

## Description

This tool automates the generation of obfuscated VBA code that, when enabled in an Office document (e.g., Word or Excel), invokes MSBuild.exe to compile and run embedded payloads. It supports PowerShell commands for dynamic downloads or shellcode for direct memory execution, evading common antivirus and endpoint detection by abusing a trusted Microsoft binary. Commonly used in scenarios where direct script execution is blocked but Office macros are permitted.

## Features

- Feature 1: Generates VBA macros compatible with Word, Excel, and PowerPoint.
- Feature 2: Supports PowerShell payload execution via MSBuild inline tasks.
- Feature 3: Handles shellcode injection using MSBuild's C# compilation capabilities.
- Feature 4: Includes basic obfuscation to reduce static detection signatures.

## Installation

### Requirements

- Windows OS with .NET Framework 4.0+ (MSBuild requires this).
- Microsoft Office installed for testing macros.
- Administrator privileges not required for generation, but for execution testing.

### Install Commands

```cmd
# Download and extract the tool (assuming a ZIP release from the repository)
# Replace with actual download link
curl -o generator.zip https://github.com/related-repo/malicious-macro-msbuild-generator/releases/latest/download/generator.zip
unzip generator.zip
cd malicious-macro-msbuild-generator
```

For development setup:

```cmd
# If building from source (requires Visual Studio or .NET SDK)
dotnet build
```

## Basic Usage

```cmd
malicious-macro-msbuild-generator.exe --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and available options |
| -v, --verbose | Enable verbose logging during generation |
| -o, --output | Specify output directory for generated files |

## Examples

### Example 1: Basic Usage

Generate a simple PowerShell macro:

```cmd
malicious-macro-msbuild-generator.exe -type powershell -output basic.vba -payload "calc.exe"
```

This creates basic.vba, which when run in Office, executes calc.exe via MSBuild.

### Example 2: Advanced Usage

Generate shellcode payload:

```cmd
malicious-macro-msbuild-generator.exe -type shellcode -output advanced.vba -shellcode "fc4883e4f0..."
```

Embed into a document using Office's VBA editor or automation scripts.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment
- [[PowerShell]] Command and Scripting Interpreter: PowerShell
- [[Compiled HTML File]] System Binary Proxy Execution: MSBuild

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor Office macro enablement logs (e.g., via Microsoft 365 auditing).
- Detection method 2: EDR alerts on MSBuild.exe spawning from winword.exe or excel.exe.
- Detection method 3: Static analysis of VBA code for MSBuild invocations or base64-encoded payloads.
- Detection method 4: Network monitoring for PowerShell downloads triggered by macro execution.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/macro-pack]]
- [[tools/msbuild-bypass-utils]]

## References

- Official documentation: https://github.com/related-repo/malicious-macro-msbuild-generator
- Related resources: MITRE ATT&CK pages for T1218.001 and Office macro abuse techniques.
