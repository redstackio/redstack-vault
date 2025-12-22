---
data: 'curl -i http://target/'
tags:
  - http
  - probe
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.925Z'
id: 98b2dbaf-ea89-4259-a2ed-fc84f9f18539
verified: false
validated: true
submitted: true
---
# curl-probe-http

## Command

```bash
curl -i http://target/
```

## Description

This command uses curl to perform an HTTP request with verbose header output (-i) to probe a target's accessibility, status code, and server headers, ideal for subdomain monitoring and vulnerability confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers in output | Yes |
| `http://target/` | The URL to probe (e.g., subdomain) | Yes |
| `-m 10` | Set maximum time in seconds (optional timeout) | No |
| `-k` | Ignore SSL certificate errors (for HTTPS) | No |
| `-I` | HEAD request only (headers without body) | No |

## Examples

### Basic Usage

```bash
curl -i http://mk.prd.vine.co/
```

### Advanced Usage

```bash
curl -i -m 10 -k https://mk.prd.vine.co/%00
```

## Expected Output

HTTP/1.1 426 Upgrade Required\nServer: awselb/2.0\n... (headers and body indicating response details).

## Related

- [[Related Procedure: Probe-Subdomain-Accessibility]]
