---
id: c0b6834c-f56f-4f21-ba2a-c8ebc322e7e7
name: Disable SMB and HTTP servers in Responder Core
type: command
executor: bash
data: '[Responder Core]

  ; Servers to start

  ...

  SMB = Off     # Turn this off

  HTTP = Off    # Turn this off'
output: null
created_at: '2023-04-06T03:56:05.401672+00:00'
updated_at: '2023-04-10T20:25:57.881468+00:00'
---

# Disable SMB and HTTP servers in Responder Core

```bash
[Responder Core]
; Servers to start
...
SMB = Off     # Turn this off
HTTP = Off    # Turn this off
```


