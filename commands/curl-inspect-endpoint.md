---
data: >-
  curl -X GET
  "https://idp.login.gov/oauth/authorize?client_id=TEST_CLIENT&redirect_uri=https://agency.gov/callback&response_type=code&scope=openid"
  -v
tags:
  - recon
  - http
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.953Z'
id: 0b9479f1-3465-421b-a879-08e2c0558964
verified: false
validated: true
submitted: true
---
# curl-inspect-endpoint

## Command

```bash
curl -X GET "https://idp.login.gov/oauth/authorize?client_id=TEST_CLIENT&redirect_uri=https://agency.gov/callback&response_type=code&scope=openid" -v
```

## Description

Inspects the OpenID Connect authorize endpoint by sending a GET request with parameters to observe validation and response behavior.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| `client_id` | OAuth client ID | Yes |
| `redirect_uri` | Callback URL to test | Yes |
| `response_type` | Type of response (code) | Yes |
| `scope` | Requested scopes | Yes |
| `-v` | Verbose output | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://idp.login.gov/oauth/authorize?client_id=TEST_CLIENT&redirect_uri=https://agency.gov/callback&response_type=code&scope=openid" -v
```

### Advanced Usage

```bash
curl -X GET "https://idp.login.gov/oauth/authorize?..." -v -H "User-Agent: Mozilla/5.0"
```

## Expected Output

Verbose HTTP exchange showing status codes, headers, and any redirects or errors indicating validation results.

## Related

- [[Related Procedure]]
