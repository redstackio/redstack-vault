---
data: >-
  curl -X POST https://api.paypal.com/v1/oauth2/token -H "Accept:
  application/json" -H "Accept-Language: en_US" -u "client_id:client_secret" -d
  "grant_type=client_credentials"
tags:
  - authentication
  - api
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 21285ab6-0fdd-49ac-9d23-336117f5fd92
created_at: '2025-12-11T06:10:30.307Z'
updated_at: '2025-12-11T06:10:30.307Z'
verified: false
validated: true
submitted: true
---
# curl-authenticate-paypal

## Command

```bash
curl -X POST https://api.paypal.com/v1/oauth2/token \
  -H "Accept: application/json" \
  -H "Accept-Language: en_US" \
  -u "client_id:client_secret" \
  -d "grant_type=client_credentials"
```

## Description

Authenticates to PayPal API using client credentials to obtain a bearer token for API access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u "client_id:client_secret"` | Client credentials | Yes |
| `-d "grant_type=client_credentials"` | Grant type | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.paypal.com/v1/oauth2/token -H "Accept: application/json" -H "Accept-Language: en_US" -u "client_id:client_secret" -d "grant_type=client_credentials"
```

## Expected Output

JSON response with access_token, token_type, and expires_in.

## Related
- [[procedures/Authenticate-to-PayPal-Business-API]]
