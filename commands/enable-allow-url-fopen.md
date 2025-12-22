---
type: command
executor: bash
data: >-
  sudo sed -i 's/allow_url_fopen = Off/allow_url_fopen = On/g'
  /etc/php/$_PHP_VERSION/apache2/php.ini && sudo systemctl restart apache2
output: null
platforms:
  - Linux
tags:
  - php
  - configuration
verified: true
validated: true
---

# enable-allow-url-fopen

## Command

```bash
sudo sed -i 's/allow_url_fopen = Off/allow_url_fopen = On/g' /etc/php/$_PHP_VERSION/apache2/php.ini && sudo systemctl restart apache2
```

## Description

Enables the allow_url_fopen directive in PHP to permit opening remote files via protocols like SMB, required for RFI exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PHP_VERSION | PHP version directory (e.g., 8.1) | Yes |

## Examples

### Basic Usage

```bash
sudo sed -i 's/allow_url_fopen = Off/allow_url_fopen = On/g' /etc/php/8.1/apache2/php.ini && sudo systemctl restart apache2
```

### Advanced Usage

For PHP-FPM: Replace apache2 with fpm and restart php8.1-fpm.

## Expected Output

No output; sed modifies file silently.

Success: `php -i | grep allow_url_fopen` shows "allow_url_fopen => On".

## Related

- [[procedures/Remote-File-Inclusion-via-SMB]]
