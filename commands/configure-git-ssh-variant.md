---
type: command
executor: bash
data: >-
  git config --global core.sshCommand 'ssh' && git config --global ssh.variant
  ssh
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - git
  - ssh
verified: true
validated: true
---

# configure-git-ssh-variant

## Command

```bash
git config --global core.sshCommand 'ssh' && git config --global ssh.variant ssh
```

## Description

Configures Git to use standard SSH for remote operations, compatible with backdoor injections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--global` | User-wide | Yes |
| `core.sshCommand` | SSH command | Yes |
| `ssh.variant` | SSH variant | Yes |

## Examples

### Basic Usage

```bash
git config --global core.sshCommand 'ssh' && git config --global ssh.variant ssh
```

## Expected Output

No output.

## Related

- [[procedures/Backdoor-Git-User-Configurations-for-Persistence]]
