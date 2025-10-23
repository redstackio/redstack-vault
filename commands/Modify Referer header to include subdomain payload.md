---
id: b49455a8-6e09-412c-ad2c-a76ab04fb962
name: Modify Referer header to include subdomain payload
type: command
executor: bash
data: '1) Open https://trusted.domain.com.attacker.com/csrf.html

  2) The Referer header is modified to include the subdomain payload.


  Referer: https://trusted.domain.com.attacker.com/csrf.html'
output: null
created_at: '2023-04-06T03:55:56.397669+00:00'
updated_at: '2023-04-10T20:21:28.281442+00:00'
---

# Modify Referer header to include subdomain payload

```bash
1) Open https://trusted.domain.com.attacker.com/csrf.html
2) The Referer header is modified to include the subdomain payload.

Referer: https://trusted.domain.com.attacker.com/csrf.html
```


