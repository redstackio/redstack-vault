---
data: 'curl -I http://target.com -A "TestAgent"'
tags:
  - recon
  - http
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 86b9f73f-cd81-41f4-ad60-3f7b187cddb5
created_at: '2025-12-13T09:01:17.716Z'
updated_at: '2025-12-13T09:01:17.716Z'
verified: false
validated: true
submitted: true
---
# Scan for Node.js Version

## Command

```bash
curl -I http://target.com -A "TestAgent"
```

## Description

This command sends a HEAD request to probe the target's server headers for Node.js version information, useful in identifying vulnerable instances.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only | Yes |
| `-A` | Set user agent | No |
| `http://target.com` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -I http://example.com
```

### Advanced Usage

```bash
curl -I -A "CustomAgent" http://example.com
```

## Expected Output

HTTP headers including 'Server: Node.js/18.7.0' if vulnerable.

## Related

- [[procedures/Identify-Vulnerable-Nodejs-Instance]]
