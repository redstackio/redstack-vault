---
data: ssh git@gitlab-vm.local -i gitlab
tags:
  - ssh
  - access
type: command
executor: bash
platforms:
  - Linux
id: dfb78950-e813-4dad-bcef-94f8fc73d422
created_at: '2025-12-11T03:47:47.568Z'
updated_at: '2025-12-11T03:47:47.568Z'
verified: false
validated: true
submitted: true
---
# ssh-connect-with-key

## Command

```bash
ssh git@gitlab-vm.local -i gitlab
```

## Description

Establishes SSH connection using a specified private key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i gitlab` | Identity file (private key) | Yes |
| `git@gitlab-vm.local` | User and host | Yes |

## Examples

### Basic Usage

```bash
ssh git@gitlab-vm.local -i gitlab
```

## Expected Output

Welcome message and shell prompt as git user.

## Related

- [[procedures/Establish-SSH-Access-and-Verify]]
