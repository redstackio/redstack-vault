---
id: fda9ad37-c83b-45c8-9971-1c89a6385a99
type: tool
verified: true
created_at: '2020-02-19T05:22:11.612123+00:00'
updated_at: '2023-05-30T19:44:56.403076+00:00'
commands:
  - '[[commands/dir-recursive-search-for-files-and-folders]]'
tags:
  - File System
  - Windows
platforms:
  - Windows
url: >-
  https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/dir
validated: true
---

# dir

**Status**: ✓ Verified

## Overview

The `dir` command is a built-in Windows Command Prompt utility for listing files and directories in a specified path. It provides details such as file names, sizes, modification dates, and attributes, making it essential for filesystem enumeration in security assessments, such as identifying sensitive files or mapping directory structures during reconnaissance or lateral movement.

## Description

`dir` displays the contents of a directory, including subdirectories if specified, along with metadata like volume label, serial number, file extensions, sizes in bytes, and last modified timestamps. It supports various filters and options for recursive searches, pattern matching, and output formatting, which are commonly used in offensive security to locate configuration files, logs, or credentials without relying on external tools.

## Features

- Feature 1: Basic listing of files and folders with metadata (size, date, attributes)
- Feature 2: Recursive traversal (/s) to search subdirectories
- Feature 3: Pattern matching (e.g., *.txt) for targeted enumeration
- Feature 4: Output redirection and sorting options for analysis

## Installation

### Requirements

- Windows operating system (XP or later)

### Install Commands

No installation required; `dir` is built-in to all Windows systems.

```command_prompt
# Verify availability
where dir
```

## Basic Usage

```command_prompt
dir
```

This lists the contents of the current directory.

### Common Options

| Option | Description |
|--------|-------------|
| /s | Recurse into subdirectories |
| /b | Bare format (filenames only) |
| /a | Display files with specified attributes (e.g., /ah for hidden) |
| /o | Sort by criteria (e.g., /on for name) |

## Examples

### Example 1: Basic Usage

List files in the current directory:

```command_prompt
dir
```

### Example 2: Advanced Usage

Recursive search for text files:

```command_prompt
dir /s *.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor Command Prompt execution logs for frequent `dir` invocations, especially with /s or pattern matching, via Windows Event Logs (Event ID 4688)
- Detection method 2: Behavioral analytics for unusual filesystem access patterns from non-admin processes
- Detection method 3: Sysmon logging of process creation and file access events

## Related Procedures

- [[procedures/Enumerate-Filesystem-for-Sensitive-Data]]

## Related Tools

- [[tools/Powershell]]
- [[tools/cmd]]

## References

- Official Microsoft Documentation: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/dir
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1083/
