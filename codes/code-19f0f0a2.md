---
id: 19f0f0a2-58d6-403d-9f7a-19620d455e6d
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:21.692369+00:00'
updated_at: '2023-04-10T20:24:56.685165+00:00'
---

# Code Snippet 19f0f0a2

**Language**: Powershell

```powershell
Add-TcpTransport -lhost <host> -lport <port> -RetryWait 10 -RetryTotal 30
Add-WebTransport -Url http(s)://<host>:<port>/<luri> -RetryWait 10 -RetryTotal 30
```
