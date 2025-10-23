---
id: 759fdc81-f66e-4f7b-bb6b-fad18c20dff6
name: Mount a Windows SMB Share (PowerShell)
type: command
executor: powershell
data: New-PSDrive -Name "$_NAME" -PSProvider FileSystem -Credential $Cred -Root \\$_TARGET_IP\$_SHARE
output: 'PS C:\> New-PSDrive -Name "Remote Share" -PSProvider FileSystem -Credential
  $Cred -Root "\\10.10.10.10\Shared Files"


  Name           Used (GB)     Free (GB) Provider      Root                                               CurrentLocation

  ----           ---------     --------- --------      ----                                               ---------------

  Remote ...                             FileSystem    \\192.168.1.173\Shared Files'
created_at: '2020-03-27T22:02:35.999967+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mount a Windows SMB Share (PowerShell)

```powershell
New-PSDrive -Name "$_NAME" -PSProvider FileSystem -Credential $Cred -Root \\$_TARGET_IP\$_SHARE
```

## Expected Output

```
PS C:\> New-PSDrive -Name "Remote Share" -PSProvider FileSystem -Credential $Cred -Root "\\10.10.10.10\Shared Files"

Name           Used (GB)     Free (GB) Provider      Root                                               CurrentLocation
----           ---------     --------- --------      ----                                               ---------------
Remote ...                             FileSystem    \\192.168.1.173\Shared Files
```


