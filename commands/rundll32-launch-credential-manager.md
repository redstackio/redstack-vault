---
id: a9f90f82-6984-4dfb-84fa-ed87ec9d58d1
name: rundll32-launch-credential-manager
type: command
executor: powershell
data: 'rundll32.exe keymgr.dll,KRShowKeyMgr'
output: null
created_at: '2023-04-06T03:56:29.258516+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - windows
  - eop
verified: true
validated: true
---

# rundll32-launch-credential-manager

## Command

```powershell
rundll32.exe keymgr.dll,KRShowKeyMgr
```

## Description

This command launches the Windows Credential Manager graphical user interface (GUI) using the built-in rundll32.exe executable. It is used in post-exploitation scenarios to view and extract stored credentials, such as passwords for network resources or applications, aiding in privilege escalation or lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| keymgr.dll | The DLL module containing the Credential Manager functionality | Yes (built-in) |
| KRShowKeyMgr | The exported function to show the key manager GUI | Yes (built-in) |

No user-supplied parameters are required; the command is fixed-syntax for Windows environments.

## Examples

### Basic Usage

```powershell
rundll32.exe keymgr.dll,KRShowKeyMgr
```

This opens the Credential Manager directly from PowerShell or Command Prompt.

### Advanced Usage

Run from a remote shell (e.g., via Invoke-Command in PowerShell remoting) to access credentials on a target machine:

```powershell
Invoke-Command -ComputerName TARGET -ScriptBlock { rundll32.exe keymgr.dll,KRShowKeyMgr }
```

## Expected Output

The command does not produce console output; instead, it launches the Windows Credential Manager window. Success is indicated by the GUI appearing, listing categories like 'Windows Credentials' and 'Web Credentials'. Each entry shows target, username, and a 'Show' option to reveal the password. If the GUI fails to open (e.g., due to policy restrictions), an error like "Access Denied" may appear.

## Related

- [[procedures/Loot-Passwords-from-Windows-Credential-Manager-for-EoP]]
