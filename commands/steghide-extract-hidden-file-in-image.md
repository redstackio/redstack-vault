---
id: 9ebf17c1-858d-4ddc-8f97-4c48229f2000
name: steghide-extract-hidden-file-in-image
type: command
executor: bash
data: steghide extract -sf $_IMAGE_FILE
output: |-
  root@kali:~# steghide extract -sf wallpaper.jpg 
  Enter passphrase: secret
  wrote extracted data to "credentials.txt".
created_at: '2019-10-10T00:34:20.345057+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - steganography
  - extract
verified: true
validated: true
---

# steghide-extract-hidden-file-in-image

## Command

```bash
steghide extract -sf $_IMAGE_FILE
```

## Description

Extracts hidden data from stego image with passphrase.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| extract | Extraction mode | Yes |
| -sf | Specify cover file | Yes |
| $_IMAGE_FILE | Path to image (e.g., wallpaper.jpg) | Yes |

## Examples

### Extract with Passphrase

```bash
steghide extract -sf image.jpg
```

## Expected Output

Prompt for passphrase, then 'wrote extracted data to "file.txt"'.

## Related

- [[procedures/extract-hidden-file-from-image-with-steghide]]
