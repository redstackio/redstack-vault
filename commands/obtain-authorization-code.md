---
id: 123e4567-e89b-12d3-a456-426614174005
name: obtain-authorization-code
type: command
executor: bash
data: >-
  # Manual browser step; no executable command, but reference URL

  # Visit:
  https://api.vimeo.com/oauth/authorize?response_type=code&client_id=79658bbee0da8be5254a5137bc0fcc93f7059a2a&redirect_uri=https://avuln.com/callback&scope=public&state=0123456789abcdef

  # Extract code from callback
output: >-
  Callback URL with code parameter, e.g.,
  code=e1fa87cd449ae55b74445b31ac79450c14eeb657
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.908Z'
platforms:
  - Web
tags:
  - oauth2
verified: false
validated: true
submitted: true
---

# obtain-authorization-code

## Command

```bash
# Manual browser step; no executable command, but reference URL
# Visit: https://api.vimeo.com/oauth/authorize?response_type=code&client_id=79658bbee0da8be5254a5137bc0fcc93f7059a2a&redirect_uri=https://avuln.com/callback&scope=public&state=0123456789abcdef
# Extract code from callback
```

## Description

This command represents the manual process of initiating OAuth2 authorization in a browser to obtain and extract an authorization code from the redirect URI.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| client_id | Vimeo app client ID | Yes |
| redirect_uri | Callback URL for code | Yes |
| scope | Requested scopes (e.g., public) | Yes |
| state | CSRF protection string | Yes |

## Examples

### Basic Usage

```bash
# Browser visit the constructed URL and authorize
```

### Advanced Usage

```bash
# For scripting, use curl to simulate but interactive login required
curl "https://api.vimeo.com/oauth/authorize?..."
```

## Expected Output

Redirect to callback with query params including state and code, e.g., https://avuln.com/callback?state=0123456789abcdef&code=e1fa87cd449ae55b74445b31ac79450c14eeb657. Extract the code value.

## Related

- [[commands/exchange-oauth-code-for-token]]
