---
id: proc-upload-gif-api
tags:
  - exploit
  - upload
  - dos
  - gif
type: procedure
tools:
  - '[[tools/Go]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:32:20.355Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[OS Exhaustion Flood]]'
---
# Upload-Malformed-GIF-via-API

## Summary

This procedure uses a Go-based POC to upload a 31-byte malformed GIF to Mattermost's upload API, triggering excessive memory consumption in gif.DecodeAll without prior resolution checks.

## Description

The upload process in Mattermost calls GetInfoForBytes, which decodes the GIF fully before checkImageResolutionLimit, leading to OOM. The POC creates an upload session via /api/v4/files and sends the crafted bytes, bypassing preprocessImage.

## Requirements

1. Go environment installed
2. Mattermost API access with channel ID
3. Valid token for authenticated upload

## Defense

Defensive measures and detection strategies:

- Implement pre-decoding dimension checks in image uploads
- Rate-limit file uploads
- Monitor RAM spikes during API calls

## Objectives

1. Create upload session for 'oom.gif'
2. Inject malformed GIF bytes
3. Trigger resource exhaustion

## Instructions

### Step 1: Prepare Go POC

**Context**: Write or compile Go code using Mattermost model package.

No command; code imports 'github.com/mattermost/mattermost-server/v5/model'.

> Define bytes: []byte{0x47, 0x49, 0x46, 0x38, 0x39, 0x61, 0x2e, 0xf8, 0xff, 0xff, 0xf, 0x18, 0x18, 0x2c, 0x7f, 0x20, 0x0, 0x0, 0x0, 0xa0, 0xff, 0xFF, 0xff, 0xd4, 0x9a, 0xf0, 0xb4, 0x8, 0x35, 0x4, 0x0}.

### Step 2: Execute Upload

**Context**: Run the POC to interact with API.

**Command** (go run poc.go):
```bash
go run poc.go --channel-id YOUR_CHANNEL_ID --token YOUR_TOKEN
```

> Creates session for 31-byte file, uploads bytes via UploadData. Expected: 200 OK response.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[OS Exhaustion Flood]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Go]]

## Tags

- exploit
- upload
- dos
- gif
