---
id: ac1505cb-733f-49ae-a06f-e4b94aa1afc3
type: command
executor: bash
data: wall "$_MESSAGE"
output: null
created_at: '2023-04-06T03:56:21.852060+00:00'
updated_at: '2023-04-06T03:56:21.864040+00:00'
platforms:
  - Linux
tags:
  - messaging
  - broadcast
verified: true
validated: true
---

# wall-send-message-to-all-users-linux

## Command

```bash
wall "$_MESSAGE"
```

## Description

Broadcasts a message to all logged-in users' terminals on a Linux system. Requires write access to /dev/tty; often needs root for full effect.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "$_MESSAGE" | Text to broadcast | Yes |

## Examples

### Basic Usage

```bash
wall "Stop messing with the service!"
```

### Longer Message

```bash
wall "System update required; please save work."
```

## Expected Output

```
Broadcast message from root (tty1) at 10:30 ...
Stop messing with the service!
```

Echoed to sender; appears on all terminals.

## Related

- [[procedures/Inter-User-Messaging]]
