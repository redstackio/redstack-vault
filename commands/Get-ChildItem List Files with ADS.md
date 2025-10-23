---
id: bbe5fa0c-a044-4309-a43c-a2bc5c5e1f4a
name: Get-ChildItem List Files with ADS
type: command
executor: powershell
data: Get-ChildItem -Recurse -Path $_PATH | % { Get-Item $_.FullName -stream * } |
  where stream -ne ':$Data'
output: 'PS C:\> Get-ChildItem -Recurse -Path "Users" | % { Get-Item $_.FullName -stream
  * } | where stream -ne '':$Data''



  PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\Users\Bob\Desktop\normal.txt:hidden.txt

  PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\Users\Bob\Desktop

  PSChildName   : normal.txt:hidden.txt

  PSDrive       : C

  PSProvider    : Microsoft.PowerShell.Core\FileSystem

  PSIsContainer : False

  FileName      : C:\Users\Bob\Desktop\normal.txt

  Stream        : hidden.txt

  Length        : 13'
created_at: '2019-11-26T17:16:42.491413+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get-ChildItem List Files with ADS

```powershell
Get-ChildItem -Recurse -Path $_PATH | % { Get-Item $_.FullName -stream * } | where stream -ne ':$Data'
```

## Expected Output

```
PS C:\> Get-ChildItem -Recurse -Path "Users" | % { Get-Item $_.FullName -stream * } | where stream -ne ':$Data'


PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\Users\Bob\Desktop\normal.txt:hidden.txt
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\Users\Bob\Desktop
PSChildName   : normal.txt:hidden.txt
PSDrive       : C
PSProvider    : Microsoft.PowerShell.Core\FileSystem
PSIsContainer : False
FileName      : C:\Users\Bob\Desktop\normal.txt
Stream        : hidden.txt
Length        : 13
```


