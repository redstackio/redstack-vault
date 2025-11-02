---
id: 9a3a4e94-ae7f-411d-89f7-91e596f5594d
name: Netcat Command
type: command
executor: ''
data: 'nc demo.testfire.net 80

  OPTIONS / HTTP/1.1

  Host: demo.testfire.net'
output: 'HTTP/1.1 200 OK

  Date: Sun, 19 July 2020 06:46:30 GMT

  Server: Apache-Coyote/1.1

  Allow: GET, HEAD, POST, OPTIONS, TRACE

  Content-Length: 0

  Connection: close

  Content-Type: text/html'
created_at: '2020-07-19T06:50:16.822559+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Netcat]]'
- '[[host]]'
- '[[type]]'
---

# Netcat Command

```bash
nc demo.testfire.net 80
OPTIONS / HTTP/1.1
Host: demo.testfire.net
```

## Expected Output

```
HTTP/1.1 200 OK
Date: Sun, 19 July 2020 06:46:30 GMT
Server: Apache-Coyote/1.1
Allow: GET, HEAD, POST, OPTIONS, TRACE
Content-Length: 0
Connection: close
Content-Type: text/html
```


