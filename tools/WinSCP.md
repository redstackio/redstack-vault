---
id: tool-1
url: 'https://winscp.net/'
tags:
  - sftp
  - scp
  - client
type: tool
verified: false
platforms:
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.880Z'
validated: true
submitted: true
---
# WinSCP

**Status**: Unverified

## Overview

WinSCP is a free SFTP, SCP, and FTP client for Windows that supports advanced URI parameter parsing, vulnerable to command injection via proxy settings in this context.

## Description

Popular for secure file transfers, WinSCP parses SFTP URIs including custom parameters like x-proxymethod and x-proxytelnetcommand, allowing local command execution in local proxy mode (method 5).

## Features

- Feature 1: SFTP/SCP/FTP/S3 support with GUI
- Feature 2: Advanced site settings and proxy configuration
- Feature 3: URI scheme handling for command-line integration

## Installation

### Requirements

- Windows OS
- .NET Framework

### Install Commands

```bash
# Download and run installer from official site
winget install WinSCP.WinSCP
```

## Basic Usage

```bash
winscp.com /command "open sftp://user:pass@host/"
```

### Common Options

| Option | Description |
|--------|-------------|
| /command | Execute scripted commands |
| /ini=nul | Use null session for testing |

## Examples

### Example 1: Basic Usage

```bash
winscp.exe
```

Opens GUI for manual transfers.

### Example 2: Advanced Usage

```bash
winscp.com /command "open sftp://test@host/ -proxymethod=5 -proxytelnetcommand=calc.exe"
```

Triggers command execution.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Process: WinSCP.exe with suspicious command-line args (e.g., x-proxytelnetcommand)
- Network: Outbound SFTP connections to unexpected hosts

## Related Procedures

- [[procedures/Exploit-OS-Handler-for-Arbitrary-Code-Execution]]

## Related Tools

- [[PuTTY]]
- [[FileZilla]]

## References

- Official documentation: https://winscp.net/eng/docs/start
- Related resources: HackerOne Report #1078002
