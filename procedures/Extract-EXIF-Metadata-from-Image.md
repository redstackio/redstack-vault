---
tags:
  - exif
  - metadata-extraction
  - geolocation
type: procedure
tools:
  - '[[tools/exiftool]]'
  - '[[tools/exif-regex-info]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/exiftool-extract]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:25:34.396Z'
sub_techniques: []
id: 7c89caff-34e6-46fc-94de-ccfb55b7c4f8
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Extract-EXIF-Metadata-from-Image

## Summary

This procedure retrieves embedded EXIF metadata from an accessed image URL, focusing on sensitive data like GPS coordinates for location disclosure.

## Description

After gaining access via IDOR, attackers analyze images for preserved EXIF tags, which include geolocation, timestamps, and device info due to lack of sanitization. Using online or local tools, metadata is dumped, enabling tracking of the uploading user's physical location. This exploits the combined vulnerabilities for high-impact information disclosure.

## Requirements

1. Direct URL to the unauthorized image
2. Access to [[tools/exif-regex-info]] or installed [[tools/exiftool]]
3. Browser or local environment for analysis

## Defense

Defensive measures and detection strategies:

- Automatically strip EXIF on server-side during upload using libraries like ImageMagick
- Scan uploads for metadata and log attempts
- Block or warn on images with GPS tags

## Objectives

1. Dump all EXIF tags from the image
2. Extract geolocation data (lat/long)
3. Identify other sensitive metadata for further exploitation

## Instructions

### Step 1: Access Image URL

**Context**: Use the IDOR-modified URL to reach the target image.

Load the URL in browser and copy the direct image link if redirected.

> Ensure image is downloadable or viewable.

### Step 2: Use Online Tool

**Context**: Paste URL into web-based EXIF viewer for quick analysis.

Visit [[tools/exif-regex-info]] and input the image URL.

> Tool fetches and displays tags like GPS Latitude, GPS Longitude.

### Step 3: Local Extraction with Tool

**Context**: For offline verification, download image and use [[commands/exiftool-extract]].

First, download the image (e.g., via browser save), then run:

```bash
exiftool -all image.jpg
```

> Outputs full metadata, including GPS: 37.7749, -122.4194, confirming exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used

- [[commands/exiftool-extract]]

## Tools Used

- [[tools/exiftool]]
- [[tools/exif-regex-info]]

## Tags

- exif
- metadata-extraction
- geolocation
