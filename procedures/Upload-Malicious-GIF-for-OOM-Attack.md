---
id: proc-mmw-gif-upload-001
tags:
  - dos
  - upload
  - gif
  - oom
type: procedure
tools:
  - '[[tools/Go]]'
  - '[[tools/Mattermost-API-v4-Client]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:10.472Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Remote File Copy]]'
---
# Upload-Malicious-GIF-for-OOM-Attack

## Summary

This procedure crafts and uploads a malicious GIF file to Mattermost's upload API, exploiting the lack of dimension checks to cause uncontrolled memory consumption and DoS.

## Description

The POC uses Go to interact with the Mattermost API v4. It creates an upload session and sends a 31-byte GIF with extreme dimensions (e.g., width/height near 2^16 via bytes like 0xf8ff, 0xff), triggering gif.DecodeAll to allocate over 4GB RAM without preprocessImage or resolution limits being applied in the GetInfoForBytes path.

## Requirements

1. Running Mattermost instance with known channel ID
2. Go installed (version 1.16+ implied)
3. Mattermost API v4 client imported
4. Crafted GIF byte array: []byte{0x47,0x49,0x46,0x38,0x39,0x61, ...} with large dims

## Defense

Defensive measures and detection strategies:

- Implement pre-upload image dimension and size validation
- Call preprocessImage or checkImageResolutionLimit before full decode
- Monitor upload API for anomalous file patterns and memory spikes
- Use WAF rules to block suspicious GIF headers

## Objectives

1. Initiate file upload session via API
2. Deliver crafted payload to trigger memory exhaustion
3. Achieve server-side resource denial

## Instructions

### Step 1: Initialize API Client and Login

**Context**: Set up authenticated client for API calls.

**Command**:

> In Go code: client := model.NewAPIv4Client("http://localhost:8065/"); _, resp := client.Login("toto", "tototo")

### Step 2: Create Upload Session

**Context**: Prepare session for the malicious file.

**Command**:

> session, _ := client.CreateUploadSession(channelId, "oom.gif", 31)

### Step 3: Upload Crafted GIF Data

**Context**: Send the byte payload to exploit decoding.

**Command**:

> gifData := []byte{ /* GIF89a header + large dims: 0xf8ff, 0xff, etc. */ }; client.UploadData(session, gifData)

> Run the Go program: go run poc.go. The upload succeeds, but decoding crashes the server.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Go]]
- [[tools/Mattermost-API-v4-Client]]

## Tags

- dos
- upload
- gif
- oom
