---
data: >-
  curl -L "https://larksuite.com/?back_uri=https://evil.com" -o /dev/null -w
  "%{http_code} %{url_effective}\n"
tags:
  - web-testing
  - redirect
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:39.519Z'
id: 3d9beb39-2cd1-4fa4-9120-f0c273e04523
verified: false
validated: true
submitted: true
---
# curl-test-back_uri-redirect

## Command

```bash
curl -L "https://larksuite.com/?back_uri=https://evil.com" -o /dev/null -w "%{http_code} %{url_effective}\n"
```

## Description

This command tests for open redirects by following the location header and printing the HTTP status and final URL. Use it to verify if the back_uri parameter allows arbitrary redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow redirects | Yes |
| `--back_uri` | URL parameter value (e.g., https://evil.com) | Yes |
| `-o /dev/null` | Discard body output | No |
| `-w` | Custom output format for status and URL | Yes |

## Examples

### Basic Usage

```bash
curl -L "https://larksuite.com/?back_uri=https://example.com" -o /dev/null -w "%{http_code} %{url_effective}\n"
```

### Advanced Usage

```bash
curl -L -v "https://larksuite.com/?back_uri=https://evil.com" -o response.html -w "%{http_code} %{url_effective}\n"
```

## Expected Output

302 https://evil.com

Indicates a successful redirect to the specified URL.

## Related

- [[Related Procedure: Exploit-Open-Redirect-in-back_uri]]
