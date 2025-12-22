---
type: tool
verified: true
created_at: '2020-02-28T22:54:27.280246+00:00'
updated_at: '2023-05-30T19:46:18.128408+00:00'
commands:
  - '[[commands/more-extract-ads-from-file]]'
platforms:
  - Windows
tags:
  - Enumeration
validated: true
---

# more-windows

**Status**: ✓ Verified

## Overview

more is a filter for paging through text one screen at a time. It is primarily a Linux tool, but has been implemented in Microsoft's Command Prompt (cmd.exe), and can be useful for reading Alternate Data Streams.

## Description

more is a filter for paging through text one screen at a time. It works by displaying the contents of a file or input stream in a paginated manner, allowing users to scroll through large amounts of text. In the Windows Command Prompt, it supports reading from Alternate Data Streams (ADS), which are hidden metadata streams attached to NTFS files. This makes it valuable for security testing, such as enumerating hidden data in files without needing additional tools.

## Features

- Paginates text output for easier reading
- Supports reading from standard input or files
- In Windows, compatible with ADS syntax (e.g., file.txt:stream)
- Built-in to cmd.exe, no installation required

## Installation

### Requirements

- Windows operating system with NTFS file system support

### Install Commands

more comes pre-installed with Windows Command Prompt. No additional installation is needed.

```command_prompt
# Simply open cmd.exe and use 'more'
more /?
```

## Basic Usage

```command_prompt
more filename.txt
```

### Common Options

| Option | Description |
|--------|-------------|
| `/E` | Enable enhanced features like searching |
| `/P` | Expand form-feed characters |
| `/C` | Clear screen before displaying |
| `/S` | Squeeze multiple blank lines into one |

## Examples

### Example 1: Basic Usage

Display a text file page by page:

```command_prompt
more C:\temp\log.txt
```

### Example 2: Advanced Usage with ADS

Extract content from an Alternate Data Stream:

```command_prompt
more < normal.txt:secret
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Command line logging showing 'more < file:stream' invocations
- File access events to ADS streams in Windows event logs
- Unusual paging through large or hidden files

## Related Commands

- [[commands/more-extract-ads-from-file]]

## References

- Microsoft Documentation: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/more
