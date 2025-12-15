---
data: ssh-keygen -t ed25519 -f /root/.ssh/id_ed25519 -N ""
tags:
  - ssh
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.882Z'
id: 6f461d58-08d2-4768-8930-47780d165292
verified: false
validated: true
submitted: true
---
# ssh-keygen-ed25519

## Command

```bash
ssh-keygen -t ed25519 -f /root/.ssh/id_ed25519 -N ""
```

## Description

Generates an ed25519 SSH key pair without passphrase.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t | Key type | Yes |
| -f | Output file | Yes |
| -N | Passphrase | Yes (empty) |

## Examples

### Basic Usage

```bash
ssh-keygen -t rsa -b 4096
```

## Expected Output

Generating public/private ed25519 key pair.
Your identification has been saved in /root/.ssh/id_ed25519

## Related

- [[procedures/Install-Dependencies-and-Generate-SSH-Key]]
