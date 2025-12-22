---
data: >-
  curl -X POST https://public-api.periscope.tv/v1/broadcast/publish -H
  "Authorization: Bearer <access_token>" -d "broadcast_id=12345" -d
  "tweet_text=Published via CSRF"
tags:
  - api
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.104Z'
id: 3143abbc-67ba-4d55-b6af-ce11523d2663
verified: false
validated: true
submitted: true
---
# curl-publish-broadcast

## Command

```bash
curl -X POST https://public-api.periscope.tv/v1/broadcast/publish -H "Authorization: Bearer <access_token>" -d "broadcast_id=12345" -d "tweet_text=Published via CSRF"
```

## Description

Publishes a Periscope broadcast to Twitter using API access token, making it public.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Authorization: ..."` | Bearer token | Yes |
| `-d "broadcast_id=..."` | ID from create step | Yes |
| `-d "tweet_text=..."` | Tweet content | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://public-api.periscope.tv/v1/broadcast/publish -H "Authorization: Bearer eyJ..." -d "broadcast_id=12345" -d "tweet_text=Live now!"
```

### Advanced Usage

With silent mode: ```bash
curl -s -X POST ... (same)
```

## Expected Output

JSON: {"status": "published", "tweet_id": "67890"}

## Related

- [[Related Procedure: Publish-Broadcast-Using-Access-Token]]
