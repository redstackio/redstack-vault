---
id: aca883e6-4786-4b8d-a7bc-e61c5c0d1846-rewritten
name: view-bloodhound-customqueries-windows
type: command
executor: powershell
data: 'Get-Content $env:APPDATA\BloodHound\customqueries.json'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - recon
  - active-directory
verified: true
validated: true
---

# view-bloodhound-customqueries-windows

## Command

```powershell
Get-Content $env:APPDATA\BloodHound\customqueries.json
```

## Description

This PowerShell command retrieves and displays the contents of BloodHound's customqueries.json file on Windows, useful for reviewing or editing custom AD queries during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses environment variable for AppData path | No |

## Examples

### Basic Usage

```powershell
Get-Content $env:APPDATA\BloodHound\customqueries.json
```

### With Error Handling

```powershell
if (Test-Path "$env:APPDATA\BloodHound\customqueries.json") { Get-Content $env:APPDATA\BloodHound\customqueries.json } else { Write-Output "File not found" }
```

## Expected Output

JSON content similar to:

```json
[
  {
    "name": "Example",
    "query": "MATCH (n) RETURN n"
  }
]
```

Errors if file missing: "Cannot find path".

## Related

- [[procedures/Active-Directory-Recon-Using-BloodHound-Custom-Queries]]
- [[tools/BloodHound]]
