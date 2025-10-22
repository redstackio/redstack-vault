---
id: de4841a0-bf87-43e3-a702-6b4f1c5b4879
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:22.845580+00:00'
updated_at: '2023-04-10T20:25:21.071478+00:00'
---

# Code Snippet de4841a0

**Language**: Powershell

```powershell
git clone https://github.com/ginuerzh/gost
cd gost/cmd/gost
go build

# Socks5 Proxy
Server side: gost -L=socks5://:1080
Client side: gost -L=:8080 -F=socks5://server_ip:1080?notls=true

# Local Port Forward
gost -L=tcp://:2222/192.168.1.1:22 [-F=..]
```
