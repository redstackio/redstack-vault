---
id: 8b8fe352-e877-4e9c-bc8a-3a6bd0886d5d
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:22.791994+00:00'
updated_at: '2023-04-10T20:25:12.829563+00:00'
---

# Code Snippet 8b8fe352

**Language**: Powershell

```powershell
# Get Ligolo and dependencies
cd `go env GOPATH`/src
git clone https://github.com/sysdream/ligolo
cd ligolo
make dep

# Generate self-signed TLS certificates (will be placed in the certs folder)
make certs TLS_HOST=example.com

make build-all
```


