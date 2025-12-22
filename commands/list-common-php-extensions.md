---
id: efb6bad3-d5c3-41f6-811d-5171289a1adf
name: list-common-php-extensions
type: command
executor: bash
data: |-
  .php
  .php3
  .php4
  .php5
  .php7
output: null
created_at: '2023-04-06T03:56:41.023806+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - file-upload
  - php
verified: true
validated: true
---

# list-common-php-extensions

## Command

```bash
echo ".php
.php3
.php4
.php5
.php7"
```

## Description

This command outputs a list of common PHP file extensions that can be used to name malicious upload files for exploitation. Use it to quickly reference standard extensions during testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Simple echo command; no parameters needed | No |

## Examples

### Basic Usage

```bash
echo ".php
.php3
.php4
.php5
.php7"
```

### Advanced Usage

Pipe to a file for scripting:

```bash
echo ".php
.php3
.php4
.php5
.php7" > php_ext.txt
```

## Expected Output

.php
.php3
.php4
.php5
.php7

## Related

- [[procedures/Exploit-Insecure-File-Upload-with-Extension-Bypass]]
