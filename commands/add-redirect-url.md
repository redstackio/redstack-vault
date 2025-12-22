---
id: f0c085bc-6765-4788-bd82-c0cb876b2435
name: add-redirect-url
type: command
executor: bash
data: curl -X GET "$_TARGET_URL?redirectUrl=$_MALICIOUS_URL" -L -v
output: null
created_at: '2023-04-06T03:56:31.693189+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - exploit
  - web
verified: true
validated: true
---

# add-redirect-url

## Command

```bash
curl -X GET "$_TARGET_URL?redirectUrl=$_MALICIOUS_URL" -L -v
```

## Description

Tests a direct URL with a malicious redirect parameter to confirm open redirection. Follows the redirect to verify it lands on the attacker's site.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Vulnerable endpoint URL | Yes |
| $_MALICIOUS_URL | Attacker-controlled URL (e.g., https://evil-website.tld/phish) | Yes |
| -L | Follow redirects | Yes |
| -v | Verbose mode | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://famous-website.tld?redirectUrl=https://evil-website.tld" -L -v
```

## Expected Output

Redirect chain ending at the malicious URL, with 302 status codes.

## Related

- [[procedures/Open-URL-Redirection-Exploitation]]
- [[commands/access-signup-page]]
