---
id: cmd-phpinfo
data: phpinfo();
tags:
  - php
  - rce
  - recon
type: command
output: PHP configuration information displayed
executor: php
platforms:
  - Web
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.085Z'
verified: false
validated: true
submitted: true
---
# phpinfo-display

## Command

```php
phpinfo();
```

## Description

Displays detailed PHP configuration and environment information, used as a proof-of-concept to verify code execution in RCE scenarios like cookie injection exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; outputs all PHP info | No |

## Examples

### Basic Usage

```php
<?php phpinfo(); ?>
```

### Advanced Usage

Inject via Base64 in requests for remote execution.

## Expected Output

Comprehensive HTML page with PHP version, modules, variables, and server details.

## Related

- [[commands/curl-inject-php-cookie]]
- [[procedures/Exploit-Ivanti-EPM-CSA-Code-Injection-via-Cookies]]
