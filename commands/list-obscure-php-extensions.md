---
id: 78499e2d-98c8-408b-a305-5938228d3f67
name: list-obscure-php-extensions
type: command
executor: bash
data: |-
  .pht
  .phps
  .phar
  .phpt
  .pgif
  .phtml
  .phtm
  .inc
output: null
created_at: '2023-04-06T03:56:41.023862+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - file-upload
  - php
  - bypass
verified: true
validated: true
---

# list-obscure-php-extensions

## Command

```bash
echo ".pht
.phps
.phar
.phpt
.pgif
.phtml
.phtm
.inc"
```

## Description

This command outputs a list of obscure PHP file extensions that may bypass upload filters while still being executable on PHP servers. Ideal for advanced extension bypass in insecure file upload exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Simple echo command; no parameters needed | No |

## Examples

### Basic Usage

```bash
echo ".pht
.phps
.phar
.phpt
.pgif
.phtml
.phtm
.inc"
```

### Advanced Usage

Save to variable for scripting:

```bash
EXTS=$(echo ".pht
.phps
.phar
.phpt
.pgif
.phtml
.phtm
.inc")
```

## Expected Output

.pht
.phps
.phar
.phpt
.pgif
.phtml
.phtm
.inc

## Related

- [[procedures/Exploit-Insecure-File-Upload-with-Extension-Bypass]]
