---
id: 690bf7f1-9642-4acd-a53b-73a723020a7f
name: check-image-type-with-file
type: command
executor: bash
data: file $_FILE_PATH
output: null
created_at: '2023-04-06T03:56:40.894031+00:00'
updated_at: '2023-04-06T03:56:40.904731+00:00'
platforms:
  - linux
  - unix
tags:
  - validation
  - mime-type
verified: true
validated: true
---

# check-image-type-with-file

## Command

```bash
file $_FILE_PATH
```

## Description

This command uses the 'file' utility to determine the MIME type of a file based on its magic bytes, useful for verifying that a polyglot file is recognized as an image before upload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILE_PATH | Path to the file to analyze (e.g., ./htaccess.xbm) | Yes |

## Examples

### Basic Usage

```bash
file .htaccess
```

### Advanced Usage

```bash
file -b .htaccess  # Brief output without filename
```

## Expected Output

.htaccess: X Bitmap image data

or

.htaccess: Wireless Bitmap image data (WBMP)

If it shows 'ASCII text' or similar, the polyglot failed.

## Related

- [[procedures/Image-Based-htaccess-Upload-Bypass]]
