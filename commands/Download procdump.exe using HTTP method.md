---
id: 6d74e531-cf88-4de3-abb1-79e262a99ae9
name: Download procdump.exe using HTTP method
type: command
executor: bash
data: certutil -urlcache -split -f http://live.sysinternals.com/procdump.exe C:\Users\Public\procdump.exe
output: null
created_at: '2023-04-06T03:56:27.176935+00:00'
updated_at: '2023-04-10T20:37:14.787792+00:00'
---

# Download procdump.exe using HTTP method

```bash
certutil -urlcache -split -f http://live.sysinternals.com/procdump.exe C:\Users\Public\procdump.exe
```
