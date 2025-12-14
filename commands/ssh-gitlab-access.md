---
data: ssh git@10.26.0.5
tags:
  - ssh
  - access
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.976Z'
id: 75942db9-507c-4f3a-bc32-64b2b2b32f72
verified: false
validated: true
submitted: true
---
# ssh-gitlab-access

## Command

```bash
ssh git@10.26.0.5
```

## Description

Establishes an SSH connection to the GitLab server as the 'git' user, authenticating via an injected public key in authorized_keys for RCE shell access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `git` | Username to connect as ('git' service account) | Yes |
| `10.26.0.5` | Target IP address of GitLab server | Yes |

## Examples

### Basic Usage

```bash
ssh git@target-ip
```

### Advanced Usage

```bash
ssh -i /path/to/private_key git@10.26.0.5 -p 22
```

## Expected Output

Interactive shell prompt (e.g., git@gitlab:~$) after key-based authentication.

## Related

- [[commands/curl-gitlab-package-upload]]
- [[procedures/Establish-SSH-Access-to-GitLab-Server]]
