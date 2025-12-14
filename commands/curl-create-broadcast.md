---
data: >-
  curl -X POST https://public-api.periscope.tv/v1/broadcast/create -H
  "Authorization: Bearer <access_token>" -d "title=Test Broadcast" -d
  "description=CSRF Demo"
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
updated_at: '2025-12-14T17:30:35.108Z'
id: 844fbbde-c6cd-4435-ac5b-049f02f2257f
verified: false
validated: true
submitted: true
---
# curl-create-broadcast

## Command

```bash
curl -X POST https://public-api.periscope.tv/v1/broadcast/create -H "Authorization: Bearer <access_token>" -d "title=Test Broadcast" -d "description=CSRF Demo"
```

## Description

Creates a new broadcast in Periscope using a bearer token. Demonstrates API access post-token theft.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Authorization: ..."` | Bearer token header | Yes |
| `-d "title=..."` | Broadcast title | Yes |
| `-d "description=..."` | Description | No |

## Examples

### Basic Usage

```bash
curl -X POST https://public-api.periscope.tv/v1/broadcast/create -H "Authorization: Bearer eyJ..." -d "title=Test"
```

### Advanced Usage

With more fields: ```bash
curl -X POST ... -d "title=Test" -d "description=Demo" -d "category=live"
```

## Expected Output

JSON: {"broadcast_id": "12345", "status": "created"}

## Related

- [[Related Procedure: Create-Broadcast-Using-Access-Token]]
