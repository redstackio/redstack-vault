---
id: 30c4e5a5-12ab-49c6-b399-f2993513e305
name: HTTP GET request to endpoint
type: command
executor: bash
data: 'GET /endpoint HTTP/1.1

  Host: victim.example.com

  Origin: https://evil.com

  Cookie: sessionid=... '
output: null
created_at: '2023-04-06T03:55:54.548875+00:00'
updated_at: '2023-04-06T03:55:54.554680+00:00'
---

# HTTP GET request to endpoint

```bash
GET /endpoint HTTP/1.1
Host: victim.example.com
Origin: https://evil.com
Cookie: sessionid=... 
```


