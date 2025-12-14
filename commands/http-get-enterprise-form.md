---
id: cmd-uuid-001
data: >-
  GET /enterprise/ HTTP/1.1

  Host: try.crashlytics.com

  Accept: */*

  Cookie: PHPSESSID=m021o0dkf7er0ub7d3541dvg43

  Pragma: no-cache

  Referer: http://try.crashlytics.com/enterprise/

  Connection: Keep-alive

  User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,
  like Gecko) Chrome/28.0.1500.63 Safari/537.36

  Cache-Control: no-cache

  Accept-Encoding: gzip,deflate

  Acunetix-Aspect: enabled

  Acunetix-Aspect-Queries: filelist;aspectalerts

  Acunetix-Aspect-Password: 082119f75623eb7abd7bf357698ff66c
tags:
  - http
  - scanning
  - csrf
type: command
output: |-
  HTTP/1.1 200 OK
  Content-Type: text/html
  Server: Apache
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:03.136Z'
verified: false
validated: true
submitted: true
---
# HTTP GET Request to Enterprise Form

## Command

```http
GET /enterprise/ HTTP/1.1
Host: try.crashlytics.com
Accept: */*
Cookie: PHPSESSID=m021o0dkf7er0ub7d3541dvg43
Pragma: no-cache
Referer: http://try.crashlytics.com/enterprise/
Connection: Keep-alive
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36
Cache-Control: no-cache
Accept-Encoding: gzip,deflate
Acunetix-Aspect: enabled
Acunetix-Aspect-Queries: filelist;aspectalerts
Acunetix-Aspect-Password: 082119f75623eb7abd7bf357698ff66c
```

## Description

This HTTP GET request accesses the enterprise contact form endpoint during a vulnerability scan, demonstrating the form's exposure and lack of CSRF protection. It is used to retrieve and analyze the HTML form structure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Host | Target domain | Yes |
| Accept | Accepted content types | Yes |
| Cookie | Session identifier (PHPSESSID) | Yes for authenticated scans |
| Referer | Origin of the request | No |
| User-Agent | Browser simulation | Yes |
| Acunetix-Aspect | Enables Acunetix scanning features | Yes for tool integration |
| Acunetix-Aspect-Password | Authentication for Aspect module | Yes |
| Acunetix-Aspect-Queries | Queries to execute during scan | Yes |

## Examples

### Basic Usage

Send the request using curl to simulate:

```bash
curl -X GET "http://try.crashlytics.com/enterprise/" -H "Host: try.crashlytics.com" -H "Accept: */*" -H "Cookie: PHPSESSID=m021o0dkf7er0ub7d3541dvg43" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36"
```

### Advanced Usage

Include full Acunetix headers for integrated scanning:

```bash
curl -X GET "http://try.crashlytics.com/enterprise/" -H "Acunetix-Aspect: enabled" -H "Acunetix-Aspect-Password: 082119f75623eb7abd7bf357698ff66c" -H "Acunetix-Aspect-Queries: filelist;aspectalerts"
```

## Expected Output

HTTP/1.1 200 OK response with Content-Type: text/html and Server: Apache, returning the HTML page containing the vulnerable form.

## Related

- [[procedures/Discover-CSRF-in-Web-Forms-Using-Automated-Scanner]]
