---
type: command
executor: bash
data: >-
  sudo sed -i 's/allow_url_include = Off/allow_url_include = On/g'
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

# enable-allow-url-include

## Command

```bash
sudo sed -i 's/allow_url_include = Off/allow_url_include = On/g' /etc/php/$_PHP_VERSION/apache2/php.ini && sudo systemctl restart apache2
```

## Description

Enables the allow_url_include directive in PHP to allow including remote files, critical for executing RFI payloads via SMB.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PHP_VERSION | PHP version directory (e.g., 8.1) | Yes |

## Examples

### Basic Usage

```bash
sudo sed -i 's/allow_url_include = Off/allow_url_include = On/g' /etc/php/8.1/apache2/php.ini && sudo systemctl restart apache2
```

### Advanced Usage

For CLI PHP: Edit /etc/php/8.1/cli/php.ini separately.

## Expected Output

No output; file modified in place.

Success: `php -i | grep allow_url_include` shows "allow_url_include => On".

## Related

- [[procedures/Remote-File-Inclusion-via-SMB]]
