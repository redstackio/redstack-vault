---
id: cmd-access-file
data: >-
  curl -u "admin:password"
  "https://target.com/wp-content/uploads/malicious.html"
tags:
  - access
  - xss
  - wordpress
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:14.183Z'
verified: false
validated: true
submitted: true
---
# access-uploaded-file

## Command

```bash
curl -u "admin:password" "https://target.com/wp-content/uploads/malicious.html"
```

## Description

Fetches an uploaded HTML file from WordPress media library to trigger or verify XSS payload execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Auth credentials if protected | No |
| URL | Direct file path | Yes |

## Examples

### Basic Usage

```bash
curl "https://site.com/wp-content/uploads/file.html"
```

### Advanced Usage

```bash
curl -u "user:pass" "https://site.com/wp-content/uploads/file.html" --cookie "wp_session=abc"
```

## Expected Output

Raw HTML content with script; in browser, executes JS.

## Related

- [[commands/upload-image-via-woocommerce-api]]
