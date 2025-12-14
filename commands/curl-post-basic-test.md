---
id: cmd-curl-post-basic-001
data: >-
  curl -X POST https://iris.lystit.com/models/default/classification/color -H
  "Content-Type: application/json" -d '{"images":
  ["https://example.com/test-image.png"]}'
tags:
  - test
  - api
type: command
output: JSON classification response
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.473Z'
verified: false
validated: true
submitted: true
---
# curl-post-basic-test

## Command

```bash
curl -X POST https://iris.lystit.com/models/default/classification/color -H "Content-Type: application/json" -d '{"images": ["https://example.com/test-image.png"]}'
```

## Description

This command sends a basic POST request with a sample external URL to test server-side fetching and classification in the Lyst Iris API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON header | Yes |
| `-d '{...}'` | JSON payload with images array | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://iris.lystit.com/models/default/classification/color -H "Content-Type: application/json" -d '{"images": ["https://example.com/test-image.png"]}'
```

### Advanced Usage

```bash
curl -X POST -v https://iris.lystit.com/models/default/classification/color -H "Content-Type: application/json" -d '{"images": ["https://example.com/test-image.png"]}'
```

## Expected Output

JSON response with image classification data, verifying SSRF behavior.

## Related

- [[Related Procedure: Identify Vulnerable Image URL Endpoint in Lyst Iris]]
