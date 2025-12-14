---
id: proc-uuid-2
tags:
  - rtmp
  - media-server
  - streaming
type: procedure
tools:
  - '[[tools/RTMPD-CPP-RTMP-Media-Server]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Flash
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:27.057Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host-MP3-via-RTMP-Server

## Summary

This procedure sets up an RTMP server to host and stream a malicious MP3 file, broadcasting its ID3 metadata unescaped to connected clients like the VideoJS SWF, enabling the XSS payload delivery.

## Description

RTMP (Real-Time Messaging Protocol) is used here because VideoJS SWF lacks a policy file for HTTP metadata access, forcing reliance on RTMP where server and file metadata (including ID3 tags) are directly passed via ExternalInterface without escaping. The attack scenario involves running a C++ RTMP server (e.g., RTMPD) configured to stream the MP3 with parameters like server name and stream key. Target environment: Any server OS supporting C++ binaries; expected outcome is a live RTMP endpoint that the SWF can connect to and ingest malicious metadata.

## Requirements

1. RTMP server software like RTMPD installed
2. Malicious MP3 file prepared
3. Network access on port 1935 (default RTMP)

## Defense

Defensive measures and detection strategies:

- Block unauthorized RTMP traffic at network boundaries
- Validate and sanitize incoming stream metadata
- Deprecate RTMP support in media players
- Log and monitor RTMP connections for anomalous payloads

## Objectives

1. Establish RTMP stream for MP3 delivery
2. Ensure metadata injection via server config and ID3
3. Maintain stream availability for SWF connection

## Instructions

### Step 1: Install and Configure RTMP Server

**Context**: Set up the RTMPD server to handle MP3 streaming.

Download and build RTMPD from source if needed:

```bash
git clone http://www.rtmpd.com/rtmpd.git
cd rtmpd && make
```

> Builds the C++ server. Expected output: Executable binary ready.

### Step 2: Launch Server with Stream Config

**Context**: Start the server and configure it to stream the MP3 with metadata.

Run the server:

```bash
./rtmpd -p 1935 -s mp3:haha -m "server_name=malicious" /path/to/haha.mp3
```

> Launches on port 1935, streams haha.mp3 with custom metadata. Expected output: Server logs indicating stream start; endpoint rtmp://localhost/mp3:haha available.

### Step 3: Verify Stream

**Context**: Test the RTMP endpoint to confirm metadata broadcast.

Use a client like ffplay to connect:

```bash
ffplay rtmp://localhost/mp3:haha
```

> Plays the stream; inspect network for metadata packets. Expected output: Audio playback with metadata visible in tools like Wireshark.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/RTMPD-CPP-RTMP-Media-Server]]

## Tags

- [[rtmp]]
- [[streaming]]
