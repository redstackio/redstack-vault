---
id: 8ce2cd4e-d997-4e61-babb-8959405ec636
name: List Removeable Drives
type: command
executor: bash
data: 'Get-WmiObject Win32_LogicalDisk | Where-Object {($_.DriveType -eq 2) -and ($_.DeviceID
  -ne ''A:'')} | %{"USB_PROCESS_DETECTED: " + $_.ProviderName + "`n"}

  '
output: null
created_at: '2020-07-14T18:21:09.547711+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List Removeable Drives

```bash
Get-WmiObject Win32_LogicalDisk | Where-Object {($_.DriveType -eq 2) -and ($_.DeviceID -ne 'A:')} | %{"USB_PROCESS_DETECTED: " + $_.ProviderName + "`n"}

```


