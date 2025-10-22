---
id: ecb11566-34b3-45df-886c-b2e394d091b0
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:22.907049+00:00'
updated_at: '2023-04-10T20:25:18.398944+00:00'
---

# Code Snippet ecb11566

**Language**: Powershell

```powershell
# Listen on the server and create a SOCKS 5 proxy on port 1080
user@VPS$ ./revsocks -listen :8443 -socks 127.0.0.1:1080 -pass Password1234

# Connect client to the server
user@PC$ ./revsocks -connect 10.10.10.10:8443 -pass Password1234
user@PC$ ./revsocks -connect 10.10.10.10:8443 -pass Password1234 -proxy proxy.domain.local:3128 -proxyauth Domain/userpame:userpass -useragent "Mozilla 5.0/IE Windows 10"
```
