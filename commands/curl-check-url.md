---
data: 'curl -I https://screenhero.uservoice.com'
tags:
  - http
  - probe
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.578Z'
id: 66424a05-dcad-486b-92ef-b6772ed04528
verified: false
validated: true
submitted: true
---
# curl-check-url

## Command

```bash
curl -I https://screenhero.uservoice.com
```

## Description

This command performs a HEAD request to check the HTTP status of a URL, helping verify if a service is active or inactive for takeover assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -I | Use HEAD method only | Yes |
| https://screenhero.uservoice.com | Target URL to probe | Yes |

## Examples

### Basic Usage

```bash
curl -I https://screenhero.uservoice.com
```

### Advanced Usage

```bash
curl -I -L https://screenhero.uservoice.com
```

## Expected Output

HTTP headers with status like "HTTP/1.1 404 Not Found", confirming inactivity.

## Related

- [[Related Procedure]]
