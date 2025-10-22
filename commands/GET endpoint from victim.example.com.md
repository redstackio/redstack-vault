---
id: 81eb4438-faff-4f5b-85fd-4bed704650bd
name: GET endpoint from victim.example.com
type: command
executor: bash
data: "GET /endpoint HTTP/1.1\nHost: victim.example.com\nOrigin: https://evil.com\n\
  Cookie: sessionid=... \n\n"
output: null
created_at: '2023-04-06T03:55:54.207493+00:00'
updated_at: '2023-04-06T03:55:54.214854+00:00'
---

# GET endpoint from victim.example.com

```bash
GET /endpoint HTTP/1.1
Host: victim.example.com
Origin: https://evil.com
Cookie: sessionid=... 

```
