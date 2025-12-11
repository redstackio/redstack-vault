---
data: ssh -i ~/.ssh/id_ed25519 git@10.26.0.3
tags:
  - access
type: command
executor: bash
platforms:
  - Linux
id: e21b205f-5065-4259-9d20-8f90414875c5
created_at: '2025-12-11T06:10:22.603Z'
updated_at: '2025-12-11T06:10:22.603Z'
verified: false
validated: true
submitted: true
---
# ssh-connect

## Command

```bash
ssh -i ~/.ssh/id_ed25519 git@10.26.0.3
```

## Description

Establishes an SSH connection using the specified private key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Specifies the identity file (private key) | Yes |
| `~/.ssh/id_ed25519` | Path to private key | Yes |
| `git@10.26.0.3` | User and host to connect to | Yes |

## Examples

### Basic Usage

```bash
ssh -i key user@host
```

## Expected Output

Connects to the server and displays a welcome message or shell.

## Related

- [[procedures/Exploit-SSH-Access]]
