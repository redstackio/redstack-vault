---
id: ad6c0245-40ec-46e4-bf99-1ab7b381f02f
name: Access /endpoint API
type: command
executor: bash
data: "GET /endpoint HTTP/1.1\nHost: victim.example.com\nOrigin: https://evil.com\n\
  Cookie: sessionid=... \n"
output: null
created_at: '2023-04-06T03:55:54.980855+00:00'
updated_at: '2023-04-06T03:55:54.986605+00:00'
---

# Access /endpoint API

```bash
GET /endpoint HTTP/1.1
Host: victim.example.com
Origin: https://evil.com
Cookie: sessionid=... 

```


