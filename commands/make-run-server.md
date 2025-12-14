---
data: make run-server
tags:
  - mattermost
  - restart
  - development
type: command
executor: bash
platforms:
  - Linux
id: 99d56cf8-9488-42bf-82b7-48a35c9f2e20
created_at: '2025-12-14T17:26:37.554Z'
updated_at: '2025-12-14T17:26:37.554Z'
verified: false
validated: true
submitted: true
---
# make-run-server

## Command

```bash
make run-server
```

## Description

This Makefile target restarts the Mattermost development server, used to recover from hangs caused by oversized logging payloads in vulnerability testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs the default server build and start | No |

## Examples

### Basic Usage

```bash
make run-server
```

### Advanced Usage

In the Mattermost source directory, after modifications:

```bash
make run-server
```

## Expected Output

Server logs indicate startup, with messages like 'Server is listening on :8065' and console logging enabled, restoring availability after DoS.

## Related

- [[procedures/Trigger-DoS-via-Large-Slash-Command-Payload]]
- [[procedures/Trigger-DoS-via-Large-Authentication-Cookie]]
