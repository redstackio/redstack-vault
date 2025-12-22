---
id: cmd-uuid-001
data: >-
  {"e":"set_watch","p":["get_datetime().strftime(\"%Y-%m-%d
  %H:%M:%S\")#__QUANTOPIAN__"]}
tags:
  - websocket
  - debugger
type: command
output: >-
  Response with evaluated expression result, e.g., {"result": "2023-10-01
  12:00:00"}
executor: websocket
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.603Z'
verified: false
validated: true
submitted: true
---
# set-watch-websocket-message

## Command

This is a WebSocket JSON message sent to set a watched expression in Quantopian's debugger.

```json
{"e":"set_watch","p":["get_datetime().strftime(\"%Y-%m-%d %H:%M:%S\")#__QUANTOPIAN__"]}
