---
id: 37a0b660-17b8-4d3c-8bf1-de2624652ccc
type: command
executor: bash
data: write $_USERNAME $_TTY
output: null
created_at: '2023-04-06T03:56:21.852268+00:00'
updated_at: '2023-04-06T03:56:21.864189+00:00'
platforms:
  - Linux
tags:
  - messaging
  - direct
verified: true
validated: true
---

# write-send-message-to-specific-user-linux

## Command

```bash
write $_USERNAME $_TTY
```

## Description

Initiates a direct message to a specific user's terminal. Type message after invocation, end with Ctrl+D.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Target user (e.g., root) | Yes |
| $_TTY | Terminal ID from 'who' (e.g., pts/2) | Yes |

## Examples

### Basic Usage

```bash
write root pts/2
```

(Type message, then Ctrl+D)

## Expected Output

On recipient: "Message from [user] on pts/0 at 10:30 ..."
[Your message here]

EOF if user blocks with 'mesg n'.

## Related

- [[procedures/Inter-User-Messaging]]
