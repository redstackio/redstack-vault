---
type: command
executor: bash
data: find /tmp -type d -name 'ssh-*' 2>/dev/null
output: |-
  /tmp/ssh-abc123DEF
  /tmp/ssh-xyz789GHI
platforms:
  - Linux
tags:
  - recon
  - ssh
verified: true
validated: true
---

# find-ssh-agent-sockets

## Command

```bash
find /tmp -type d -name 'ssh-*' 2>/dev/null
```

## Description

This command searches for active SSH agent forwarding directories in /tmp, which are created when agent forwarding (-A) is enabled. It helps identify potential sessions to hijack on an intermediary system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /tmp | Base directory to search (standard temp location for sockets) | Yes |
| -type d | Restrict to directories only | Yes |
| -name 'ssh-*' | Pattern match for SSH directories | Yes |
| 2>/dev/null | Suppress permission denied errors | No |

## Examples

### Basic Usage

```bash
find /tmp -type d -name 'ssh-*' 2>/dev/null
```

### Advanced Usage

```bash
find /tmp -maxdepth 1 -type d -name 'ssh-*' -mtime -1 2>/dev/null
```

> Limits to directories modified in the last day for recent sessions.

## Expected Output

Description of what output to expect when the command runs successfully.

/tmp/ssh-abc123DEF
/tmp/ssh-xyz789GHI

These are paths to SSH forwarding directories; inspect with ls -ld for timestamps.

## Related

- [[procedures/SSH-Agent-Forwarding-Hijack]]
- [[commands/list-ssh-agent-files]]
