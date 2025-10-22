---
id: c8c84d0f-2f2c-4714-a45e-d91a4de8908b
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:22.907308+00:00'
updated_at: '2023-04-10T20:25:18.398944+00:00'
---

# Code Snippet c8c84d0f

**Language**: Powershell

```powershell
# Build for Linux
git clone https://github.com/kost/revsocks
export GOPATH=~/go
go get github.com/hashicorp/yamux
go get github.com/armon/go-socks5
go get github.com/kost/go-ntlmssp
go build
go build -ldflags="-s -w" && upx --brute revsocks

# Build for Windows
go get github.com/hashicorp/yamux
go get github.com/armon/go-socks5
go get github.com/kost/go-ntlmssp
GOOS=windows GOARCH=amd64 go build -ldflags="-s -w"
go build -ldflags -H=windowsgui
upx revsocks
```
