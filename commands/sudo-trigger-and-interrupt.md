---
type: command
executor: bash
data: sudo whatever
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - sudo
  - privilege-escalation
verified: true
validated: true
---

# sudo-trigger-and-interrupt

## Command

```bash
sudo whatever
```

## Description

Triggers the sudo authentication prompt using a placeholder command, which is then interrupted to create an invalid sudo token for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `whatever` | Placeholder command to trigger prompt (any invalid command works) | Yes |

## Examples

### Basic Usage

```bash
sudo ls
```

Interrupt with Ctrl+C upon password prompt.

## Expected Output

Prompt: `[sudo] password for user: ` followed by interruption (no output, but invalid token created internally).

## Related

- [[procedures/Linux-Privilege-Escalation-via-SUDO-Injection]]
