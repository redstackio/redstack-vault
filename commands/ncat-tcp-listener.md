---
id: 241bbd2d-1526-459f-aebf-6ef1e0b76dfd
name: ncat-tcp-listener
type: command
executor: bash
data: ncat --tcp -lvp $_PORT
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - listener
  - reverse-shell
verified: true
validated: true
---

# ncat-tcp-listener

## Command

```bash
ncat --tcp -lvp $_PORT
```

## Description

Starts an Ncat listener on the specified TCP port to accept incoming reverse shell connections. Use this on the attacker machine to receive shells from compromised targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | The port to listen on (e.g., 4242) | Yes |
| --tcp | Specifies TCP protocol | Built-in |
| -l | Listen mode | Built-in |
| -v | Verbose output for connection details | Built-in |
| -p | Port specification | Built-in |

## Examples

### Basic Usage

```bash
ncat --tcp -lvp 4242
```

### With Exec for Shell

Once connected, Ncat can exec a shell, but for reverse, the target handles -e.

## Expected Output

Ncat: Version 7.94 ( https://nmap.org/ncat )
Listening on :::4242

(Waits for connection; upon connect: Connection from [target_ip] port 4242 [tcp/*] accepted)

## Related

- [[commands/ncat-reverse-tcp-connect]]
- [[procedures/linux-reverse-shell-persistence-via-ncat-systemd]]
