---
data: >-
  curl -X POST https://accounts.shopify.com/oauth/token -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "grant_type=urn:ietf:params:oauth:grant-type:token-exchange&audience=...&scope=https://api.shopify.com/auth/destinations.readonly&subject_token=[tokenA]&subject_token_type=urn:ietf:params:oauth:token-type:access_token&client_id=8bb79a45-2d69-4890-9006-ab6ca705d708"
tags:
  - token-exchange
  - post-logout
type: command
output: HTTP/1.1 200 OK with new token
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.054Z'
id: 37fac2eb-549f-47ee-b4b5-50951dd6b5b8
verified: false
validated: true
submitted: true
---
# token-exchange-post-logout

## Command

```bash
curl -X POST https://accounts.shopify.com/oauth/token -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=urn:ietf:params:oauth:grant-type:token-exchange&audience=...&scope=https://api.shopify.com/auth/destinations.readonly&subject_token=[tokenA]&subject_token_type=urn:ietf:params:oauth:token-type:access_token&client_id=8bb79a45-2d69-4890-9006-ab6ca705d708"
```

## Description

Exchanges persistent tokenA post-logout.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `grant_type` | token-exchange | Yes |
| `subject_token` | tokenA | Yes |
| Others | As specified | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

New token issued.

## Related

- [[Related Procedure: Verify-Persistent-Access-Token-Post-Logout]]
