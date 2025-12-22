---
id: tool-putty-pscp
url: 'https://www.putty.org/'
tags:
  - ssh
  - client
  - scp
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.683Z'
configuration: Versions <= 0.66 (vulnerable)
validated: true
submitted: true
---
# PuTTY-PSCP

**Status**: Unverified

## Overview

PuTTY PSCP is the secure copy client component of the PuTTY SSH suite, used for transferring files over SSH connections on Windows systems.

## Description

PSCP implements SCP protocol over SSH, handling authentication and file operations. In vulnerable versions (<=0.66), it suffers from a stack buffer overflow in post-auth file size parsing using unsafe sscanf, plus DoS via null pointer reads. It's commonly used in pentesting for SSH file ops but here serves as the exploit target. Runs as a command-line tool on Windows.

## Features

- Feature 1: SCP file transfer via SSH
- Feature 2: Supports authentication with keys or passwords
- Feature 3: Batch mode for scripted transfers

## Installation

### Requirements

- Windows OS

### Install Commands

Download from official site:

```bash
# Via installer or binary download
# No CLI install; extract pscp.exe
```

## Basic Usage

```cmd
pscp file user@host:/path
```

### Common Options

| Option | Description |
|--------|-------------|
| -scp | Use SCP protocol |
| -pw pass | Specify password |
| -P port | Custom port |

## Examples

### Example 1: Basic Usage

```cmd
pscp localfile user@host:/remote/
```

### Example 2: Advanced Usage

With password:

```cmd
pscp -pw secret -scp user@192.168.1.100:/etc/passwd output.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution (as target)

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for pscp.exe executions
- Outbound SSH traffic logs
- Crash reports from buffer overflows

## Related Procedures

- [[procedures/Connect-Vulnerable-PuTTY-PSCP-Client]]

## Related Tools

- [[Related Tool|tools/poc-py]]

## References

- PuTTY Documentation: https://www.putty.org/
- CVE-2016-2563 Report
