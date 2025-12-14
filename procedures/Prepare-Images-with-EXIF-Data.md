---
tags:
  - exif
  - metadata
  - preparation
type: procedure
tools:
  - '[[tools/exiftool]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:34.415Z'
sub_techniques: []
id: 213b9eca-b202-4c09-89f2-e12ebc6680b5
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Prepare-Images-with-EXIF-Data

## Summary

This procedure involves obtaining or creating JPEG images embedded with GPS EXIF metadata to use in testing image upload vulnerabilities for information disclosure.

## Description

In the context of web-based image upload services like IRCCloud, attackers prepare images with sensitive metadata such as GPS coordinates to exploit failures in metadata sanitization. This step ensures the test images contain verifiable EXIF data, simulating real user uploads from geolocated devices. Expected outcomes include confirmed presence of GPS tags (e.g., latitude, longitude) that can later be extracted post-upload.

## Requirements

1. Access to a machine with internet for downloading sample images
2. Installation of [[tools/exiftool]] for metadata verification
3. Basic knowledge of image formats (JPEG)

## Defense

Defensive measures and detection strategies:

- Implement server-side image processing to strip EXIF data on upload
- Monitor for anomalous image uploads with metadata tools
- Educate users on removing metadata before uploading sensitive images

## Objectives

1. Obtain images with embedded GPS EXIF data
2. Verify metadata integrity for testing
3. Prepare assets for upload without altering core image content

## Instructions

### Step 1: Download Sample Images

**Context**: Source images containing GPS metadata from public repositories to avoid creating from scratch.

No specific command; manually download JPEG files from a GitHub repository hosting EXIF sample images.

> Download files like 'gps_sample.jpg' which include latitude/longitude tags.

### Step 2: Verify EXIF Data

**Context**: Use [[tools/exiftool]] to confirm GPS metadata is present.

Execute [[commands/exiftool-verify]] to inspect the image:

```bash
exiftool -GPS* gps_sample.jpg
```

> This command outputs GPS-related tags, such as GPS Latitude: 37.7749 N, GPS Longitude: 122.4194 W, confirming data presence.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/exiftool]]

## Tags

- exif
- metadata
- preparation
