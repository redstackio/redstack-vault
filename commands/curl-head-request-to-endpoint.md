---
id: cmd-uuid-1234-5678
data: 'curl -I https://gopher.hey.com/metrics'
tags:
  - recon
  - http
  - probe
type: command
output: |-
  HTTP/1.1 200 OK
  Server: nginx
  Content-Type: text/plain
  ...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.348Z'
verified: false
validated: true
submitted: true
---
# curl-head-request-to-endpoint

## Command

```bash
curl -I https://gopher.hey.com/metrics
```

## Description

This command performs a HEAD request to probe an HTTP endpoint for accessibility and status without retrieving the full body, useful for initial reconnaissance of exposed directories like /metrics to detect information disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only (HEAD request instead of GET) | Yes |
| `https://gopher.hey.com/metrics` | Target URL to probe | Yes |

## Examples

### Basic Usage

```bash
curl -I https://gopher.hey.com/metrics
```

### Advanced Usage

```bash
curl -I -s -o /dev/null -w "%{http_code}\n" https://gopher.hey.com/metrics
```

> The `-s` silences progress, `-o /dev/null` discards output, and `-w` prints the HTTP code for scripting.

## Expected Output

Description of what output to expect when the command runs successfully: HTTP headers with a 200 OK status if the endpoint is exposed, e.g., "HTTP/1.1 200 OK\nServer: nginx\nContent-Type: text/plain", indicating no authentication barriers.

## Related

- [[Related Procedure: Enumerate-Subdomains-and-Access-Exposed-Metrics]]
