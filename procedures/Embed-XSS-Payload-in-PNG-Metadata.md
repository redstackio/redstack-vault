---
id: proc-embed-xss-png-964550
tags:
  - xss
  - metadata-injection
type: procedure
tools:
  - '[[tools/exiftool]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/exiftool-inject-xss-into-png-comment]]'
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.289Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Embed-XSS-Payload-in-PNG-Metadata

## Summary

This procedure embeds a JavaScript XSS payload into the EXIF Comment metadata of a PNG image file using exiftool, allowing the file to be uploaded as an avatar while triggering HTML interpretation for payload execution.

## Description

In the context of exploiting unrestricted file uploads, this step prepares a seemingly benign PNG image with malicious HTML/JavaScript hidden in its metadata. The payload is injected into the PNG's Comment field, which is not sanitized during upload or rendering on Shopify's CDN. When the file is served with a manipulated MIME type (text/html), the metadata is treated as HTML, executing the script. Prerequisites include a base PNG image and exiftool installed.

## Requirements

1. exiftool installed on the attacker's machine
2. A clean base PNG image file
3. Basic command-line access

## Defense

Defensive measures and detection strategies:

- Sanitize and strip all metadata from uploaded images using libraries like ImageMagick or Pillow
- Validate file content against MIME type (e.g., check for PNG signature, reject if HTML-like)
- Serve images with strict Content-Type: image/png and Content-Security-Policy headers

## Objectives

1. Inject XSS payload into image metadata without corrupting the file
2. Ensure payload survives upload and rendering
3. Enable stored XSS execution on access

## Instructions

### Step 1: Prepare Base Image

**Context**: Start with a valid PNG image to avoid upload rejections.

Download or create a simple PNG file named base.png.

### Step 2: Inject XSS Payload

**Context**: Use exiftool to embed the script in the Comment field, escaping quotes for HTML context.

**Command** ([[commands/exiftool-inject-xss-into-png-comment]]):
```bash
exiftool -Comment="\"><script>alert(prompt('XSS BY ZEROX4'))</script>" xss_comment_exif_metadata_double_quote.png
```

> This command sets the EXIF Comment to "><script>alert(prompt('XSS BY ZEROX4'))</script>", closing any prior HTML tags. Expected output: "1 image files updated". The resulting file is ready for upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/exiftool-inject-xss-into-png-comment]]

## Tools Used

- [[tools/exiftool]]

## Tags

- xss
- file-upload
