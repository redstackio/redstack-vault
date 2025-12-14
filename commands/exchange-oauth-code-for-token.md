---
id: 123e4567-e89b-12d3-a456-426614174006
name: exchange-oauth-code-for-token
type: command
executor: bash
data: ./getAccessToken.sh <authorization_code>
output: >-
  { "access_token": "d3ac3bb53d1c4ebc3de7d28e4ed801c0", "token_type": "bearer",
  "scope": "public private", "user": { "uri": "/users/39285903", ... } }
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.906Z'
platforms:
  - Web
tags:
  - oauth2
  - token-exchange
verified: false
validated: true
submitted: true
---

# exchange-oauth-code-for-token

## Command

```bash
./getAccessToken.sh <authorization_code>
```

## Description

Executes the getAccessToken.sh script to exchange an OAuth2 authorization code for an access token via Vimeo's API, useful for initial access or bypass testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <authorization_code> | The code to exchange (e.g., e1fa87cd449ae55b74445b31ac79450c14eeb657) | Yes |

## Examples

### Basic Usage

```bash
./getAccessToken.sh e1fa87cd449ae55b74445b31ac79450c14eeb657
```

### Advanced Usage

```bash
./getAccessToken.sh 82e24f835184f47cd83f249907e7bd5018bf62c9
```

## Expected Output

JSON response with access_token, token_type, scope, and user details on success.

## Related

- [[commands/verify-access-token]]
