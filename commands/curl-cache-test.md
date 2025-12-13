---
data: 'curl -I "https://target.algolia.com/dynamic-page/fake.css"'
tags:
  - web
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: b24c3a1b-0da4-4b66-a1d5-e84eeb2aa865
created_at: '2025-12-13T09:00:34.258Z'
updated_at: '2025-12-13T09:00:34.258Z'
verified: false
validated: true
submitted: true
---
# Curl Cache Test

## Command

```bash
curl -I "https://target.algolia.com/dynamic-page/fake.css"
```

## Description

This command tests caching behavior by sending a HEAD request to a manipulated URL, checking headers for cache indicators like Age or Cache-Control.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only | Yes |
| `url` | Target URL with fake extension | Yes |

## Examples

### Basic Usage

```bash
curl -I "https://target.com/page/fake.css"
```

### Advanced Usage

```bash
curl -I -H "User-Agent: Test" "https://target.com/page/fake.css"
```

## Expected Output

HTTP headers including caching details, e.g., 'HTTP/1.1 200 OK\nCache-Control: public, max-age=3600\nAge: 120'.

## Related
- [[procedures/Identify-Vulnerable-Endpoint-for-Cache-Deception]]
- [[procedures/Verify-and-Execute-Reflected-XSS]]
