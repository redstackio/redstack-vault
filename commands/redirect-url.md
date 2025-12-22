---
id: 354ade09-eee6-40a4-a64b-6f0dea7f5824
name: redirect-url
type: command
executor: bash
data: curl -X GET "$_PHISHING_URL" -L -v
output: null
created_at: '2023-04-06T03:56:31.692614+00:00'
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

# redirect-url

## Command

```bash
curl -X GET "$_PHISHING_URL" -L -v
```

## Description

Tests the full crafted phishing URL that exploits the open redirect.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PHISHING_URL | Full URL with malicious redirect (e.g., https://famous-website.tld?redirectUrl=https://evil-website.tld) | Yes |
| -L | Follow redirects | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://famous-website.tld/signup?redirectUrl=https://evil-website.tld" -L -v
```

## Expected Output

< Location: https://evil-website.tld

## Related

- [[procedures/Open-URL-Redirection-Exploitation]]
- [[commands/add-redirect-url]]
