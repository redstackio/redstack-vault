---
id: 123e4567-e89b-12d3-a456-426614174004
name: Disclose-and-Playback-Private-Video-Using-Config-Data
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.186Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Cloud Storage]]'
sub_techniques: []
tags:
  - information-disclosure
  - private-video
commands: []
platforms:
  - Web
tools:
  - '[[tools/videoLeak-php]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Cloud Storage]]'
---

# Disclose-and-Playback-Private-Video-Using-Config-Data

## Summary

This procedure leverages the config JSON to directly access and play or download the private video files, achieving full unauthorized disclosure without login.

## Description

With file URLs from the config, this step embeds the video in a player or downloads it directly. The links are signed via the token, bypassing Vimeo's privacy. Targets web browsers or downloaders; assumes config data available. Outcome is complete video access.

## Requirements

1. File URLs from config JSON
2. Browser or download tool (e.g., wget, curl)
3. No additional auth needed

## Defense

Defensive measures and detection strategies:

- Sign file URLs with short expirations tied to valid sessions
- Monitor direct file access logs for token reuse
- Block playback from unauthorized referers

## Objectives

1. Play or download private video
2. Verify full disclosure
3. Demonstrate impact

## Instructions

### Step 1: Embed or Access Video

**Context**: Use a file URL from config to load the video.

Example embed in HTML:
```html
<iframe src="https://player.vimeo.com/video/[VIDEO_ID]?h=[FILE_HASH]&s=[SECRET]" width="640" height="360"></iframe>
```

> Or direct download: curl -O [FILE_URL_FROM_CONFIG]. Expected: Video loads/plays.

### Step 2: Download Files

**Context**: Fetch progressive download links.

**Command** (curl-download-video):
```bash
curl -O "[DIRECT_FILE_URL_FROM_CONFIG]"
```

> Replaces with actual URL; expected: MP4 or similar file saved.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Cloud Storage]] Data from Cloud Storage

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/videoLeak-php]]

## Tags

- [[information-disclosure]]
- [[private-video]]
