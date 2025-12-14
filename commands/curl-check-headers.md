---
id: cmd-curl-check-headers
data: curl -I $URL
tags:
  - recon
  - web
  - headers
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.825Z'
verified: false
validated: true
submitted: true
---
# curl-check-headers

## Command

```bash
curl -I $URL
```

## Description

This command uses curl to perform a HEAD request on a target URL, retrieving HTTP response headers to inspect security configurations like X-Frame-Options for Clickjacking vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only (HEAD method) | Yes |
| `$URL` | Target URL to check (e.g., https://ylands.com/) | Yes |

## Examples

### Basic Usage

```bash
curl -I https://ylands.com/
```

### Advanced Usage

```bash
curl -I https://ylands.com/ | grep -i frame
```

> Filters output for frame-related headers.

## Expected Output

Description of what output to expect when the command runs successfully.

HTTP/2 200 
server: nginx
... (no X-Frame-Options line indicates vulnerability)

## Related

- [[Related Procedure|procedures/Identify-Clickjacking-Vulnerability]]
