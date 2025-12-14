---
data: >-
  curl
  "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=████:vwt2u5wngbk&siteBaseUrl=http://example.com"
tags:
  - api
  - recon
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:11.119Z'
id: 46f3188d-fbda-419e-8a07-c23cfcd11d20
verified: false
validated: true
submitted: true
---
# access-basic-api-endpoint

## Command

```bash
curl "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=████:vwt2u5wngbk&siteBaseUrl=http://example.com"
```

## Description

Sends a basic GET request to the Starbucks API search endpoint to verify accessibility and parameter handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| x-api-key | API authentication key | Yes |
| query | Search term (e.g., coffe) | Yes |
| partnerid | Partner identifier | Yes |
| siteBaseUrl | Base URL for site context | No |

## Examples

### Basic Usage

```bash
curl "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=yourkey&query=coffe&partnerid=yourid&siteBaseUrl=http://example.com"
```

### Advanced Usage

Add verbose output:

```bash
curl -v "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=yourkey&query=coffe&partnerid=yourid&siteBaseUrl=http://example.com"
```

## Expected Output

JSON response with search results, e.g., {"results": [...]}, indicating successful parameter processing.

## Related

- [[commands/inject-xss-payload-sitebaseurl]]
