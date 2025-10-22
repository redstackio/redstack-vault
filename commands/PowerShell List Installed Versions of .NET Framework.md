---
id: f614cb71-2fc6-4c03-a3bf-33bcc0a2585e
name: PowerShell List Installed Versions of .NET Framework
type: command
executor: powershell
data: Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP' -recurse |
  Get-ItemProperty -name Version,Release -EA 0 |  Where { $_.PSChildName -match '^(?!S)\p{L}'}
  | Select PSChildName, Version, Release
output: 'PS C:\> Get-ChildItem ''HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP''
  -recurse | Get-ItemProperty -name Version,Release -EA 0 |  Where { $_.PSChildName
  -match ''^(?!S)\p{L}''} | Select PSChildName, Version, Release

  PSChildName                      Version        Release

  -----------                      -------        -------

  v2.0.50727                       2.0.50727.4927

  v3.0                             3.0.30729.4926

  Windows Communication Foundation 3.0.4506.4926

  Windows Presentation Foundation  3.0.6920.4902

  v3.5                             3.5.30729.4926

  Client                           4.8.03752      528040

  Full                             4.8.03752      528040

  Client                           4.0.0.0'
created_at: '2020-07-03T19:54:47.044197+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PowerShell List Installed Versions of .NET Framework

```powershell
Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP' -recurse | Get-ItemProperty -name Version,Release -EA 0 |  Where { $_.PSChildName -match '^(?!S)\p{L}'} | Select PSChildName, Version, Release
```

## Expected Output

```
PS C:\> Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP' -recurse | Get-ItemProperty -name Version,Release -EA 0 |  Where { $_.PSChildName -match '^(?!S)\p{L}'} | Select PSChildName, Version, Release

PSChildName                      Version        Release
-----------                      -------        -------
v2.0.50727                       2.0.50727.4927
v3.0                             3.0.30729.4926
Windows Communication Foundation 3.0.4506.4926
Windows Presentation Foundation  3.0.6920.4902
v3.5                             3.5.30729.4926
Client                           4.8.03752      528040
Full                             4.8.03752      528040
Client                           4.0.0.0
```
