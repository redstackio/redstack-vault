---
id: c7e11694-19e4-42f3-974c-d34f1ce4f4be
type: command
executor: bash
data: wall -n "$_MESSAGE"
output: null
created_at: '2023-04-06T03:56:21.852116+00:00'
updated_at: '2023-04-06T03:56:21.864086+00:00'
platforms:
  - Linux
tags:
  - messaging
  - non-broadcast
verified: true
validated: true
---

# wall-send-message-non-broadcast-linux

## Command

```bash
wall -n "$_MESSAGE"
```

## Description

Sends a wall message without broadcasting to terminals (root-only). Useful for logged alerts without screen disruption.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | No broadcast to terminals | No |
| "$_MESSAGE" | Message text | Yes |

## Examples

### Root-Only Usage

```bash
wall -n "Maintenance at 13:00 PM for 2 hours."
```

## Expected Output

No terminal echo; message logged or sent selectively. Error if not root: "Permission denied".

## Related

- [[procedures/Inter-User-Messaging]]
