---
data: >-
  curl -X POST https://api.instacart.com/oauth/token -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "grant_type=client_credentials&client_id=CLIENT_ID&client_secret=PRIVATE_KEY"
tags:
  - api
  - oauth
  - auth
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.222Z'
id: 1b28671e-b0e8-4439-b50e-9c60eca592cb
verified: false
validated: true
submitted: true
---
# curl-oauth-auth

## Command

```bash
curl -X POST https://api.instacart.com/oauth/token -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=client_credentials&client_id=CLIENT_ID&client_secret=PRIVATE_KEY"
```

## Description

Sends an OAuth client credentials request to Instacart's API using an extracted private key to obtain an access token for unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H` | Header for content type | Yes |
| `-d` | POST data with grant type, client ID, and secret | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.instacart.com/oauth/token -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=client_credentials&client_id=extracted_id&client_secret=extracted_key"
```

### Advanced Usage

```bash
curl -X POST https://api.instacart.com/oauth/token -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=client_credentials&client_id=ID&client_secret=KEY" -v
```

## Expected Output

JSON like {"access_token": "token_value", "token_type": "Bearer", "expires_in": 3600}.

## Related

- [[Related Procedure|procedures/Authenticate-to-Instacart-API-Using-Extracted-OAuth-Key]]
