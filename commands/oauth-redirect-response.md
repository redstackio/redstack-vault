---
id: cmd-periscope-oauth-response
data: >-
  <!DOCTYPE html><html><head><meta http-equiv="refresh"
  content="0;https://twitter.com/oauth/authenticate?oauth_token=████████"></head></html>
tags:
  - oauth
  - redirect
type: command
output: Auto-redirect to Twitter OAuth
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.667Z'
verified: false
validated: true
submitted: true
---
# oauth-redirect-response

## Command

```html
<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0;https://twitter.com/oauth/authenticate?oauth_token=████████"></head></html>
```

## Description

HTML response from poisoned request, used to capture the OAuth authenticate URL via meta refresh tag.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| oauth_token | Temporary token in URL | Yes |

## Examples

### Basic Usage

Parse the content attribute for the full URL.

## Expected Output

Browser would auto-redirect, but manually extract URL.

## Related

- [[commands/poisoned-host-header-request]]
