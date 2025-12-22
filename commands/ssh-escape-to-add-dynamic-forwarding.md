---
type: command
executor: bash
data: '[ENTER]~C\n-D $_LOCAL_PORT'
tags:
  - ssh
  - escape-sequence
  - tunneling
platforms:
  - Linux
  - macOS
  - Unix
verified: true
validated: true
---

# ssh-escape-to-add-dynamic-forwarding

## Command

```bash
# Within an active SSH session:\n[ENTER] then ~C to enter command mode\n-D $_LOCAL_PORT\n[ENTER] to resume session
```

## Description

This escape sequence adds dynamic port forwarding (SOCKS proxy) to an ongoing SSH session without disconnecting. Useful for adding pivoting capabilities mid-session during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ~C | Escape character (tilde) followed by C to enter SSH command mode | Yes |
| -D $_LOCAL_PORT | Add dynamic forwarding on specified local port (e.g., 1090) | Yes |

## Examples

### Basic Usage

In active SSH: Press Enter, then ~C, type '-D 1090', Enter.

### Advanced Usage

For multiple forwards: After ~C, type '-L 8080:internal:80' or combine with -D.

## Expected Output

Command mode prompt (e.g., "ssh>"), then "Forwarding port" confirmation. Session resumes seamlessly. No shell output change.

## Related

- [[procedures/SSH-Tunneling-for-SOCKS-Proxy]]
- [[commands/ssh-create-background-socks-proxy]]
