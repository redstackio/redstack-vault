---
id: cmd-curl-initial-access-001
data: >-
  curl --data
  "grant_type=authorization_code&code=AUTHORIZATION_CODE_VALUE&client_id=APPLICATION_ID&client_secret=APPLICATION_SECRET&redirect_uri=APPLICATION_REDIRECT_URI"
  "https://OAUTH_PROVIDER_DOMAIN/oauth/token"
tags:
  - oauth
  - initial-token
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.759Z'
verified: false
validated: true
submitted: true
---
# curl-oauth-initial-access

## Command

```bash
curl --data "grant_type=authorization_code&code=AUTHORIZATION_CODE_VALUE&client_id=APPLICATION_ID&client_secret=APPLICATION_SECRET&redirect_uri=APPLICATION_REDIRECT_URI" "https://OAUTH_PROVIDER_DOMAIN/oauth/token"
```

## Description

Performs a single legitimate exchange of an authorization code for access and refresh tokens to obtain initial credentials before racing refreshes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| code | Authorization code | Yes |
| client_id | App ID | Yes |
| client_secret | App secret | Yes |
| redirect_uri | Callback URI | Yes |
| grant_type | 'authorization_code' | Yes |

## Examples

### Basic Usage

```bash
curl --data "grant_type=authorization_code&code=abc123&client_id=app1&client_secret=secret&redirect_uri=https://example.com/cb" "https://provider.com/oauth/token"
```

## Expected Output

Single JSON: {"access_token": "eyJ...", "refresh_token": "def456"}

## Related

- [[commands/curl-oauth-refresh-race]]
- [[procedures/Exploit-Refresh-Token-Race-Condition]]
