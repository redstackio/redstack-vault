---
id: c1d2e3f4-g5h6-7891-defg-4567890123
data: >-
  curl -X GET
  "https://ads.tiktok.com/some-endpoint?redirect=https://example.com" -v
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-13T23:52:39.347Z'
verified: false
validated: true
submitted: true
---
# curl-redirect-test

## Command

```bash
curl -X GET "https://ads.tiktok.com/some-endpoint?redirect=https://example.com" -v
```

## Description

This command tests if the 'redirect' parameter is reflected in the response by sending a GET request to the TikTok Ads endpoint and enabling verbose output to inspect headers and body.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| `redirect=https://example.com` | Test URL in parameter | Yes |
| `-v` | Verbose mode for detailed output | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://ads.tiktok.com/some-endpoint?redirect=https://example.com" -v
```

### Advanced Usage

```bash
curl -X GET "https://ads.tiktok.com/some-endpoint?redirect=https://example.com" -v -H "User-Agent: Mozilla/5.0"
```

## Expected Output

Verbose HTTP response including the reflected 'https://example.com' in the body if vulnerable, e.g., <a href="https://example.com"> or direct text insertion.

## Related

- [[Related Procedure]]
