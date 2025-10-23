---
id: 60f73fb3-e550-48f0-b0db-2449c1e2932d
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:21:10.827696+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 60f73fb3

**Language**: Bash

```bash

Get-ItemProperty -Path Registry::"HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" |Select-Object -ExpandProperty WUServer Get-ItemProperty -Path Registry::"HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" |Select-Object -ExpandProperty WUStatusServer Get-ItemProperty -Path Registry::"HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" |Select-Object -ExpandProperty UseWUServer reg query HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate

```


