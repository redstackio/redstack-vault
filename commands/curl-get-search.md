---
id: cmd-001
data: 'curl -X GET "https://target.com/search/node/test"'
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.105Z'
verified: false
validated: true
submitted: true
---
# curl-get-search

## Command

```bash
curl -X GET "https://target.com/search/node/test"
```

## Description

Fetches the search endpoint with a test query to inspect for reflection points in the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| URL | Target search endpoint with query | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/search/node/test"
```

### Advanced Usage

```bash
curl -X GET "https://target.com/search/node/test" | grep internalPath
```

## Expected Output

HTML response containing the search page, potentially with reflected input in JavaScript variables.

## Related

- [[Related Procedure]]
