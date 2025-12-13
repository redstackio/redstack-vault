---
data: 'curl -I https://target.example.com/forms -A "Mozilla/5.0"'
tags:
  - recon
  - web
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 1cddcff9-2030-490f-899d-b11590ae0e98
created_at: '2025-12-13T09:00:27.611Z'
updated_at: '2025-12-13T09:00:27.611Z'
verified: false
validated: true
submitted: true
---
# curl-scan-for-aem-endpoint

## Command

```bash
curl -I https://target.example.com/forms -A "Mozilla/5.0"
```

## Description

This command uses curl to send a HEAD request to probe for AEM Forms endpoints, checking response headers for service indicators.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only | Yes |
| `-A` | Set User-Agent string | No |
| `url` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -I https://target.example.com/forms -A "Mozilla/5.0"
```

### Advanced Usage

```bash
curl -I -k https://target.example.com/forms -A "Custom Agent"
```

## Expected Output

HTTP headers including Server or other AEM indicators, e.g., 'HTTP/1.1 200 OK\nServer: Adobe Experience Manager'.

## Related
- [[procedures/Identify-Vulnerable-AEM-Forms-Instance]]
- [[tools/Curl]]
