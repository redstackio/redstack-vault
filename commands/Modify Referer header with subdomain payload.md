---
id: ab9941b4-14c8-4793-98b3-49aa816544de
name: Modify Referer header with subdomain payload
type: command
executor: bash
data: 'Open https://trusted.domain.com.attacker.com/csrf.html

  The Referer header is modified to include the subdomain payload.

  Referer: https://trusted.domain.com.attacker.com/csrf.html'
output: null
created_at: '2023-04-06T03:55:55.678440+00:00'
updated_at: '2023-04-06T03:55:55.684184+00:00'
---

# Modify Referer header with subdomain payload

```bash
Open https://trusted.domain.com.attacker.com/csrf.html
The Referer header is modified to include the subdomain payload.

Referer: https://trusted.domain.com.attacker.com/csrf.html
```
