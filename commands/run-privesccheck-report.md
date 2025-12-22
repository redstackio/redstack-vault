---
id: 33cf40e1-ce36-4468-9932-68bb1ce653e5
name: run-privesccheck-report
type: command
executor: powershell
data: >-
  powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Report
  PrivescCheck_%COMPUTERNAME% -Format TXT,CSV,HTML"
output: null
created_at: '2023-04-06T03:56:28.514734+00:00'
updated_at: '2023-04-10T20:37:50.966188+00:00'
platforms:
  - Windows
tags:
  - privesc
  - reporting
verified: true
validated: true
---

# run-privesccheck-report

## Command

```powershell
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Report PrivescCheck_%COMPUTERNAME% -Format TXT,CSV,HTML"
```

## Description

Runs extended checks and generates multi-format reports for offline analysis of privesc findings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Report PrivescCheck_%COMPUTERNAME% | Sets report filename with hostname | Yes |
| -Format TXT,CSV,HTML | Specifies output formats | Yes |

## Examples

### Basic Usage

```powershell
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Report PrivescCheck_%COMPUTERNAME% -Format TXT,CSV,HTML"
```

## Expected Output

Files like PrivescCheck_WORKSTATION.txt, .csv, .html with tabulated risks, e.g., columns for Technique, Risk, Exploitation Steps.

## Related

- [[commands/run-privesccheck-extended]]
- [[procedures/windows-privilege-escalation-using-powerup-privesccheck-and-wes-ng]]
