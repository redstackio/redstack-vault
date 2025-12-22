---
id: 6e352a62-e1f0-42d8-a1f4-f93911eb2767
name: run-privesccheck-extended
type: command
executor: powershell
data: powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Extended"
output: null
created_at: '2023-04-06T03:56:28.514679+00:00'
updated_at: '2023-04-10T20:37:50.966188+00:00'
platforms:
  - Windows
tags:
  - privesc
  - enumeration
verified: true
validated: true
---

# run-privesccheck-extended

## Command

```powershell
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Extended"
```

## Description

Performs extended privilege escalation checks, including deeper scans for services and registry issues.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Extended | Enables additional checks beyond basic | Yes |

## Examples

### Basic Usage

```powershell
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Extended"
```

## Expected Output

Enhanced output with more vectors, e.g., "[*] Writable Service: Spooler - Can replace binary".

## Related

- [[commands/run-privesccheck-basic]]
- [[procedures/windows-privilege-escalation-using-powerup-privesccheck-and-wes-ng]]
