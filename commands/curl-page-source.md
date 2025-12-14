---
id: cmd-curl-page-source
data: 'curl -s https://target.com | grep -i ''generator.*wordpress'''
tags:
  - recon
  - http
type: command
output: <meta name="generator" content="WordPress 4.6.2" />
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.942Z'
verified: false
validated: true
submitted: true
---
# curl-page-source

## Command

```bash
curl -s https://target.com | grep -i 'generator.*wordpress'
```

## Description

Retrieves the full page source silently and searches for WordPress generator meta tag to confirm version.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode (no progress) | Yes |
| `https://target.com` | Target URL | Yes |
| `grep -i 'generator.*wordpress'` | Case-insensitive search for generator tag | Yes |

## Examples

### Basic Usage

```bash
curl -s https://example.com | grep -i 'generator.*wordpress'
```

### Advanced Usage

```bash
curl -s -L https://target.com | grep -i 'generator'
```

## Expected Output

Meta tag like <meta name="generator" content="WordPress 4.6.2" />.

## Related

- [[Related Procedure: Reconnaissance-of-WordPress-Version]]
