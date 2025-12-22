---
data: php rst.php
tags:
  - php
  - lfi
  - parsing
type: command
output: >-
  <p><em>Test</em></p><p>##\n# Host Database\n#\n# localhost is used to
  configure the loopback interface\n# when the system is booting. Do not change
  this
  entry.\n##\n127.0.0.1\tlocalhost\n255.255.255.255\tbroadcasthost\n::1\tlocalhost
  </p>\n[...]
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.095Z'
id: 455d0130-c377-4d0e-b482-274769455983
verified: false
validated: true
submitted: true
---
# php-rst-parse

## Command

```bash
php rst.php
```

## Description

Executes a PHP script (rst.php) that parses malicious RST content using the Gregwar/RST library, demonstrating LFI by including and rendering the contents of /etc/hosts in HTML output. Use this in a local PHP environment to test RST-based vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `rst.php` | PHP file with RST parser code and malicious content | Yes |

## Examples

### Basic Usage

```bash
php rst.php
```

### Advanced Usage

```bash
php -f rst.php > output.html
```

> Redirects output to a file for inspection.

## Expected Output

HTML embedding the target file: <p><em>Test</em></p><p>##\n# Host Database... 127.0.0.1\tlocalhost</p>, confirming successful LFI.

## Related

- [[Related Procedure: Execute-PHP-Script-to-Parse-RST-and-Disclose-Files]]
