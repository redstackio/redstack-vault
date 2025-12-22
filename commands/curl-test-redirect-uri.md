---
data: >-
  curl -X GET
  "https://idp.login.gov/oauth/authorize?client_id=TEST_CLIENT&redirect_uri=https://agency.gov.example.com/malicious&response_type=code&scope=openid"
  -v
tags:
  - bypass
  - http
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.951Z'
id: 5741e152-9039-4ad1-9d34-72a5a1d8e00e
verified: false
validated: true
submitted: true
---
# curl-test-redirect-uri

## Command

```bash
curl -X GET "https://idp.login.gov/oauth/authorize?client_id=TEST_CLIENT&redirect_uri=https://agency.gov.example.com/malicious&response_type=code&scope=openid" -v
```

## Description

Tests a crafted redirect_uri for validation bypass by sending it to the authorize endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| `redirect_uri` | Malicious URI to test | Yes |
| `-v` | Verbose | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://idp.login.gov/oauth/authorize?client_id=TEST_CLIENT&redirect_uri=https://agency.gov.example.com/malicious&response_type=code&scope=openid" -v
```

### Advanced Usage

```bash
curl -X GET "https://idp.login.gov/oauth/authorize?..." -v -L
```

## Expected Output

No error if bypass succeeds; 302 or auth prompt.

## Related

- [[Related Procedure]]
