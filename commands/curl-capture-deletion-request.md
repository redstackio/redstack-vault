---
data: >-
  curl -X POST https://gitlab.com/users -H "Cookie:
  _gitlab_session=1staccount_cookie;" -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "_method=delete&authenticity_token=auth_1staccount"
tags:
  - csrf
  - http-post
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:27:29.415Z'
id: e0c2bdfa-d33e-4f15-b6f5-8cfd0f828bc3
verified: false
validated: true
submitted: true
---
# curl-capture-deletion-request

## Command

```bash
curl -X POST https://gitlab.com/users -H "Cookie: _gitlab_session=1staccount_cookie;" -H "Content-Type: application/x-www-form-urlencoded" -d "_method=delete&authenticity_token=auth_1staccount"
```

## Description

This curl command simulates the POST request for GitLab account deletion, used to capture or test the authenticity_token in a proxy like Burp Suite.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Cookie: ..."` | Sets the session cookie for authentication | Yes |
| `-H "Content-Type: ..."` | Sets form-encoded content type | Yes |
| `-d "_method=delete&authenticity_token=..."` | Payload with delete method and CSRF token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://gitlab.com/users -H "Cookie: _gitlab_session=1staccount_cookie;" -H "Content-Type: application/x-www-form-urlencoded" -d "_method=delete&authenticity_token=auth_1staccount"
```

### Advanced Usage

Add referer and user-agent for realism:

```bash
curl -X POST https://gitlab.com/users -H "Referer: https://gitlab.com/profile/account" -H "Cookie: _gitlab_session=1staccount_cookie;" -H "Content-Type: application/x-www-form-urlencoded" -d "_method=delete&authenticity_token=auth_1staccount"
```

## Expected Output

HTTP 200 or redirect indicating deletion success, or error if token invalid. Used primarily for interception.

## Related

- [[commands/curl-modified-deletion-request]]
- [[procedures/Capture-Account-Deletion-Request-Using-Burp-Suite]]
