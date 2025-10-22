---
id: 4a7eecf0-d67f-492c-ac2f-4b0f458dfc77
name: BitsTransfer Download a File from a Web Server
type: command
executor: powershell
data: 'Import-Module BitsTransfer

  Start-BitsTransfer -Source http://$_REMOTE_IP/$_FILENAME -Destination $_FILENAME'
output: 'PS C:\> Import-Module BitsTransfer

  PS C:\> Start-BitsTransfer -Source http://10.10.10.100/secrets -Destination secrets'
created_at: '2019-11-25T23:58:29.353247+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# BitsTransfer Download a File from a Web Server

```powershell
Import-Module BitsTransfer
Start-BitsTransfer -Source http://$_REMOTE_IP/$_FILENAME -Destination $_FILENAME
```

## Expected Output

```
PS C:\> Import-Module BitsTransfer
PS C:\> Start-BitsTransfer -Source http://10.10.10.100/secrets -Destination secrets
```
