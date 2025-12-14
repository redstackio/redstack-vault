---
data: >-
  curl -X POST https://accounts.shopify.com/oauth/token -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "subject_token=[tokenA]&subject_token_type=urn:ietf:params:oauth:token-type:access_token&client_id=8bb79a45-2d69-4890-9006-ab6ca705d708"
tags:
  - token-exchange
type: command
output: HTTP/1.1 200 OK with new access_token
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.082Z'
id: 95b3e1d4-daad-40ff-94cf-cd2100d18c0f
verified: false
validated: true
submitted: true
---
# token-exchange-for-unified-bearer

## Command

```bash
curl -X POST https://accounts.shopify.com/oauth/token -H "Content-Type: application/x-www-form-urlencoded" -d "subject_token=[tokenA]&subject_token_type=urn:ietf:params:oauth:token-type:access_token&client_id=8bb79a45-2d69-4890-9006-ab6ca705d708"
```

## Description

Exchanges tokenA for tokenB.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `subject_token` | tokenA | Yes |
| `subject_token_type` | urn:ietf:params:oauth:token-type:access_token | Yes |
| `client_id` | Client ID | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

New token.

## Related

- [[Related Procedure: Perform-Authenticated-Actions-with-Primary-Token]]
