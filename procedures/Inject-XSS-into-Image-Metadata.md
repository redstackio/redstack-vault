---
tags:
  - xss
  - metadata-injection
  - image-prep
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.434Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6189ff14-cabb-40b9-97c3-346bd884559e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-into-Image-Metadata

## Summary

This procedure embeds a malicious JavaScript payload into an image file's title metadata, exploiting lack of sanitization in applications like WooCommerce to enable stored XSS.

## Description

In the context of WooCommerce on WordPress, image files uploaded as product images have their metadata (e.g., EXIF title) output unsanitized on product pages. By modifying the title field to include XSS code, an attacker can store and execute JavaScript when any user views the page, leading to session hijacking, data theft, or defacement. This requires access to an image editor or file properties tool; no server interaction yet.

## Requirements

1. A valid image file (e.g., JPEG)
2. Windows environment or tool to edit file metadata (e.g., ExifTool)
3. Knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize all file metadata on upload using libraries like WordPress's wp_check_filetype_and_ext
- Strip EXIF data with tools like ImageMagick's mogrify -strip
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor uploads for suspicious metadata patterns

## Objectives

1. Embed executable JavaScript in image title without corrupting the file
2. Ensure payload survives upload and display processes
3. Prepare for stored XSS execution on frontend

## Instructions

### Step 1: Prepare the Image File

**Context**: Select or create a benign image file to avoid detection during upload.

No specific command; use graphical interface:

Right-click the image in Windows Explorer, select Properties > Details tab, and edit the "Title" field to include the XSS payload, e.g., `<script>alert(document.cookie)</script>`.

> This embeds the payload in the file's metadata. Verify by reopening properties; the file should remain viewable as an image.

### Step 2: Validate Payload

**Context**: Test the metadata embedding to ensure the payload is intact.

Use a metadata viewer or command-line tool like ExifTool (if available):

```bash
exiftool -Title test.jpg
```

> Expected output shows the injected title with the script tag. If using Windows only, rely on properties dialog for verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- metadata
- image
