---
id: 54f9b771-ec59-4acc-8058-4375f33dd5d3
type: command
executor: powershell
data: Import-Module .\SkyArk.ps1 -force
output: null
created_at: '2023-04-06T03:56:08.936650+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Windows
tags:
  - powershell
  - module
verified: true
validated: true
---

# Import SkyArk PowerShell Module

## Command

```powershell
Import-Module .\SkyArk.ps1 -force
```

## Description

Imports the SkyArk PowerShell module forcefully, overriding any existing versions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| .\SkyArk.ps1 | Path to the module file | Yes |
| -force | Overwrite if loaded | Yes |

## Examples

### Basic Usage

```powershell
Import-Module .\SkyArk.ps1 -force
```

## Expected Output

No output if successful; error if module not found.
