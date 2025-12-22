---
data: >-
  OPTIONS /user/check_email HTTP/1.1

  Host: localhost

  User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101
  Firefox/61.0

  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

  Accept-Language: en-GB,en;q=0.5

  Accept-Encoding: gzip, deflate

  Access-Control-Request-Method: POST

  Access-Control-Request-Headers: x-csrf-token,x-smulen

  Origin: https://www.smule.com

  Connection: close
tags:
  - http
  - cors
type: command
executor: bash
platforms:
  - Web
id: 30989e92-2adf-4cee-9647-3192912f1935
created_at: '2025-12-13T09:00:34.284Z'
updated_at: '2025-12-13T09:00:34.284Z'
verified: false
validated: true
submitted: true
---
# OPTIONS Check Email

## Command

```bash
OPTIONS /user/check_email HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Access-Control-Request-Method: POST
Access-Control-Request-Headers: x-csrf-token,x-smulen
Origin: https://www.smule.com
Connection: close
```

## Description

This preflight OPTIONS request checks CORS permissions before a POST to /user/check_email, triggered in poisoned login scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Access-Control-Request-Method` | Method to request (POST) | Yes |
| `Access-Control-Request-Headers` | Headers to allow (x-csrf-token,x-smulen) | Yes |

## Examples

### Basic Usage

```bash
OPTIONS /user/check_email HTTP/1.1
Host: localhost
Access-Control-Request-Method: POST
```

### Advanced Usage

```bash
OPTIONS /user/check_email HTTP/1.1
Host: attacker.com
Access-Control-Request-Headers: x-csrf-token,x-smulen
Origin: https://www.smule.com
```

## Expected Output

CORS headers allowing the subsequent POST request.

## Related

- [[procedures/Trigger-Login-on-Poisoned-Page-to-Disclose-CSRF-Token]]
