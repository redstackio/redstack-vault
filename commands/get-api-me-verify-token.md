---
id: cmd-get-api-me-001
data: >-
  curl -X GET
  "https://OAUTH_PROVIDER_DOMAIN/api/me?access_token=ACCESS_TOKEN_VALUE"
tags:
  - token-verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.767Z'
verified: false
validated: true
submitted: true
---
# get-api-me-verify-token

## Command

```bash
curl -X GET "https://OAUTH_PROVIDER_DOMAIN/api/me?access_token=ACCESS_TOKEN_VALUE"
```

## Description

Sends a GET request to a protected user info endpoint using the access token to verify its validity and functionality.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| access_token | The token to test | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://provider.com/api/me?access_token=eyJ..."
```

### Advanced Usage

With headers: curl -H "Accept: application/json" ...

## Expected Output

JSON user data like {"id": 123, "email": "user@example.com"} if valid; 401 Unauthorized if invalid.

## Related

- [[commands/curl-oauth-access-race]]
- [[procedures/Verify-Tokens-and-Test-Revocation]]
