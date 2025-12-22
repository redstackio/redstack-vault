---
id: d9c0eb06-3edb-4123-877a-a9c0076542d0
type: command
executor: cmd
data: 'msg * /V /W /SERVER:$_SERVER "$_MESSAGE"'
output: null
created_at: '2023-04-06T03:56:21.852007+00:00'
updated_at: '2023-04-06T03:56:21.863988+00:00'
platforms:
  - Windows
tags:
  - messaging
  - broadcast
verified: true
validated: true
---

# msg-send-message-to-all-users-windows

## Command

```cmd
msg * /V /W /SERVER:$_SERVER "$_MESSAGE"
```

## Description

Broadcasts a message to all active user sessions on a Windows system, local or remote. /V displays in title bar, /W waits for acknowledgment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| * | Wildcard for all users | Yes |
| /V | Verbose: Show in title bar | No |
| /W | Wait for response | No |
| /SERVER:$_SERVER | Target server (omit for local) | No |
| "$_MESSAGE" | Message content | Yes |

## Examples

### Basic Broadcast (Local)

```cmd
msg * "Hello all!"
```

### With Options (Remote)

```cmd
msg * /V /W /SERVER:CRASHLAB "Maintenance in 5 minutes."
```

## Expected Output

```
All users responded to the message.
```

Popups appear on all screens; errors if no sessions.

## Related

- [[procedures/Inter-User-Messaging]]
