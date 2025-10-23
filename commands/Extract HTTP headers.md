---
id: fd516d0b-1ad9-4bac-bf9e-71e5201c1e04
name: Extract HTTP headers
type: command
executor: bash
data: 'Values: User-Agent

  Values: Cookie

  Header: X-Forwarded-Host

  Header: X-Host

  Header: X-Forwarded-Server

  Header: X-Forwarded-Scheme (header; also in combination with X-Forwarded-Host)

  Header: X-Original-URL (Symfony)

  Header: X-Rewrite-URL (Symfony)'
output: null
created_at: '2023-04-06T03:56:41.273135+00:00'
updated_at: '2023-04-06T03:56:41.280667+00:00'
---

# Extract HTTP headers

```bash
Values: User-Agent
Values: Cookie
Header: X-Forwarded-Host
Header: X-Host
Header: X-Forwarded-Server
Header: X-Forwarded-Scheme (header; also in combination with X-Forwarded-Host)
Header: X-Original-URL (Symfony)
Header: X-Rewrite-URL (Symfony)
```


