---
data: 'KickClient(client, full)'
tags:
  - csgo
  - sourcemod
  - kick
type: command
executor: bash
platforms:
  - Windows
  - 'CS:GO'
id: 6155d761-41be-427d-8736-2701e4bbd6db
created_at: '2025-12-14T00:11:25.207Z'
updated_at: '2025-12-14T00:11:25.207Z'
verified: false
validated: true
submitted: true
---
# Kickclient with Unlimited Payload

## Command

```bash
KickClient(client, full)
```

## Description

SourceMod function to kick a client with a custom message without character limit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `client` | Target client ID | Yes |
| `full` | Kick message string | Yes |

## Examples

### Basic Usage

```bash
KickClient(client, full)
```

## Expected Output

Kicks the client and displays the message in popup.

## Related

- [[procedures/Develop-SourceMod-Plugin-for-RCE-Testing]]
