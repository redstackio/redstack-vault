---
id: cmd-curl-access-single-001
data: >-
  curl --data
  "grant_type=authorization_code&code=AUTHORIZATION_CODE_VALUE&client_id=APPLICATION_ID&client_secret=APPLICATION_SECRET&redirect_uri=APPLICATION_REDIRECT_URI"
  "https://OAUTH_PROVIDER_DOMAIN/oauth/token"
tags:
  - oauth
  - code-exchange
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.742Z'
verified: false
validated: true
submitted: true
---
# curl-oauth-access-single

## Command

```bash
curl --data "grant_type=authorization_code&code=AUTHORIZATION_CODE_VALUE&client_id=APPLICATION_ID&client_secret=APPLICATION_SECRET&redirect_uri=APPLICATION_REDIRECT_URI" "https://OAUTH_PROVIDER_DOMAIN/oauth/token"
```

## Description

Single POST to exchange a saved authorization code for tokens, used post-revocation to restore access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| code | Saved code | Yes |
| client_id | App ID | Yes |
| client_secret | Secret | Yes |
| redirect_uri | URI | Yes |
| grant_type | 'authorization_code' | Yes |

## Examples

### Basic Usage

```bash
curl --data "grant_type=authorization_code&code=saved123&client_id=app1&client_secret=secret&redirect_uri=https://example.com/cb" "https://provider.com/oauth/token"
```

## Expected Output

JSON with access_token and refresh_token.

## Related

- [[commands/curl-oauth-initial-access]]
- [[procedures/Exploit-Authorization-Code-Revocation-Flaw]]
