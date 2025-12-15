---
id: cmd-curl-redirect-test
data: 'curl -L -v "https://smartreports.mtncameroon.net//example.com/..;/css"'
tags:
  - web-testing
  - redirect-check
type: command
output: 'null'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:30.582Z'
verified: false
validated: true
submitted: true
---
# curl-follow-redirect

## Command

```bash
curl -L -v "https://smartreports.mtncameroon.net//example.com/..;/css"
```

## Description

This command uses curl to test for open redirection by accessing a malformed URL on the target site, following any redirects, and displaying verbose details to inspect the Location header and final destination.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow HTTP redirects | Yes |
| `-v` | Verbose output to show headers | Yes |
| URL | The malformed target URL | Yes |

## Examples

### Basic Usage

```bash
curl -L -v "https://smartreports.mtncameroon.net//example.com/..;/css"
```

### Advanced Usage

```bash
curl -L "https://smartreports.mtncameroon.net//example.com/..;/css" -o /dev/null -w "%{url_effective}\n"
```

## Expected Output

Verbose output including a 3xx status code and Location header like "Location: http://example.com", followed by the content or final URL if successful.

## Related

- [[Related Procedure|procedures/Trigger-Open-Redirect-via-Malformed-URL-Path]]
