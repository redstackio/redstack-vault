---
data: >-
  curl -I -L
  'https://hackerone.com/users//saml/sign_in?email=teste@snapchat.com&remember_me=true'
tags:
  - web
  - redirect-test
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: cf41edb9-8792-4dfd-9905-c4a2a72b26f9
created_at: '2025-12-13T09:01:26.450Z'
updated_at: '2025-12-13T09:01:26.450Z'
verified: false
validated: true
submitted: true
---
# curl-test-open-redirect

## Command

```bash
curl -I -L 'https://hackerone.com/users//saml/sign_in?email=teste@snapchat.com&remember_me=true'
```

## Description

This command uses curl to test an open redirection by fetching headers and following redirects, useful for verifying bypasses in web vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only | Yes |
| `-L` | Follow redirects | Yes |
| `URL` | The target URL to test | Yes |

## Examples

### Basic Usage

```bash
curl -I -L 'https://example.com/redirect'
```

### Advanced Usage

```bash
curl -I -L --max-redirs 10 'https://example.com/redirect'
```

## Expected Output

HTTP headers showing the redirection chain and final location, e.g., Location: https://external-site.com

## Related

- [[procedures/Insert-Crafted-Open-Redirect-URL]]
- [[procedures/Trigger-Redirection-via-Link-Click]]
