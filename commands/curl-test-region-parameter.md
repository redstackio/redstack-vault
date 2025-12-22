---
data: 'curl "https://example.tiktok.endpoint?region=test"'
tags:
  - recon
  - web
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 8e480fd1-f73d-43e2-a917-dce642015642
created_at: '2025-12-14T00:11:25.157Z'
updated_at: '2025-12-14T00:11:25.157Z'
verified: false
validated: true
submitted: true
---
# Curl Test Region Parameter

## Command

```bash
curl "https://example.tiktok.endpoint?region=test"
```

## Description

This command sends a GET request to a TikTok endpoint with a test value in the 'region' parameter to check for reflection, useful in identifying potential XSS vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | The target endpoint URL with region parameter | Yes |

## Examples

### Basic Usage

```bash
curl "https://example.tiktok.endpoint?region=test"
```

### Advanced Usage

```bash
curl -v "https://example.tiktok.endpoint?region=test" -o response.html
```

## Expected Output

HTTP response body showing the 'test' value reflected, indicating potential lack of sanitization.

## Related

- [[procedures/Identify-Vulnerable-TikTok-Endpoint]]
