---
data: ssh -i ~/.ssh/id_ed25519 git@10.26.0.3
tags:
  - access
  - ssh
type: command
executor: bash
platforms:
  - Linux
id: dd8f88d0-01eb-43d4-a115-e25b9bc452dc
created_at: '2025-12-11T03:47:39.957Z'
updated_at: '2025-12-11T03:47:39.957Z'
verified: false
validated: true
submitted: true
---
# ssh-connect-git

## Command

```bash
ssh -i ~/.ssh/id_ed25519 git@10.26.0.3
```

## Description

Connects via SSH to the GitLab server using the injected public key for RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Specifies the identity file (private key) | Yes |
| `~/.ssh/id_ed25519` | Path to private key | Yes |
| `git@10.26.0.3` | User and host to connect to | Yes |

## Examples

### Basic Usage

```bash
ssh -i ~/.ssh/id_ed25519 git@10.26.0.3
```

## Expected Output

SSH connection established, displaying Ubuntu welcome message and shell prompt.

## Related

- [[procedures/Establish-SSH-Connection-for-RCE]]
