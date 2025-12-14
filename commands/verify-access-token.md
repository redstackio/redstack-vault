---
id: 123e4567-e89b-12d3-a456-426614174007
name: verify-access-token
type: command
executor: bash
data: ./me.sh <access_token>
output: 'HTTP/1.1 200 OK ... { "uri": "/users/39285903", ... } or 401 Unauthorized'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.892Z'
platforms:
  - Web
tags:
  - oauth2
  - verification
verified: false
validated: true
submitted: true
---

# verify-access-token

## Command

```bash
./me.sh <access_token>
```

## Description

Runs the me.sh script to test an access token by querying Vimeo's /me endpoint, confirming validity or revocation status.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <access_token> | Bearer token to verify (e.g., d3ac3bb53d1c4ebc3de7d28e4ed801c0) | Yes |

## Examples

### Basic Usage

```bash
./me.sh d3ac3bb53d1c4ebc3de7d28e4ed801c0
```

### Advanced Usage

```bash
./me.sh 9eabdc746910ea39c07395ee1b69a2b9
```

## Expected Output

200 OK with user JSON on valid token; 401 with error on invalid/revoked.

## Related

- [[commands/exchange-oauth-code-for-token]]
