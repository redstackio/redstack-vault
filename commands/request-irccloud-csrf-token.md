---
data: >-
  curl -X POST https://www.irccloud.com/chat/auth-formtoken -H "Content-Type:
  application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With:
  XMLHttpRequest" -H "Referer: https://www.irccloud.com/" -d "_reqid=1"
tags:
  - csrf
  - web-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:29.972Z'
id: fdf9556a-cafb-40a0-a859-0e6564ec8ff8
verified: false
validated: true
submitted: true
---
# request-irccloud-csrf-token

## Command

```bash
curl -X POST https://www.irccloud.com/chat/auth-formtoken \
  -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Referer: https://www.irccloud.com/" \
  -d "_reqid=1"
```

## Description

This command sends an anonymous POST request to IRCCloud's CSRF token endpoint to obtain a valid token for login form protection, exploitable in CSRF attacks due to lack of authentication checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: ..."` | Sets form-encoded content type | Yes |
| `-H "X-Requested-With: ..."` | Mimics AJAX request | Yes |
| `-H "Referer: ..."` | Fakes origin referer | Yes |
| `-d "_reqid=1"` | Request identifier body | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.irccloud.com/chat/auth-formtoken -H "Content-Type: application/x-www-form-urlencoded" -d "_reqid=1"
```

### Advanced Usage

```bash
curl -s -X POST https://www.irccloud.com/chat/auth-formtoken -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "User-Agent: Mozilla/5.0" -d "_reqid=1" | jq '.token'
```

## Expected Output

JSON response like {"token": "1397481736.3b1f59ae47e1a139e8a631b2589dfae2"}, indicating successful token issuance without errors.

## Related

- [[Related Procedure: Obtain-Anonymous-CSRF-Token-from-IRCCloud]]
