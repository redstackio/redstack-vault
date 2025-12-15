---
id: cmd-uuid-001
data: 'curl -i "https://target.com/payload"'
tags:
  - http
  - testing
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.290Z'
verified: false
validated: true
submitted: true
---
# curl-http-request

## Command

```bash
curl -i "https://target.com/payload"
```

## Description

Sends an HTTP request to a target URL with verbose headers (-i) to test web responses, commonly used for injection payload delivery and response observation in web vulnerability testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers in output | Yes |
| URL | Target endpoint with payload | Yes |

## Examples

### Basic Usage

```bash
curl -i "https://www.ibm.com/'/path"
```

### Advanced Usage

```bash
curl -i --max-redirs 1 "https://www.ibm.com/'AND1=1--/path"
```

## Expected Output

HTTP status code, headers, and body; e.g., 500 Internal Server Error for failed injections or 302 redirects for successful ones.

## Related

- [[Related Procedure]]
