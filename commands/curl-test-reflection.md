---
id: cmd-002
data: 'curl -X GET "https://target.com/search/node/chron0x" | grep internalPath'
tags:
  - web
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.097Z'
verified: false
validated: true
submitted: true
---
# curl-test-reflection

## Command

```bash
curl -X GET "https://target.com/search/node/chron0x" | grep internalPath
```

## Description

Tests for input reflection by searching a benign term and grepping for the JavaScript variable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP GET method | Yes |
| URL | Endpoint with benign query | Yes |
| `grep internalPath` | Filters for reflection indicator | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/search/node/chron0x" | grep internalPath
```

### Advanced Usage

```bash
curl -v -X GET "https://target.com/search/node/chron0x" | grep -A5 internalPath
```

## Expected Output

var internalPath ='search/node/chron0x';

## Related

- [[Related Procedure]]
