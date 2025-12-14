---
url: ''
tags:
  - debugger
  - rop
type: tool
verified: false
platforms:
  - Windows
id: fa9b7fb5-a16c-4031-b943-87ae872a347b
created_at: '2025-12-13T23:55:06.733Z'
updated_at: '2025-12-13T23:55:06.733Z'
validated: true
submitted: true
---
# Windbg

**Status**: Unverified

## Overview

Microsoft debugging tool for finding ROP offsets and verifying exploits on Windows.

## Description

Kernel/user-mode debugger used to inspect memory, symbols, and offsets like kernel32!WinExec for ROP chains in V8 exploits.

## Features

- Feature 1: Symbol loading
- Feature 2: Memory inspection
- Feature 3: Breakpoint setting

## Installation

### Requirements

- Windows SDK

### Install Commands

```bash
# Download from MSDN
choco install windbg
```

## Basic Usage

```bash
windbg.exe
```

### Common Options

| Option | Description |
|--------|-------------|
| -k | Kernel mode |

## Examples

### Example 1: Basic Usage

```bash
windbg -z exploit.exe
```

### Example 2: Advanced Usage

```bash
!symfix; .reload /f; x kernel32!WinExec
```

## MITRE ATT&CK Mapping

### Techniques

- [[Exploitation for Client Execution]]

### Tactics

- [[Execution]]

## Detection

- Detect debugger attachments via anti-debug

## Related Procedures

- [[procedures/Adjust-ROP-Chain-for-Target-OS]]

## Related Tools


## References

- Microsoft Docs
