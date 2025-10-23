---
id: 3230da79-bb35-4418-be32-99a7bf7db1b3
name: HTTP GET Request to /endpoint
type: command
executor: bash
data: "GET /endpoint HTTP/1.1\nHost: victim.example.com\nOrigin: https://evil.com\n\
  Cookie: sessionid=... \n"
output: null
created_at: '2023-04-06T03:55:55.731485+00:00'
updated_at: '2023-04-10T20:21:21.233901+00:00'
---

# HTTP GET Request to /endpoint

```bash
GET /endpoint HTTP/1.1
Host: victim.example.com
Origin: https://evil.com
Cookie: sessionid=... 

```


