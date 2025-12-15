---
id: cmd-curl-test-domain-redirect
data: 'curl -L -I "https://www.uber.com//google.com/cities"'
tags:
  - testing
  - redirect
type: command
output: |-
  HTTP/1.1 404 Not Found
  ...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.897Z'
verified: false
validated: true
submitted: true
---
# curl-test-domain-redirect

## Command

```bash
curl -L -I "https://www.uber.com//google.com/cities"
```

## Description

Tests a malformed URL on Uber.com with double slashes and a domain to check for 404 response indicating path handling issues.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow redirects | Yes |
| `-I` | Show headers only | Yes |
| URL | Malformed target URL | Yes |

## Examples

### Basic Usage

```bash
curl -L -I "https://www.uber.com//google.com/cities"
```

### Advanced Usage

```bash
curl -L -I -v "https://www.uber.com//google.com/cities"
```

## Expected Output

HTTP 404 Not Found from Uber, with no redirect to external domain.

## Related

- [[Related Procedure: Test-Double-Slash-Redirection]]
