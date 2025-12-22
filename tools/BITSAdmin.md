---
id: 70437be9-5c9d-4d6e-a9fb-df15722147a4
type: tool
verified: true
created_at: '2020-03-06T00:31:36.728802+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - file-transfer
  - network
url: 'https://learn.microsoft.com/en-us/windows/win32/bits/bitsadmin-exe'
commands:
  - '[[commands/bitsadmin-download-file-from-remote-web-server]]'
validated: true
---

# BITSAdmin

**Status**: ✓ Verified

## Overview

BITSAdmin is a command-line tool for managing Background Intelligent Transfer Service (BITS) jobs on Windows systems. It enables creating, monitoring, and completing download and upload transfers, often used in security testing to move files to or from compromised hosts without relying on common tools like PowerShell or certutil that may be monitored.

## Description

BITSAdmin interacts with the BITS service to handle asynchronous file transfers over HTTP, HTTPS, or SMB. It supports job prioritization, progress tracking, and resuming interrupted transfers. In offensive operations, it's valuable for ingress tool transfer as it blends with legitimate system traffic. Note that while user-level jobs are visible to the current user, administrative privileges are needed to enumerate all system jobs.

## Features

- Job creation for downloads and uploads
- Real-time progress monitoring
- Transfer resumption after interruptions
- Job prioritization (low, normal, high, realtime)
- Enumeration and management of existing jobs
- Support for multiple files per job

## Installation

### Requirements

- Windows Vista or later (BITSAdmin is deprecated in favor of PowerShell but still functional)
- Command Prompt access

### Install Commands

BITSAdmin is included by default in all modern Windows installations. No separate installation is required.

```command_prompt
# Verify availability
where bitsadmin
```

## Basic Usage

```command_prompt
bitsadmin /?
```

### Common Options

| Option | Description |
|--------|-------------|
| /create | Creates a new BITS job |
| /addfile | Adds a file to an existing job |
| /complete | Completes a job and writes files to disk |
| /list | Lists all jobs for the current user |
| /transfer | Shortcut to create, add file, and transfer in one command |
| /download | Specifies a download operation for the job |
| /upload | Specifies an upload operation for the job |
| /setpriority | Sets job priority level |

## Examples

### Example 1: Basic Download

Use the [[commands/bitsadmin-download-file-from-remote-web-server]] command to download a file from a remote server.

### Example 2: Advanced Usage - Resume Interrupted Transfer

```command_prompt
bitsadmin /create MyJob /addfile http://example.com/largefile.exe C:\Downloads\largefile.exe
bitsadmin /setpriority MyJob HIGH
bitsadmin /resume MyJob
bitsadmin /complete MyJob
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[Exfiltration to Cloud Storage]] Exfiltration Over Web Service

### Tactics

- [[Execution]] Execution
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for bitsadmin.exe executions, especially with /transfer or /download flags
- BITS service logs (Microsoft-Windows-Bits-Client/Operational, Event ID 59 for job creation)
- Network flows showing HTTP/HTTPS downloads from suspicious IPs to common drop paths (e.g., C:\Windows\Tasks)
- File system changes in temporary or system directories for downloaded payloads
- Behavioral analytics for unusual BITS job activity outside normal admin tasks

## Related Procedures

(None currently linked)

## Related Tools

- [[tools/Certutil]] (Alternative Windows built-in for file transfers)
- [[tools/Powershell]] (Modern replacement for BITS management via Start-BitsTransfer)

## References

- [Microsoft Documentation: bitsadmin.exe](https://learn.microsoft.com/en-us/windows/win32/bits/bitsadmin-exe)
- [MITRE ATT&CK: T1105](https://attack.mitre.org/techniques/T1105/)
