---
data: 'curl -i "https://www.ibm.com/''"'
tags:
  - http
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.329Z'
id: b8ff102a-4541-4b9c-aaa9-846b556fd296
verified: false
validated: true
submitted: true
---
# curl-send-request

## Command

```bash
curl -i "https://www.ibm.com/'"
```

## Description

Sends an HTTP GET request to a target URL with an injected payload to test for SQL injection, using -i to include headers in output for status code analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers | Yes |
| URL | Target URL with payload | Yes |

## Examples

### Basic Usage

```bash
curl -i "https://www.ibm.com/"
```

### Advanced Usage

```bash
curl -i -L --max-redirs 1 "https://www.ibm.com/'AND1=1--"
```

## Expected Output

HTTP/1.1 500 Internal Server Error for failed injections, or 302 redirect for successes, followed by headers and body.

## Related

- [[Related Procedure]]
