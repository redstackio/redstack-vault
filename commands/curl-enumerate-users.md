---
data: >-
  curl -X GET https://www.paypal.com/businessmanage/users/api/v1/users -H
  "Authorization: Bearer your_access_token" -H "Content-Type: application/json"
tags:
  - discovery
  - api
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 29ed36cc-65c5-4116-a2a6-af58be5d27e7
created_at: '2025-12-11T06:10:30.208Z'
updated_at: '2025-12-11T06:10:30.208Z'
verified: false
validated: true
submitted: true
---
# curl-enumerate-users

## Command

```bash
curl -X GET https://www.paypal.com/businessmanage/users/api/v1/users \
  -H "Authorization: Bearer your_access_token" \
  -H "Content-Type: application/json"
```

## Description

Enumerates users via PayPal Business API to identify potential targets for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer your_access_token"` | Bearer token | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://www.paypal.com/businessmanage/users/api/v1/users -H "Authorization: Bearer your_access_token" -H "Content-Type: application/json"
```

## Expected Output

JSON array of user objects including user_ids.

## Related
- [[procedures/Identify-Target-User-for-IDOR-Exploitation]]
