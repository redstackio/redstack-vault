---
data: >-
  curl -X POST
  'https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_rules' -H
  'Authorization: Bearer {api_token}' -H 'Content-Type: application/json' --data
  '{"action_parameters": {"host_header": "example.com"}}'
tags:
  - api
  - cloudflare
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 81a28d79-99bc-4a13-9641-52d77eb915ae
created_at: '2025-12-13T09:01:22.251Z'
updated_at: '2025-12-13T09:01:22.251Z'
verified: false
validated: true
submitted: true
---
# curl-api-request

## Command

```bash
curl -X POST 'https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_rules' \
  -H 'Authorization: Bearer {api_token}' \
  -H 'Content-Type: application/json' \
  --data '{"action_parameters": {"host_header": "example.com"}}'
```

## Description

This command interacts with the Cloudflare Origin Rules API to create or test rules, useful for vulnerability probing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H 'Authorization: Bearer {api_token}'` | API authentication | Yes |
| `--data` | JSON payload for rule | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_rules' \
  -H 'Authorization: Bearer {api_token}' \
  -H 'Content-Type: application/json' \
  --data '{"action_parameters": {"host_header": "example.com"}}'
```

### Advanced Usage

```bash
curl -X POST 'https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_rules' \
  -H 'Authorization: Bearer {api_token}' \
  -H 'Content-Type: application/json' \
  --data '{"action_parameters": {"host_header": "example.com\r\nTest"}}'
```

## Expected Output

JSON response with rule details if successful, or error if invalid.

## Related

- [[commands/curl-inject-crlf]]
- [[procedures/Identify-Insufficient-Validation-in-Host-Header-Parameter]]
