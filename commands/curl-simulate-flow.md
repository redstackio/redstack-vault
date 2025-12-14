---
data: >-
  curl -X GET
  "https://idp.login.gov/oauth/authorize?client_id=CLIENT_ID&redirect_uri=https://agency.gov.example.com/malicious&response_type=code&scope=openid&state=STATE"
  -L -v
tags:
  - simulation
  - http
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.948Z'
id: eec31ec0-a054-4909-969a-e825600cd362
verified: false
validated: true
submitted: true
---
# curl-simulate-flow

## Command

```bash
curl -X GET "https://idp.login.gov/oauth/authorize?client_id=CLIENT_ID&redirect_uri=https://agency.gov.example.com/malicious&response_type=code&scope=openid&state=STATE" -L -v
```

## Description

Simulates the authorization flow, following redirects to mimic user interaction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow redirects | Yes |
| `state` | CSRF protection param | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://idp.login.gov/oauth/authorize?..." -L -v
```

## Expected Output

Full redirect chain ending at malicious site.

## Related

- [[Related Procedure]]
