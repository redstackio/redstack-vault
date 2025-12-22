---
id: 64893ee0-c4a1-430a-8c87-0477283abdc7
name: run-privesccheck-basic
type: command
executor: powershell
data: powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
output: null
created_at: '2023-04-06T03:56:28.514587+00:00'
updated_at: '2023-04-10T20:37:50.966188+00:00'
platforms:
  - Windows
tags:
  - privesc
  - enumeration
verified: true
validated: true
---

# run-privesccheck-basic

## Command

```powershell
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
```

## Description

Runs basic privilege escalation checks using PrivescCheck script to identify common vectors like token privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ep bypass | Bypasses execution policy | Yes |
| -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck" | Loads script and invokes basic check | Yes |

## Examples

### Basic Usage

```powershell
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
```

## Expected Output

Console results like "[*] Checking for SeDebugPrivilege: Available - Potential JuicyPotato vector".

## Related

- [[commands/run-privesccheck-extended]]
- [[procedures/windows-privilege-escalation-using-powerup-privesccheck-and-wes-ng]]
