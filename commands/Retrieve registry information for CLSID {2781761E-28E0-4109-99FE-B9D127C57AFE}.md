---
id: 7703cebb-1c22-4684-a910-538dfda4bf57
name: Retrieve registry information for CLSID {2781761E-28E0-4109-99FE-B9D127C57AFE}
type: command
executor: bash
data: 'Get-ChildItem -Path ''HKLM:\SOFTWARE\Classes\CLSID\{2781761E-28E0-4109-99FE-B9D127C57AFE}''

  Name                           Property

  ----                           --------

  Hosts                          (default) : Scanned Hosting Applications

  InprocServer32                 (default) : "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2210.4-0\MpOav.dll"'
output: null
created_at: '2023-04-06T03:56:25.869094+00:00'
updated_at: '2023-04-10T20:36:15.840247+00:00'
---

# Retrieve registry information for CLSID {2781761E-28E0-4109-99FE-B9D127C57AFE}

```bash
Get-ChildItem -Path 'HKLM:\SOFTWARE\Classes\CLSID\{2781761E-28E0-4109-99FE-B9D127C57AFE}'
Name                           Property
----                           --------
Hosts                          (default) : Scanned Hosting Applications
InprocServer32                 (default) : "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2210.4-0\MpOav.dll"
```
