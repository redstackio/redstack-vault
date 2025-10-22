---
id: a6211ab3-d4ed-414c-aa41-05ced0cb5009
name: Check for HTTP Header Injection
type: command
executor: bash
data: 'Connection: keep-alive

  Content-Length: 178

  Content-Type: text/html

  Date: Mon, 09 May 2016 14:47:29 GMT

  Location: https://www.example.net/[INJECTION STARTS HERE]

  Set-Cookie: mycookie=myvalue

  X-Frame-Options: SAMEORIGIN

  X-Sucuri-ID: 15016

  x-content-type-options: nosniff

  x-xss-protection: 1; mode=block'
output: null
created_at: '2023-04-06T03:55:55.988331+00:00'
updated_at: '2023-04-10T20:21:20.890908+00:00'
---

# Check for HTTP Header Injection

```bash
Connection: keep-alive
Content-Length: 178
Content-Type: text/html
Date: Mon, 09 May 2016 14:47:29 GMT
Location: https://www.example.net/[INJECTION STARTS HERE]
Set-Cookie: mycookie=myvalue
X-Frame-Options: SAMEORIGIN
X-Sucuri-ID: 15016
x-content-type-options: nosniff
x-xss-protection: 1; mode=block
```
