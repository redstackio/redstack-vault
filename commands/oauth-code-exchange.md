---
data: >-
  curl -X POST https://accounts.shopify.com/oauth/token -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "code=ABCDEFG&grant_type=authorization_code&redirect_uri=com.shopify.ping%3A%2F%2Fauth%2Fcallback&code_verifier=Uiz7J0nHRPvKDpX8ETGYaV9YEW0fx_drl7W4Mmiy-ZOMkwY0mb-5mvNmsDcg3IqBIXQ5XtYrS-wHh1xa6IbEkA&client_id=8bb79a45-2d69-4890-9006-ab6ca705d708"
tags:
  - oauth
  - token
type: command
output: >-
  {"access_token":"atkn_0......","refresh_token":"atkn_9.....","id_token":"eyJ0eXA....."}
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.091Z'
id: 77796fdb-623a-4c7a-b374-8a2d195b8220
verified: false
validated: true
submitted: true
---
# oauth-code-exchange

## Command

```bash
curl -X POST https://accounts.shopify.com/oauth/token -H "Content-Type: application/x-www-form-urlencoded" -d "code=ABCDEFG&grant_type=authorization_code&redirect_uri=com.shopify.ping%3A%2F%2Fauth%2Fcallback&code_verifier=Uiz7J0nHRPvKDpX8ETGYaV9YEW0fx_drl7W4Mmiy-ZOMkwY0mb-5mvNmsDcg3IqBIXQ5XtYrS-wHh1xa6IbEkA&client_id=8bb79a45-2d69-4890-9006-ab6ca705d708"
```

## Description

Exchanges OAuth code for tokens using PKCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `code` | Authorization code | Yes |
| `grant_type` | authorization_code | Yes |
| `redirect_uri` | App callback URI | Yes |
| `code_verifier` | PKCE verifier | Yes |
| `client_id` | App client ID | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

JSON with tokens.

## Related

- [[Related Procedure: Exchange-Authorization-Code-for-Access-Tokens]]
