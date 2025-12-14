---
data: >-
  curl -X GET
  'https://target.weblate.org/accounts/complete/email/?verification_code=51554eb9e31b44d6a48f8b41acda9a43&id=uy7kg0n6l8nhmihjvcgwzg3dpama80gn&type=reset'
  -H 'Cookie: sessionid=your_session_cookie'
tags:
  - web
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.293Z'
id: 316a0fd0-3038-4b2d-b9b2-a8f81d17d064
verified: false
validated: true
submitted: true
---
# curl-verify-weblate-email

## Command

```bash
curl -X GET 'https://target.weblate.org/accounts/complete/email/?verification_code=51554eb9e31b44d6a48f8b41acda9a43&id=uy7kg0n6l8nhmihjvcgwzg3dpama80gn&type=reset' \
  -H 'Cookie: sessionid=your_session_cookie'
```

## Description

This command verifies an email addition in Weblate by accessing the verification URL with session cookie, enabling the email for further use.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | GET method | Yes |
| URL params | verification_code, id, type from email link | Yes |
| `-H 'Cookie: ...'` | Maintains session | Yes |

## Examples

### Basic Usage

```bash
curl -X GET 'https://weblate.example.com/accounts/complete/email/?verification_code=abc123&id=def456&type=reset' -H 'Cookie: sessionid=abc123'
```

### Advanced Usage

With follow redirects `-L`:

```bash
curl -L -X GET 'https://weblate.example.com/accounts/complete/email/?verification_code=abc123&id=def456&type=reset' -H 'Cookie: sessionid=abc123'
```

## Expected Output

HTML page confirming "Email verified" or redirect to profile.

## Related

- [[Related Procedure: Verify-New-Email-in-Weblate]]
