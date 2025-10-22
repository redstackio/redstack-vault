---
id: 1e436bf4-57c3-4755-abaf-77e7b998d41b
name: Misc Powershell Pasties
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:09.567780+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Misc Powershell Pasties

**Command** ([[List Removeable Drives]]):

```bash
Get-WmiObject Win32_LogicalDisk | Where-Object {($_.DriveType -eq 2) -and ($_.DeviceID -ne 'A:')} | %{"USB_PROCESS_DETECTED: " + $_.ProviderName + "`n"}

```

**Code**: [[
$visio = [activator]::CreateInstance([type]::GetT]]
