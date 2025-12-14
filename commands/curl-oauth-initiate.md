---
id: i9j0k1l2-m3n4-5678-ijkl-901234567890
data: >-
  curl
  "https://login.uber.com/oauth/authorize?client_id=$CLIENT_ID&redirect_uri=$REDIRECT_URI&response_type=code&scope=$SCOPE"
tags:
  - oauth
  - auth
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:30:18.216Z'
verified: false
validated: true
submitted: true
---
# curl-oauth-initiate

## Command

```bash
curl "https://login.uber.com/oauth/authorize?client_id=UBER_CLIENT_ID&redirect_uri=https://dangling-app.herokuapp.com/callback&response_type=code&scope=profile"
```

## Description

Initiates an OAuth 2.0 authorization request to obtain an authorization code via redirect.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `client_id` | OAuth client identifier | Yes |
| `redirect_uri` | Callback URL | Yes |
| `response_type` | Set to 'code' for auth code flow | Yes |
| `scope` | Requested permissions | Yes |

## Examples

### Basic Usage

```bash
curl "https://login.uber.com/oauth/authorize?client_id=UBER_CLIENT_ID&redirect_uri=https://example.com/callback&response_type=code"
```

### Advanced Usage

```bash
curl -L "https://login.uber.com/oauth/authorize?..." # Follow redirects
```

## Expected Output

HTML login page or redirect to callback with ?code=AUTH_CODE.

## Related

- [[commands/curl-token-exchange]]
- [[procedures/Intercept-OAuth-Callback-for-Account-Takeover]]
