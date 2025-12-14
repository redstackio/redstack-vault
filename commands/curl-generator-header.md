---
id: cmd-curl-generator-header
data: 'curl -I https://target.com | grep -i generator'
tags:
  - recon
  - http
type: command
output: 'X-Generator: WordPress 4.6.2'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.944Z'
verified: false
validated: true
submitted: true
---
# curl-generator-header

## Command

```bash
curl -I https://target.com | grep -i generator
```

## Description

Fetches HTTP headers from the target site and filters for the X-Generator header to detect WordPress version during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Head request only (headers) | Yes |
| `https://target.com` | Target URL | Yes |
| `grep -i generator` | Filter for generator header | Yes |

## Examples

### Basic Usage

```bash
curl -I https://example.com | grep -i generator
```

### Advanced Usage

```bash
curl -I -H "User-Agent: Mozilla/5.0" https://target.com | grep -i generator
```

## Expected Output

Header line like "X-Generator: WordPress 4.6.2" indicating the CMS version.

## Related

- [[Related Procedure: Reconnaissance-of-WordPress-Version]]
