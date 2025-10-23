---
id: fffa0eb2-8c85-451a-b64b-4280d9917cd7
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:29.867288+00:00'
updated_at: '2023-04-10T20:37:34.443913+00:00'
---

# Code Snippet fffa0eb2

**Language**: ps1

```ps1
PS C:\target> $serverName  = 'printer-installed-host'
PS C:\target> $printerName = 'EasySystemShell'
PS C:\target> $fullprinterName = '\\' + $serverName + '\' + $printerName + ' - ' + $(If ([System.Environment]::Is64BitOperatingSystem) {'x64'} Else {'x86'})
PS C:\target> Remove-Printer -Name $fullprinterName -ErrorAction SilentlyContinue
PS C:\target> Add-Printer -ConnectionName $fullprinterName
```


