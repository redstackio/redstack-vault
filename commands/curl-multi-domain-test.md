---
id: cmd-curl-multi-domain-test
data: 'curl -L -I "https://www.uber.com//hackerone.com/rohk"'
tags:
  - verification
  - redirect
type: command
output: |-
  HTTP/1.1 301 Moved Permanently
  Location: https://hackerone.com/rohk
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.853Z'
verified: false
validated: true
submitted: true
---
# curl-multi-domain-test

## Command

```bash
curl -L -I "https://www.uber.com//hackerone.com/rohk"
```

## Description

Tests open redirect on Uber.com with various external domains to confirm consistency.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow redirects | Yes |
| `-I` | Headers | Yes |
| URL | Multi-domain variant | Yes |

## Examples

### Basic Usage

```bash
curl -L -I "https://www.uber.com//hackerone.com/rohk"
```

### Advanced Usage

Test Facebook: replace with //facebook.com/path

## Expected Output

Redirect to the external domain.

## Related

- [[Related Procedure: Verify-Redirect-on-Multiple-Domains]]
