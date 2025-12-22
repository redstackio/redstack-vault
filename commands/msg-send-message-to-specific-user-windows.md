---
id: 3f298afd-25c1-4df5-bc0e-67b62ef20b6b
type: command
executor: cmd
data: 'msg $_USERNAME /SERVER:$_SERVER "$_MESSAGE"'
output: null
created_at: '2023-04-06T03:56:21.851945+00:00'
updated_at: '2023-04-06T03:56:21.863955+00:00'
platforms:
  - Windows
tags:
  - messaging
  - lateral-movement
verified: true
validated: true
---

# msg-send-message-to-specific-user-windows

## Command

```cmd
msg $_USERNAME /SERVER:$_SERVER "$_MESSAGE"
```

## Description

Sends a popup message to a specific user session on a local or remote Windows system. Requires the Messenger service or Terminal Services; administrative rights for remote targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Target username (e.g., Swissky) | Yes |
| /SERVER:$_SERVER | Remote server name or IP (omit for local) | No |
| "$_MESSAGE" | Message text (up to 128 chars) | Yes |

## Examples

### Basic Usage (Local)

```cmd
msg Swissky "Stop rebooting the service!"
```

### Remote Usage

```cmd
msg Swissky /SERVER:CRASHLAB "Alert: System check required."
```

## Expected Output

```
Success: The message was sent to session 1.
```

Or error if session inactive or permissions denied.

## Related

- [[procedures/Inter-User-Messaging]]
