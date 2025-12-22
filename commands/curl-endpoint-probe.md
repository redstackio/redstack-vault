---
data: >-
  curl -X POST
  'https://api.larksuite.com/open-apis/im/v1/messages?receive_id_type=user_id'
  -H 'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d
  '{"receive_id": "test_user", "msg_type": "text", "content":
  "{\"text\":\"test\"}"}'
tags:
  - recon
  - api-probe
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.425Z'
id: af146559-3a24-44de-a545-6d39610db776
verified: false
validated: true
submitted: true
---
# curl-endpoint-probe

## Command

```bash
curl -X POST 'https://api.larksuite.com/open-apis/im/v1/messages?receive_id_type=user_id' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"receive_id": "test_user", "msg_type": "text", "content": "{\"text\":\"test\"}"}'
```

## Description

Probes the Lark Suite messenger endpoint to verify accessibility and basic functionality before attempting SSRF exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `URL` | API endpoint | Yes |
| `-H 'Authorization'` | Auth header | Yes |
| `-d` | Test JSON payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.larksuite.com/open-apis/im/v1/messages' -H 'Authorization: Bearer token' -d '{"content": "test"}'
```

### Advanced Usage

```bash
curl -X POST 'https://api.larksuite.com/open-apis/im/v1/messages' -H 'Authorization: Bearer token' -v -d '{"msg_type": "text", "content": "probe"}'
```

## Expected Output

`{"code":0,"msg":"ok"}` or similar success JSON.

## Related

- [[Related Procedure|procedures/Identify-Lark-Messenger-SSRF-Endpoint]]
