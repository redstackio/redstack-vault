---
data: 'curl -I https://subdomain.kaspersky.com/sensitive-page.css'
tags:
  - recon
  - web
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: e412129a-7e59-4328-94a4-9edaf08f9cf5
created_at: '2025-12-13T09:00:34.039Z'
updated_at: '2025-12-13T09:00:34.039Z'
verified: false
validated: true
submitted: true
---
# curl-test-cache-behavior

## Command

```bash
curl -I https://subdomain.kaspersky.com/sensitive-page.css
```

## Description

This command tests the caching behavior of a web page by requesting headers only, checking for Cache-Control directives that might indicate vulnerability to Web Cache Deception.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only | Yes |
| `URL` | Target URL with cacheable extension | Yes |

## Examples

### Basic Usage

```bash
curl -I https://subdomain.kaspersky.com/sensitive-page.css
```

### Advanced Usage

```bash
curl -I -H 'User-Agent: Custom' https://subdomain.kaspersky.com/sensitive-page.css
```

## Expected Output

HTTP headers including Cache-Control; look for 'public' or missing 'no-cache' indicating vulnerability.

## Related

- [[commands/curl-retrieve-cached-page]]
- [[procedures/Identify-Vulnerable-Subdomains]]
