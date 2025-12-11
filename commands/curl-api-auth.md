---
data: >-
  curl -X POST 'https://api.paypal.com/v1/oauth2/token' -H 'Authorization: Basic
  <client_id:client_secret>' -d 'grant_type=client_credentials'
tags:
  - api
  - authentication
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 4b05b3bc-413d-4ff5-bf44-757d85da8985
created_at: '2025-12-11T03:47:39.693Z'
updated_at: '2025-12-11T03:47:39.693Z'
verified: false
validated: true
submitted: true
---
# curl-api-auth

## Command

```bash
curl -X POST 'https://api.paypal.com/v1/oauth2/token' \
  -H 'Authorization: Basic <client_id:client_secret>' \
  -d 'grant_type=client_credentials'
```

## Description

This command authenticates to the PayPal API using client credentials to obtain an OAuth bearer token for subsequent requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H 'Authorization: Basic <creds>'` | Basic auth with client ID and secret | Yes |
| `-d 'grant_type=client_credentials'` | Grant type for token request | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.paypal.com/v1/oauth2/token' \
  -H 'Authorization: Basic ABC123:XYZ789' \
  -d 'grant_type=client_credentials'
```

## Expected Output

JSON response containing 'access_token' and other token details if successful.

## Related

- [[commands/curl-idor-exploit]]
- [[procedures/Authenticate-to-PayPal-Business-API]]
