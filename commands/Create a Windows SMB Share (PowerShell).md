---
id: 0bb61fff-7ae2-4e5e-b298-584a23d8ed39
name: Create a Windows SMB Share (PowerShell)
type: command
executor: powershell
data: New-SmbShare -Name "$_NAME" -Path "$_FULL/PATH/TO/SHARE" -FullAccess "$_USERNAME"
output: 'PS C:\ > New-SmbShare -Name "Shared Files" -Path "C:\Users\Bob\Desktop\shared"
  -FullAccess Bob"

  Name         ScopeName Path                         Description

  ----         --------- ----                         -----------

  Shared Files *         C:\Users\Bob\Desktop\test'
created_at: '2020-03-27T22:21:14.917913+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Create a Windows SMB Share (PowerShell)

```powershell
New-SmbShare -Name "$_NAME" -Path "$_FULL/PATH/TO/SHARE" -FullAccess "$_USERNAME"
```

## Expected Output

```
PS C:\ > New-SmbShare -Name "Shared Files" -Path "C:\Users\Bob\Desktop\shared" -FullAccess Bob"

Name         ScopeName Path                         Description
----         --------- ----                         -----------
Shared Files *         C:\Users\Bob\Desktop\test
```
