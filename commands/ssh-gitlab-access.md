---
data: ssh git@gitlab-vm.local -i gitlab
tags:
  - ssh
  - access
type: command
executor: bash
platforms:
  - Linux
id: 82c37aca-9679-4e49-940c-d1d97a3a67e5
created_at: '2025-12-11T06:10:29.363Z'
updated_at: '2025-12-11T06:10:29.363Z'
verified: false
validated: true
submitted: true
---
# ssh-gitlab-access

## Command

```bash
ssh git@gitlab-vm.local -i gitlab
```

## Description

Establishes SSH connection to GitLab server using specified private key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i gitlab` | Identity file | Yes |
| `git@gitlab-vm.local` | User and host | Yes |

## Examples

### Basic Usage

```bash
ssh git@gitlab-vm.local -i gitlab
```

## Expected Output

Welcome message and shell prompt as git user.

## Related

- [[procedures/Establish-SSH-Access]]
