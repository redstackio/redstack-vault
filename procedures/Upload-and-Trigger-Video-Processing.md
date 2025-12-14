---
id: proc-upload-trigger-001
tags:
  - upload
  - ffmpeg-trigger
  - wordpress
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
updated_at: '2025-12-14T03:46:09.415Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-and-Trigger-Video-Processing

## Summary

This procedure uploads the crafted malicious AVI to WordPress.com's media/videos endpoint and triggers FFmpeg processing by editing the video, causing SSRF requests from internal servers.

## Description

WordPress.com processes uploaded videos using FFmpeg on Automattic's internal nodes. Selecting and editing the video initiates HLS playlist fetching, executing the embedded external URL for SSRF. Requires a paid account; impacts include arbitrary internal HTTP requests.

## Requirements

1. Paid WordPress.com account
2. Modified AVI file from prior procedure
3. Attacker server listening for requests

## Defense

Defensive measures and detection strategies:

- Limit video uploads to authenticated users with rate limiting
- Scan uploads for anomalous subtitle chunks or HLS references
- Log and alert on FFmpeg outbound traffic

## Objectives

1. Successfully upload AVI
2. Initiate processing to trigger SSRF
3. Confirm request from internal IP (e.g., 192.0.87.12)

## Instructions

### Step 1: Access Upload Endpoint

**Context**: Log in to WordPress.com and navigate to the video upload page.

No command; browser navigation to https://wordpress.com/media/videos/your-blog.

> Ensure paid account privileges are active.

### Step 2: Upload and Edit Video

**Context**: Upload the AVI and trigger processing.

No command; select file, upload, then click 'Edit' on the uploaded video.

> Wait for processing; monitor attacker server logs for incoming GET /test_ssrf with User-Agent 'Lavf/56.25.101'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- wordpress-upload
- ssrf-trigger
