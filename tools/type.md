---
id: baa40410-bcc0-4d39-b4e2-b7bc33989932
type: tool
verified: true
created_at: '2020-03-04T21:21:14.431050+00:00'
updated_at: '2023-05-30T19:54:58.208059+00:00'
platforms:
  - Windows
tags:
  - Enumeration
  - Obfuscation
  - File-System
commands:
  - '[[commands/type-embed-content-into-alternate-data-stream]]'
url: >-
  https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/type
validated: true
---

# type

**Status**: ✓ Verified

## Overview

type is a built-in Windows Command Prompt utility used to display the contents of text files at the command line. In PowerShell, 'type' is an alias for the Get-Content cmdlet, providing the same functionality. It is commonly used for quick file viewing during security assessments, scripting, and data manipulation tasks like redirecting content to alternate data streams for obfuscation.

## Description

type reads and outputs the contents of specified files without opening them in an editor. It supports redirection and piping, making it versatile for tasks such as embedding data into NTFS alternate data streams (ADS) to hide payloads or sensitive information without altering the host file's visible properties. This is particularly useful in Windows environments for evasion techniques during penetration testing or red team operations.

## Features

- Displays file contents directly in the console
- Supports wildcard patterns for multiple files
- Integrates with redirection operators (> , >>) for output manipulation
- PowerShell alias for seamless use in modern shells
- No external dependencies; native to Windows

## Installation

### Requirements

- Windows operating system (XP or later)
- Command Prompt or PowerShell access

### Install Commands

No installation required; type is pre-installed on all modern Windows releases.

## Basic Usage

```cmd
type filename.txt
```

### Common Options

| Option | Description |
|--------|-------------|
| No options needed for basic display | Outputs file content to console |
| Combined with > | Redirects output to another file or stream |

## Examples

### Example 1: Basic Usage

Display the contents of a text file:

```cmd
type C:\path\to\file.txt
```

### Example 2: Advanced Usage

Embed content into an alternate data stream (see related command for details):

```cmd
type secret.txt > normal.txt:hidden
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[NTFS File Attributes]] Hidden Files and Directories (for ADS usage)
- [[Obfuscated Files or Information]] Obfuscated Files or Information

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor Command Prompt or PowerShell logs for 'type' invocations with redirection to ADS (e.g., via Event ID 4688 in Windows Security logs)
- Use tools like Sysinternals Streams to detect ADS presence on files
- File system auditing for unusual stream attachments

## Related Procedures

- [[procedures/Embed-Alternate-Data-Stream-in-File]]

## Related Tools

- [[Get-Content]] (PowerShell equivalent)
- [[tools/dir]] (for listing ADS with /R flag)

## References

- Official Microsoft documentation: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/type
