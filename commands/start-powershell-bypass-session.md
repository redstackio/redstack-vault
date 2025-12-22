---
id: new-uuid-1
type: command
executor: powershell
data: powershell -ExecutionPolicy Bypass -NoProfile
output: null
created_at: '2023-04-06T03:56:08.936635+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Windows
tags:
  - powershell
  - bypass
verified: true
validated: true
---

# Start PowerShell Bypass Session

## Command

```powershell
powershell -ExecutionPolicy Bypass -NoProfile
```

## Description

Launches a PowerShell session bypassing execution policy restrictions and without loading the user profile for stealth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ExecutionPolicy Bypass | Ignores script execution policies | Yes |
| -NoProfile | Skips profile loading | Yes |

## Examples

### Basic Usage

```powershell
powershell -ExecutionPolicy Bypass -NoProfile
```

## Expected Output

PS C:\Users\> 

Interactive PowerShell prompt.
