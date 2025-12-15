---
url: 'https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/'
tags:
  - debugging
  - reverse-engineering
  - crash-analysis
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.810Z'
id: b90330ec-0039-4820-86c9-fbdf70d2765f
validated: true
submitted: true
---
# WinDBG

**Status**: Unverified

## Overview

WinDBG is a powerful Windows debugger from Microsoft, used for analyzing crashes, memory dumps, and kernel/user-mode debugging. In security testing, it's commonly employed to reproduce vulnerabilities like buffer overflows in applications such as CS:GO by attaching to processes and inspecting exceptions.

## Description

WinDbg supports live process attachment, symbol loading for executables like csgo.exe, and commands for stack tracing, memory inspection, and extension analysis. For offensive security, it aids in exploit development by confirming overflow conditions and identifying control flow hijacks. It's integrated with the Windows SDK and excels in handling Source Engine crashes.

## Features

- Feature 1: Live kernel and user-mode debugging with process attachment
- Feature 2: Extension support (e.g., !analyze for automated crash diagnosis)
- Feature 3: Symbol server integration for accurate stack traces

## Installation

### Requirements

- Windows 10/11
- Administrative privileges

### Install Commands

```cmd
# Download and install Windows SDK from Microsoft, selecting Debugging Tools
# Or use standalone: winget install Microsoft.WinDbg
```

## Basic Usage

```cmd
windbg.exe
```

### Common Options

| Option | Description |
|--------|-------------|
| -k | Kernel debugging mode |
| -p <pid> | Attach to specific process ID |
| -z <file> | Open dump file |

## Examples

### Example 1: Basic Usage

```cmd
windbg -p <csgo_pid>
```

### Example 2: Advanced Usage

```cmd
windbg -p <pid> -srcpath "C:\Symbols"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for windbg.exe execution
- Event logs showing debugger attachments (Event ID 4688)
- Anti-debugging heuristics in protected applications

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/
- Related resources: WinDbg Preview on Microsoft Store
